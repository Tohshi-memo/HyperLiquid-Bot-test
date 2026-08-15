# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-15T16:58:53.612319+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11700`

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

- `market_context_high->unknown_24h` score `140.2251` n `127` status `ready` deltaP `-23.2399` edge `12.1316` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `33.8411` n `32` status `ready` deltaP `-36.0106` edge `4.6537` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `33.8411` n `32` status `ready` deltaP `-36.0106` edge `4.6537` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `12.9767` n `36` status `ready` deltaP `26.6609` edge `0.9416` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `7.7629` n `36` status `ready` deltaP `40.3963` edge `0.3776` maxDD `0.0`
- `market_context_high->commodity_24h` score `5.6558` n `127` status `ready` deltaP `33.3397` edge `0.2548` maxDD `-0.1266`
- `risk_on_high->commodity_24h` score `5.2094` n `32` status `ready` deltaP `35.7019` edge `0.1961` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.2094` n `32` status `ready` deltaP `35.7019` edge `0.1961` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `4.1753` n `32` status `ready` deltaP `27.8542` edge `0.4652` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `4.1753` n `32` status `ready` deltaP `27.8542` edge `0.4652` maxDD `-6.2481`
- `news_risk_high->index_24h` score `3.6883` n `36` status `ready` deltaP `30.8492` edge `0.1017` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.9791` n `32` status `ready` deltaP `21.5701` edge `0.1227` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.9791` n `32` status `ready` deltaP `21.5701` edge `0.1227` maxDD `-0.1258`
- `market_context_high->commodity_4h` score `2.0141` n `127` status `ready` deltaP `19.8231` edge `0.0828` maxDD `-0.7687`
- `news_risk_high->index_4h` score `1.9254` n `36` status `ready` deltaP `22.2053` edge `0.0256` maxDD `-0.0546`
- `news_risk_high->equity_1h` score `1.7646` n `36` status `ready` deltaP `8.5829` edge `0.1217` maxDD `-0.5496`
- `risk_on_high->commodity_1h` score `1.3833` n `32` status `ready` deltaP `14.8578` edge `0.0395` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.3833` n `32` status `ready` deltaP `14.8578` edge `0.0395` maxDD `-0.1957`
- `risk_on_high->equity_24h` score `0.7887` n `32` status `ready` deltaP `15.2026` edge `0.1777` maxDD `-11.2348`
- `risk_on_and_context->equity_24h` score `0.7887` n `32` status `ready` deltaP `15.2026` edge `0.1777` maxDD `-11.2348`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
