# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-17T17:22:12.339507+00:00`
- Price records: `672`
- Market context records: `1033`
- Flow alert records: `4884`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8635`

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

- `market_context_high->crypto_major_24h` score `14.2802` n `182` status `ready` deltaP `32.9949` edge `1.0289` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `4.5141` n `182` status `ready` deltaP `11.3364` edge `0.424` maxDD `-9.5387`
- `market_context_high->equity_24h` score `3.4829` n `182` status `ready` deltaP `11.8006` edge `0.2904` maxDD `-3.6396`
- `market_context_high->index_24h` score `2.5962` n `182` status `ready` deltaP `11.0926` edge `0.2232` maxDD `-2.1308`
- `market_context_high->metal_24h` score `1.264` n `182` status `ready` deltaP `-5.835` edge `0.4161` maxDD `-14.7496`
- `market_context_high->fx_1h` score `-0.089` n `182` status `ready` deltaP `5.0487` edge `0.0005` maxDD `-0.3124`
- `market_context_high->index_1h` score `-0.4167` n `182` status `ready` deltaP `4.6604` edge `0.0122` maxDD `-2.2395`
- `market_context_high->equity_1h` score `-0.6335` n `182` status `ready` deltaP `0.1151` edge `0.0221` maxDD `-4.3858`
- `market_context_high->commodity_1h` score `-0.6557` n `182` status `ready` deltaP `1.2963` edge `0.0175` maxDD `-3.7959`
- `market_context_high->fx_4h` score `-0.9971` n `182` status `ready` deltaP `2.0772` edge `0.0027` maxDD `-1.6381`
- `market_context_high->crypto_major_1h` score `-1.1173` n `182` status `ready` deltaP `5.8466` edge `-0.0081` maxDD `-7.9187`
- `market_context_high->crypto_alt_1h` score `-1.4021` n `182` status `ready` deltaP `0.0066` edge `-0.0083` maxDD `-5.3538`
- `market_context_high->index_4h` score `-1.4172` n `182` status `ready` deltaP `-0.5193` edge `0.033` maxDD `-6.1444`
- `market_context_high->equity_4h` score `-1.6275` n `182` status `ready` deltaP `1.6467` edge `0.0686` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-1.9812` n `182` status `ready` deltaP `2.2538` edge `-0.0353` maxDD `-7.2528`
- `market_context_high->crypto_alt_4h` score `-3.059` n `182` status `ready` deltaP `0.6584` edge `0.0185` maxDD `-15.2248`
- `market_context_high->fx_24h` score `-3.1529` n `182` status `ready` deltaP `3.4822` edge `-0.0198` maxDD `-19.2774`
- `market_context_high->crypto_major_4h` score `-3.2947` n `182` status `ready` deltaP `7.2066` edge `0.048` maxDD `-22.648`
- `market_context_high->commodity_4h` score `-3.56` n `182` status `ready` deltaP `-4.8312` edge `0.0523` maxDD `-13.0076`
- `market_context_high->metal_4h` score `-3.9774` n `182` status `ready` deltaP `-1.454` edge `-0.1569` maxDD `-20.7994`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
