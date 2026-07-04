# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-04T23:22:25.551996+00:00`
- Price records: `672`
- Market context records: `5714`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8874`

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

- `market_context_high->crypto_major_4h` score `1.6761` n `269` status `ready` deltaP `10.6351` edge `0.2059` maxDD `-6.6368`
- `market_context_high->equity_24h` score `1.0106` n `219` status `ready` deltaP `17.0496` edge `0.5238` maxDD `-31.6316`
- `market_context_high->crypto_alt_4h` score `0.5369` n `269` status `ready` deltaP `8.0623` edge `0.1519` maxDD `-7.5392`
- `market_context_high->equity_4h` score `0.1862` n `269` status `ready` deltaP `7.062` edge `0.1323` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.1956` n `281` status `ready` deltaP `3.2876` edge `0.0011` maxDD `-0.5144`
- `market_context_high->crypto_major_1h` score `-0.4344` n `281` status `ready` deltaP `3.344` edge `0.0371` maxDD `-3.9811`
- `market_context_high->metal_1h` score `-0.4604` n `281` status `ready` deltaP `1.3782` edge `-0.0007` maxDD `-2.0682`
- `market_context_high->equity_1h` score `-0.5771` n `281` status `ready` deltaP `3.7052` edge `0.0279` maxDD `-5.0555`
- `market_context_high->crypto_alt_1h` score `-0.6127` n `281` status `ready` deltaP `1.6041` edge `0.0326` maxDD `-3.8812`
- `market_context_high->index_1h` score `-0.6157` n `281` status `ready` deltaP `0.6297` edge `0.0037` maxDD `-0.9472`
- `market_context_high->commodity_1h` score `-1.0831` n `281` status `ready` deltaP `-0.8162` edge `-0.0041` maxDD `-3.7906`
- `market_context_high->fx_24h` score `-1.1468` n `219` status `ready` deltaP `10.4856` edge `0.0412` maxDD `-3.6505`
- `market_context_high->index_4h` score `-1.2172` n `269` status `ready` deltaP `0.3117` edge `0.0106` maxDD `-3.165`
- `market_context_high->fx_4h` score `-1.3102` n `269` status `ready` deltaP `1.6729` edge `0.0054` maxDD `-1.4288`
- `market_context_high->metal_4h` score `-2.6111` n `269` status `ready` deltaP `-7.1233` edge `-0.0497` maxDD `-11.6719`
- `market_context_high->index_24h` score `-2.8612` n `219` status `ready` deltaP `2.6018` edge `0.0303` maxDD `-18.1572`
- `market_context_high->commodity_4h` score `-3.8562` n `269` status `ready` deltaP `-3.794` edge `-0.0285` maxDD `-14.071`
- `market_context_high->crypto_major_24h` score `-4.5455` n `219` status `ready` deltaP `6.2405` edge `0.0253` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-7.7881` n `219` status `ready` deltaP `-6.4332` edge `-0.2394` maxDD `-32.2951`
- `market_context_high->commodity_24h` score `-11.821` n `219` status `ready` deltaP `-10.0885` edge `-0.0692` maxDD `-45.5568`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
