# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-13T10:52:32.249380+00:00`
- Price records: `672`
- Market context records: `6596`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9808`

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

- `market_context_high->unknown_24h` score `3.9085` n `162` status `ready` deltaP `5.06` edge `0.622` maxDD `-15.0689`
- `market_context_high->unknown_1h` score `2.052` n `210` status `ready` deltaP `-4.98` edge `0.2943` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `0.697` n `162` status `ready` deltaP `10.2611` edge `0.1765` maxDD `-5.2791`
- `market_context_high->fx_1h` score `-0.3012` n `210` status `ready` deltaP `1.7565` edge `0.0004` maxDD `-0.7249`
- `market_context_high->crypto_major_1h` score `-0.4368` n `210` status `ready` deltaP `6.7479` edge `0.0256` maxDD `-6.7936`
- `market_context_high->index_1h` score `-0.5452` n `210` status `ready` deltaP `-0.231` edge `0.0036` maxDD `-0.7564`
- `market_context_high->commodity_1h` score `-0.5495` n `210` status `ready` deltaP `0.1896` edge `-0.0034` maxDD `-2.1314`
- `market_context_high->crypto_alt_1h` score `-0.6396` n `210` status `ready` deltaP `4.5438` edge `0.019` maxDD `-5.8368`
- `market_context_high->index_4h` score `-0.9262` n `210` status `ready` deltaP `8.9896` edge `0.0093` maxDD `-5.7046`
- `market_context_high->equity_1h` score `-1.1897` n `210` status `ready` deltaP `1.9319` edge `-0.001` maxDD `-4.2147`
- `market_context_high->commodity_4h` score `-1.2341` n `210` status `ready` deltaP `-0.5168` edge `-0.0053` maxDD `-5.6246`
- `market_context_high->metal_1h` score `-1.3339` n `210` status `ready` deltaP `-4.1759` edge `-0.0026` maxDD `-2.1239`
- `market_context_high->fx_4h` score `-1.6539` n `210` status `ready` deltaP `1.6013` edge `-0.0015` maxDD `-3.3635`
- `market_context_high->unknown_4h` score `-1.7495` n `210` status `ready` deltaP `-17.5232` edge `0.2116` maxDD `-10.5788`
- `market_context_high->crypto_major_4h` score `-1.8971` n `210` status `ready` deltaP `6.5143` edge `0.0448` maxDD `-16.8495`
- `market_context_high->metal_4h` score `-2.1941` n `210` status `ready` deltaP `-1.8061` edge `0.0168` maxDD `-5.2172`
- `market_context_high->crypto_alt_4h` score `-2.2055` n `210` status `ready` deltaP `3.4088` edge `0.0347` maxDD `-19.2145`
- `market_context_high->fx_24h` score `-3.7881` n `162` status `ready` deltaP `-4.7332` edge `-0.0006` maxDD `-9.2795`
- `market_context_high->metal_24h` score `-4.0991` n `162` status `ready` deltaP `1.3221` edge `0.0644` maxDD `-9.5181`
- `market_context_high->equity_4h` score `-4.8291` n `210` status `ready` deltaP `7.0485` edge `-0.0225` maxDD `-27.1529`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
