# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-28T17:07:25.488257+00:00`
- Price records: `672`
- Market context records: `2161`
- Flow alert records: `8116`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9178`

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

- `market_context_high->crypto_alt_4h` score `13.4045` n `141` status `ready` deltaP `37.3464` edge `0.9617` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `11.7905` n `141` status `ready` deltaP `41.4958` edge `0.7589` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `5.7995` n `141` status `ready` deltaP `23.9708` edge `0.3984` maxDD `-2.6599`
- `market_context_high->equity_4h` score `4.1968` n `141` status `ready` deltaP `25.1979` edge `0.2912` maxDD `-5.0894`
- `news_risk_high->commodity_4h` score `4.0377` n `42` status `ready` deltaP `32.1719` edge `0.3703` maxDD `-3.0367`
- `market_context_high->crypto_major_1h` score `3.315` n `141` status `ready` deltaP `17.6041` edge `0.2066` maxDD `-1.817`
- `market_context_high->crypto_alt_1h` score `3.2897` n `141` status `ready` deltaP `16.8164` edge `0.2484` maxDD `-4.9097`
- `market_context_high->index_24h` score `3.2369` n `141` status `ready` deltaP `12.7918` edge `0.3073` maxDD `-4.1604`
- `market_context_high->index_4h` score `3.0881` n `141` status `ready` deltaP `23.521` edge `0.1689` maxDD `-1.8022`
- `market_context_high->unknown_24h` score `2.6334` n `141` status `ready` deltaP `27.5081` edge `0.5681` maxDD `-35.8966`
- `market_context_high->equity_24h` score `2.3908` n `141` status `ready` deltaP `24.6417` edge `0.5248` maxDD `-33.1875`
- `market_context_high->metal_4h` score `2.2197` n `141` status `ready` deltaP `19.563` edge `0.1933` maxDD `-4.7664`
- `news_risk_high->fx_4h` score `2.1771` n `42` status `ready` deltaP `27.6931` edge `0.0152` maxDD `-0.1382`
- `market_context_high->crypto_major_24h` score `2.1505` n `141` status `ready` deltaP `19.8877` edge `1.0017` maxDD `-62.3533`
- `news_risk_high->unknown_4h` score `1.4312` n `42` status `ready` deltaP `14.9536` edge `0.0919` maxDD `-2.7857`
- `news_risk_high->equity_4h` score `1.1904` n `42` status `ready` deltaP `-2.7656` edge `0.2918` maxDD `-4.6598`
- `news_risk_high->unknown_1h` score `1.1023` n `43` status `ready` deltaP `19.0189` edge `0.012` maxDD `-1.7548`
- `market_context_high->equity_1h` score `0.8624` n `141` status `ready` deltaP `11.0099` edge `0.0773` maxDD `-2.6402`
- `news_risk_high->commodity_1h` score `0.8157` n `43` status `ready` deltaP `10.7645` edge `0.1008` maxDD `-2.1052`
- `market_context_high->metal_1h` score `0.598` n `141` status `ready` deltaP `9.7242` edge `0.052` maxDD `-2.3594`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
