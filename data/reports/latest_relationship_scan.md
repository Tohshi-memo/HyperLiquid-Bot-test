# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-27T03:37:26.627012+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14779`

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

- `news_risk_high->unknown_24h` score `49.5713` n `50` status `ready` deltaP `11.5717` edge `4.0538` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `14.8164` n `50` status `ready` deltaP `36.9326` edge `1.0326` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `12.2451` n `50` status `ready` deltaP `25.4024` edge `0.861` maxDD `-0.1276`
- `news_risk_high->equity_24h` score `6.0277` n `50` status `ready` deltaP `28.5596` edge `0.4052` maxDD `-4.7964`
- `news_risk_high->fx_4h` score `3.8677` n `50` status `ready` deltaP `45.2012` edge `0.03` maxDD `-0.0559`
- `news_risk_high->index_24h` score `3.444` n `50` status `ready` deltaP `35.323` edge `0.0667` maxDD `-0.2147`
- `market_context_high->unknown_4h` score `3.0877` n `137` status `ready` deltaP `24.1031` edge `0.1373` maxDD `-0.5878`
- `news_risk_high->metal_24h` score `2.9803` n `50` status `ready` deltaP `38.0691` edge `-0.0012` maxDD `-0.0053`
- `news_risk_high->unknown_1h` score `2.664` n `50` status `ready` deltaP `15.479` edge `0.1544` maxDD `-0.8474`
- `news_risk_high->fx_1h` score `1.4306` n `50` status `ready` deltaP `19.3054` edge `0.0075` maxDD `-0.0257`
- `news_risk_high->equity_4h` score `1.3235` n `50` status `ready` deltaP `20.2073` edge `0.0521` maxDD `-2.1218`
- `market_context_high->unknown_1h` score `1.2961` n `137` status `ready` deltaP `12.8513` edge `0.0673` maxDD `-1.5974`
- `news_risk_high->equity_1h` score `1.2444` n `50` status `ready` deltaP `16.6647` edge `0.0205` maxDD `-0.2319`
- `market_context_high->unknown_24h` score `0.8966` n `134` status `ready` deltaP `5.6016` edge `0.1105` maxDD `-3.1835`
- `news_risk_high->commodity_1h` score `0.5175` n `50` status `ready` deltaP `14.2994` edge `0.0023` maxDD `-0.5024`
- `news_risk_high->index_4h` score `0.1916` n `50` status `ready` deltaP `7.6951` edge `0.0044` maxDD `-0.1788`
- `news_risk_high->index_1h` score `0.1186` n `50` status `ready` deltaP `7.0599` edge `0.0021` maxDD `-0.0505`
- `news_risk_high->metal_1h` score `0.0345` n `50` status `ready` deltaP `4.503` edge `-0.003` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `-0.328` n `50` status `ready` deltaP `5.7866` edge `-0.0128` maxDD `-0.249`
- `market_context_high->fx_1h` score `-0.3492` n `137` status `ready` deltaP `4.2397` edge `0.0002` maxDD `-0.8587`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
