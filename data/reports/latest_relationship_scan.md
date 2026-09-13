# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-13T16:52:41.377560+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13440`

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

- `market_context_high->unknown_24h` score `17793.2628` n `56` status `ready` deltaP `10.2093` edge `1482.724` maxDD `-0.613`
- `risk_on_high->unknown_24h` score `7944.6327` n `37` status `ready` deltaP `11.0298` edge `661.9857` maxDD `-0.1869`
- `risk_on_and_context->unknown_24h` score `7944.6327` n `37` status `ready` deltaP `11.0298` edge `661.9857` maxDD `-0.1869`
- `news_risk_high->unknown_1h` score `422.0703` n `82` status `ready` deltaP `-5.1008` edge `35.2487` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `18.6139` n `82` status `ready` deltaP `35.8578` edge `1.3609` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `18.4012` n `82` status `ready` deltaP `38.0236` edge `1.427` maxDD `-9.098`
- `news_risk_high->equity_24h` score `8.9526` n `82` status `ready` deltaP `26.0639` edge `0.7503` maxDD `-6.5742`
- `news_risk_high->index_24h` score `6.9801` n `82` status `ready` deltaP `49.836` edge `0.2671` maxDD `-0.0797`
- `news_risk_high->metal_24h` score `4.6248` n `82` status `ready` deltaP `24.9327` edge `0.2646` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `4.313` n `37` status `ready` deltaP `39.8276` edge `0.0939` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.313` n `37` status `ready` deltaP `39.8276` edge `0.0939` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.2782` n `56` status `ready` deltaP `39.8276` edge `0.091` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `3.3135` n `37` status `ready` deltaP `9.6878` edge `0.4755` maxDD `-6.5554`
- `risk_on_and_context->crypto_alt_24h` score `3.3135` n `37` status `ready` deltaP `9.6878` edge `0.4755` maxDD `-6.5554`
- `market_context_high->crypto_alt_24h` score `3.0401` n `56` status `ready` deltaP `8.2881` edge `0.4823` maxDD `-9.1576`
- `market_context_high->metal_24h` score `0.8186` n `56` status `ready` deltaP `10.6034` edge `0.1226` maxDD `-1.4001`
- `news_risk_high->index_4h` score `0.3966` n `82` status `ready` deltaP `12.0427` edge `0.0334` maxDD `-0.6935`
- `risk_on_high->index_24h` score `0.3822` n `37` status `ready` deltaP `25.1492` edge `-0.0057` maxDD `-4.0372`
- `risk_on_and_context->index_24h` score `0.3822` n `37` status `ready` deltaP `25.1492` edge `-0.0057` maxDD `-4.0372`
- `risk_on_high->crypto_alt_4h` score `0.2564` n `63` status `ready` deltaP `9.0351` edge `0.1401` maxDD `-6.7304`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
