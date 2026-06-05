# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-05T22:52:23.321133+00:00`
- Price records: `672`
- Market context records: `3014`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6984`

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

- `market_context_high->crypto_alt_24h` score `21.0881` n `98` status `ready` deltaP `8.762` edge `2.0906` maxDD `-22.6673`
- `market_context_high->commodity_24h` score `12.9056` n `98` status `ready` deltaP `43.3355` edge `0.7976` maxDD `-0.2165`
- `market_context_high->unknown_24h` score `12.5668` n `98` status `ready` deltaP `20.9999` edge `0.9537` maxDD `-1.7175`
- `market_context_high->equity_24h` score `11.1888` n `98` status `ready` deltaP `19.735` edge `1.0012` maxDD `-12.6963`
- `market_context_high->index_24h` score `6.9731` n `98` status `ready` deltaP `19.3453` edge `0.5502` maxDD `-2.5127`
- `market_context_high->commodity_4h` score `2.4272` n `106` status `ready` deltaP `18.192` edge `0.1457` maxDD `-2.8438`
- `market_context_high->equity_4h` score `0.6599` n `106` status `ready` deltaP `13.6274` edge `0.1742` maxDD `-12.1029`
- `market_context_high->index_4h` score `0.2049` n `106` status `ready` deltaP `17.1997` edge `0.0963` maxDD `-10.4423`
- `market_context_high->crypto_alt_4h` score `-0.1172` n `106` status `ready` deltaP `22.6301` edge `0.3889` maxDD `-38.7172`
- `market_context_high->commodity_1h` score `-0.1693` n `117` status `ready` deltaP `0.6833` edge `0.016` maxDD `-1.7142`
- `market_context_high->equity_1h` score `-0.2187` n `117` status `ready` deltaP `4.8263` edge `0.0476` maxDD `-5.6254`
- `market_context_high->index_1h` score `-0.322` n `117` status `ready` deltaP `5.2997` edge `0.0248` maxDD `-4.1126`
- `market_context_high->crypto_alt_1h` score `-0.5821` n `117` status `ready` deltaP `6.4103` edge `0.0956` maxDD `-14.7034`
- `market_context_high->fx_1h` score `-0.604` n `117` status `ready` deltaP `-2.1803` edge `0.0008` maxDD `-0.2615`
- `market_context_high->unknown_1h` score `-0.9278` n `117` status `ready` deltaP `3.7157` edge `-0.029` maxDD `-3.1801`
- `market_context_high->crypto_major_1h` score `-1.0856` n `117` status `ready` deltaP `4.1264` edge `0.0596` maxDD `-15.1032`
- `market_context_high->metal_1h` score `-1.1482` n `117` status `ready` deltaP `-1.8131` edge `-0.0033` maxDD `-6.8783`
- `market_context_high->fx_4h` score `-1.1722` n `106` status `ready` deltaP `-10.5298` edge `-0.0011` maxDD `-0.6521`
- `market_context_high->unknown_4h` score `-1.631` n `106` status `ready` deltaP `-2.5915` edge `-0.0133` maxDD `-3.7602`
- `market_context_high->fx_24h` score `-1.7699` n `98` status `ready` deltaP `-5.265` edge `-0.0252` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
