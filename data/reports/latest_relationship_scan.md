# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-06T10:52:21.206026+00:00`
- Price records: `672`
- Market context records: `3066`
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

- `market_context_high->crypto_alt_24h` score `16.9408` n `91` status `ready` deltaP `12.1909` edge `2.4823` maxDD `-22.6673`
- `market_context_high->commodity_24h` score `14.6422` n `91` status `ready` deltaP `46.358` edge `0.9352` maxDD `-1.2589`
- `market_context_high->unknown_24h` score `13.4979` n `91` status `ready` deltaP `23.159` edge `1.0169` maxDD `-1.7175`
- `market_context_high->index_24h` score `11.8393` n `91` status `ready` deltaP `30.0481` edge `0.8785` maxDD `-4.7103`
- `market_context_high->equity_24h` score `10.5764` n `91` status `ready` deltaP `24.441` edge `1.4682` maxDD `-18.3486`
- `market_context_high->commodity_4h` score `2.3979` n `128` status `ready` deltaP `16.5206` edge `0.1544` maxDD `-2.8438`
- `market_context_high->unknown_4h` score `-0.1663` n `128` status `ready` deltaP `3.0869` edge `0.0709` maxDD `-3.7602`
- `market_context_high->commodity_1h` score `-0.2705` n `128` status `ready` deltaP `-0.2667` edge `0.0215` maxDD `-1.7142`
- `market_context_high->index_1h` score `-0.5639` n `128` status `ready` deltaP `2.7273` edge `0.0158` maxDD `-4.5023`
- `market_context_high->fx_1h` score `-0.6229` n `128` status `ready` deltaP `-6.133` edge `-0.0017` maxDD `-0.3147`
- `market_context_high->crypto_alt_1h` score `-0.6658` n `128` status `ready` deltaP `3.9905` edge `0.101` maxDD `-14.7034`
- `market_context_high->fx_24h` score `-0.7711` n `91` status `ready` deltaP `-0.3853` edge `-0.0091` maxDD `-0.6418`
- `market_context_high->unknown_1h` score `-0.9619` n `128` status `ready` deltaP `2.9893` edge `-0.027` maxDD `-3.1801`
- `market_context_high->crypto_major_1h` score `-1.0506` n `128` status `ready` deltaP `2.1145` edge `0.0775` maxDD `-15.1032`
- `market_context_high->equity_1h` score `-1.056` n `128` status `ready` deltaP `0.3321` edge `0.0078` maxDD `-8.6319`
- `market_context_high->fx_4h` score `-1.2285` n `128` status `ready` deltaP `-10.0991` edge `-0.0058` maxDD `-1.0829`
- `market_context_high->metal_1h` score `-1.2829` n `128` status `ready` deltaP `-3.3543` edge `-0.0053` maxDD `-7.278`
- `market_context_high->index_4h` score `-1.3728` n `128` status `ready` deltaP `8.9558` edge `0.0552` maxDD `-17.6057`
- `market_context_high->crypto_alt_4h` score `-3.0892` n `128` status `ready` deltaP `17.359` edge `0.2927` maxDD `-58.6918`
- `market_context_high->equity_4h` score `-3.6853` n `128` status `ready` deltaP `6.6883` edge `0.0068` maxDD `-36.242`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
