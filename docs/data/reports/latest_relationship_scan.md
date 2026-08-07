# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-07T13:22:56.947658+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11740`

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

- `market_context_high->commodity_4h` score `1.1083` n `117` status `ready` deltaP `13.003` edge `0.0903` maxDD `-2.7703`
- `market_context_high->commodity_1h` score `0.7074` n `121` status `ready` deltaP `10.2526` edge `0.0322` maxDD `-1.3282`
- `market_context_high->metal_24h` score `0.5826` n `110` status `ready` deltaP `1.0518` edge `0.1408` maxDD `-2.2743`
- `market_context_high->fx_24h` score `0.5577` n `110` status `ready` deltaP `21.1018` edge `0.0499` maxDD `-4.1933`
- `market_context_high->fx_1h` score `-0.0309` n `121` status `ready` deltaP `7.1745` edge `-0.0038` maxDD `-1.0616`
- `market_context_high->fx_4h` score `-0.1606` n `117` status `ready` deltaP `9.1216` edge `0.0046` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.5001` n `121` status `ready` deltaP `-1.5205` edge `-0.0055` maxDD `-1.5448`
- `market_context_high->index_1h` score `-0.58` n `121` status `ready` deltaP `-1.8978` edge `-0.0083` maxDD `-1.6054`
- `market_context_high->equity_1h` score `-1.0576` n `121` status `ready` deltaP `4.9476` edge `-0.0121` maxDD `-10.5179`
- `market_context_high->crypto_alt_1h` score `-1.4157` n `121` status `ready` deltaP `-4.5331` edge `-0.0167` maxDD `-3.0178`
- `market_context_high->crypto_alt_4h` score `-1.4216` n `117` status `ready` deltaP `0.0352` edge `-0.0435` maxDD `-5.7857`
- `market_context_high->index_24h` score `-1.5044` n `110` status `ready` deltaP `-1.0654` edge `0.077` maxDD `-6.9542`
- `market_context_high->metal_4h` score `-1.5739` n `117` status `ready` deltaP `-2.1536` edge `-0.011` maxDD `-2.7977`
- `market_context_high->index_4h` score `-1.5866` n `117` status `ready` deltaP `-7.1399` edge `-0.0308` maxDD `-4.6675`
- `market_context_high->crypto_major_1h` score `-1.6081` n `121` status `ready` deltaP `-5.3719` edge `-0.0368` maxDD `-7.3514`
- `market_context_high->crypto_alt_24h` score `-3.855` n `110` status `ready` deltaP `-10.821` edge `-0.1048` maxDD `-4.5445`
- `market_context_high->equity_4h` score `-6.1479` n `117` status `ready` deltaP `-0.542` edge `-0.2557` maxDD `-34.9766`
- `market_context_high->commodity_24h` score `-6.1959` n `110` status `ready` deltaP `10.2853` edge `0.0136` maxDD `-52.7876`
- `market_context_high->crypto_major_4h` score `-7.6121` n `117` status `ready` deltaP `-7.7549` edge `-0.1781` maxDD `-26.0299`
- `market_context_high->crypto_major_24h` score `-8.0888` n `110` status `ready` deltaP `-9.5811` edge `-0.3682` maxDD `-36.3957`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
