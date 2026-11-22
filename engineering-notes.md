# Engineering case studies

[Back to the profile](README.md)

## Calcifer · Day One

I gave a team of agents separate roles, a shared Board, and an auditable handoff. The [case study and animated recap](case-studies/calcifer-day-one/) report the first day’s results and distinguish shipped routing infrastructure from unattended pickup still under test.

## Liberty Energy · Logistics software

**From field testing to a production decision.** I’m the product owner for a logistics platform that planners, dispatchers, and carriers use to coordinate loads. I build working UI prototypes when the team needs to settle a workflow with field users. I turn the feedback into acceptance criteria and work with frontend, backend, QA, and DevOps to get the change through staging. I do stage acceptance and help make the call on whether to go to production. That work includes triaging field issues, writing incident follow-ups, and feeding regressions back into QA.

**A decision the software had to support.** How many drivers should dispatch add or remove as consumption changes? I worked on an approach that uses live consumption to estimate demand and projects inventory against deliveries already in motion. It puts driver demand and reorder timing in the same conversation, so dispatchers can act on where inventory is headed.

**Teaching the workflow.** I helped shape enterprise Claude adoption and coached engineers on how to work from a Jira ticket, give an agent bounded repository context, and verify the result. We piloted sending stakeholders a narrated before-and-after view of a UI change. Playwright supplied the screenshots, ElevenLabs supplied the voice, and Remotion rendered the clip. Acceptance criteria, diff review, tests, and merge approval stay with the engineering team.

## AI Meeting Memory · A recorder that can recover

I built a mobile meeting recorder with a Next.js frontend, private object storage for audio, and Postgres for processing state, transcripts, and summaries. The browser keeps recording chunks locally while they upload. A worker claims a leased job, writes the timestamped transcript, and verifies the persisted checksum before audio cleanup is allowed. Summarization is a separate step, so a failed summary can retry from the saved transcript.

I built an OAuth-secured MCP interface with scoped access. I verified the migrations on an isolated Postgres branch and ran 16 server integration checks against test Postgres and object storage. Those checks covered concurrent job claims, resumable uploads, and rejection of premature audio deletion. A Chromium test covered recording and upload with synthetic audio.

**Public code I can walk through.** The [CPU fallback](https://github.com/CJIMENZ/cpu-transcript-recovery) takes a local recording and writes timestamped JSON. The [publication step](https://github.com/CJIMENZ/cpu-transcript-recovery/blob/main/transcribe_cpu.py#L27) writes a temporary file and uses an atomic hard link to claim the output path. If another run gets there first, the existing transcript and the source audio survive. The full application source is private.

## Denver Energy Network · The site and the work behind it

As a board member, I built the site around how our volunteers run an event. Someone registers on the site, gets a confirmation with their QR code through Gmail, and checks in with that code at the door. The same event record supports reminders and attendee follow-up. Alongside it, the team manages sponsors, mailing lists, Google Calendar events, and Stripe payments and receipts. [Visit Denver Energy Network](https://www.denverenergynetwork.com/)

Gmail is part of the application in both directions. The campaign scheduler sends through the Gmail API in batches and tracks recipients so an interrupted send can resume. Going the other way, the site checks the connected inbox for delivery failures and suppresses bounced addresses in the mailing list. Volunteers can manage a campaign from the site and the results feed back into the list they’ll use next time.

## Denver Petroleum Club · Operating a site through MCP

I built a white-label Next.js site for the club and gave it a Model Context Protocol (MCP) server for the work that happens after the layout is in place. An organizer can ask a connected assistant to create an event, attach a sponsor, and draft an invitation for a mailing group. Each step uses a named operation on the club’s records. The invitation is saved as a draft for review. [Explore the Denver Petroleum Club build](https://denver-petroleum-club.vercel.app/)

The same interface can register an attendee, update a membership, or revise approved wording on a public page while preserving its layout and payment links. That’s the part I’d reuse on another site. The site defines the actions its business supports, and the assistant can call them directly. For a storefront, one such action might be submitting an order. For the club, it’s running an event from the first listing to the attendee list.
