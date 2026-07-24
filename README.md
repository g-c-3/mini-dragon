# Mini Dragon

**87 lines of Python. Full legal chess. No dependencies.**

Mini Dragon is a compact chess engine that implements everything a "real" engine needs — legal move generation, search, and evaluation — without cutting corners on correctness. It runs entirely in your browser via [Pyodide](https://pyodide.org): no server, no build step, no install.

It's built to go head-to-head with **[Sunfish](https://github.com/thomasahle/sunfish)**, the well-known 111-line engine that showed a serious chess AI could fit in a handful of code. Sunfish is bundled in for direct comparison — challenge it yourself, or set the two engines against each other and watch the game play out move by move.

**▶ Play it (or watch it play itself):** https://g-c-3.github.io/mini-dragon/

---

## Mini Dragon vs. Sunfish

| | 🐉 Mini Dragon | 🐟 Sunfish |
|---|---|---|
| **Lines of code** | 87 | 111 |
| **Board representation** | 0x88 | Padded 10×12 mailbox |
| **Move legality** | Full — castling, en passant, underpromotion | Full |
| **Evaluation** | Tapered piece-square tables (midgame → endgame) | Piece-square tables |
| **Search** | Negamax, transposition table, null-move pruning, quiescence search | Iterative deepening, transposition table, null-move-based quiescence |
| **Dependencies** | None | None |
| **Runs in browser** | Yes (Pyodide) | Yes (Pyodide) |

Both engines are written in plain Python with zero dependencies and share the same minimalist philosophy: a full, rules-correct chess engine in as few lines as possible. Where they differ is in the specific engineering choices behind search and evaluation — which is what makes watching them play each other interesting.

## Watch them duel

The playable page has an **auto-play mode**: set Mini Dragon (White) against Sunfish (Black) and let them play out a full game with no human input. It's the quickest way to see how their styles differ — openings, trades, endgame technique.

You can also play against either engine yourself, as White or Black.

## Files

- **`engine_compact.py`** — Mini Dragon's source code.
- **`index.html`** — the playable page. It fetches `engine_compact.py` live from this repo on load, so any change pushed here shows up the next time the page loads. Sunfish's source is bundled directly in the page for the comparison.

## Why 87 lines?

The point of Mini Dragon is to show that a chess engine's core requirements — correct legal move generation, a working search, and a reasonable evaluation function — don't take a large codebase to implement well. Sunfish demonstrated this at 111 lines; Mini Dragon is a further attempt at the same idea, in fewer.
