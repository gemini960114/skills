---
name: debug
description: Use this skill when asked to review, audit, or debug code. Covers systematic bug-finding across frontend (TypeScript/React/Canvas), backend (Python/FastAPI), and full-stack projects. Apply this BEFORE delivering any code to catch issues proactively.
---

# Debug Skill Instructions

This skill defines a **mandatory, systematic code review process** to identify and fix bugs before delivery. Apply it whenever code is newly written, significantly modified, or when the user asks for a bug check.

---

## When to Apply This Skill

- After writing or generating new code (proactive audit)
- When the user explicitly asks to "check for bugs", "review code", or "debug"
- Before marking a task as complete if the code is non-trivial
- After a significant refactor

---

## Step 1 — Read All Files First

Before making any judgement, read **every relevant file** in full.

Priority reading order:
1. Type / interface definitions
2. Core logic / algorithm implementation
3. State management hooks / stores
4. API route handlers and schemas
5. Main entrypoint / app bootstrap

Do NOT skip a file because it "looks simple". Bugs often hide in helper utilities and type definitions.

---

## Step 2 — Systematic Checklist

Work through each category below. For each item, explicitly confirm ✅ or flag 🔴/🟡.

### 2-A  Types & Interfaces
- [ ] Are all interface fields actually used and correctly typed?
- [ ] Are there missing fields in interfaces that are referenced in implementation? (e.g. added a field to impl but forgot to update the type)
- [ ] Are union types / discriminated unions exhaustively handled?
- [ ] Are optional fields (`?`) handled safely (null-check before use)?

### 2-B  Logic / Algorithm
- [ ] Are loop bounds correct? (off-by-one: `< n` vs `<= n`)
- [ ] Is integer vs float arithmetic intentional? (`Math.floor` where needed?)
- [ ] Are comparisons using correct operators? (`===` not `==`, object reference vs value)
- [ ] Do recursive / self-referential functions have correct base cases?
- [ ] Are formulas correct with respect to domain rules? (e.g. level-up formula does not accidentally include a level multiplier in the divisor)

### 2-C  State Management (React / Frontend)
- [ ] `useCallback` — are all variables captured in the closure listed in `deps`?
- [ ] `useEffect` — are all reactive values listed in `deps`? Are stale closures possible?
- [ ] Object reference vs value comparison (`!== ` on objects from spread/new is always `true`)
- [ ] Are timers (`setTimeout`, `setInterval`, `requestAnimationFrame`) properly cleared on unmount?
- [ ] Can a state update fire after component unmount (memory leak)?
- [ ] Are `useRef` values mutated correctly without triggering unnecessary re-renders?

### 2-D  Async / Promise
- [ ] Are all `await` calls inside `try/catch`?
- [ ] Is error state always reset before a new async operation starts?
- [ ] Are loading flags set to `false` in `finally` (not just `then`)?
- [ ] Can multiple concurrent calls cause a race condition? (debounce / cancel needed?)

### 2-E  Canvas / WebGL Rendering
- [ ] Is `ctx.save()` / `ctx.restore()` used when changing global canvas state (`globalAlpha`, `shadowBlur`, `font`, `textAlign`)?
- [ ] Is `shadowBlur` reset to `0` **and** `shadowColor` reset to `'transparent'` after use?
- [ ] Are `globalAlpha` values always reset to `1` after use?
- [ ] Does the render loop correctly handle the case when the canvas ref is null?
- [ ] Are particle arrays or pools bounded? (prevent unbounded memory growth)

### 2-F  Backend — API & Validation
- [ ] Are all input fields validated for type, range, and non-empty?
- [ ] Is string input stripped of leading/trailing whitespace before validation?
- [ ] Are SQL queries parameterised? (no f-string / string concat with user data)
- [ ] Does the error response format match the success response format (consistent envelope)?
- [ ] Are HTTP status codes correct? (201 for create, 400 for validation, 404 for not found, 500 for server error)

### 2-G  Backend — Database
- [ ] Is the DB connection closed / returned to pool in all code paths (use context manager)?
- [ ] Are transactions committed only after the full operation succeeds?
- [ ] Are indexes created for columns used in ORDER BY or WHERE clauses?
- [ ] Is `lastrowid` / `RETURNING` used safely after commit?

### 2-H  Dead Code & Unused Imports
- [ ] Are there any imports that are never used?
- [ ] Are there variables declared but never referenced?
- [ ] Are there exported functions that are no longer called anywhere?
- [ ] Are there deprecated API usages? (e.g. `@app.on_event` in FastAPI ≥0.93)

### 2-I  Security & Safety
- [ ] Is user-supplied data ever rendered as HTML without sanitisation?
- [ ] Are CORS origins restricted to known domains (not `*` in production)?
- [ ] Are error messages safe to expose to the client? (no stack traces / DB details)

---

## Step 3 — Classify & Report

For each bug found, classify severity:

| Level | Label | Criteria |
|---|---|---|
| 🔴 | **Critical** | Logic error, data corruption, crash, security hole |
| 🟡 | **Medium** | Feature defect, performance issue, deprecated API |
| 🟢 | **Minor** | Dead code, cosmetic, non-functional warning |

Report format:

```
| # | Severity | File:Line | Description | Fix |
```

---

## Step 4 — Apply Fixes

Fix bugs in order of severity (Critical first). For each fix:

1. Use `replace_file_content` or `multi_replace_file_content` — targeted diffs only, never replace the whole file unnecessarily
2. After ALL fixes, run TypeScript type check if applicable:
   ```powershell
   npx tsc --noEmit
   ```
3. If backend was changed, confirm the server reloaded (uvicorn `--reload` auto-detects)
4. Run a quick smoke test (curl / browser check) to confirm no regression

---

## Step 5 — Final Verification

```
✅ TypeScript: 0 errors
✅ All Critical bugs fixed
✅ All Medium bugs fixed or explicitly deferred with reason
✅ Server responds to /health or equivalent
✅ No new warnings introduced
```

---

## Common Bug Patterns (Quick Reference)

### React Hooks — Object Reference vs Value

Anytime state is produced via spread (`{ ...prev, x: newX }`) or a function that returns a new object,
the resulting reference is **always different** even if the value is logically the same.

```typescript
// ❌ WRONG — `newItem` is a new {} every update; reference compare always true
if (next.item !== prev.item) { triggerEffect() }

// ✅ CORRECT — compare by value (coordinate, counter, id, or JSON)
if (next.item.id !== prev.item.id) { triggerEffect() }
if (next.itemCount > prev.itemCount) { triggerEffect() }
```

### React Hooks — Stale Closure on Recursive `useCallback`

A `useCallback` with empty `[]` deps captures the initial version of every variable.
Recursive calls inside `setTimeout` / `setInterval` will always invoke the **stale** version.

```typescript
// ❌ WRONG — doWork captures stale deps because deps array is empty
const doWork = useCallback(() => {
  setTimeout(() => doWork(), delay)  // calls the original stale closure
}, [])

// ✅ CORRECT — bridge via ref so the latest version is always called
const workRef = useRef<() => void>(() => {})
const doWork = useCallback(() => {
  setTimeout(() => workRef.current(), delay)  // always latest
}, [delay])
useEffect(() => { workRef.current = doWork }, [doWork])
```

### Canvas — Shadow State Leak

`shadowBlur` and `shadowColor` are global canvas state. Resetting only `shadowBlur` to `0`
does NOT stop the GPU from computing shadows — `shadowColor` must also be cleared.

```typescript
// ❌ WRONG — shadowColor still active, GPU overhead remains
ctx.shadowBlur = 0

// ✅ CORRECT
ctx.shadowBlur = 0
ctx.shadowColor = 'transparent'
```

> **Best Practice**: wrap any shadow/globalAlpha changes in `ctx.save()` / `ctx.restore()` to automatically restore state.

### FastAPI — Deprecated Lifecycle Hook

```python
# ❌ WRONG — deprecated since FastAPI 0.93, will be removed
@app.on_event("startup")
def startup(): setup()

# ✅ CORRECT — use lifespan context manager
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    setup()   # startup logic
    yield
    teardown()  # shutdown logic (optional)

app = FastAPI(lifespan=lifespan)
```

### Circular Formula (Score containing a multiplier used in its own divisor)

When a computed value (e.g. `score`) already embeds a multiplier (e.g. `level`),
reusing it in the formula that recalculates `level` creates a circular dependency.

```typescript
// ❌ WRONG — score = base × level, so score / (base × threshold) cancels level
//            → level never increases correctly at higher levels
const newLevel = 1 + Math.floor(score / (BASE_POINTS * THRESHOLD))

// ✅ CORRECT — track an independent event counter that has no multiplier
const newCount  = prevCount + 1
const newLevel  = 1 + Math.floor(newCount / THRESHOLD)
const newScore  = prevScore + BASE_POINTS * newLevel  // apply multiplier after
```
