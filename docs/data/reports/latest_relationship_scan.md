# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-05T21:37:27.984323+00:00`
- Price records: `672`
- Market context records: `5814`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10006`

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

- `market_context_high->equity_4h` score `0.238` n `287` status `ready` deltaP `6.0322` edge `0.1254` maxDD `-6.9958`
- `market_context_high->equity_24h` score `0.0473` n `248` status `ready` deltaP `15.3954` edge `0.4092` maxDD `-31.6316`
- `market_context_high->fx_1h` score `-0.1827` n `287` status `ready` deltaP `3.5579` edge `0.0014` maxDD `-0.5499`
- `market_context_high->commodity_1h` score `-0.5807` n `287` status `ready` deltaP `-1.364` edge `-0.0028` maxDD `-2.3374`
- `market_context_high->metal_1h` score `-0.6414` n `287` status `ready` deltaP `2.0609` edge `-0.0001` maxDD `-2.0339`
- `market_context_high->index_1h` score `-0.6537` n `287` status `ready` deltaP `0.0193` edge `0.0029` maxDD `-0.9472`
- `market_context_high->equity_1h` score `-0.6944` n `287` status `ready` deltaP `2.4943` edge `0.0262` maxDD `-5.0555`
- `market_context_high->crypto_major_1h` score `-0.878` n `287` status `ready` deltaP `3.1552` edge `0.0379` maxDD `-6.2348`
- `market_context_high->crypto_alt_1h` score `-1.0473` n `287` status `ready` deltaP `1.6608` edge `0.0351` maxDD `-6.6758`
- `market_context_high->index_4h` score `-1.2295` n `287` status `ready` deltaP `0.0` edge `0.0111` maxDD `-3.165`
- `market_context_high->fx_4h` score `-1.4396` n `287` status `ready` deltaP `0.9364` edge `0.0041` maxDD `-2.2593`
- `market_context_high->fx_24h` score `-1.4581` n `248` status `ready` deltaP `9.6718` edge `0.0303` maxDD `-5.5367`
- `market_context_high->metal_4h` score `-2.1558` n `287` status `ready` deltaP `-4.1376` edge `-0.0429` maxDD `-9.1388`
- `market_context_high->crypto_major_4h` score `-2.6717` n `287` status `ready` deltaP `8.1446` edge `0.1603` maxDD `-25.6458`
- `market_context_high->commodity_4h` score `-2.7331` n `287` status `ready` deltaP `-1.5679` edge `-0.0175` maxDD `-8.6511`
- `market_context_high->index_24h` score `-4.3309` n `248` status `ready` deltaP `3.7131` edge `0.0288` maxDD `-18.1572`
- `market_context_high->crypto_alt_4h` score `-4.3847` n `287` status `ready` deltaP `5.6185` edge `0.098` maxDD `-28.7346`
- `market_context_high->commodity_24h` score `-5.923` n `248` status `ready` deltaP `-12.6904` edge `-0.0638` maxDD `-31.5432`
- `market_context_high->metal_24h` score `-8.156` n `248` status `ready` deltaP `-3.8474` edge `-0.2329` maxDD `-18.6892`
- `market_context_high->crypto_major_24h` score `-12.0142` n `248` status `ready` deltaP `-3.1418` edge `-0.2865` maxDD `-36.4989`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
