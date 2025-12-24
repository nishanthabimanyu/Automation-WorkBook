# 📂 Project Name: [Insert Title Here]

**Category:** [e.g. Lead Generation / Chatbot / Data Scraping]
**Tools Used:** n8n, [Tool A], [Tool B]

---

## 📝 1. The Job Description (The "Ask")
*(Paste the original Upwork job description or your simulated prompt here. This shows you understand the client's language.)*

> **Client:** "I need an automation that takes leads from a Google Sheet, finds their email on Apollo, and adds them to Hubspot..."

---

## 🎯 2. My Interpretation & Scope
*(Here is where you show your expertise. Breakdown the request into technical requirements.)*

*   **Goal:** Automate lead enrichment and CRM syncing.
*   **Triggers:** New row in Google Sheet.
*   **Actions:**
    1.  API Call to Apollo.io.
    2.  Data Formatting.
    3.  Upsert to HubSpot.
*   **Edge Cases:** What if the email is missing? What if the contact exists?

---

## 🧠 3. The Plan (My Personal Notebook)
*(This is the "Notebook" part. Explain your thought process. Why did you choose this path?)*

*   *Initial Thought:* I considered using Zapier, but n8n handles the complex error handling better.
*   *Logic:* I need to use the `SplitInBatches` node because Apollo has a rate limit.
*   *Architecture:* 
    *   Step 1: Watch Google Sheet.
    *   Step 2: Check if processed column is empty (to avoid loops).
    *   Step 3: ...

---

## 📸 4. The Solution (Visuals)

### The Bird's Eye View
*(Place a screenshot of the full n8n workflow here. Save images in the `assets/` folder.)*
![Workflow Overview](./assets/workflow_overview.png)

### Key Node Configurations
*(Highlight specific tricky parts, like a complex HTTP Request or a Function Item node.)*
![HTTP Request Setup](./assets/http_setup.png)

---

## ⚙️ 5. How to Run This
1.  **Download:** Get the `workflow.json` from this folder.
2.  **Import:** Open n8n > Import Workflow.
3.  **Credentials:** You will need API keys for:
    *   Service A
    *   Service B

---

## 💡 6. Results & Impact
*   **Time Saved:** Estimated 5 hours/week.
*   **Efficiency:** 100% accuracy in data entry.
