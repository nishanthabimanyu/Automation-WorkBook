# Automating Sales Research with AI (My Experience)

Hi everyone! 👋

So, I want to share this really cool project I worked on recently. It’s for a B2B agency that uses **Pipedrive** for their sales.

## 1. The Problem (Why I built this)
Basically, the client had a big issue. Their sales team was wasting *so much time* (like 20 minutes per lead!) just visiting websites to figure out what a company actually does.

They were doing manual research like:
*   Opening the website.
*   Reading the "About Us" page.
*   Trying to guess the target market.

I thought, "Why are we doing this manually? AI can read faster than us." So, I decided to build a bot that does the homework for them.

## 2. How I Solved It
I built an automation in **n8n** that runs automatically.

Here is the flow I created:
1.  **Trigger:** Whenever a new "Organization" is added in Pipedrive.
2.  **Scraping:** I used **ScrapingBee** (because normal scraping gets blocked easily) to grab the text from their website.
3.  **The AI Part:** I sent that text to **GPT-4o**. I gave it a specific prompt: *"Tell me the USP, the target market, and who their competitors are."*
4.  **Saving it:** The AI writes a nice summary and saves it as a **Note** right inside Pipedrive.
5.  **Alert:** It also sends a message to Slack, so the sales team sees it immediately.

## 3. The Result
Honestly, it turned out great.
Now, the sales guys don't have to "lurk" on websites anymore. By the time they check Pipedrive, the research is already done for them. It saves them hours every week.

It was a fun project to build because it actually solves a real boring task!

## 4. Tech Stack I Used
*   **n8n** (obviously!)
*   **Pipedrive CRM**
*   **OpenAI GPT-4o**
*   **ScrapingBee**
*   **Slack**
