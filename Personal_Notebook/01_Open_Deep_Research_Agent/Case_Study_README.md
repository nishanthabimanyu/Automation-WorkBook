# Open Deep Research Agent - My Journey to a Fully Autonomous Researcher

So, here is the full story of how I built this "Deep Research" agent. I picked this up from a high-ticket Upwork client (budget was decent, $1,500). 

The requirement was actually quite simple on paper: I give a vague topic like "Future of Solid State Batteries", and the AI should go out, search the web, read articles, and write a full, cited report without me holding its hand.

Basically, I wanted to automate the boring part of research.

## 1. The Reality Check (It was not easy, ya)
At first, I thought, "Easy peasy, I will finish this in one weekend." 
But actually, it was quite tough. I started connecting everything—SerpAPI for Google search, standard scrapers, OpenAI... and it was a mess.

**The problems I faced:**
*   **Too much noise:** The AI was reading garbage data from websites and getting confused.
*   **Hallucinations:** Sometimes it would just make up facts because it forgot the context.
*   **API Limits:** My API bill was going up like anything because I was sending too much text to ChatGPT.

I realized that just connecting nodes is not enough. You need a proper system.

## 2. The Solution (How I actually fixed it)
I was stuck, so I asked around in the n8n community. I realized I was building a "Pipeline" (do A, then B, then C) when I needed an "Agent" (Think, then Do, then Check).

So, I completely changed the architecture. Here is exactly what I did:

### Step 1: The Planner (The Brain)
Instead of just searching for the keyword directly, I added an LLM node at the start. 
This node "thinks" first. If I ask for "EV Batteries", it breaks it down:
*   "I need to search for current costs."
*   "I need to check safety standards."
*   "I need to find recent breakthroughs."
It creates 4 distinct search angles. This makes the research much deeper.

### Step 2: Jina AI (The Cleaner)
This was the game changer. Scraping raw HTML from websites is a headache; there are too many ads and popups.
I used Jina AI. It takes a website and converts it into clean, simple Markdown text. 
*   **Before:** Huge HTML mess with scripts and ads.
*   **After:** Clean text that the AI can actually understand.
This improved the quality of the report by 100%.

### Step 3: Batching (Slow and Steady)
You can't just throw 20 websites at OpenAI at once. It will choke or crash.
I used the SplitInBatches node (Loop). The workflow processes 3-4 websites at a time, summarizes them, and then moves to the next batch. This keeps it stable and cheap.

## 3. What Can This Agent Do?
Now that it is working, here is what it can handle:

*   **Autonomously Plan:** You give a one-line topic; it creates the research plan.
*   **Deep Web Search:** It uses SerpAPI to find the best articles, not just the first one.
*   **Read & Understand:** It reads the full content (thanks to Jina AI), not just the Google snippet.
*   **Write Reports:** It synthesizes everything into a professional document.
*   **Cite Sources:** It tells you exactly where it got the information (very important for clients).

## 4. The "Human-in-the-Loop" (Don't trust blindly)
Look, AI is smart, but it is not perfect. I made sure the workflow outputs a Draft.
The idea is: The AI does 95% of the heavy lifting (searching, reading, summarizing), but a Human must review the final report. 

We cannot blindly trust it 100% yet. But frankly, it saves hundreds of hours of manual work.

## 5. Outcome
Now, I can just put in a topic, go for a chai, and come back to a comprehensive research document waiting for me. 

It was a steep learning curve, but totally worth it!
