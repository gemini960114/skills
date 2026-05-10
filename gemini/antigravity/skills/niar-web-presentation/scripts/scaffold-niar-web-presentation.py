#!/usr/bin/env python
"""Create a starter NIAR-style static HTML web presentation."""

from __future__ import annotations

import argparse
import json
import re
import shutil
from html import escape
from pathlib import Path
from textwrap import dedent


SKILL_DIR = Path(__file__).resolve().parents[1]
BACKGROUND_DIR = SKILL_DIR / "assets" / "backgrounds"


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(dedent(text).lstrip(), encoding="utf-8")


def copy_backgrounds(out: Path) -> None:
    dest = out / "assets" / "niar" / "backgrounds"
    dest.mkdir(parents=True, exist_ok=True)
    for src in sorted(BACKGROUND_DIR.glob("*.png")):
        shutil.copy2(src, dest / src.name)


def safe_project_id(value: str) -> str:
    value = re.sub(r"[^a-zA-Z0-9_-]+", "-", value.strip()).strip("-").lower()
    return value or "niar-web-presentation"


def build_index_html(title: str, project_id: str) -> str:
    title_html = escape(title, quote=True)
    title_json = json.dumps(title, ensure_ascii=False)
    project_json = json.dumps(project_id, ensure_ascii=False)

    template = r"""
    <!doctype html>
    <html lang="zh-Hant">
      <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <title>__TITLE_HTML__</title>
        <style>
          :root {
            --stage-w: 1920;
            --stage-h: 1080;
            --niar-navy: #0e2841;
            --niar-teal: #156082;
            --niar-orange: #e97132;
            --niar-gold: #f0c23a;
            --niar-red: #a80022;
            --niar-cream: #f7f4ea;
            --niar-line: rgba(233, 113, 50, 0.32);
            --niar-font: "Microsoft JhengHei", "Microsoft YaHei", "Noto Sans TC", system-ui, sans-serif;
          }

          * {
            box-sizing: border-box;
          }

          html,
          body {
            width: 100%;
            height: 100%;
          }

          body {
            margin: 0;
            overflow: hidden;
            background: #101010;
            color: var(--niar-navy);
            font-family: var(--niar-font);
          }

          .viewport {
            width: 100vw;
            height: 100vh;
            position: fixed;
            inset: 0;
            overflow: hidden;
          }

          .stage {
            position: absolute;
            top: 50%;
            left: 50%;
            width: 1920px;
            height: 1080px;
            overflow: hidden;
            background: white;
            box-shadow: 0 20px 70px rgba(0, 0, 0, 0.34);
            transform-origin: center center;
          }

          .slide {
            position: absolute;
            inset: 0;
            display: none;
            padding: 72px 104px;
            background-color: white;
            background-position: center;
            background-size: cover;
          }

          .slide.is-active {
            display: block;
          }

          .bg-cover {
            background-image: url("assets/niar/backgrounds/cover-gradient-wave-logo.png");
          }

          .bg-white-wave {
            background-image: url("assets/niar/backgrounds/white-content-wave-logo.png");
          }

          .bg-dark {
            background-image: url("assets/niar/backgrounds/dark-section-bokeh-logo.png");
          }

          .bg-closing {
            background-image: url("assets/niar/backgrounds/closing-gradient-wave-logo.png");
          }

          .kicker {
            margin: 0 0 18px;
            color: var(--niar-orange);
            font-size: 24px;
            font-weight: 700;
            letter-spacing: 0;
          }

          .kicker.light {
            color: var(--niar-cream);
          }

          h1,
          h2,
          h3,
          p {
            margin-top: 0;
          }

          .cover-panel,
          .closing-panel {
            position: absolute;
            left: 110px;
            top: 200px;
            width: 900px;
            min-height: 510px;
            padding: 64px 70px;
            background: rgba(14, 40, 65, 0.96);
            color: white;
            box-shadow: 0 12px 30px rgba(0, 0, 0, 0.26);
          }

          .cover-panel h1,
          .closing-panel h2 {
            max-width: 770px;
            margin-bottom: 0;
            font-size: 72px;
            line-height: 1.08;
            letter-spacing: 0;
          }

          .orange-rule {
            width: 250px;
            height: 12px;
            margin: 32px 0;
            background: var(--niar-orange);
          }

          .lead {
            max-width: 760px;
            color: var(--niar-gold);
            font-size: 34px;
            font-weight: 700;
            line-height: 1.38;
          }

          .meta,
          .closing-panel p:not(.kicker) {
            color: var(--niar-cream);
            font-size: 28px;
            line-height: 1.5;
          }

          .page-label {
            position: absolute;
            left: 104px;
            top: 70px;
            color: var(--niar-orange);
            font-size: 24px;
            font-weight: 700;
          }

          .content-title {
            width: 1240px;
            margin: 48px 0 0;
            color: var(--niar-navy);
            font-size: 62px;
            line-height: 1.14;
          }

          .content-rule {
            width: 310px;
            height: 8px;
            margin: 26px 0 54px;
            background: linear-gradient(90deg, var(--niar-orange), var(--niar-gold));
          }

          .content-grid {
            display: grid;
            grid-template-columns: 1.05fr 0.95fr;
            gap: 54px;
            width: 1450px;
          }

          .navy-panel {
            min-height: 440px;
            padding: 46px 52px;
            background: rgba(14, 40, 65, 0.96);
            color: white;
          }

          .navy-panel h3,
          .white-panel h3 {
            margin-bottom: 22px;
            font-size: 34px;
            line-height: 1.2;
          }

          .navy-panel p,
          .white-panel p {
            margin-bottom: 20px;
            font-size: 27px;
            line-height: 1.48;
          }

          .white-panel {
            min-height: 440px;
            padding: 42px 46px;
            border-left: 10px solid var(--niar-orange);
            background: rgba(255, 255, 255, 0.92);
            box-shadow: 0 9px 26px rgba(14, 40, 65, 0.14);
          }

          .metric-row {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 34px;
            width: 1450px;
            margin-top: 42px;
          }

          .metric {
            padding: 28px 30px;
            border-top: 8px solid var(--niar-orange);
            background: rgba(255, 255, 255, 0.94);
            box-shadow: 0 9px 22px rgba(14, 40, 65, 0.12);
          }

          .metric strong {
            display: block;
            color: var(--niar-teal);
            font-size: 42px;
            line-height: 1;
          }

          .metric span {
            display: block;
            margin-top: 16px;
            color: #4d4d4d;
            font-size: 24px;
            line-height: 1.35;
          }

          .dark-title {
            width: 1160px;
            margin: 58px 0 0;
            color: white;
            font-size: 68px;
            line-height: 1.1;
          }

          .dark-card-row {
            position: absolute;
            left: 140px;
            right: 140px;
            top: 430px;
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 50px;
          }

          .dark-card {
            min-height: 230px;
            padding: 34px;
            border-left: 12px solid var(--niar-orange);
            background: rgba(14, 40, 65, 0.96);
            color: white;
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.28);
          }

          .dark-card h3 {
            margin-bottom: 24px;
            font-size: 36px;
          }

          .dark-card p {
            color: var(--niar-cream);
            font-size: 26px;
            line-height: 1.45;
          }

          [data-reveal] {
            opacity: 0;
            transform: translateY(20px);
            transition: opacity 380ms ease, transform 380ms ease;
          }

          [data-reveal].is-visible {
            opacity: 1;
            transform: translateY(0);
          }

          .controls {
            position: absolute;
            left: 50%;
            bottom: 28px;
            z-index: 30;
            display: flex;
            align-items: center;
            gap: 14px;
            padding: 10px 14px;
            color: white;
            background: rgba(14, 40, 65, 0.78);
            border: 1px solid rgba(255, 255, 255, 0.2);
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.22);
            opacity: 0;
            transform: translateX(-50%);
            transition: opacity 180ms ease;
          }

          .stage:hover .controls,
          .controls:focus-within {
            opacity: 1;
          }

          body.clean .controls {
            display: none;
          }

          .controls button {
            min-width: 46px;
            min-height: 38px;
            border: 0;
            padding: 8px 12px;
            color: white;
            background: var(--niar-orange);
            font: inherit;
            cursor: pointer;
          }

          .progress {
            min-width: 140px;
            font-size: 18px;
            text-align: center;
            white-space: nowrap;
          }
        </style>
      </head>
      <body>
        <main class="viewport" aria-label="__TITLE_HTML__">
          <section id="stage" class="stage" aria-roledescription="slide deck">
            <article class="slide bg-cover is-active" data-title="Cover" aria-labelledby="slide-cover-title">
              <div class="cover-panel">
                <p class="kicker">NIAR WEB PRESENTATION</p>
                <h1 id="slide-cover-title">__TITLE_HTML__</h1>
                <div class="orange-rule" aria-hidden="true"></div>
                <p class="lead" data-reveal="1">可現場播放，也適合桌面錄影的 NIAR 風格網頁投影片。</p>
                <p class="meta" data-reveal="2">靜態 HTML，不需要 npm 或開發伺服器。</p>
              </div>
            </article>

            <article class="slide bg-white-wave" data-title="Message" aria-labelledby="slide-message-title">
              <p class="page-label">01 / 核心訊息</p>
              <h2 id="slide-message-title" class="content-title">把正式簡報的品牌秩序，轉成可點擊播放的網頁舞台</h2>
              <div class="content-rule" aria-hidden="true"></div>
              <div class="content-grid">
                <section class="navy-panel" data-reveal="1">
                  <h3>一頁一個主題</h3>
                  <p>每一頁維持單一重點，頁內元素用 reveal 分段出現，讓講者可以順著節奏說明。</p>
                  <p>畫面採固定 1920 x 1080 座標，再依瀏覽器視窗等比例縮放。</p>
                </section>
                <section class="white-panel" data-reveal="2">
                  <h3>保留 NIAR 辨識度</h3>
                  <p>使用 NIAR 背景、右上 Logo 區、橘紅金漸層、深藍內容面板與白底內容頁節奏。</p>
                  <p>控制列預設隱藏，避免干擾客戶展示或錄影畫面。</p>
                </section>
              </div>
              <section class="metric-row" data-reveal="3" aria-label="簡報特性摘要">
                <div class="metric"><strong>16:9</strong><span>固定舞台比例</span></div>
                <div class="metric"><strong>HTML</strong><span>直接開啟播放</span></div>
                <div class="metric"><strong>Reveal</strong><span>同頁分段出現</span></div>
              </section>
            </article>

            <article class="slide bg-dark" data-title="Flow" aria-labelledby="slide-flow-title">
              <p class="kicker light">02 / 製作流程</p>
              <h2 id="slide-flow-title" class="dark-title">來源整理、腳本節奏、視覺場景一起收斂</h2>
              <div class="orange-rule" aria-hidden="true"></div>
              <div class="dark-card-row">
                <article class="dark-card" data-reveal="1">
                  <h3>輸入判讀</h3>
                  <p>確認是簡單主題、單一文件、多文件、既有講稿或既有簡報。</p>
                </article>
                <article class="dark-card" data-reveal="2">
                  <h3>證據整理</h3>
                  <p>多文件任務先建立來源盤點與證據表，避免沒有依據的內容進入畫面。</p>
                </article>
                <article class="dark-card" data-reveal="3">
                  <h3>HTML 交付</h3>
                  <p>輸出 index.html 與 assets 資料夾，使用者打開檔案即可播放。</p>
                </article>
              </div>
            </article>

            <article class="slide bg-closing" data-title="Closing" aria-labelledby="slide-closing-title">
              <div class="closing-panel">
                <p class="kicker light">結語</p>
                <h2 id="slide-closing-title">一眼是 NIAR，播放像 web。</h2>
                <div class="orange-rule" aria-hidden="true"></div>
                <p data-reveal="1">把正式簡報的品牌風格，變成適合現場展示、客戶簡報與桌面錄影的網頁播放介面。</p>
              </div>
            </article>

            <nav class="controls" aria-label="Presentation controls">
              <button type="button" data-action="previous" title="Previous">Prev</button>
              <span class="progress" id="progress" aria-live="polite">1/4 · 1/1</span>
              <button type="button" data-action="next" title="Next">Next</button>
              <button type="button" data-action="reset" title="Reset">Reset</button>
              <button type="button" data-action="clean" title="Clean mode">Clean</button>
            </nav>
          </section>
        </main>

        <script>
          const deckTitle = __TITLE_JSON__;
          const projectId = __PROJECT_JSON__;
          const deckVersion = "v1";
          const storageKey = `niar-web-presentation:${projectId}:${deckVersion}:cursor`;
          const stage = document.getElementById("stage");
          const slides = Array.from(document.querySelectorAll(".slide"));
          const progress = document.getElementById("progress");
          const cleanFromUrl = new URLSearchParams(location.search).get("clean") === "1";
          let clean = cleanFromUrl;
          let cursor = readCursor();

          function readCursor() {
            const fallback = { slide: 0, reveal: 0 };
            try {
              const saved = JSON.parse(localStorage.getItem(storageKey) || "null");
              return clampCursor(saved || fallback);
            } catch {
              return fallback;
            }
          }

          function maxReveal(slideIndex) {
            const values = Array.from(slides[slideIndex].querySelectorAll("[data-reveal]"))
              .map((element) => Number(element.dataset.reveal || 0));
            return Math.max(0, ...values);
          }

          function clampCursor(value) {
            const slide = Math.min(Math.max(Number(value.slide) || 0, 0), slides.length - 1);
            const reveal = Math.min(Math.max(Number(value.reveal) || 0, 0), maxReveal(slide));
            return { slide, reveal };
          }

          function saveCursor() {
            localStorage.setItem(storageKey, JSON.stringify(cursor));
          }

          function render() {
            cursor = clampCursor(cursor);
            slides.forEach((slide, slideIndex) => {
              const isActive = slideIndex === cursor.slide;
              slide.classList.toggle("is-active", isActive);
              slide.querySelectorAll("[data-reveal]").forEach((element) => {
                const step = Number(element.dataset.reveal || 0);
                element.classList.toggle("is-visible", isActive && step <= cursor.reveal);
              });
            });
            document.body.classList.toggle("clean", clean);
            progress.textContent = `${cursor.slide + 1}/${slides.length} · ${cursor.reveal + 1}/${maxReveal(cursor.slide) + 1}`;
            document.title = `${deckTitle} - ${slides[cursor.slide].dataset.title || cursor.slide + 1}`;
            saveCursor();
          }

          function next() {
            if (cursor.reveal < maxReveal(cursor.slide)) {
              cursor.reveal += 1;
            } else if (cursor.slide < slides.length - 1) {
              cursor.slide += 1;
              cursor.reveal = 0;
            }
            render();
          }

          function previous() {
            if (cursor.reveal > 0) {
              cursor.reveal -= 1;
            } else if (cursor.slide > 0) {
              cursor.slide -= 1;
              cursor.reveal = maxReveal(cursor.slide);
            }
            render();
          }

          function reset() {
            cursor = { slide: 0, reveal: 0 };
            render();
          }

          function toEnd() {
            cursor = { slide: slides.length - 1, reveal: maxReveal(slides.length - 1) };
            render();
          }

          function resizeStage() {
            const scale = Math.max(0.1, Math.min(window.innerWidth / 1920, window.innerHeight / 1080));
            stage.style.transform = `translate(-50%, -50%) scale(${scale})`;
          }

          stage.addEventListener("click", (event) => {
            if (event.target.closest(".controls")) return;
            const rect = stage.getBoundingClientRect();
            const x = event.clientX - rect.left;
            if (x < rect.width / 2) previous();
            else next();
          });

          document.querySelectorAll("[data-action]").forEach((button) => {
            button.addEventListener("click", (event) => {
              event.stopPropagation();
              const action = button.dataset.action;
              if (action === "previous") previous();
              if (action === "next") next();
              if (action === "reset") reset();
              if (action === "clean") {
                clean = !clean;
                render();
              }
            });
          });

          window.addEventListener("keydown", (event) => {
            if (event.key === " " || event.key === "ArrowRight" || event.key === "PageDown") {
              event.preventDefault();
              next();
            }
            if (event.key === "ArrowLeft" || event.key === "PageUp") previous();
            if (event.key === "Home") reset();
            if (event.key === "End") toEnd();
            if (event.key.toLowerCase() === "r") reset();
            if (event.key.toLowerCase() === "c") {
              clean = !clean;
              render();
            }
          });

          window.addEventListener("resize", resizeStage);
          resizeStage();
          render();
        </script>
      </body>
    </html>
    """

    return (
        dedent(template)
        .replace("__TITLE_HTML__", title_html)
        .replace("__TITLE_JSON__", title_json)
        .replace("__PROJECT_JSON__", project_json)
    )


def build_readme(title: str) -> str:
    return f"""
    # {title}

    This is a static NIAR-style HTML web presentation.

    ## Open

    Double-click `index.html`, or open it from a browser. No npm install, dev server, or build step is required.

    ## Controls

    - Right click area / `Space` / `ArrowRight`: next reveal or slide.
    - Left click area / `ArrowLeft`: previous reveal or slide.
    - `Home`: first slide.
    - `End`: final slide.
    - `R`: reset.
    - `C` or `?clean=1`: clean mode.

    ## Assets

    NIAR backgrounds are stored in `assets/niar/backgrounds/`.
    """


def build_outline(title: str) -> str:
    return f"""
    # outline

    Title: {title}

    ## Slide 1 - Cover
    Goal: Open with NIAR identity and presentation title.
    Reveals: subtitle, delivery note.

    ## Slide 2 - Message
    Goal: Explain why this is a web presentation instead of a PPTX.
    Reveals: stage rule, NIAR visual identity, metrics.

    ## Slide 3 - Flow
    Goal: Show the source-to-presentation workflow.
    Reveals: input, evidence, static HTML delivery.

    ## Slide 4 - Closing
    Goal: Close with the key promise.
    Reveals: closing sentence.
    """


def scaffold(out: Path, title: str, project_id: str) -> None:
    out.mkdir(parents=True, exist_ok=True)
    project_id = safe_project_id(project_id)
    copy_backgrounds(out)
    write(out / "index.html", build_index_html(title, project_id))
    write(out / "README.md", build_readme(title))
    write(out / "outline.md", build_outline(title))


def main() -> None:
    parser = argparse.ArgumentParser(description="Scaffold a static NIAR web presentation.")
    parser.add_argument("output_dir", help="Output directory for the HTML presentation")
    parser.add_argument("--title", default="NIAR Web Presentation", help="Presentation title")
    parser.add_argument("--project-id", default="niar-web-presentation", help="Project id for cursor storage")
    args = parser.parse_args()

    out = Path(args.output_dir).resolve()
    scaffold(out, args.title, args.project_id)
    print(f"created static NIAR HTML presentation at {out}")
    print(f"open {out / 'index.html'}")


if __name__ == "__main__":
    main()
