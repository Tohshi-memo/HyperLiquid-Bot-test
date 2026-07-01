# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-01T19:52:25.511543+00:00`
- Price records: `672`
- Market context records: `5382`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11510`

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

- `market_context_high->unknown_24h` score `7.0123` n `185` status `ready` deltaP `16.8563` edge `0.485` maxDD `-0.3748`
- `market_context_high->crypto_major_24h` score `5.4996` n `185` status `ready` deltaP `22.9692` edge `0.7592` maxDD `-29.6555`
- `market_context_high->crypto_major_4h` score `3.3924` n `205` status `ready` deltaP `14.4817` edge `0.4154` maxDD `-14.0065`
- `market_context_high->crypto_alt_4h` score `2.8843` n `205` status `ready` deltaP `11.6159` edge `0.327` maxDD `-9.46`
- `market_context_high->equity_24h` score `2.1474` n `185` status `ready` deltaP `11.8694` edge `0.6627` maxDD `-40.0306`
- `market_context_high->equity_4h` score `2.1235` n `205` status `ready` deltaP `10.5183` edge `0.2707` maxDD `-7.4425`
- `market_context_high->equity_1h` score `0.2942` n `205` status `ready` deltaP `6.8614` edge `0.0753` maxDD `-5.0555`
- `market_context_high->crypto_alt_1h` score `0.0264` n `205` status `ready` deltaP `2.2287` edge `0.0835` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `0.0058` n `205` status `ready` deltaP `4.1748` edge `0.0972` maxDD `-6.9639`
- `market_context_high->index_1h` score `-0.0199` n `205` status `ready` deltaP `4.9774` edge `0.0145` maxDD `-0.9472`
- `market_context_high->fx_24h` score `-0.1433` n `185` status `ready` deltaP `7.0637` edge `0.0305` maxDD `-0.8294`
- `market_context_high->index_24h` score `-0.2739` n `185` status `ready` deltaP `15.8155` edge `0.0896` maxDD `-9.0959`
- `market_context_high->unknown_4h` score `-0.3025` n `205` status `ready` deltaP `8.75` edge `0.0349` maxDD `-6.1421`
- `market_context_high->fx_1h` score `-0.4485` n `205` status `ready` deltaP `-1.1034` edge `-0.0012` maxDD `-0.5823`
- `market_context_high->metal_1h` score `-0.5095` n `205` status `ready` deltaP `1.7796` edge `0.0132` maxDD `-2.0682`
- `market_context_high->index_4h` score `-1.0939` n `205` status `ready` deltaP `5.3353` edge `0.0342` maxDD `-2.874`
- `market_context_high->fx_4h` score `-1.2059` n `205` status `ready` deltaP `0.2439` edge `0.0008` maxDD `-1.567`
- `market_context_high->commodity_1h` score `-1.5334` n `205` status `ready` deltaP `-3.9192` edge `-0.0072` maxDD `-3.5563`
- `market_context_high->metal_4h` score `-2.4794` n `205` status `ready` deltaP `-5.7622` edge `-0.027` maxDD `-12.8631`
- `market_context_high->crypto_alt_24h` score `-3.1551` n `185` status `ready` deltaP `13.6815` edge `0.374` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
