# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-04T22:52:28.739363+00:00`
- Price records: `672`
- Market context records: `5712`
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

- `market_context_high->crypto_major_4h` score `1.7104` n `269` status `ready` deltaP `10.8543` edge `0.2073` maxDD `-6.6368`
- `market_context_high->equity_24h` score `1.0106` n `219` status `ready` deltaP `17.0496` edge `0.5238` maxDD `-31.6316`
- `market_context_high->crypto_alt_4h` score `0.5976` n `269` status `ready` deltaP `8.2816` edge `0.1555` maxDD `-7.5392`
- `market_context_high->equity_4h` score `0.1451` n `269` status `ready` deltaP `6.6234` edge `0.1318` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.2186` n `281` status `ready` deltaP `2.8752` edge `0.0009` maxDD `-0.5144`
- `market_context_high->crypto_major_1h` score `-0.4179` n `281` status `ready` deltaP `3.5502` edge `0.0371` maxDD `-3.9811`
- `market_context_high->metal_1h` score `-0.4374` n `281` status `ready` deltaP `1.7906` edge `-0.0005` maxDD `-2.0682`
- `market_context_high->equity_1h` score `-0.5771` n `281` status `ready` deltaP `3.7052` edge `0.0279` maxDD `-5.0555`
- `market_context_high->crypto_alt_1h` score `-0.5806` n `281` status `ready` deltaP `1.8103` edge `0.0339` maxDD `-3.8812`
- `market_context_high->index_1h` score `-0.604` n `281` status `ready` deltaP `0.6297` edge `0.0052` maxDD `-0.9472`
- `market_context_high->commodity_1h` score `-1.0759` n `281` status `ready` deltaP `-0.8162` edge `-0.0035` maxDD `-3.7906`
- `market_context_high->fx_24h` score `-1.148` n `219` status `ready` deltaP `10.4856` edge `0.0408` maxDD `-3.6309`
- `market_context_high->index_4h` score `-1.2071` n `269` status `ready` deltaP `0.3117` edge `0.0119` maxDD `-3.165`
- `market_context_high->fx_4h` score `-1.3088` n `269` status `ready` deltaP `1.6729` edge `0.0052` maxDD `-1.3989`
- `market_context_high->metal_4h` score `-2.6111` n `269` status `ready` deltaP `-7.1233` edge `-0.0497` maxDD `-11.6719`
- `market_context_high->index_24h` score `-2.8401` n `219` status `ready` deltaP `2.6018` edge `0.033` maxDD `-18.1572`
- `market_context_high->commodity_4h` score `-3.8466` n `269` status `ready` deltaP `-3.794` edge `-0.0277` maxDD `-14.071`
- `market_context_high->crypto_major_24h` score `-4.7036` n `219` status `ready` deltaP `5.6744` edge `0.0159` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-7.9152` n `219` status `ready` deltaP `-6.9991` edge `-0.2405` maxDD `-32.5421`
- `market_context_high->commodity_24h` score `-12.0267` n `219` status `ready` deltaP `-10.6544` edge `-0.0703` maxDD `-45.8715`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
