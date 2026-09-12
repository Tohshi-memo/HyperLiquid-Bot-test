# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-12T22:37:27.377931+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12499`

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

- `market_context_high->unknown_24h` score `13991.2777` n `65` status `ready` deltaP `12.3745` edge `1165.8625` maxDD `-0.082`
- `news_risk_high->unknown_1h` score `382.3792` n `82` status `ready` deltaP `-5.5499` edge `31.9441` maxDD `-1.7068`
- `news_risk_high->crypto_major_24h` score `18.0398` n `80` status `ready` deltaP `39.2361` edge `1.3888` maxDD `-9.098`
- `news_risk_high->crypto_alt_24h` score `17.9752` n `80` status `ready` deltaP `32.6736` edge `1.3289` maxDD `-2.2369`
- `market_context_high->crypto_alt_24h` score `11.9358` n `65` status `ready` deltaP `25.5582` edge `0.907` maxDD `-3.9523`
- `market_context_high->equity_24h` score `9.9569` n `65` status `ready` deltaP `44.2708` edge `0.5346` maxDD `0.0`
- `news_risk_high->equity_24h` score `6.3716` n `80` status `ready` deltaP `15.5208` edge `0.5907` maxDD `-6.0567`
- `news_risk_high->index_24h` score `6.2412` n `80` status `ready` deltaP `43.1944` edge `0.2498` maxDD `-0.0797`
- `news_risk_high->metal_24h` score `5.2574` n `80` status `ready` deltaP `30.4514` edge `0.2805` maxDD `-0.6317`
- `market_context_high->commodity_24h` score `3.5495` n `65` status `ready` deltaP `37.5721` edge `0.0545` maxDD `-0.0687`
- `market_context_high->index_24h` score `3.319` n `65` status `ready` deltaP `35.4059` edge `0.0799` maxDD `-0.1483`
- `risk_on_high->crypto_alt_4h` score `0.3986` n `47` status `ready` deltaP `8.3614` edge `0.1414` maxDD `-6.0162`
- `risk_on_and_context->crypto_alt_4h` score `0.3986` n `47` status `ready` deltaP `8.3614` edge `0.1414` maxDD `-6.0162`
- `risk_on_high->index_1h` score `0.1158` n `53` status `ready` deltaP `7.4427` edge `0.0006` maxDD `-0.163`
- `risk_on_and_context->index_1h` score `0.1158` n `53` status `ready` deltaP `7.4427` edge `0.0006` maxDD `-0.163`
- `news_risk_high->index_4h` score `0.0747` n `82` status `ready` deltaP `6.7073` edge `0.0277` maxDD `-0.6935`
- `risk_on_high->metal_1h` score `-0.0248` n `53` status `ready` deltaP `4.3865` edge `0.0006` maxDD `-0.3081`
- `risk_on_and_context->metal_1h` score `-0.0248` n `53` status `ready` deltaP `4.3865` edge `0.0006` maxDD `-0.3081`
- `market_context_high->metal_24h` score `-0.097` n `65` status `ready` deltaP `5.2591` edge `0.1034` maxDD `-3.4053`
- `risk_on_high->fx_1h` score `-0.184` n `53` status `ready` deltaP `-0.1356` edge `0.003` maxDD `-0.0548`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
