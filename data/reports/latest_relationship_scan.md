# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-13T18:07:25.938608+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12774`

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

- `market_context_high->unknown_24h` score `17736.8508` n `56` status `ready` deltaP `10.2093` edge `1478.023` maxDD `-0.613`
- `risk_on_high->unknown_24h` score `7856.1555` n `37` status `ready` deltaP `11.0298` edge `654.6126` maxDD `-0.1869`
- `risk_on_and_context->unknown_24h` score `7856.1555` n `37` status `ready` deltaP `11.0298` edge `654.6126` maxDD `-0.1869`
- `news_risk_high->unknown_1h` score `426.9519` n `82` status `ready` deltaP `-5.2505` edge `35.6565` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `18.6607` n `82` status `ready` deltaP `36.2027` edge `1.3625` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `18.3916` n `82` status `ready` deltaP `38.0236` edge `1.4262` maxDD `-9.098`
- `news_risk_high->equity_24h` score `9.2124` n `82` status `ready` deltaP `26.926` edge `0.7662` maxDD `-6.5742`
- `news_risk_high->index_24h` score `7.0827` n `82` status `ready` deltaP `50.698` edge `0.2699` maxDD `-0.0797`
- `news_risk_high->metal_24h` score `4.7034` n `82` status `ready` deltaP `25.7948` edge `0.2654` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `4.5194` n `37` status `ready` deltaP `39.8276` edge `0.1111` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.5194` n `37` status `ready` deltaP `39.8276` edge `0.1111` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.4102` n `56` status `ready` deltaP `39.8276` edge `0.102` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `2.7242` n `37` status `ready` deltaP `4.6273` edge `0.452` maxDD `-7.0204`
- `risk_on_and_context->crypto_alt_24h` score `2.7242` n `37` status `ready` deltaP `4.6273` edge `0.452` maxDD `-7.0204`
- `market_context_high->crypto_alt_24h` score `2.6124` n `56` status `ready` deltaP `5.0616` edge `0.4673` maxDD `-9.6226`
- `news_risk_high->index_4h` score `0.4125` n `82` status `ready` deltaP `12.3475` edge `0.0334` maxDD `-0.6935`
- `market_context_high->commodity_4h` score `0.3304` n `131` status `ready` deltaP `10.1576` edge `0.0081` maxDD `-0.5295`
- `risk_on_high->fx_24h` score `0.262` n `37` status `ready` deltaP `21.6962` edge `-0.0083` maxDD `-2.2197`
- `risk_on_and_context->fx_24h` score `0.262` n `37` status `ready` deltaP `21.6962` edge `-0.0083` maxDD `-2.2197`
- `risk_on_high->fx_1h` score `0.145` n `68` status `ready` deltaP `5.037` edge `0.0039` maxDD `-0.0318`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
