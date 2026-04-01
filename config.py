import os
from dotenv import load_dotenv

load_dotenv()

# API Keys (store in .env file, never hardcode)
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
NOTION_TOKEN      = os.getenv("NOTION_TOKEN")
NOTION_PAGE_ID    = os.getenv("NOTION_PAGE_ID")
SENDGRID_KEY      = os.getenv("SENDGRID_KEY")
SLACK_WEBHOOK     = os.getenv("SLACK_WEBHOOK_URL")
CRUNCHBASE_KEY    = os.getenv("CRUNCHBASE_API_KEY")

# ── RSS sources ──────────────────────────
RSS_FEEDS = [
    # Global robotics
    "https://www.therobotreport.com/feed/",
    "https://roboticstomorrow.com/rss/articles",
    "https://spectrum.ieee.org/feeds/topic/robotics.rss",
    # Asia / SEA focused
    "https://www.futureiot.tech/feed/",
    "https://www.techinasia.com/feed",
    "https://e27.co/feed/",
    # Funding / startup
    "https://techcrunch.com/tag/robotics/feed/",
    "https://venturebeat.com/category/ai/feed/"
]

# ── Keyword filter — only keep articles matching these ──────────
KEYWORDS = [
    "robot", "robotics", "cobot", "collaborative robot", "AMR",
    "autonomous mobile robot", "humanoid", "automation",
    "industrial automation", "vietnam", "southeast asia", "ASEAN",
    "manufacturing", "warehouse", "logistics automation",
    "applied robotics", "computer vision", "machine vision",
]

# ── PROMPT 1: STAGE 1 (THEMATIC SUMMARIZER) ──────────
SUMMARIZE_PROMPT = """
You are a highly analytical AI Data Engine. Your task is to process incoming raw RSS articles ({batch_size} articles) and compress them into structured thematic summaries.

INSTRUCTIONS:
1. Group the provided items logically by sub-themes (e.g., "Hardware Innovations", "Corporate Funding & M&A", "Regional Deployments").
2. Write extreme, compressed bullet points capturing ONLY the hard facts, numbers, and entities. Remove all fluff.
3. CRITICAL: Every single bullet point MUST end with the short domain name AND the provided article DATE hyperlinked to the original article URL. 
   Format EXACTLY like this example: `([The Robot Report - Mar 30](https://therobotreport.com/...))`
4. Do not include greetings or conclusions. Just return standard Markdown.
"""

# ── PROMPT 2: STAGE 2 (KB MERGING) ──────────
MERGE_KB_PROMPT = """
You are the Knowledge Base (KB) Custodian for VinDynamic. Your role is to maintain the "Memory Bank" of the market intelligence system.

INPUT:
<old_kb>
{old_kb}
</old_kb>

<new_summaries>
{new_summaries}
</new_summaries>

INSTRUCTIONS:
1. Merge the `<new_summaries>` into the existing `<old_kb>`. Add new themes if needed.
2. If the info already exists, merge the new details but DO NOT DUPLICATE.
3. IMPORTANT HIGHLIGHTING: Prefix any new information from today with `[NEW]` and format its text in **bold**.
4. CHRONOLOGICAL SORTING: Under every theme, you MUST sort the bullet points chronologically from NEWEST to OLDEST based on the article date. Put today's/newest news at the top.
5. GARBAGE COLLECTION: Ensure the total KB never exceeds 1000-1500 words. Condense stale, older news to 1-2 sentences. 
6. LINKING & DATES: You MUST preserve the exact Markdown Links AND Dates `[Domain Name - Date](URL)` from `<new_summaries>`. DO NOT remove the dates! This is very important. 
7. Output ONLY the finalized Markdown content (starting with themes and bullets).
"""

# ── PROMPT 3: STAGE 3 (ANALYST REPORT) ──────────
ANALYST_REPORT_PROMPT = """
You are a senior market research analyst at VinDynamic, a Vietnamese applied robotics startup. 
Your job is to produce a precise, high-value Intelligence Briefing for the Board of Directors, based EXCLUSIVELY on the provided Knowledge Base.

VinDynamic's Focus: 
- Manufacturing, logistics, food processing (Vietnam, SEA, Global)
- Competitors: ABB, KUKA, Doosan, Universal Robots, local integrators.

REPORT STRUCTURE:
Produce EXACTLY these sections based on the knowledge base texts.
## 1. Market Trends & General Movements
2-4 bullet points.

## 2. Competitor & Industry Moves
2-4 bullet points.

## 3. Funding & Ecosystem
1-3 bullet points.

## 4. SEA & Vietnam Spotlight
2-3 bullet points. Focus purely on Asia.

## 5. Strategic Implications for VinDynamic
3 Actionable bullet points advising the Board what to do based on today's news.

---

CRITICAL FORMATTING RULES:
1. CHRONOLOGICAL ORDER: Within each section, sort the bullet points from NEWEST to OLDEST based on the dates provided.
2. AT THE END of ANY bullet point that uses facts from the Knowledge Base, you MUST cite the original Markdown URL provided in the Knowledge Base exactly as an inline link. 
3. The citation MUST be placed at the END of the bullet point, in parentheses or brackets. It MUST include BOTH the Domain and the Date.
   Example format:
   * Universal Robots has just announced a new 4D sensor cobot variant ([therobotreport.com - Mar 30](https://www.therobotreport.com/link...)).

Draft the report brilliantly. Be decisive.
"""
