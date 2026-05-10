# NIAR PPTX Style Guide

Use this guide to recreate the NIAR / 國家實驗研究院 presentation style without opening `niar.pptx`.

## Canvas

- Size: `16:9`, `13.333 x 7.5 in`
- PowerPoint EMU: `12192000 x 6858000`
- Base layout: full-bleed background image first, editable text and shapes above it.
- Margins: keep main content inside `x=0.70-12.55 in`; reserve the top-right logo zone.
- Treat coordinates as starting positions, not hard locks. Preserve the NIAR rhythm and protected logo zone, but adjust panel size, split content, or add slides when real content is longer than the recipe examples.

## Brand Grammar

The deck alternates between high-impact gradient pages and restrained white content pages:

- Cover / section / closing: orange-red-gold gradient with wave lines, dark navy text panels, white title text.
- Main content: white or cream background, subtle wave ornaments near the bottom, navy titles, orange accent rule, generous whitespace.
- Dense diagrams: white-footer-line background with a thin bottom gradient rule.
- Tables: red-to-gold header, alternating white/light-gray rows, navy or black text.

## Content Rhythm

- Each slide should have one primary goal.
- Do not force a fixed slide count unless the user specified one.
- Prefer splitting dense content into more slides over shrinking body text below 10.5 pt.
- Use cards, tables, timelines, or diagrams to structure information instead of long bullet dumps.
- Plan a reading order: title -> key message -> supporting evidence -> takeaway.
- PowerPoint animations are optional. The slide must still read correctly when exported to PDF or opened without animation playback.

## Colors

Use these exact theme colors from the source deck:

| Role | Hex |
|---|---|
| Deep navy | `0E2841` |
| Light gray | `E8E8E8` |
| Teal blue | `156082` |
| Orange | `E97132` |
| Green | `196B24` |
| Bright cyan | `0F9ED5` |
| Purple | `A02B93` |
| Green accent | `4EA72E` |
| Muted teal | `467886` |
| Mauve | `96607D` |
| Black | `000000` |

Common derived colors that fit the system:

- Gold accent: `F0C23A`
- Deep red accent: `A80022`
- Cream text on dark slides: `F7F4EA`
- Body gray: `666666`

## Typography

- Font: `Microsoft JhengHei` / `微軟正黑體`
- Fallback: `Microsoft YaHei`
- Title weight: bold
- Body weight: regular; bold only for labels
- Letter spacing: normal

Suggested sizes:

| Element | Size |
|---|---:|
| Cover title | 32-36 pt |
| Dark section title | 32-36 pt |
| White slide title | 28-34 pt |
| Kicker / section label | 10-12 pt |
| Subtitle / key sentence | 16-22 pt |
| Body text | 12-16 pt |
| Captions | 8-10.5 pt |
| Footer | 7.5-10 pt |

## Standard Elements

### Header

- Kicker: `x=0.72`, `y=0.33`, `w=5.8`, `h=0.24`, 10-12 pt, orange on white slides, cream/white on dark slides.
- Title: `x=0.72`, `y=0.54`, `w=8.8`, `h=0.62`, 28-34 pt, bold.
- Accent rule: orange rectangle at `x=0.72`, `y=1.20`, `w=1.35`, `h=0.07`. For big section titles, extend to `w=1.8-2.0`.

### Logo

- Full-slide backgrounds already include NIAR logo.
- Protect top-right zone: `x=10.4-13.0`, `y=0.25-0.95`.
- Do not add a second logo unless using a blank background.

### Footer

- Page number: `x=0.10`, `y=6.92`, `w=0.81`, `h=0.40`, 9-10 pt.
- Footer label: `x=0.72`, `y=6.94`, `w=4.2`, `h=0.18`, 7.5-8.5 pt.
- White slides: navy page number and gray footer label.
- Dark slides: cream/white page number and footer label.

## Layout Recipes

### 1. Cover

- Background: `cover-gradient-wave-logo.png`
- Navy panel: `x=0.67`, `y=1.42`, `w=7.45`, `h=3.48`, optional 10-20% transparency.
- Title: `x=0.86`, `y=1.66`, `w=6.9`, `h=1.25`, 32-36 pt, white, bold.
- Accent rule: `x=0.88`, `y=3.21`, `w=2.0`, `h=0.09`, orange.
- Subtitle: `x=0.88`, `y=3.55`, `w=6.55`, `h=0.46`, 18-22 pt, gold.
- Date/source: `x=0.90`, `y=4.27`, `w=4.7`, `h=0.34`, 12-13 pt, cream.

### 2. Dark Key Message

- Background: `dark-section-bokeh-logo.png`
- Header as above, white title.
- Key sentence: `x=0.82`, `y=1.56`, `w=7.5`, `h=0.92`, 20-22 pt, white, bold.
- Three dark cards: `y=3.0`, `w=3.58`, `h=1.45`; x positions `0.85`, `4.78`, `8.70`.
- Use navy card fills, orange/gold/cyan edge accents, cream body text.

### 3. White Two-Column Explanation

- Background: `light-title-cream-logo.png` or `white-content-wave-logo.png`
- Two white panels: left `x=0.86`, right `x=7.02`, `y=1.58`, `w=5.25`, `h=4.42`.
- Panel header: `x+0.29`, `y=1.90`, 18 pt, navy, bold.
- Body: 13-14 pt, black. Use bold inline labels such as `政策驅動：`.

### 4. Text Plus Official Photo

- Background: `white-content-wave-logo.png`
- Left stacked callouts: `x=0.78`, `w=5.15`, `h=1.15`, y positions around `1.55`, `2.95`, `4.35`.
- Right photo frame: `x=6.55`, `y=1.42`, `w=5.92`, `h=2.95`.
- Caption under photo: `x=6.55`, `y=4.48`, `w=5.55`, `h=0.34`, 9-10.5 pt gray.

### 5. Four Strategy Cards

- Background: `white-content-wave-logo.png`
- Cards: `w=5.55`, `h=1.42`.
- Positions: `(0.86,1.55)`, `(6.92,1.55)`, `(0.86,3.48)`, `(6.92,3.48)`.
- Left number bar: `w=0.40`; use orange, gold, green, cyan.
- Header: 14-15 pt navy bold. Body: 11-12 pt black.
- Add one strong summary sentence near `y=5.42`.

### 6. Supply Chain / Process Chain

- Background: `white-footer-line-logo.png`.
- Five cards: `x=0.95 + i*2.42`, `y=2.55`, `w=1.74`, `h=1.42`.
- Put numbered orange/teal circles near card top-left.
- Link cards with short orange connectors.
- Bottom navy conclusion bar: `x=0.95`, `y=4.55`, `w=11.35`, `h=0.82`.

### 7. Split Infrastructure Panels

- Background: `white-content-wave-logo.png`.
- Left panel: `x=0.86`, `y=1.58`, `w=5.58`, `h=3.95`, orange border.
- Right panel: `x=6.90`, `y=1.58`, `w=5.58`, `h=3.95`, teal border.
- Optional vertical divider: `x=6.55`, `y=2.15-5.28`, pale beige line.

### 8. Dark Network / Ecosystem Page

- Background: `closing-gradient-wave-logo.png`.
- Use white title and one short white key sentence; avoid wrapping into cards.
- Center node: navy panel `x=4.87`, `y=2.72`, `w=3.55`, `h=1.16`, gold border, `TAIWAN` in gold.
- Four partner cards around it: `x=1.0/9.15`, `y=2.05/4.40`, `w=3.10`, `h=1.02`.
- Connect cards to center with thin gold/cyan lines.

### 9. Governance / Table Page

- Background: `white-content-wave-logo.png`.
- Intro sentence: `x=0.88`, `y=1.48`, `w=8.6`, `h=0.48`, 16-17 pt navy bold.
- Table rows: `x=0.92`, `y=2.18`, `w=11.35`, `h=0.72`, row gap `0.06`.
- Label column: `w=1.36`; first label orange, later labels navy.
- Body column: `x=2.55`, 13 pt black.
- Bottom principle bar: `x=0.92`, `y=5.58`, `w=11.35`, `h=0.38`, navy.

### 10. Roadmap / Timeline

- Background: `white-footer-line-logo.png`.
- Horizontal line: `x=1.10-11.70`, `y=3.28`, orange, 2 pt.
- Five phase anchors: `x=0.86 + i*2.48`.
- Alternate labels above and below the line to keep rhythm.
- Bottom final sentence around `x=1.0`, `y=5.72`, navy bold.

### 11. Closing With Photo

- Background: `closing-gradient-wave-logo.png`.
- Left navy panel: `x=0.72`, `y=1.08`, `w=5.95`, `h=3.35`.
- Closing title: `x=1.00`, `y=1.36`, `w=5.35`, 32-36 pt, white bold.
- Body: `x=1.00`, `y=3.04`, `w=5.10`, 14-16 pt, cream.
- Photo frame: `x=7.12`, `y=1.52`, `w=5.18`, `h=3.22`, gold border.
- Photo caption bar: navy, `x=7.12`, `y=4.74`, `w=5.18`, `h=0.42`.

## Quality Checklist

- The NIAR logo is visible and unobstructed on every slide.
- The deck alternates dark/white pages instead of repeating one layout.
- Text remains editable PowerPoint text.
- Tables, charts, captions, source notes, and key numbers remain editable whenever practical.
- Page number and footer appear consistently.
- Dark-page footer text is light enough to read.
- No text overlaps the protected logo area, footer, photos, or cards.
- No content intrudes into the bottom wave area on `white-content-wave-logo.png` unless it is a footer.
- Every slide has a clear purpose and an intentional reading order.
