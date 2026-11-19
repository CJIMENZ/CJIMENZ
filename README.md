# Christian Jimenez-Escorcia

**Software founder · Consultant · Nonprofit board member**

I co-founded **Accelerated Innovations** to build software around the way people actually work. As a consultant, I help teams figure out what to build and make it tangible, from scoping a document-sharing portal to prototyping an app for dispatchers and drivers.

In Denver, I give back through [Denver Energy Network](https://www.denverenergynetwork.com/). I serve on the board and build the tools our volunteers use to put on events, stay in touch with members, and bring the local energy community together.

AI is also what I tinker with for fun. Erik Nelson asked me to coffee because he wanted help building an app. I ended up teaching him how to build it himself. That conversation became [AI Coffee Shop](https://github.com/CJIMENZ/ai-coffee-shop-course), a 14-module course that takes you from your first useful prompt to building with Git, APIs, authentication, and agents.

[Engineering case studies](engineering-notes.md)

## 01 / Selected engineering work

| System | What I did | Where to look |
| --- | --- | --- |
| **Denver Energy Network** | As a board member, I lead the website and AI work. I built the Next.js site and admin tools for CRM, sponsorships, campaigns, registration and QR check-in, and Stripe payments and receipts. | [Live site](https://www.denverenergynetwork.com/) · [Behind the site](engineering-notes.md#denver-energy-network--the-site-and-the-work-behind-it) |
| **AI Meeting Memory** | Built a mobile recorder with resumable uploads, a Postgres job queue, and OAuth for connecting assistants. A worker can retry processing, and audio cleanup waits on a verified transcript. | [System design and verification](engineering-notes.md#ai-meeting-memory--a-recorder-that-can-recover) · [Public recovery code](https://github.com/CJIMENZ/cpu-transcript-recovery/blob/main/transcribe_cpu.py) |

## 02 / How I got here

- **2016.** I graduated from Colorado School of Mines in petroleum engineering, then went into aerospace manufacturing. At CableNet I worked on rocket umbilicals and did the CAD for ground equipment used to fuel satellites before launch.
- **2018–2022.** I worked the Permian and DJ basins at Liberty and built a three-day tank-volume forecast to schedule chemical deliveries. In **November 2022**, I moved into Job Profitability and started writing Excel VBA by hand.
- **2023 onward.** With my first kid on the way, I signed up for ChatGPT to help write emails. That grew into Python reporting automation, document-grounded chat, and co-founding **Accelerated Innovations**. We built a coaching assistant with custom AI workflows and a tutoring operations suite that went from lesson requests through invoicing and tutor payroll. I earned more than 20 programming course certificates while we built.

I’ve run Llama on my own NVIDIA hardware, built a vision chatbot on a 64 GB Mac, served models through Ollama, and moved a prototype from an on-premises Tesla T4 to OpenAI’s API. I’ve worked in Codex, Claude Code, Cursor with Claude and Grok, and used Antigravity to build Denver Energy Network’s site.

## 03 / Open the code

- [CPU transcript recovery](https://github.com/CJIMENZ/cpu-transcript-recovery) · Validate timestamps and publish a complete transcript without replacing an existing file. [Run it on sample speech](https://github.com/CJIMENZ/cpu-transcript-recovery#try-it-with-synthetic-speech).
- [Ollama local workflows](https://github.com/CJIMENZ/ollama-local-workflows) · Add local model inference to a Python app. Conversation state advances only after a complete response. [Try the integration](https://github.com/CJIMENZ/ollama-local-workflows#use-it-in-your-application).
- [Codezilla workflow core](https://github.com/CJIMENZ/codezilla-workflow-core) · An in-memory TypeScript pilot with versioned specifications and approval rules. [Read the workflow tests](https://github.com/CJIMENZ/codezilla-workflow-core/blob/main/tests/unit/workflow-service.test.ts).
- [Food Tinder](https://github.com/CJIMENZ/Food-Tinder) · A browser-local recipe app that learns your taste from swipes.
- [Potluck Postcard](https://github.com/CJIMENZ/potluck-postcard) · A party invitation editor with calendar export.

## 04 / At Liberty Energy

Of course, I need a day job too. I’m a **Staff Engineer – Application Support** at Liberty Energy, where I lead a development team’s technical work and serve as product owner for a logistics platform. I prototype workflows with field users, build across React, .NET/C#, and Oracle, and work with QA and platform engineers to test in staging and decide what’s ready for production. [Field pilots, QA, and releases](engineering-notes.md#liberty-energy--logistics-software)

At Liberty, I’ve trained **about 500 people on Microsoft 365 Copilot** and **about 50 on Claude**, by my estimate. Our nine-session Copilot training report recorded **69% more weekly actions and 41% more weekly active users** across the measurement window. I also helped shape Claude adoption and coached engineers through a delivery workflow that takes work from Teams to Jira to a repository, with humans writing the acceptance criteria, reviewing the diff, and owning the merge.

One of my favorite pilots turned a merge request into a **90-second before-and-after video**. Playwright captured the change, ElevenLabs narrated it, and Remotion rendered it. The clips took under five minutes of developer time each in the pilot, and stakeholders could leave feedback right where the change was being reviewed.

> “You can outsource the lookup, you can’t outsource the accountability.”
