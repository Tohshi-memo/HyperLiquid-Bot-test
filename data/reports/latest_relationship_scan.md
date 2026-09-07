# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-07T13:07:27.586247+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10186`

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

- `risk_on_high->unknown_24h` score `394.1276` n `93` status `ready` deltaP `25.0` edge `32.6773` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `394.1276` n `93` status `ready` deltaP `25.0` edge `32.6773` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `22.3314` n `93` status `ready` deltaP `38.5865` edge `1.6554` maxDD `-1.4687`
- `risk_on_and_context->crypto_major_24h` score `22.3314` n `93` status `ready` deltaP `38.5865` edge `1.6554` maxDD `-1.4687`
- `risk_on_high->crypto_alt_24h` score `15.1838` n `93` status `ready` deltaP `32.1181` edge `1.0512` maxDD `0.0`
- `risk_on_and_context->crypto_alt_24h` score `15.1838` n `93` status `ready` deltaP `32.1181` edge `1.0512` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `8.5296` n `196` status `ready` deltaP `24.465` edge `0.6052` maxDD `-2.5998`
- `market_context_high->equity_24h` score `5.5108` n `196` status `ready` deltaP `19.4444` edge `0.3296` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `5.2893` n `117` status `ready` deltaP `28.8058` edge `0.2859` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.2893` n `117` status `ready` deltaP `28.8058` edge `0.2859` maxDD `-1.9733`
- `risk_on_high->equity_24h` score `4.7008` n `93` status `ready` deltaP `19.4444` edge `0.2621` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `4.7008` n `93` status `ready` deltaP `19.4444` edge `0.2621` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `4.3483` n `117` status `ready` deltaP `24.3043` edge `0.2862` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.3483` n `117` status `ready` deltaP `24.3043` edge `0.2862` maxDD `-3.8693`
- `risk_on_high->index_24h` score `2.4034` n `93` status `ready` deltaP `20.7325` edge `0.0663` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `2.4034` n `93` status `ready` deltaP `20.7325` edge `0.0663` maxDD `-0.0051`
- `market_context_high->index_24h` score `1.6277` n `196` status `ready` deltaP `14.7746` edge `0.0765` maxDD `-0.1483`
- `risk_on_high->metal_24h` score `0.8572` n `93` status `ready` deltaP `17.1875` edge `0.1109` maxDD `-0.9131`
- `risk_on_and_context->metal_24h` score `0.8572` n `93` status `ready` deltaP `17.1875` edge `0.1109` maxDD `-0.9131`
- `risk_on_high->crypto_alt_1h` score `0.7822` n `117` status `ready` deltaP `3.6479` edge `0.0761` maxDD `-1.1521`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
