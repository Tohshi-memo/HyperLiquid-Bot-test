# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-04T23:37:25.363167+00:00`
- Price records: `672`
- Market context records: `5716`
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

- `market_context_high->crypto_major_4h` score `1.6441` n `269` status `ready` deltaP `10.4157` edge `0.2047` maxDD `-6.6368`
- `market_context_high->equity_24h` score `1.0052` n `219` status `ready` deltaP `17.0496` edge `0.5231` maxDD `-31.6316`
- `market_context_high->crypto_alt_4h` score `0.47` n `269` status `ready` deltaP `7.8429` edge `0.1495` maxDD `-7.6764`
- `market_context_high->equity_4h` score `0.2061` n `269` status `ready` deltaP `7.2814` edge `0.1325` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.1948` n `281` status `ready` deltaP `3.2876` edge `0.0012` maxDD `-0.5144`
- `market_context_high->metal_1h` score `-0.4489` n `281` status `ready` deltaP `1.5844` edge `-0.0006` maxDD `-2.0682`
- `market_context_high->crypto_major_1h` score `-0.4593` n `281` status `ready` deltaP `3.1379` edge `0.0364` maxDD `-3.9811`
- `market_context_high->equity_1h` score `-0.5948` n `281` status `ready` deltaP `3.4991` edge `0.0278` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.6157` n `281` status `ready` deltaP `0.6297` edge `0.0037` maxDD `-0.9472`
- `market_context_high->crypto_alt_1h` score `-0.6509` n `281` status `ready` deltaP `1.3979` edge `0.0316` maxDD `-3.9464`
- `market_context_high->commodity_1h` score `-0.7163` n `281` status `ready` deltaP `-1.0223` edge `-0.0043` maxDD `-3.7906`
- `market_context_high->fx_24h` score `-1.1453` n `219` status `ready` deltaP `10.4856` edge `0.0415` maxDD `-3.6587`
- `market_context_high->index_4h` score `-1.205` n `269` status `ready` deltaP `0.5309` edge `0.0107` maxDD `-3.165`
- `market_context_high->fx_4h` score `-1.298` n `269` status `ready` deltaP `1.8922` edge `0.0055` maxDD `-1.4288`
- `market_context_high->metal_4h` score `-2.6126` n `269` status `ready` deltaP `-7.1233` edge `-0.0499` maxDD `-11.6719`
- `market_context_high->index_24h` score `-2.8628` n `219` status `ready` deltaP `2.6018` edge `0.0301` maxDD `-18.1572`
- `market_context_high->commodity_4h` score `-3.8586` n `269` status `ready` deltaP `-3.794` edge `-0.0287` maxDD `-14.071`
- `market_context_high->crypto_major_24h` score `-4.5036` n `219` status `ready` deltaP `6.5235` edge `0.0269` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-7.719` n `219` status `ready` deltaP `-6.1501` edge `-0.2387` maxDD `-32.1268`
- `market_context_high->commodity_24h` score `-11.7028` n `219` status `ready` deltaP `-9.8055` edge `-0.0685` maxDD `-45.3089`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
