---
name: google-auth-gsi
description: Implement, review, or debug Google Identity Services (GSI) login in Express/static web apps, especially invitation-code plus Google credential-button flows, GOOGLE_CLIENT_ID environment setup, OAuth Authorized JavaScript origins, Cloud Run env vars, and Helmet header issues such as Cross-Origin-Opener-Policy and Referrer-Policy causing blank popups or "The given origin is not allowed for the given client ID".
---

# Google Auth GSI

Use this skill for Google Identity Services credential-button login in apps that resemble an Express backend serving static frontend code, especially when debugging popup hangs, origin allowlist errors, or deployment variable drift.

## Core Workflow

1. Trace the actual auth flow from code before giving advice:
   - Frontend config load, usually `GET /api/auth/config`.
   - GSI initialization, usually `window.google.accounts.id.initialize` and `renderButton`.
   - Credential POST, usually `POST /api/auth/google` with `{ credential, invitationCode }`.
   - Backend token/session creation and protected route middleware.
2. Verify environment variables and deployment wiring:
   - `AUTH_ENABLED`
   - `INVITATION_CODE`
   - `INVITATION_HINT`
   - `SESSION_SECRET`
   - `GOOGLE_CLIENT_ID`
   - Cloud Run or build substitutions that map `_GOOGLE_CLIENT_ID` to `GOOGLE_CLIENT_ID`.
3. Verify Google Cloud Console settings:
   - OAuth client type must be Web application.
   - Authorized JavaScript origins must exactly match every real `location.origin`.
   - Do not use callback paths for GSI credential-button origin checks.
4. Verify production response headers when GSI popup or origin errors occur:
   - `Cross-Origin-Opener-Policy: same-origin-allow-popups`
   - `Referrer-Policy: strict-origin-when-cross-origin`
5. Test from the same origin the user uses, then compare against local origins.

## Key Diagnosis Patterns

- If console shows `The given origin is not allowed for the given client ID`, compare `location.origin` with Google Console Authorized JavaScript origins and confirm the backend is serving the intended `GOOGLE_CLIENT_ID`.
- If the popup opens to `accounts.google.com/gsi/transform` and stays blank, check `Cross-Origin-Opener-Policy`; Helmet default `same-origin` can block GSI popup communication.
- If Google Console looks correct but the error persists, check `Referrer-Policy`; GSI expects an origin-preserving policy such as `strict-origin-when-cross-origin`.
- If local works but production fails, suspect Cloud Run env vars, reverse proxy headers, or missing production origin.
- If production works but local fails, distinguish `localhost`, `127.0.0.1`, scheme, and port; each is a different origin.

## Standard Express Helmet Patch

For Express apps using Helmet and GSI popup login, prefer:

```js
app.use(helmet({
  contentSecurityPolicy: false,
  crossOriginOpenerPolicy: { policy: 'same-origin-allow-popups' },
  referrerPolicy: { policy: 'strict-origin-when-cross-origin' },
}));
```

Keep this scoped: explain that this preserves security headers while allowing Google popup communication and origin verification.

## Validation Commands

Use PowerShell examples when working in this Windows repo style:

```powershell
Invoke-WebRequest -UseBasicParsing http://localhost:3000/api/auth/config
$r = Invoke-WebRequest -UseBasicParsing https://example.com
$r.Headers
```

In browser DevTools, ask for or inspect:

```js
location.origin
document.referrer
```

## Detailed Reference

For the full implementation plan and checklist extracted from the original project artifact, read `references/google-auth-gsi-plan.md` when the task needs a complete handoff, review checklist, or repo-specific plan.
