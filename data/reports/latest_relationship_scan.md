# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-29T06:22:26.217197+00:00`
- Price records: `672`
- Market context records: `5118`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5560`

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

- `market_context_high->unknown_24h` score `24.7832` n `69` status `ready` deltaP `28.6836` edge `1.9083` maxDD `-1.4072`
- `market_context_high->unknown_1h` score `8.3408` n `126` status `ready` deltaP `7.3377` edge `0.7103` maxDD `-2.7986`
- `market_context_high->unknown_4h` score `7.474` n `114` status `ready` deltaP `20.483` edge `0.5885` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `5.4983` n `114` status `ready` deltaP `15.5568` edge `0.5144` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `3.9306` n `114` status `ready` deltaP `13.2301` edge `0.4686` maxDD `-14.0065`
- `market_context_high->crypto_alt_1h` score `0.8708` n `126` status `ready` deltaP `6.5583` edge `0.125` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `0.6655` n `126` status `ready` deltaP `7.4708` edge `0.1302` maxDD `-6.9639`
- `market_context_high->equity_1h` score `0.6336` n `126` status `ready` deltaP `7.5468` edge `0.0618` maxDD `-2.745`
- `market_context_high->equity_4h` score `0.1339` n `114` status `ready` deltaP `6.2153` edge `0.1396` maxDD `-7.4425`
- `market_context_high->metal_1h` score `0.1128` n `126` status `ready` deltaP `6.7223` edge `0.0211` maxDD `-1.4501`
- `market_context_high->commodity_24h` score `0.003` n `69` status `ready` deltaP `14.855` edge `0.0885` maxDD `-9.639`
- `market_context_high->index_1h` score `-0.0267` n `126` status `ready` deltaP `5.0613` edge `0.0144` maxDD `-1.0296`
- `market_context_high->index_4h` score `-0.5178` n `114` status `ready` deltaP `3.0086` edge `0.0253` maxDD `-2.9391`
- `market_context_high->metal_4h` score `-0.5632` n `114` status `ready` deltaP `1.9389` edge `0.0559` maxDD `-4.6157`
- `market_context_high->fx_1h` score `-0.6775` n `126` status `ready` deltaP `-3.1152` edge `-0.002` maxDD `-0.7944`
- `market_context_high->commodity_1h` score `-0.9533` n `126` status `ready` deltaP `0.0594` edge `-0.0029` maxDD `-2.155`
- `market_context_high->fx_4h` score `-1.0682` n `114` status `ready` deltaP `-4.5384` edge `0.0006` maxDD `-1.9169`
- `market_context_high->fx_24h` score `-1.4811` n `69` status `ready` deltaP `-2.5815` edge `-0.0088` maxDD `-1.4601`
- `market_context_high->metal_24h` score `-2.4956` n `69` status `ready` deltaP `-2.3702` edge `0.0803` maxDD `-23.4221`
- `market_context_high->commodity_4h` score `-2.5676` n `114` status `ready` deltaP `-1.38` edge `-0.0315` maxDD `-7.5281`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
