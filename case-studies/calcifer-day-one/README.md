# Calcifer · Day One

I wanted to see whether I could run a software team made up of agents without becoming the person who moves every ticket by hand. Calcifer started as a meeting recorder. For this experiment, I gave it a shared work board, four distinct Codex roles, and a digital office where I could see and talk to the team.

[Read the case study and play the animated recap in your browser](https://cjimenz.github.io/CJIMENZ/case-studies/calcifer-day-one/). You can also [download the standalone recap](day-one.html) for offline viewing.

## What shipped

Across a roughly 19-hour window on November 21–22, 2026, **117 pull requests merged across four repositories**. **102** were in Calcifer; the other **15** landed in related projects. Those are GitHub merge counts, not a count of features, production deployments, or work done without human involvement.

The most useful change wasn’t the number. It was giving PM, Dev, Review, and QA separate identities and a shared record for the ticket, handoff, and evidence. The pixel-art office gave each role a desk, plus a War Room for discussions. And yes, the break room got a pool table.

## How one ticket moves

1. **PM** defines the work and assigns it on the board.
2. **Dev** claims the ticket and links a pull request.
3. **Review** checks the exact change before it merges.
4. **QA** tests the deployed build and links the result to the ticket.
5. **The owner** closes the loop with that evidence still attached.

A queue label tells you who should act. It doesn’t prove who picked the work up. Calcifer stores a handoff for an eligible recipient, so the team can compare the delivery with the eventual pickup in the work log. Roles can discover work without treating every reader as a participant or granting them write access.

## What I’d measure next

For the first automatic-routing pilot, I’d watch whether a single ticket gets picked up without a nudge, gets returned to the right role when it fails a check, and reaches deployed QA with an auditable record. The role connections and handoff storage shipped; unattended pickup across the full path was still being validated.

*The original Day One recap was created with Hark. This public version uses an illustrative board and office, not production screenshots or private records.*
