# Christian Jimenez-Escorcia

**Staff Engineer at Liberty Energy · Co-founder of Accelerated Innovations · Nonprofit board member · Denver**

Using AI every day has helped me do things I used to think were out of reach. I built a team of agents that dreams up fantasy worlds for my kids’ [bedtime stories](https://cjimenz.github.io/bedtime-story-studio/), co-founded **Accelerated Innovations**, and started teaching engineering teams how to use AI on software they ship. I’m still the friend people call with an app idea. My favorite part is handing over the keyboard and seeing what they build.

In Denver, I give back through [Denver Energy Network](https://www.denverenergynetwork.com/). I serve on the board and build the tools our volunteers use to put on events, stay in touch with members, and bring the local energy community together.

AI is also what I tinker with for fun. Erik Nelson asked me to coffee because he wanted help building an app. I ended up teaching him how to build it himself. That conversation became [AI Coffee Shop](https://aicoffeeshop.dev), a 14-module course that takes you from your first useful prompt to building with Git, APIs, authentication, and agents.

## Current research focus

**The Agent Evolution Thesis** · My north star for building AI systems whose specialized agent lineages accumulate validated experience across short-lived executions. [Read the working thesis](https://cjimenz.github.io/CJIMENZ/agent-evolution/) · [Versioned source](docs/agent-evolution/THESIS.md)

## Selected work

**Bedtime Story Studio** · I built a continuing fantasy series for my kids, narrated it with ElevenLabs, and turned the recordings into an audio library. [Listen to the stories and read the case study](https://cjimenz.github.io/bedtime-story-studio/)

**Calcifer · Day One** · I set up four distinct AI roles around a shared work board, then measured what shipped and what still needed a human. [Read the case study and play the recap](https://cjimenz.github.io/CJIMENZ/case-studies/calcifer-day-one/)

The code for these two projects is private. The engineering notes walk through how each one works.

**Calcifer · Special Projects Build Log** · A phone-to-Blender experiment with a timed 3D workflow, editable artifacts, and lessons about when to work outside the software delivery pipeline. [Read the November 28 update](https://cjimenz.github.io/CJIMENZ/case-studies/calcifer-day-update-2026-11-28/)

**Denver Energy Network** · I built the platform our volunteers use to run events. Gmail delivers registration confirmations, QR codes, and campaigns. The site reads delivery failures back from the inbox to keep the mailing list current. [Visit DEN](https://www.denverenergynetwork.com/) · [How the Gmail integration works](engineering-notes.md#denver-energy-network--the-site-and-the-work-behind-it)

**Denver Petroleum Club** · I built a white-label site that an organizer can operate through a connected AI assistant. Once the layout is in place, the organizer can create an event, attach a sponsor, and draft its email campaign through the site’s MCP server. [Explore the build](https://denver-petroleum-club.vercel.app/) · [How the business actions work](engineering-notes.md#denver-petroleum-club--operating-a-site-through-mcp)

**AI Meeting Memory** · I wanted to record a meeting on my phone and trust that I could recover it if my transcription worker went offline. The recorder resumes interrupted uploads, workers can retry jobs, and cleanup waits until the saved transcript passes a checksum check. [System design](engineering-notes.md#ai-meeting-memory--a-recorder-that-can-recover) · [Recovery code](https://github.com/CJIMENZ/cpu-transcript-recovery/blob/main/transcribe_cpu.py)

## Across the stack

- **Application engineering.** I’ve used TypeScript, React, Next.js, and MongoDB for tutoring operations and nonprofit software. For the meeting recorder I used IndexedDB on the phone and Drizzle with Postgres on Neon. My enterprise work spans C#, .NET services, and Oracle SQL.
- **Automation and data.** I started with Excel VBA for job profitability, moved reporting pipelines into Python, and wrote thinkScript studies and scans for my own trading. Each grew out of a calculation or decision I was repeating by hand.
- **Cloud and identity.** On AWS I’ve worked on architecture using Bedrock for model access and ECS Fargate for services. On Google Cloud (GCP) I explored automating application setup and OAuth provisioning. I’ve also worked across Oracle Cloud Infrastructure (OCI) and Fusion, Microsoft 365 and Entra ID, and Vercel for web apps.
- **Model engineering.** I ran Llama on my own NVIDIA hardware, built a vision chatbot on a 64 GB Mac, and used Ollama to serve models locally. Our coaching assistant took me from PyTorch and Transformers on a Tesla T4 to hosted inference through the OpenAI API.

## How I got here

- **2016.** I graduated from Colorado School of Mines in petroleum engineering, then went into aerospace manufacturing. At CableNet I worked on rocket umbilicals and did the CAD for ground equipment used to fuel satellites before launch.
- **2018–2022.** I worked the Permian and DJ basins at Liberty and built a three-day tank-volume forecast to schedule chemical deliveries. In **November 2022**, I moved into Job Profitability and started writing Excel VBA by hand.
- **2023 onward.** With my first kid on the way, I signed up for ChatGPT to help write emails. That grew into Python reporting automation, document-grounded chat, and co-founding **Accelerated Innovations**. We built a coaching assistant with custom AI workflows and a tutoring operations suite that went from lesson requests through invoicing and tutor payroll. I earned more than 20 programming course certificates while we built.

## Open the code

- [CPU transcript recovery](https://github.com/CJIMENZ/cpu-transcript-recovery) · Validate timestamps and publish a complete transcript without replacing an existing file. [Run it on sample speech](https://github.com/CJIMENZ/cpu-transcript-recovery#try-it-with-synthetic-speech).
- [Ollama local workflows](https://github.com/CJIMENZ/ollama-local-workflows) · Add local model inference to a Python app. Conversation state advances only after a complete response. [Try the integration](https://github.com/CJIMENZ/ollama-local-workflows#use-it-in-your-application).
- [Codezilla workflow core](https://github.com/CJIMENZ/codezilla-workflow-core) · An in-memory TypeScript pilot with versioned specifications and approval rules. [Read the workflow tests](https://github.com/CJIMENZ/codezilla-workflow-core/blob/main/tests/unit/workflow-service.test.ts).
- [Food Tinder](https://github.com/CJIMENZ/Food-Tinder) · A browser-local recipe app that learns your taste from swipes.
- [Potluck Postcard](https://github.com/CJIMENZ/potluck-postcard) · A party invitation editor with calendar export.

## At Liberty Energy

I’m a **Staff Engineer – Application Support** at Liberty Energy, where I lead a development team’s technical work and serve as product owner for a logistics platform. I prototype workflows with field users, then work with QA and platform engineers through GitLab CI/CD, staging, and the production release decision. [Field pilots, QA, and releases](engineering-notes.md#liberty-energy--logistics-software)

At Liberty, I’ve trained **about 500 people on Microsoft 365 Copilot** and **about 50 on Claude**, by my estimate. Our nine-session Copilot training report recorded **69% more weekly actions and 41% more weekly active users** across the measurement window. I helped shape the adoption plan and coach engineers on taking a decision from Teams into Jira and through code review. The engineer writes the acceptance criteria, checks the diff, and owns the merge.

One of my favorite pilots turned a merge request into a **90-second before-and-after video**. Playwright captured the change, ElevenLabs narrated it, and Remotion rendered it. The clips took under five minutes of developer time each in the pilot, and stakeholders could leave feedback right where the change was being reviewed.

> “You can outsource the lookup, you can’t outsource the accountability.”

## Just for family

For my wife's birthday this year, I turned our family photo album into a page about her year, the one our daughter arrived. [Happy Birthday, Ellie](https://cjimenz.github.io/ellie-birthday/)

## Get in touch

Have an app idea or a team that wants to build with AI? Email me at [christian.jimenez0408@gmail.com](mailto:christian.jimenez0408@gmail.com).
