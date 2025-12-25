# Telegram AI Agent with Long-Term Memory (DeepSeek V3)

Here is another interesting project I worked on. This one is very popular on Upwork right now.

**The Client's Problem:**
The client was building a personal coaching bot on Telegram. They had a big issue: The bot was forgetting everything.

> "If a user tells the bot 'I am vegetarian' on Monday, and then asks for a recipe on Friday, the bot forgets and suggests steak. This is useless for us."

Also, they wanted to stop using GPT-4 because it is too expensive. They specifically asked for DeepSeek V3 (which is much cheaper and very smart).

## 1. My Thought Process (Why simple memory is hard)
Building a chatbot is easy. Building a chatbot that remembers is hard.

Usually, people use a simple "Window Buffer" memory. This only remembers the last 5-10 messages. Once you close the chat or talk too much, the bot forgets your name, your goals, everything.

For this project, I needed a Long-Term Memory storage. I thought about using fancy vector databases like Pinecone, but for this client, it was overkill. 
I decided to use Google Docs as a simple, reliable memory store. It is easy to debug (you can just open the doc and read what the bot knows).

## 2. The Solution (How I built it)

I created an n8n workflow that acts like a real personal assistant.

### Step 1: The Gatekeeper (Security)
First, the bot checks who is talking. 
*   It compares the Telegram User ID with a trusted list. 
*   If a random stranger tries to talk to the bot, it says "Access Denied." 
This keeps the bot private and secure.

### Step 2: The Brain (DeepSeek V3)
Instead of OpenAI's GPT-4, I used the DeepSeek V3 model.
*   **Cost:** It is way cheaper.
*   **Setup:** Since DeepSeek is "OpenAI Compatible", I just used the standard OpenAI node in n8n but changed the Base URL to https://api.deepseek.com. Simple swap!

### Step 3: Long-Term Memory (Google Docs)
This is the magic part.
1.  **Read First:** Before the bot answers, it goes to a specific Google Doc and reads the "User Profile."
2.  **Think & Answer:** It uses that info (e.g., "User is vegetarian") to generate the answer.
3.  **Update:** If the user says something new (e.g., "I started running today"), the bot uses a tool to write this new fact into the Google Doc.

## 3. The Result
Now, the bot is actually useful.
*   **Monday:** "I am vegetarian." -> Bot saves this to Google Doc.
*   **Friday:** "Give me a dinner recipe." -> Bot checks Doc -> "Here is a nice Tofu Stir-fry recipe for you!"

The client was super happy because it solves the "Context" problem and saves them money on API bills.

## 4. Key Features
*   **Multi-Modal:** Handles Text, Audio (Voice Notes), and Images.
*   **Cheap:** Uses DeepSeek V3 instead of GPT-4.
*   **Permanent Memory:** Remembers facts forever, not just for the session.