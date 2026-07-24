# Mini Dragon

**87 lines of Python. Full legal chess. No dependencies.**

Mini Dragon is a compact chess engine built to do everything a "real" engine does — legal move generation, search, evaluation — in as little code as possible, without cutting corners on correctness. It runs entirely in your browser via [Pyodide](https://pyodide.org): no server, no build step, no install.

It was built to go head-to-head with **[Sunfish](https://github.com/thomasahle/sunfish)**, the well-known 111-line engine that proved a serious chess AI could fit on a napkin. Sunfish is bundled in for direct comparison — challenge it yourself, or set the two loose on each other and watch them fight it out move by move.

**▶ Play it (or watch it play itself):** https://g-c-3.github.io/mini-dragon/

---

## The Matchup

| | 🐉 Mini Dragon | 🐟 Sunfish |
|---|---|---|
| **Lines of code** | 87 | 111 |
| **Board representation** | 0x88 | Padded 10×12 mailbox |
| **Move legality** | Full — castling, en passant, underpromotion | Full |
| **Evaluation** | Tapered piece-square tables (midgame → endgame) | Piece-square tables |
| **Search** | Negamax + transposition table + null-move pruning + quiescence | Iterative deepening + transposition table + null-move-based quiescence |
| **Language** | Python (via Pyodide) | Python (via Pyodide) |
| **Dependencies** | 0 | 0 |
| **Runs in browser?** | Yes | Yes |

Same board, same rules, same 87-vs-111-line minimalist philosophy — different engineering choices. That's what makes the duel interesting: it's not a mismatch of "toy vs. real engine," it's two different answers to the same design constraint.

## Watch Them Duel

The playable page includes an **auto-play mode**: set Mini Dragon and Sunfish against each other and let the game play itself out, move by move, with no human in the loop. It's the fastest way to get a feel for how each engine's style differs in practice — how it opens, how it trades, how it closes out an endgame.

You can also step in yourself and challenge either engine directly, playing White or Black.

## Files

- `engine_compact.py` — Mini Dragon, the engine
- `index.html` — the playable page (fetches `engine_compact.py` live from this repo, so any changes pushed here are reflected on next page load; Sunfish is bundled inline for the comparison)

## Why 87 lines?

Because a chess engine's real complexity — legality, search, evaluation — doesn't need thousands of lines to exist correctly. Mini Dragon is proof that the essentials fit in less code than most `README`s. Sunfish proved it first, at 111; Mini Dragon is the attempt to do it in fewer.
