# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-01T13:52:24.876519+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6597`

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

- `market_context_high->unknown_24h` score `7031.4134` n `55` status `ready` deltaP `1.5625` edge `585.9407` maxDD `0.0`
- `market_context_high->unknown_4h` score `379.4723` n `55` status `ready` deltaP `5.0416` edge `31.5934` maxDD `-0.0124`
- `market_context_high->unknown_1h` score `74.7819` n `55` status `ready` deltaP `3.6119` edge `6.2188` maxDD `-0.2178`
- `market_context_high->equity_24h` score `21.1484` n `55` status `ready` deltaP `43.4943` edge `1.496` maxDD `-1.5546`
- `news_risk_high->crypto_alt_24h` score `12.9032` n `98` status `ready` deltaP `29.6379` edge `1.0133` maxDD `-6.8493`
- `market_context_high->index_24h` score `6.8144` n `55` status `ready` deltaP `55.5556` edge `0.1975` maxDD `0.0`
- `market_context_high->commodity_24h` score `6.4562` n `55` status `ready` deltaP `45.6156` edge `0.265` maxDD `-0.8203`
- `market_context_high->crypto_alt_4h` score `5.9725` n `55` status `ready` deltaP `23.75` edge `0.3688` maxDD `-1.6876`
- `market_context_high->crypto_major_4h` score `5.5571` n `55` status `ready` deltaP `30.5876` edge `0.2928` maxDD `-1.6901`
- `news_risk_high->crypto_alt_4h` score `3.9176` n `116` status `ready` deltaP `15.3017` edge `0.3631` maxDD `-7.4246`
- `market_context_high->equity_4h` score `3.3786` n `55` status `ready` deltaP `5.4379` edge `0.3155` maxDD `-2.283`
- `market_context_high->commodity_4h` score `3.3673` n `55` status `ready` deltaP `31.6768` edge `0.0945` maxDD `-0.3387`
- `market_context_high->crypto_major_24h` score `2.4467` n `55` status `ready` deltaP `11.0322` edge `0.3078` maxDD `-3.0799`
- `market_context_high->crypto_alt_24h` score `1.7524` n `55` status `ready` deltaP `-5.1673` edge `0.4109` maxDD `-8.8096`
- `market_context_high->metal_4h` score `1.5666` n `55` status `ready` deltaP `18.3508` edge `0.0507` maxDD `-0.7323`
- `market_context_high->equity_1h` score `1.465` n `55` status `ready` deltaP `2.4279` edge `0.1584` maxDD `-1.5336`
- `market_context_high->crypto_major_1h` score `1.3448` n `55` status `ready` deltaP `7.7327` edge `0.1215` maxDD `-2.2118`
- `market_context_high->crypto_alt_1h` score `1.2672` n `55` status `ready` deltaP `3.3261` edge `0.1505` maxDD `-2.3659`
- `market_context_high->metal_1h` score `0.9115` n `55` status `ready` deltaP `11.3255` edge `0.0253` maxDD `-0.3209`
- `news_risk_high->crypto_alt_1h` score `0.7209` n `128` status `ready` deltaP `9.1926` edge `0.0942` maxDD `-3.9659`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
