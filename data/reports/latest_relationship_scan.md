# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-07T12:52:28.643802+00:00`
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

- `risk_on_high->unknown_24h` score `397.4583` n `93` status `ready` deltaP `25.1736` edge `32.9537` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `397.4583` n `93` status `ready` deltaP `25.1736` edge `32.9537` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `22.3242` n `93` status `ready` deltaP `38.5865` edge `1.6548` maxDD `-1.4687`
- `risk_on_and_context->crypto_major_24h` score `22.3242` n `93` status `ready` deltaP `38.5865` edge `1.6548` maxDD `-1.4687`
- `risk_on_high->crypto_alt_24h` score `15.1922` n `93` status `ready` deltaP `32.1181` edge `1.0519` maxDD `0.0`
- `risk_on_and_context->crypto_alt_24h` score `15.1922` n `93` status `ready` deltaP `32.1181` edge `1.0519` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `8.5721` n `195` status `ready` deltaP `24.4258` edge `0.609` maxDD `-2.5998`
- `market_context_high->equity_24h` score `5.581` n `195` status `ready` deltaP `19.6181` edge `0.3343` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `5.3037` n `117` status `ready` deltaP `28.8058` edge `0.2871` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.3037` n `117` status `ready` deltaP `28.8058` edge `0.2871` maxDD `-1.9733`
- `risk_on_high->equity_24h` score `4.735` n `93` status `ready` deltaP `19.6181` edge `0.2638` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `4.735` n `93` status `ready` deltaP `19.6181` edge `0.2638` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `4.3471` n `117` status `ready` deltaP `24.3043` edge `0.2861` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.3471` n `117` status `ready` deltaP `24.3043` edge `0.2861` maxDD `-3.8693`
- `risk_on_high->index_24h` score `2.4233` n `93` status `ready` deltaP `20.9061` edge `0.0668` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `2.4233` n `93` status `ready` deltaP `20.9061` edge `0.0668` maxDD `-0.0051`
- `market_context_high->index_24h` score `1.6498` n `195` status `ready` deltaP `14.9011` edge `0.0775` maxDD `-0.1483`
- `risk_on_high->metal_24h` score `0.865` n `93` status `ready` deltaP `17.1875` edge `0.1119` maxDD `-0.9131`
- `risk_on_and_context->metal_24h` score `0.865` n `93` status `ready` deltaP `17.1875` edge `0.1119` maxDD `-0.9131`
- `risk_on_high->crypto_alt_1h` score `0.8098` n `117` status `ready` deltaP `3.7976` edge `0.0774` maxDD `-1.1521`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
