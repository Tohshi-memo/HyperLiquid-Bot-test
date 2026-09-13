# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-13T17:37:29.619468+00:00`
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

- `market_context_high->unknown_24h` score `17736.9828` n `56` status `ready` deltaP `10.2093` edge `1478.034` maxDD `-0.613`
- `risk_on_high->unknown_24h` score `7856.3631` n `37` status `ready` deltaP `11.0298` edge `654.6299` maxDD `-0.1869`
- `risk_on_and_context->unknown_24h` score `7856.3631` n `37` status `ready` deltaP `11.0298` edge `654.6299` maxDD `-0.1869`
- `news_risk_high->unknown_1h` score `426.9771` n `82` status `ready` deltaP `-5.1008` edge `35.6576` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `18.6487` n `82` status `ready` deltaP `36.2027` edge `1.3615` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `18.3928` n `82` status `ready` deltaP `38.0236` edge `1.4263` maxDD `-9.098`
- `news_risk_high->equity_24h` score `9.1068` n `82` status `ready` deltaP `26.5812` edge `0.7597` maxDD `-6.5742`
- `news_risk_high->index_24h` score `7.0407` n `82` status `ready` deltaP `50.3532` edge `0.2687` maxDD `-0.0797`
- `news_risk_high->metal_24h` score `4.6722` n `82` status `ready` deltaP `25.45` edge `0.2651` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `4.4246` n `37` status `ready` deltaP `39.8276` edge `0.1032` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.4246` n `37` status `ready` deltaP `39.8276` edge `0.1032` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.349` n `56` status `ready` deltaP `39.8276` edge `0.0969` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `2.8366` n `37` status `ready` deltaP `4.6273` edge `0.4664` maxDD `-7.0204`
- `risk_on_and_context->crypto_alt_24h` score `2.8366` n `37` status `ready` deltaP `4.6273` edge `0.4664` maxDD `-7.0204`
- `market_context_high->crypto_alt_24h` score `2.6842` n `56` status `ready` deltaP `5.0616` edge `0.4765` maxDD `-9.6226`
- `market_context_high->metal_24h` score `0.4129` n `56` status `ready` deltaP `5.7636` edge `0.118` maxDD `-1.6124`
- `news_risk_high->index_4h` score `0.3958` n `82` status `ready` deltaP `12.0427` edge `0.0333` maxDD `-0.6935`
- `market_context_high->commodity_4h` score `0.2058` n `131` status `ready` deltaP `8.9358` edge `0.0073` maxDD `-0.6445`
- `risk_on_high->fx_1h` score `0.1359` n `70` status `ready` deltaP `4.9529` edge `0.0037` maxDD `-0.0318`
- `risk_on_and_context->fx_1h` score `0.1359` n `70` status `ready` deltaP `4.9529` edge `0.0037` maxDD `-0.0318`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
