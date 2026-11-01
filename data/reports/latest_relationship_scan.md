# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-01T16:22:29.619319+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6601`

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

- `market_context_high->unknown_24h` score `7121.5579` n `55` status `ready` deltaP `1.3889` edge `593.4539` maxDD `0.0`
- `market_context_high->unknown_4h` score `379.9834` n `55` status `ready` deltaP `5.9562` edge `31.6299` maxDD `-0.0124`
- `market_context_high->unknown_1h` score `74.8946` n `55` status `ready` deltaP `3.9113` edge `6.2262` maxDD `-0.2178`
- `market_context_high->equity_24h` score `21.082` n `55` status `ready` deltaP `42.7999` edge `1.4951` maxDD `-1.5546`
- `news_risk_high->crypto_alt_24h` score `13.1429` n `94` status `ready` deltaP `30.7883` edge `1.0256` maxDD `-6.8493`
- `market_context_high->index_24h` score `6.686` n `55` status `ready` deltaP `54.3403` edge `0.1949` maxDD `0.0`
- `market_context_high->commodity_24h` score `6.2966` n `55` status `ready` deltaP `44.4003` edge `0.2598` maxDD `-0.8203`
- `market_context_high->crypto_alt_4h` score `6.1266` n `55` status `ready` deltaP `24.2073` edge `0.3786` maxDD `-1.6876`
- `market_context_high->crypto_major_4h` score `5.7035` n `55` status `ready` deltaP `31.5023` edge `0.2989` maxDD `-1.6901`
- `market_context_high->equity_4h` score `3.5153` n `55` status `ready` deltaP `6.3525` edge `0.3208` maxDD `-2.283`
- `market_context_high->commodity_4h` score `3.3126` n `55` status `ready` deltaP `31.0671` edge `0.094` maxDD `-0.3387`
- `news_risk_high->crypto_alt_4h` score `3.2243` n `119` status `ready` deltaP `13.9552` edge `0.3143` maxDD `-7.4246`
- `market_context_high->crypto_major_24h` score `2.4076` n `55` status `ready` deltaP `10.685` edge `0.3051` maxDD `-3.0799`
- `news_risk_high->unknown_1h` score `2.1351` n `126` status `ready` deltaP `-7.4018` edge `0.2559` maxDD `-0.9571`
- `market_context_high->crypto_alt_24h` score `1.8532` n `55` status `ready` deltaP `-4.4728` edge `0.4192` maxDD `-8.8096`
- `market_context_high->metal_4h` score `1.6616` n `55` status `ready` deltaP `19.4179` edge `0.0515` maxDD `-0.7323`
- `market_context_high->equity_1h` score `1.5596` n `55` status `ready` deltaP `3.3261` edge `0.1603` maxDD `-1.5336`
- `market_context_high->crypto_major_1h` score `1.4431` n `55` status `ready` deltaP `8.4812` edge `0.1247` maxDD `-2.2118`
- `market_context_high->crypto_alt_1h` score `1.4243` n `55` status `ready` deltaP `4.2243` edge `0.1576` maxDD `-2.3659`
- `market_context_high->metal_1h` score `0.963` n `55` status `ready` deltaP `11.9243` edge `0.0256` maxDD `-0.3209`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
