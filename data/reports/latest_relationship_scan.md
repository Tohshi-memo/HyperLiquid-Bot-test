# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-13T19:52:27.120858+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12738`

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

- `market_context_high->unknown_24h` score `17678.9724` n `56` status `ready` deltaP `10.2093` edge `1473.1998` maxDD `-0.613`
- `risk_on_high->unknown_24h` score `7765.3803` n `37` status `ready` deltaP `11.0298` edge `647.048` maxDD `-0.1869`
- `risk_on_and_context->unknown_24h` score `7765.3803` n `37` status `ready` deltaP `11.0298` edge `647.048` maxDD `-0.1869`
- `news_risk_high->unknown_1h` score `429.5787` n `82` status `ready` deltaP `-5.1008` edge `35.8744` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `18.6787` n `82` status `ready` deltaP `36.2027` edge `1.364` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `18.3448` n `82` status `ready` deltaP `38.0236` edge `1.4223` maxDD `-9.098`
- `news_risk_high->equity_24h` score `9.5717` n `82` status `ready` deltaP `28.1329` edge `0.7881` maxDD `-6.5742`
- `news_risk_high->index_24h` score `7.2308` n `82` status `ready` deltaP `51.9049` edge `0.2742` maxDD `-0.0797`
- `news_risk_high->metal_24h` score `4.7843` n `82` status `ready` deltaP `26.6569` edge `0.2664` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `4.7582` n `37` status `ready` deltaP `39.8276` edge `0.131` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.7582` n `37` status `ready` deltaP `39.8276` edge `0.131` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.5614` n `56` status `ready` deltaP `39.8276` edge `0.1146` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `3.9163` n `37` status `ready` deltaP `4.6273` edge `0.4291` maxDD `-7.0204`
- `risk_on_and_context->crypto_alt_24h` score `3.9163` n `37` status `ready` deltaP `4.6273` edge `0.4291` maxDD `-7.0204`
- `market_context_high->crypto_alt_24h` score `2.4986` n `56` status `ready` deltaP `5.0616` edge `0.4527` maxDD `-9.6226`
- `risk_on_high->fx_24h` score `1.6674` n `37` status `ready` deltaP `39.4082` edge `0.0144` maxDD `-1.4012`
- `risk_on_and_context->fx_24h` score `1.6674` n `37` status `ready` deltaP `39.4082` edge `0.0144` maxDD `-1.4012`
- `risk_on_high->commodity_4h` score `0.9355` n `59` status `ready` deltaP `15.3756` edge `0.0118` maxDD `-0.2407`
- `risk_on_and_context->commodity_4h` score `0.9355` n `59` status `ready` deltaP `15.3756` edge `0.0118` maxDD `-0.2407`
- `market_context_high->commodity_4h` score `0.7577` n `131` status `ready` deltaP `13.823` edge `0.0128` maxDD `-0.345`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
