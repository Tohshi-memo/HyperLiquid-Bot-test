# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-03T05:37:20.029758+00:00`
- Price records: `672`
- Market context records: `2735`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9250`

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

- `market_context_high->crypto_alt_24h` score `11.3251` n `111` status `ready` deltaP `16.3523` edge `1.1841` maxDD `-19.9486`
- `market_context_high->unknown_24h` score `8.5638` n `111` status `ready` deltaP `17.3048` edge `0.6311` maxDD `-1.6255`
- `market_context_high->crypto_major_24h` score `1.4038` n `111` status `ready` deltaP `6.5175` edge `0.8928` maxDD `-44.169`
- `market_context_high->unknown_4h` score `1.271` n `143` status `ready` deltaP `8.0782` edge `0.1574` maxDD `-3.7602`
- `market_context_high->index_4h` score `0.0625` n `143` status `ready` deltaP `9.7892` edge `0.0269` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `-0.1387` n `143` status `ready` deltaP `3.0485` edge `0.0412` maxDD `-3.1801`
- `market_context_high->index_1h` score `-0.1861` n `143` status `ready` deltaP `2.7512` edge `0.0072` maxDD `-1.2855`
- `market_context_high->crypto_alt_4h` score `-0.3749` n `143` status `ready` deltaP `16.8206` edge `0.2907` maxDD `-28.7261`
- `market_context_high->fx_1h` score `-0.5063` n `143` status `ready` deltaP `-0.1978` edge `0.0035` maxDD `-0.2164`
- `market_context_high->commodity_1h` score `-0.5475` n `143` status `ready` deltaP `0.8009` edge `-0.0002` maxDD `-4.3601`
- `market_context_high->crypto_alt_1h` score `-0.5939` n `143` status `ready` deltaP `6.1451` edge `0.0589` maxDD `-10.747`
- `market_context_high->metal_1h` score `-0.7528` n `143` status `ready` deltaP `-1.25` edge `-0.0036` maxDD `-3.0996`
- `market_context_high->crypto_major_1h` score `-0.9448` n `143` status `ready` deltaP `3.6473` edge `0.0415` maxDD `-9.622`
- `market_context_high->fx_4h` score `-1.0055` n `143` status `ready` deltaP `-2.2685` edge `0.0092` maxDD `-0.5631`
- `market_context_high->fx_24h` score `-1.1386` n `111` status `ready` deltaP `0.7508` edge `-0.0127` maxDD `-0.6418`
- `market_context_high->equity_1h` score `-1.3334` n `143` status `ready` deltaP `-5.1337` edge `0.0064` maxDD `-2.6634`
- `market_context_high->commodity_4h` score `-1.4185` n `143` status `ready` deltaP `1.2089` edge `0.0021` maxDD `-10.0279`
- `market_context_high->commodity_24h` score `-1.6659` n `111` status `ready` deltaP `2.5807` edge `0.0786` maxDD `-12.4171`
- `market_context_high->equity_4h` score `-2.0783` n `143` status `ready` deltaP `-1.2493` edge `-0.0269` maxDD `-5.7037`
- `market_context_high->crypto_major_4h` score `-2.2328` n `143` status `ready` deltaP `6.9046` edge `0.1583` maxDD `-32.2466`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
