# Mini Dragon

An 87-line Python chess engine — 0x88 board, full legal move generation (castling, en passant, underpromotion), tapered piece-square evaluation, transposition table, null-move pruning, and quiescence search. Built to go head-to-head with [Sunfish](https://github.com/thomasahle/sunfish), the well-known 111-line engine.

**▶ Play it:** https://g-c-3.github.io/mini-dragon/

Runs entirely client-side via [Pyodide](https://pyodide.org) — no server, no build step. `index.html` fetches `engine_compact.py` live from this repo, so any changes you push are reflected on next page load. Sunfish is bundled in for direct comparison.

### Files
- `engine_compact.py` — the engine
- `index.html` — the playable page
