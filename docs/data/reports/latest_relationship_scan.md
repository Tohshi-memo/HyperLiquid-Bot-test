# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-03T05:52:25.777538+00:00`
- Price records: `672`
- Market context records: `2736`
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

- `market_context_high->crypto_alt_24h` score `11.2591` n `111` status `ready` deltaP `16.3523` edge `1.1786` maxDD `-19.9486`
- `market_context_high->unknown_24h` score `8.5422` n `111` status `ready` deltaP `17.3048` edge `0.6293` maxDD `-1.6255`
- `market_context_high->crypto_major_24h` score `1.4085` n `111` status `ready` deltaP `6.5175` edge `0.8934` maxDD `-44.169`
- `market_context_high->unknown_4h` score `1.2722` n `143` status `ready` deltaP `8.0782` edge `0.1575` maxDD `-3.7602`
- `market_context_high->index_4h` score `0.0633` n `143` status `ready` deltaP `9.7892` edge `0.027` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `-0.1351` n `143` status `ready` deltaP `3.0485` edge `0.0415` maxDD `-3.1801`
- `market_context_high->index_1h` score `-0.1861` n `143` status `ready` deltaP `2.7512` edge `0.0072` maxDD `-1.2855`
- `market_context_high->crypto_alt_4h` score `-0.4013` n `143` status `ready` deltaP `16.8206` edge `0.2885` maxDD `-28.7261`
- `market_context_high->fx_1h` score `-0.5075` n `143` status `ready` deltaP `-0.1978` edge `0.0034` maxDD `-0.2164`
- `market_context_high->commodity_1h` score `-0.5569` n `143` status `ready` deltaP `0.6512` edge `-0.0004` maxDD `-4.3601`
- `market_context_high->crypto_alt_1h` score `-0.6079` n `143` status `ready` deltaP `6.1451` edge `0.0571` maxDD `-10.747`
- `market_context_high->metal_1h` score `-0.7598` n `143` status `ready` deltaP `-1.25` edge `-0.0045` maxDD `-3.0996`
- `market_context_high->crypto_major_1h` score `-0.9549` n `143` status `ready` deltaP `3.6473` edge `0.0402` maxDD `-9.622`
- `market_context_high->fx_4h` score `-1.0189` n `143` status `ready` deltaP `-2.421` edge `0.0091` maxDD `-0.5631`
- `market_context_high->fx_24h` score `-1.1573` n `111` status `ready` deltaP `0.5772` edge `-0.0131` maxDD `-0.6418`
- `market_context_high->equity_1h` score `-1.3346` n `143` status `ready` deltaP `-5.1337` edge `0.0063` maxDD `-2.6634`
- `market_context_high->commodity_4h` score `-1.4404` n `143` status `ready` deltaP `1.0565` edge `0.0003` maxDD `-10.0279`
- `market_context_high->commodity_24h` score `-1.6776` n `111` status `ready` deltaP `2.5807` edge `0.0771` maxDD `-12.4171`
- `market_context_high->equity_4h` score `-2.0747` n `143` status `ready` deltaP `-1.2493` edge `-0.0266` maxDD `-5.7037`
- `market_context_high->crypto_major_4h` score `-2.2382` n `143` status `ready` deltaP `6.9046` edge `0.1576` maxDD `-32.2466`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
