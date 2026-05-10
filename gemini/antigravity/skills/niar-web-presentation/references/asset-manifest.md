# NIAR Web Background Asset Manifest

Use these PNGs from `assets/backgrounds/` as full-stage backgrounds. In generated static HTML projects, copy them to `assets/niar/backgrounds/` and use CSS `background-image`.

The design stage is `1920 x 1080`. All full-stage PNGs are 16:9 and should cover the stage.

| File | Source Size | Web Use | Visual Description |
|---|---:|---|---|
| `cover-gradient-wave-logo.png` | 2000 x 1125 | Cover / opening | Orange-red-gold gradient, large abstract mark, wave lines from lower-left, white NIAR logo top-right. |
| `dark-section-bokeh-logo.png` | 2000 x 1125 | Section divider / key message | Deep red-to-gold gradient with soft bokeh and white NIAR logo. Good for large white text and navy cards. |
| `closing-gradient-wave-logo.png` | 2000 x 1125 | Closing / network / ecosystem | Red-orange-gold wave mesh, white NIAR logo top-right. Strongest for final scene or relationship maps. |
| `white-content-wave-logo.png` | 2000 x 1124 | Main content | White page, colored NIAR logo top-right, faint orange/gold wave lines in lower quarter. |
| `white-footer-line-logo.png` | 2000 x 1125 | Timeline / diagram | Mostly white page with colored NIAR logo and thin orange-red-gold bottom line. More vertical room than `white-content-wave-logo.png`. |
| `light-title-cream-logo.png` | 2000 x 1125 | Quiet framing / agenda | Cream-white glow, faint circular geometry on the right, colored NIAR logo top-right. |
| `table-red-header-grid.png` | 1752 x 683 | Table style reference | Red-to-gold header and alternating table rows. Recreate web tables in HTML/CSS rather than placing this as final content. |
| `template-layout-overview.png` | 590 x 531 | Reference only | Screenshot of original NIAR theme layout overview. Do not place in final decks. |

## Protected Brand Area

Treat the top-right area as protected:

- Stage coordinates: `x=1500-1885`, `y=40-145`.
- Do not place titles, cards, photos, controls, or reveal animations over it.
- Controls must never cover this area, even on hover.

## Recommended Static HTML Paths

When scaffolded:

```text
assets/niar/backgrounds/cover-gradient-wave-logo.png
assets/niar/backgrounds/dark-section-bokeh-logo.png
assets/niar/backgrounds/closing-gradient-wave-logo.png
assets/niar/backgrounds/white-content-wave-logo.png
assets/niar/backgrounds/white-footer-line-logo.png
assets/niar/backgrounds/light-title-cream-logo.png
```

For an explicitly requested Vite app, the same files may live under `public/niar/backgrounds/`. Do not make that the default user-facing delivery path.
