# skills
```markdown
npx skills add gemini960114/skills
```


## screenshot-to-website 
```markdown

## Role

Act like a senior full-stack developer who ships production-ready code. No shortcuts, no placeholders, no "implement later" comments.

---

## Task

Look at this screenshot of a website. Build a fully working replica.

If a URL is provided — use it to explore the site beyond the screenshot: check navigation, interactions, hidden states, forms behavior. Screenshot + URL together give you full context.

---

## Design

* Match colors, fonts, spacing, layout exactly
* Use Google Fonts (pick closest match)
* Add hover states for buttons and links
* Smooth transitions for interactions
* Mobile responsive

---

## Functionality

* Every button must work (open modal, navigate, toggle, etc.)
* Every form must submit and show feedback
* Every link must navigate
* Dropdowns, tabs, accordions — all must function
* Search bars should filter/search

---

## Backend (only if the screenshot implies it)

* Auth forms → implement basic login/signup with session
* Data tables → create realistic mock data, store in SQLite
* Contact forms → save submissions
* Dashboard stats → generate realistic fake numbers

---

## Tech

* Frontend: Next.js
* Backend (if needed): Python 3.12, FastAPI, full type hints, SQLite

---

## Final Check (IMPORTANT)

Before finishing, verify:

* [ ] App runs without errors
* [ ] Every button does something when clicked
* [ ] Every form submits and shows response
* [ ] Every link navigates somewhere
* [ ] No placeholder text like "lorem ipsum" or "coming soon"
* [ ] No TODO comments or unfinished code
* [ ] Mobile view works (375px width)

If any check fails — fix it before submitting.

---

Here is the website to replicate:
[https://www.stocktaper.com/](https://www.stocktaper.com/)

You have one attempt to complete the full task.
When you will finish — start backend and give me link to open frontend.
Also measure how much time it took you to complete the task and print me execution time.
```

## reddit-business-ideas.md
```markdown

## Role

Act like a senior full-stack developer who ships production-ready code.  
No shortcuts, no placeholders, no "implement later" comments.

Build a Reddit Business Idea Finder website.

---

## Requirements

1. User enters a list of subreddits (e.g., "startup, SaaS, smallbusiness")
2. Website scrapes recent posts and top comments from those subreddits
3. LLM analyzes the content — finds complaints, frustrations, pain points of users
4. Extracts viral business ideas based on real problems
5. Displays everything in a clean, easy to understand dashboard

---

## Features

- Input field for subreddits (comma separated or one per line)
- Progress indicator while scraping and analyzing
- Results provided in convenient way
- Each idea shows:
  - Problem summary
  - Source posts
  - Potential solution
  - Estimated demand
- Filter/sort ideas by relevance, recency, or engagement
- Click on idea to see original Reddit posts
- Export results as JSON or CSV

---

## Scraping

- Use Reddit API or web scraping (handle rate limits), credentials provided in `.env`
- Get posts from last 365 days by default (make configurable)
- Sort posts by upvotes to scrape only most popular posts
- Scrape post title, body, and top 10–20 comments
- Skip posts with low engagement

---

## LLM Analysis

- Send batches of posts to OpenAI API, API key provided in `.env`
- Prompt should extract:
  - What problem is described
  - How painful it seems
  - Any existing solutions mentioned
- Group similar problems together
- Generate business idea suggestions for each problem cluster

---

## Tech

- Frontend: Next.js + Tailwind
- Backend: Python 3.12, FastAPI, full type hints
- Database: SQLite for caching scraped data
- Use environment variables for API keys

---

## UI/Design

- Reddit-inspired design — familiar to Reddit users (cards, upvote-style indicators, threaded look)
- Dark mode support
- Cards for each business idea
- Expandable sections for details
- Mobile responsive

---

## Dashboard Design

- Find an interesting way to visualize ideas and connections between related problems
- Show clusters/categories — so user can see which problems are from similar areas
- Could be a network graph, mind map, 2D scatter, treemap — your choice
- Whatever you pick: it MUST work correctly, be easy to use, and actually be useful
- Make it interactive — clickable, zoomable, explorable
- Not just a list of cards. Make it something people want to play with.

---

## Final Check (IMPORTANT)

Before finishing, verify:

- [ ] Scraping works and returns real data
- [ ] LLM analysis runs without errors
- [ ] Ideas display correctly in the UI
- [ ] Filters and sorting work
- [ ] No placeholder or mock data in final version
- [ ] No TODO comments or unfinished code
- [ ] Loading states for all async operations
```
