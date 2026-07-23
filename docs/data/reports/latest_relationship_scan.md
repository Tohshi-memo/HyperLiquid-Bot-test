# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-23T11:22:25.956933+00:00`
- Price records: `672`
- Market context records: `7663`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14697`

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

- `market_context_high->index_1h` score `0.0156` n `146` status `ready` deltaP `5.9114` edge `0.0105` maxDD `-0.8324`
- `market_context_high->crypto_major_1h` score `-0.2025` n `146` status `ready` deltaP `7.7065` edge `0.0187` maxDD `-4.0162`
- `market_context_high->crypto_alt_1h` score `-0.2513` n `146` status `ready` deltaP `2.0548` edge `0.0173` maxDD `-2.7243`
- `market_context_high->fx_24h` score `-0.3304` n `145` status `ready` deltaP `9.4545` edge `0.0182` maxDD `-3.0343`
- `market_context_high->commodity_1h` score `-0.4389` n `146` status `ready` deltaP `0.7774` edge `-0.0044` maxDD `-1.5641`
- `market_context_high->equity_1h` score `-0.5782` n `146` status `ready` deltaP `4.6259` edge `0.0464` maxDD `-7.7764`
- `market_context_high->metal_1h` score `-0.6497` n `146` status `ready` deltaP `0.9392` edge `0.015` maxDD `-1.0307`
- `market_context_high->commodity_4h` score `-0.7008` n `146` status `ready` deltaP `1.6066` edge `0.0054` maxDD `-2.2943`
- `market_context_high->fx_1h` score `-0.7434` n `146` status `ready` deltaP `-1.4727` edge `-0.0022` maxDD `-0.6615`
- `market_context_high->index_4h` score `-0.7696` n `146` status `ready` deltaP `7.0755` edge `0.0243` maxDD `-3.2774`
- `market_context_high->commodity_24h` score `-1.0636` n `145` status `ready` deltaP `8.0128` edge `0.0163` maxDD `-7.0012`
- `market_context_high->crypto_alt_4h` score `-1.086` n `146` status `ready` deltaP `2.1299` edge `0.0455` maxDD `-9.5815`
- `market_context_high->crypto_major_4h` score `-1.2168` n `146` status `ready` deltaP `8.9792` edge `0.0519` maxDD `-14.4206`
- `market_context_high->unknown_1h` score `-1.5325` n `146` status `ready` deltaP `-1.4334` edge `-0.0558` maxDD `-1.3217`
- `market_context_high->metal_4h` score `-1.7084` n `146` status `ready` deltaP `-2.7376` edge `0.0449` maxDD `-4.6535`
- `market_context_high->equity_4h` score `-1.8816` n `146` status `ready` deltaP `-0.3854` edge `0.1757` maxDD `-20.4824`
- `market_context_high->metal_24h` score `-2.2832` n `146` status `ready` deltaP `-3.2772` edge `0.0548` maxDD `-7.3868`
- `market_context_high->equity_24h` score `-2.3713` n `145` status `ready` deltaP `12.6217` edge `0.1024` maxDD `-34.5784`
- `market_context_high->fx_4h` score `-2.7278` n `146` status `ready` deltaP `-8.0349` edge `-0.0053` maxDD `-2.1425`
- `market_context_high->index_24h` score `-3.5913` n `145` status `ready` deltaP `-21.0849` edge `-0.0351` maxDD `-8.114`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
