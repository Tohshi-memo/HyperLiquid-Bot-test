# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-13T18:37:26.531315+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12834`

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

- `market_context_high->unknown_24h` score `17736.8448` n `56` status `ready` deltaP `10.2093` edge `1478.0225` maxDD `-0.613`
- `risk_on_high->unknown_24h` score `7856.1471` n `37` status `ready` deltaP `11.0298` edge `654.6119` maxDD `-0.1869`
- `risk_on_and_context->unknown_24h` score `7856.1471` n `37` status `ready` deltaP `11.0298` edge `654.6119` maxDD `-0.1869`
- `news_risk_high->unknown_1h` score `426.8884` n `82` status `ready` deltaP `-5.4002` edge `35.6522` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `18.6727` n `82` status `ready` deltaP `36.2027` edge `1.3635` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `18.3844` n `82` status `ready` deltaP `38.0236` edge `1.4256` maxDD `-9.098`
- `news_risk_high->equity_24h` score `9.3167` n `82` status `ready` deltaP `27.2708` edge `0.7726` maxDD `-6.5742`
- `news_risk_high->index_24h` score `7.1247` n `82` status `ready` deltaP `51.0429` edge `0.2711` maxDD `-0.0797`
- `news_risk_high->metal_24h` score `4.7358` n `82` status `ready` deltaP `26.1396` edge `0.2658` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `4.5818` n `37` status `ready` deltaP `39.8276` edge `0.1163` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.5818` n `37` status `ready` deltaP `39.8276` edge `0.1163` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.4486` n `56` status `ready` deltaP `39.8276` edge `0.1052` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `2.6135` n `37` status `ready` deltaP `4.6273` edge `0.4378` maxDD `-7.0204`
- `risk_on_and_context->crypto_alt_24h` score `2.6135` n `37` status `ready` deltaP `4.6273` edge `0.4378` maxDD `-7.0204`
- `market_context_high->crypto_alt_24h` score `2.5415` n `56` status `ready` deltaP `5.0616` edge `0.4582` maxDD `-9.6226`
- `risk_on_high->fx_24h` score `0.6602` n `37` status `ready` deltaP `26.7568` edge `-0.0021` maxDD `-1.9974`
- `risk_on_and_context->fx_24h` score `0.6602` n `37` status `ready` deltaP `26.7568` edge `-0.0021` maxDD `-1.9974`
- `market_context_high->commodity_4h` score `0.4664` n `131` status `ready` deltaP `11.3794` edge `0.01` maxDD `-0.4265`
- `news_risk_high->index_4h` score `0.4291` n `82` status `ready` deltaP `12.6524` edge `0.0335` maxDD `-0.6935`
- `risk_on_high->commodity_4h` score `0.3407` n `59` status `ready` deltaP `9.2058` edge `0.0047` maxDD `-0.348`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
