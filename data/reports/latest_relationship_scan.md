# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-24T08:37:18.457009+00:00`
- Price records: `672`
- Market context records: `1718`
- Flow alert records: `6853`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8834`

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

- `market_context_high->metal_24h` score `6.4971` n `139` status `ready` deltaP `25.0392` edge `0.6171` maxDD `-12.7414`
- `market_context_high->unknown_24h` score `6.3065` n `139` status `ready` deltaP `17.2177` edge `0.9428` maxDD `-35.8966`
- `market_context_high->crypto_alt_4h` score `6.0526` n `196` status `ready` deltaP `21.8859` edge `0.5351` maxDD `-9.1295`
- `market_context_high->crypto_major_4h` score `4.5066` n `196` status `ready` deltaP `23.1769` edge `0.4616` maxDD `-10.9117`
- `market_context_high->index_24h` score `3.7473` n `139` status `ready` deltaP `16.6526` edge `0.3241` maxDD `-4.1604`
- `market_context_high->unknown_4h` score `3.1111` n `196` status `ready` deltaP `13.9466` edge `0.3934` maxDD `-11.1695`
- `market_context_high->equity_4h` score `2.9961` n `196` status `ready` deltaP `16.2643` edge `0.2507` maxDD `-5.0894`
- `market_context_high->equity_24h` score `1.2092` n `139` status `ready` deltaP `15.332` edge `0.4884` maxDD `-33.1875`
- `market_context_high->crypto_alt_1h` score `0.7501` n `196` status `ready` deltaP `7.5706` edge `0.1144` maxDD `-4.1892`
- `market_context_high->index_4h` score `0.5276` n `196` status `ready` deltaP `8.6642` edge `0.0951` maxDD `-3.7119`
- `market_context_high->crypto_major_1h` score `0.1921` n `196` status `ready` deltaP `4.7477` edge `0.0917` maxDD `-3.9211`
- `market_context_high->equity_1h` score `0.0167` n `196` status `ready` deltaP `4.6713` edge `0.0511` maxDD `-2.8014`
- `market_context_high->crypto_alt_24h` score `-0.2384` n `139` status `ready` deltaP `23.1821` edge `1.0065` maxDD `-88.8062`
- `market_context_high->metal_4h` score `-0.3013` n `196` status `ready` deltaP `12.444` edge `0.1476` maxDD `-12.5349`
- `market_context_high->index_1h` score `-0.4635` n `196` status `ready` deltaP `1.0724` edge `0.0174` maxDD `-1.7205`
- `market_context_high->metal_1h` score `-0.5448` n `196` status `ready` deltaP `5.6459` edge `0.0261` maxDD `-6.3532`
- `market_context_high->fx_1h` score `-0.6638` n `196` status `ready` deltaP `-3.1162` edge `-0.0011` maxDD `-0.3914`
- `market_context_high->fx_24h` score `-0.8203` n `139` status `ready` deltaP `4.3875` edge `0.0073` maxDD `-1.3925`
- `market_context_high->crypto_major_24h` score `-1.2071` n `139` status `ready` deltaP `21.3786` edge `0.5613` maxDD `-62.3533`
- `market_context_high->unknown_1h` score `-1.5048` n `196` status `ready` deltaP `1.5367` edge `0.0113` maxDD `-7.7558`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
