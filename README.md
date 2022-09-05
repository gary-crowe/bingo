# bingo

Initial stab at a bingo program using K8's/Service mesh.
This contains experimental code for the bingo program. The idea is to have a central pod doing the
bingo calling and multipl client pods as the players.  
A mysql backend will contain the stats.  Once developed I want to incorporate service mesh to run across multiple clouds

Useful Links:
Bingo card generator (pay): https://myfreebingocards.com/bingo-card-generator/edit/y6gbar
https://github.com/delins/bingo : generates pdf 5x5 bingo card. Might be useful to print out cards. 
https://github.com/digitalsleuth/bingo-card-generator: Similar, looks to have a gui frontend.

Some theory here using conjure programming language: https://journal.artfuldev.com/generating-tickets-for-tambola-or-bingo-or-housie-or-whatever-58df409205ae

Automated number caller page: https://www.online-stopwatch.com/random-number-generators/online-bingo-caller/
and this one: https://partystuff.in/tambola-board

Here's a solution but in js I think: ./tambola-tickets

A typical card looks like this:

![Home System](img/card.jpg)

The challenge is to get that working first.

