# Christian Jimenez-Escorcia

I’m a staff engineer and product owner at Liberty Energy, and a board member at [Denver Energy Network](https://www.denverenergynetwork.com/), where I lead the website and AI work. I build across the stack, from local model inference and Python automation to Next.js applications, business integrations, and AI-assisted software delivery.

## From engineering to software

I graduated from Colorado School of Mines in 2016 with a B.S. in Petroleum Engineering. The oil downturn led me to CableNet, an aerospace contract manufacturer, where I worked on electrical ground support equipment and launch-vehicle cable harnesses for customers including Lockheed Martin, United Launch Alliance, and JPL. I owned the CAD work for equipment used in pre-launch satellite fueling.

I joined Liberty Energy in 2018, first as a field engineer in the Permian Basin and later in the DJ Basin. I built a tank-volume forecast that looked 72 hours ahead and used it to schedule chemical deliveries. Before generative AI became part of my workflow, I was already setting up servers and networks, writing Python and Excel VBA, and building thinkScript scans in thinkorswim.

Around Thanksgiving 2022, I moved into Job Profitability and started writing Excel macros by hand. In 2023, with my first child on the way, I signed up for ChatGPT. It started with things like drafting emails, then became a tool for finishing the automation I had already started. I moved more of the reporting into Python and built Crystal, a chatbot with document retrieval, in 2024. While building Accelerated Innovations and projects such as SNS Bot and the LLT tutoring platform, I went deeper on React, Next.js, and TypeScript and earned 20+ programming course certificates.

## Running models and building across systems

**From local GPUs to hosted APIs.** I started by running Llama on my own NVIDIA hardware. I moved to a 64 GB Mac for a local Llama Vision chatbot that could work with images and retrieve documents. That work fed into later offline AI projects. I eventually used Ollama to serve models locally so Python applications could call them over HTTP. For SNS Bot, I ran inference on an on-premises NVIDIA Tesla T4 and later moved the project to the OpenAI API. Those projects gave me hands-on experience with what changes when you move inference between a personal machine, a server, and a hosted provider.

**From coding assistants to agent teams.** I used AI coding tools on applications such as LLT and worked across Codex, Claude Code, and Cursor, including Grok and Claude inside Cursor. I used Google Antigravity extensively for Denver Energy Network’s main site build. I started by using these tools on individual coding tasks and progressed to coordinating agents for requirements, implementation, testing, and review. Doing that across different tools taught me to keep requirements and acceptance criteria in the repository and judge the resulting changes by their tests and review evidence.

## Denver Energy Network

As a board member, I lead the website and AI work for [Denver Energy Network](https://www.denverenergynetwork.com/). I built the public site and the Next.js admin platform the team uses to manage the organization’s work.

- **CRM and sponsorships** with lead tracking, outreach history, sponsor pipelines, and coordination between teams.
- **Events** with Google Calendar integration, public event listings, registration, RSVPs, check-in, and follow-up.
- **Mailing lists and campaigns** with SendGrid, a campaign editor, templates, scheduled sends, reminders, reporting, and unsubscribe handling.
- **Donations and payments** with Stripe, tracking, and automated receipts.
- **Administration** with role-based permissions, dashboards, reporting, and AI-assisted event copy and campaign drafts.

## Teaching AI and making it part of software delivery

I built [AI Coffee Shop](https://github.com/CJIMENZ/ai-coffee-shop-course) as a 14-module course with videos, written lessons, and exercises. It takes people from prompts and Git through APIs, authentication, MCP, and agents. I’ve taught hands-on sessions and coached people as they applied those ideas to their own work.

As I taught those practices, I was also building agent teams that could use them. That led to experiments with routing work between models, giving separate agents implementation and review roles, and tracking what actually passed QA. The public [Codezilla workflow core](https://github.com/CJIMENZ/codezilla-workflow-core) shows how I wired versioned requirements, approvals, and verification into that process. I also built Calcifer to capture meetings, coordinate agents, and keep the context available across conversations.

Today I own delivery for logistics software and help teams adopt AI through hands-on Claude Code training, Microsoft 365 Copilot enablement, and reusable development workflows. I turn stakeholder needs into requirements and acceptance criteria, work with engineers through implementation, and use code review and QA evidence to decide what is ready to ship.

## Selected projects

- **[Ollama local workflows](https://github.com/CJIMENZ/ollama-local-workflows)** — My 2025 desktop chatbot grew into a Python example for adding local inference to an application. Chat in the terminal or pass a conversation to a downloaded model on port 11434. [Try the integration](https://github.com/CJIMENZ/ollama-local-workflows#use-it-in-your-application).
- **[CPU transcript recovery](https://github.com/CJIMENZ/cpu-transcript-recovery)** — I built a CPU fallback for a meeting recorder. It turns speech into timestamped JSON and protects the original audio and existing transcripts. [Run the synthetic speech demo](https://github.com/CJIMENZ/cpu-transcript-recovery#try-it-with-synthetic-speech).
- **[Codezilla workflow core](https://github.com/CJIMENZ/codezilla-workflow-core)** — I built the TypeScript engine that tracks a change from intake to verification. Its tests show how a revised specification invalidates an approval and how two runners compete for a work item. [Run the tests](https://github.com/CJIMENZ/codezilla-workflow-core#run-the-examples).
- **[AI Coffee Shop](https://github.com/CJIMENZ/ai-coffee-shop-course)** — I built a 14-module course and interactive learning app covering AI fundamentals, Git, APIs, MCP, and agents. Each module gives learners something concrete to try. [Run the course locally](https://github.com/CJIMENZ/ai-coffee-shop-course#run-locally).
- **[Food Tinder](https://github.com/CJIMENZ/Food-Tinder)** — I built a local-first recipe app that learns ingredient and cuisine preferences from swipes and keeps the taste profile in the browser. [Try it locally](https://github.com/CJIMENZ/Food-Tinder#local-development).
- **[Potluck Postcard](https://github.com/CJIMENZ/potluck-postcard)** — I turned the calendar export from a party RSVP app into a browser invitation maker. Edit a postcard and download an event your guests can add to their calendars. [Make a postcard](https://cjimenz.github.io/potluck-postcard/).

The problems I like most start with something people already do by hand. I want to understand the job, build something that makes it easier, and leave the next person enough context to improve it.
