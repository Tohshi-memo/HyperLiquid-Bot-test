# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-24T19:07:21.622012+00:00`
- Price records: `672`
- Market context records: `1767`
- Flow alert records: `6986`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8872`

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

- `market_context_high->metal_24h` score `7.1706` n `175` status `ready` deltaP `28.1478` edge `0.6525` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `6.1726` n `195` status `ready` deltaP `21.7949` edge `0.5457` maxDD `-9.1295`
- `news_risk_high->commodity_4h` score `5.8724` n `30` status `ready` deltaP `27.2765` edge `0.373` maxDD `-3.5713`
- `market_context_high->crypto_major_4h` score `4.7626` n `195` status `ready` deltaP `23.3615` edge `0.4817` maxDD `-10.9117`
- `market_context_high->index_24h` score `3.8374` n `175` status `ready` deltaP `18.498` edge `0.3193` maxDD `-4.1604`
- `market_context_high->equity_4h` score `3.2423` n `195` status `ready` deltaP `17.3608` edge `0.2639` maxDD `-5.0894`
- `market_context_high->unknown_4h` score `3.1319` n `195` status `ready` deltaP `13.9368` edge `0.3952` maxDD `-11.1695`
- `news_risk_high->commodity_1h` score `3.1007` n `30` status `ready` deltaP `24.2715` edge `0.1283` maxDD `-1.2043`
- `market_context_high->unknown_24h` score `2.7598` n `175` status `ready` deltaP `14.3889` edge `0.6661` maxDD `-35.8966`
- `market_context_high->equity_24h` score `2.6576` n `175` status `ready` deltaP `16.9068` edge `0.5986` maxDD `-33.1875`
- `market_context_high->index_4h` score `1.0642` n `195` status `ready` deltaP `13.0777` edge `0.1104` maxDD `-3.7119`
- `market_context_high->crypto_alt_1h` score `0.8458` n `195` status `ready` deltaP `7.8819` edge `0.1203` maxDD `-4.1892`
- `news_risk_high->fx_4h` score `0.8427` n `30` status `ready` deltaP `20.874` edge `-0.0039` maxDD `-0.1774`
- `market_context_high->crypto_major_24h` score `0.3771` n `175` status `ready` deltaP `18.9464` edge `0.7637` maxDD `-62.3533`
- `market_context_high->crypto_major_1h` score `0.3402` n `195` status `ready` deltaP `5.3401` edge `0.1001` maxDD `-3.9211`
- `news_risk_high->unknown_4h` score `0.1608` n `30` status `ready` deltaP `9.065` edge `0.0325` maxDD `-2.7857`
- `market_context_high->equity_1h` score `0.1228` n `195` status `ready` deltaP `5.4422` edge `0.0548` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.1393` n `195` status `ready` deltaP `4.5248` edge `0.0214` maxDD `-1.7205`
- `market_context_high->metal_4h` score `-0.1962` n `195` status `ready` deltaP `12.6056` edge `0.16` maxDD `-12.5349`
- `news_risk_high->unknown_1h` score `-0.4832` n `30` status `ready` deltaP `16.5569` edge `-0.1251` maxDD `-2.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
