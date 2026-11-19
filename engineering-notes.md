# Engineering case studies

[Back to the profile](README.md)

## Liberty Energy · Logistics software

**From field testing to a production decision.** I’m the product owner for a logistics platform that planners, dispatchers, and carriers use to coordinate loads. I build working UI prototypes when the team needs to settle a workflow with field users. I turn the feedback into acceptance criteria and work with frontend, backend, QA, and DevOps to get the change through staging. I do stage acceptance and help make the call on whether to go to production. That work includes triaging field issues, writing incident follow-ups, and feeding regressions back into QA.

**A decision the software had to support.** How many drivers should dispatch add or remove as consumption changes? I worked on an approach that uses live consumption to estimate demand and projects inventory against deliveries already in motion. It puts driver demand and reorder timing in the same conversation, so dispatchers can act on where inventory is headed.

**Teaching the workflow.** I helped shape enterprise Claude adoption and coached engineers on how to work from a Jira ticket, give an agent bounded repository context, and verify the result. We piloted sending stakeholders a narrated before-and-after view of a UI change. Playwright supplied the screenshots, ElevenLabs supplied the voice, and Remotion rendered the clip. Acceptance criteria, diff review, tests, and merge approval stay with the engineering team.

## AI Meeting Memory · A recorder that can recover

I built a mobile meeting recorder with a Next.js frontend, private object storage for audio, and Postgres for processing state, transcripts, and summaries. The browser keeps recording chunks locally while they upload. A worker claims a leased job, writes the timestamped transcript, and verifies the persisted checksum before audio cleanup is allowed. Summarization is a separate step, so a failed summary can retry from the saved transcript.

I built an OAuth-secured MCP interface with scoped access. I verified the migrations on an isolated Postgres branch and ran 16 server integration checks against test Postgres and object storage. Those checks covered concurrent job claims, resumable uploads, and rejection of premature audio deletion. A Chromium test covered recording and upload with synthetic audio.

**Public code I can walk through.** The [CPU fallback](https://github.com/CJIMENZ/cpu-transcript-recovery) takes a local recording and writes timestamped JSON. The [publication step](https://github.com/CJIMENZ/cpu-transcript-recovery/blob/main/transcribe_cpu.py#L27) writes a temporary file and uses an atomic hard link to claim the output path. If another run gets there first, the existing transcript and the source audio survive. The full application source is private.

## Denver Energy Network · The site and the work behind it

As a board member I lead the website and AI work. I built the Next.js and MongoDB platform around what the volunteers do between events. One team tracks sponsor outreach, another drafts and schedules SendGrid campaigns, and volunteers register and check in guests. The admin tools carry each event from a Google Calendar entry through registration, QR check-in, and follow-up. The same platform includes role-based access, Stripe payments and webhook handling, automated receipts, and AI-assisted campaign drafts.

The [public site](https://www.denverenergynetwork.com/) shows the events and the community signup. The admin source is private.
