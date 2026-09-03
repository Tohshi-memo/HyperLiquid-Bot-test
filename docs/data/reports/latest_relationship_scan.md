# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-03T09:52:27.467744+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11581`

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

- `risk_on_high->unknown_4h` score `37.9453` n `129` status `ready` deltaP `14.2702` edge `3.1288` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `37.9453` n `129` status `ready` deltaP `14.2702` edge `3.1288` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `28.6848` n `164` status `ready` deltaP `11.5854` edge `2.3827` maxDD `-2.563`
- `risk_on_high->unknown_1h` score `19.7426` n `133` status `ready` deltaP `2.5392` edge `1.686` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `19.7426` n `133` status `ready` deltaP `2.5392` edge `1.686` maxDD `-1.95`
- `market_context_high->unknown_1h` score `13.656` n `176` status `ready` deltaP `1.8984` edge `1.1884` maxDD `-2.0446`
- `risk_on_high->equity_24h` score `4.125` n `107` status `ready` deltaP `20.2298` edge `0.6234` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `4.125` n `107` status `ready` deltaP `20.2298` edge `0.6234` maxDD `-19.828`
- `market_context_high->equity_24h` score `2.9126` n `140` status `ready` deltaP `18.9881` edge `0.5507` maxDD `-20.7654`
- `risk_on_high->crypto_alt_24h` score `2.0597` n `107` status `ready` deltaP `20.3888` edge `0.8185` maxDD `-42.8959`
- `risk_on_and_context->crypto_alt_24h` score `2.0597` n `107` status `ready` deltaP `20.3888` edge `0.8185` maxDD `-42.8959`
- `news_risk_high->crypto_alt_24h` score `2.0307` n `59` status `ready` deltaP `20.3096` edge `0.4184` maxDD `-19.4761`
- `news_risk_high->crypto_major_24h` score `1.3909` n `59` status `ready` deltaP `14.0007` edge `0.4609` maxDD `-30.7329`
- `news_risk_high->equity_24h` score `1.1251` n `59` status `ready` deltaP `6.1794` edge `0.2993` maxDD `-15.4056`
- `risk_on_high->crypto_major_24h` score `0.7518` n `107` status `ready` deltaP `20.3368` edge `0.8352` maxDD `-56.9519`
- `risk_on_and_context->crypto_major_24h` score `0.7518` n `107` status `ready` deltaP `20.3368` edge `0.8352` maxDD `-56.9519`
- `market_context_high->crypto_alt_24h` score `0.6938` n `140` status `ready` deltaP `15.9028` edge `0.7328` maxDD `-46.3234`
- `market_context_high->crypto_major_24h` score `0.481` n `140` status `ready` deltaP `22.8869` edge `0.8555` maxDD `-61.3797`
- `news_risk_high->commodity_4h` score `0.266` n `67` status `ready` deltaP `5.6425` edge `0.0324` maxDD `-0.8733`
- `risk_on_high->metal_1h` score `0.04` n `133` status `ready` deltaP `11.0655` edge `0.0026` maxDD `-1.699`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
