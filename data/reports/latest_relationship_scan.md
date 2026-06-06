# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-06T11:07:23.188069+00:00`
- Price records: `672`
- Market context records: `3067`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6969`

## Conditions

- `news_risk_high`: News Risk is elevated.
- `macro_risk_high`: Macro Risk is elevated.
- `risk_on_high`: Risk-On score is elevated.
- `market_context_high`: Market Context is supportive.
- `polymarket_volume_spike`: Polymarket 24h volume z-score is elevated.
- `flow_alert_high`: Flow Alert score is elevated.
- `news_and_polymarket`: News Risk and Polymarket volume spike happen together.
- `risk_on_and_context`: Risk-On and Market Context are both supportive.
- `macro_and_flow`: Macro Risk and Flow Alert are elevated together.

## Top Patterns

- `market_context_high->crypto_alt_24h` score `17.0044` n `91` status `ready` deltaP `12.3645` edge `2.4893` maxDD `-22.6673`
- `market_context_high->commodity_24h` score `14.6849` n `91` status `ready` deltaP `46.5316` edge `0.9376` maxDD `-1.2589`
- `market_context_high->unknown_24h` score `13.4739` n `91` status `ready` deltaP `23.159` edge `1.0149` maxDD `-1.7175`
- `market_context_high->index_24h` score `11.9233` n `91` status `ready` deltaP `30.0481` edge `0.8855` maxDD `-4.7103`
- `market_context_high->equity_24h` score `10.6931` n `91` status `ready` deltaP `24.6147` edge `1.482` maxDD `-18.3486`
- `market_context_high->commodity_4h` score `2.3979` n `128` status `ready` deltaP `16.5206` edge `0.1544` maxDD `-2.8438`
- `market_context_high->unknown_4h` score `-0.1663` n `128` status `ready` deltaP `3.0869` edge `0.0709` maxDD `-3.7602`
- `market_context_high->commodity_1h` score `-0.2717` n `128` status `ready` deltaP `-0.2667` edge `0.0214` maxDD `-1.7142`
- `market_context_high->index_1h` score `-0.5655` n `128` status `ready` deltaP `2.7273` edge `0.0156` maxDD `-4.5023`
- `market_context_high->fx_1h` score `-0.6151` n `128` status `ready` deltaP `-5.9833` edge `-0.0017` maxDD `-0.3147`
- `market_context_high->crypto_alt_1h` score `-0.6705` n `128` status `ready` deltaP `3.9905` edge `0.1004` maxDD `-14.7034`
- `market_context_high->fx_24h` score `-0.768` n `91` status `ready` deltaP `-0.3853` edge `-0.0087` maxDD `-0.6418`
- `market_context_high->unknown_1h` score `-0.9643` n `128` status `ready` deltaP `2.9893` edge `-0.0272` maxDD `-3.1801`
- `market_context_high->crypto_major_1h` score `-1.0506` n `128` status `ready` deltaP `2.1145` edge `0.0775` maxDD `-15.1032`
- `market_context_high->equity_1h` score `-1.0568` n `128` status `ready` deltaP `0.3321` edge `0.0077` maxDD `-8.6319`
- `market_context_high->fx_4h` score `-1.2285` n `128` status `ready` deltaP `-10.0991` edge `-0.0058` maxDD `-1.0829`
- `market_context_high->metal_1h` score `-1.2907` n `128` status `ready` deltaP `-3.504` edge `-0.0053` maxDD `-7.278`
- `market_context_high->index_4h` score `-1.3736` n `128` status `ready` deltaP `8.9558` edge `0.0551` maxDD `-17.6057`
- `market_context_high->crypto_alt_4h` score `-3.0908` n `128` status `ready` deltaP `17.359` edge `0.2925` maxDD `-58.6918`
- `market_context_high->equity_4h` score `-3.6727` n `128` status `ready` deltaP `6.8408` edge `0.0074` maxDD `-36.242`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
