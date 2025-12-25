# Open Deep Research - My Journey to an Autonomous Agent

I picked up a challenge to build a "Deep Research" agent for a high-ticket Upwork client ($1,500 budget). The goal? A system that could take a vague topic like "Future of Solid State Batteries" and write a full, cited report without me holding its hand.

## 1. The Reality Check (Drowning in Tutorials)
I thought this would be a quick weekend project. I was wrong.

I started down the rabbit hole of APIs. SerpAPI for search, Jina AI for scraping, OpenAI for reasoning... I spent days just drowning in tutorials and documentation. Every time I fixed one thing, another broke. 

*   "How do I handle pagination?" 
*   "Why does the LLM forget the context halfway through?"
*   "My API bill is exploding!"

I realized that **robustness** isn't just about connecting nodes; it's about handling the messiness of the real web.

## 2. The Discord Query
I was stuck. My workflow was a fragile house of cards. So, I jumped into the n8n Discord and basically vented:
> "Guys, I'm drowning here. My agent either hallucinates or crashes when I try to scrape 10+ pages. How do you actually make this *production-ready*?"

## 3. The Turning Point
A friend (shoutout to the community!) pointed out that I was thinking too linearly.
> "You're trying to build a pipeline. You need an **Agentic Loop**. 
> 1.  **Planner vs. Doer:** Separate the logic that *plans* the search from the logic that *writes* the report.
> 2.  **Jina AI is key:** Don't scrape raw HTML. Use Jina to get clean Markdown so your LLM doesn't choke.
> 3.  **Batching:** If you don't use `SplitInBatches`, you'll hit rate limits instantly."

## 4. The Revised Architecture
Taking that advice, I completely re-engineered the flow to ensure it met the client's strict specifications for autonomy and depth.

![Workflow Screenshot](./assets/workflow_screenshot.png)

### Key Improvements:
1.  **The Planner:** A dedicated LLM node that "thinks" before it acts, generating 4 distinct search angles.
2.  **Robust Scraping:** Chaining SerpAPI into Jina AI meant I got high-quality data, not just noise.
3.  **Batch Processing:** I implemented loops to process results in chunks. This was crucial for handling large datasets without crashing.

## 5. The Need for "Human-in-the-Loop"
Even with all this automation, I realized something important: **AI isn't perfect.** 

To truly solve the client's problem, I added a "Human-in-the-Loop" philosophy. While the agent does 95% of the heavy lifting (searching, reading, summarizing), a human should always review the final report. The workflow is designed to output a draft that is *ready for review*, not necessarily ready to publish. This ensures accuracy while saving hundreds of hours of manual work.

## 6. Outcome
The final result is a beast. It solves the Upwork brief perfectly:
*   **Think:** Breaks down complex topics.
*   **Hunt & Read:** Autonomously gathers real data.
*   **Synthesize:** Writes a professional report.

I can now give it a topic, go grab a coffee, and come back to a comprehensive research document. It was a steep learning curve, but totally worth it.
