# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-21T20:38:05.351667+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9868`

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

- `market_context_high->unknown_4h` score `27.7411` n `58` status `ready` deltaP `1.6874` edge `2.3155` maxDD `-0.5326`
- `news_risk_high->crypto_major_24h` score `14.5714` n `101` status `ready` deltaP `2.7623` edge `1.8817` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `9.2374` n `101` status `ready` deltaP `3.1473` edge `1.2369` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `3.6121` n `101` status `ready` deltaP `17.2422` edge `0.307` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `2.8034` n `101` status `ready` deltaP `18.6141` edge `0.2353` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `2.5507` n `101` status `ready` deltaP `15.6326` edge `0.1549` maxDD `-2.058`
- `news_risk_high->commodity_24h` score `2.116` n `101` status `ready` deltaP `28.4052` edge `0.2125` maxDD `-3.4467`
- `news_risk_high->crypto_major_1h` score `1.8326` n `101` status `ready` deltaP `17.1296` edge `0.0908` maxDD `-2.8494`
- `market_context_high->index_24h` score `0.8749` n `42` status `ready` deltaP `-3.6458` edge `0.1761` maxDD `-1.644`
- `market_context_high->equity_1h` score `0.6509` n `58` status `ready` deltaP `4.6614` edge `0.0485` maxDD `-0.36`
- `news_risk_high->metal_1h` score `0.5382` n `101` status `ready` deltaP `13.8495` edge `0.0127` maxDD `-0.8144`
- `market_context_high->index_1h` score `0.5064` n `58` status `ready` deltaP `8.3316` edge `0.0122` maxDD `-0.0435`
- `market_context_high->fx_1h` score `0.4337` n `58` status `ready` deltaP `9.8235` edge `0.0063` maxDD `-0.1854`
- `news_risk_high->fx_4h` score `0.367` n `101` status `ready` deltaP `10.3175` edge `0.0254` maxDD `-0.421`
- `market_context_high->metal_1h` score `0.2603` n `58` status `ready` deltaP `5.3996` edge `0.0165` maxDD `-0.1314`
- `news_risk_high->metal_4h` score `0.2503` n `101` status `ready` deltaP `14.05` edge `0.0326` maxDD `-2.0994`
- `market_context_high->equity_24h` score `0.0932` n `42` status `ready` deltaP `-7.6389` edge `0.3426` maxDD `-17.7117`
- `market_context_high->index_4h` score `0.0777` n `58` status `ready` deltaP `11.1228` edge `-0.0005` maxDD `-1.0949`
- `market_context_high->metal_24h` score `-0.0564` n `42` status `ready` deltaP `12.8224` edge `-0.0668` maxDD `-0.2042`
- `news_risk_high->fx_1h` score `-0.1154` n `101` status `ready` deltaP `4.1901` edge `0.0068` maxDD `-0.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
