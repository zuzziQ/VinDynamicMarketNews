# User Guide: How the VinDynamic AI Agent Works

This document explains the inner workings of the VinDynamic Artificial Intelligence (AI) system using simple, non-technical language. You can think of the core system as a **miniature newsroom run by three exceptional digital employees**.

---

## Stage 1: The News Gatherer (Data Pipeline)
Every day, thousands of articles are published on the internet. Instead of you manually reading each site, the system dispatches a "news gatherer":
- This gatherer carries a **list of target websites** (RSS Sources) that you have provided.
- They also carry a **List of Keywords** (like "robot", "vietnam", "automation").
- They scan the websites. If an article contains at least one target keyword, they grab it. If the article mentions regions like Vietnam, Singapore, or ASEAN, they stick a **"Regional News"** label on it. Otherwise, it simply gets a **"Global News"** label.
- Finally, they throw away any articles that the system has already read on previous days (using a Memory Log), keeping only **brand-new, unseen information**.

---

## Stage 2: The Speed Reader (Stage 1 AI)
At this point, the newsroom might have acquired dozens of long, complex articles. Handing all of this raw text to the Chief Editor would be too time-consuming and expensive.
- The system hands the stack of articles to a "Speed Typist/Secretary" (powered by a fast, cost-effective AI called Claude Haiku).
- The secretary reads everything rapidly, slices the information, and summarizes it into the shortest possible bullet points. They carefully record exactly which website and URL each bullet point came from.

---

## Stage 3: The Memory Keeper (Stage 2 AI)
After the Secretary finishes typing the rough summaries, they are passed down to "The Librarian" (also powered by Claude Haiku).
- The Librarian maintains a massive ledger called the **Knowledge Base**. This ledger remembers all market movements and historical context from previous days.
- The Librarian merges today's fresh summaries into the ledger. For every brand-new piece of intel, they use a highlighter to mark it clearly with **`[NEW]`**. 
- To prevent the ledger from becoming bloated and costing too much money to read, the Librarian actively erases or condenses very old, stale news.

---

## Stage 4: The Chief Strategist (Stage 3 AI)
This is where the most important figure steps in: The **Senior Analyst** (powered by the highly intelligent Claude 3.5 Sonnet).
- The Analyst doesn't waste time reading the messy junk from the internet. They **work EXCLUSIVELY by reading the pristine "Knowledge Base"** ledger prepared by the Librarian.
- Relying on the ledger's organized [Global] and [Regional] sections, the Analyst drafts a flawless **Market Intelligence Briefing**:
  - They begin by outlining broad global market trends.
  - They then isolate the "Regional News" and write a dedicated *SEA & Vietnam Spotlight* section.
  - Finally, they formulate actionable strategic advice for the company's Board of Directors.
  - Every single fact is **transparently cited** with an inline hyperlink, directly pointing back to the original source article.

---

## Stage 5: Publishing (The PDF Generator)
Finally, the system's "printing press" takes the brilliant text written by the Analyst, formats it beautifully into a structured report, and exports it as a PDF file named `VinDynamic_Strategy_Day_Month_Year.pdf`. This file is ready for you to email to stakeholders or archive internally!

> **Core Value Summary:** This workflow ensures that the system **never forgets historical context**, strictly separates **domestic vs. international news**, and **maximizes cost-efficiency** by letting a cheap AI (Haiku) handle the heavy lifting, reserving the expensive expert AI (Sonnet) only for the final strategic report.
