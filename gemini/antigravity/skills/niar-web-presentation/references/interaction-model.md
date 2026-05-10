# Interaction Model

`niar-web-presentation` is a web slide presentation with page navigation and per-slide reveal steps.

## Cursor

Use two coordinates:

```ts
type DeckCursor = {
  slideIndex: number;
  revealIndex: number;
};
```

## Next

```text
if revealIndex < currentSlide.reveals - 1:
  revealIndex += 1
else:
  slideIndex += 1
  revealIndex = 0
```

## Previous

```text
if revealIndex > 0:
  revealIndex -= 1
else:
  slideIndex -= 1
  revealIndex = previousSlide.reveals - 1
```

Clamp at the first and last reveal.

## Controls

- `Space` / `ArrowRight`: next reveal/slide.
- `ArrowLeft`: previous reveal/slide.
- `Home`: first slide, reveal 0.
- `End`: last slide, last reveal.
- `R`: reset cursor.
- `C`: toggle clean mode.
- Click right half of stage: next.
- Click left half of stage: previous.

## Stage Scaling

Use absolute center positioning for the stage, then update one combined transform on resize:

```js
stage.style.transform = `translate(-50%, -50%) scale(${scale})`;
```

Do not use `stage.style.transform = scale(...)` alone, because it removes the centering compensation. Do not rely on CSS Grid centering for the primary stage layout.

When handling mouse clicks, read the transformed bounds with `stage.getBoundingClientRect()` and compare `event.clientX - rect.left` against `rect.width / 2`.

## Chrome

Controls are presentation aids, not part of the visual design.

- Default: controls hidden or very low opacity.
- Hover bottom/side safe zone: show controls.
- `?clean=1`: hide controls entirely.
- Optional `?presenter=1`: show slide/reveal status for rehearsals.
- Controls must not overlap the NIAR logo protected zone.

## Persistence

Use localStorage:

```text
niar-web-presentation:<project-id>:cursor
```

Also store a `deckVersion`. Change it when slide count or reveal count changes so stale cursors do not land on invalid steps.

## Reveal Semantics

Each reveal should add meaning:

- Introduce a point.
- Highlight a relationship.
- Reveal a number.
- Move a process forward.
- Compare before/after.

Avoid arbitrary animation that does not clarify content.
