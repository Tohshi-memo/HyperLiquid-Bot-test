# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-22T08:52:29.897349+00:00`
- Price records: `672`
- Market context records: `7548`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14475`

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

- `risk_on_high->crypto_major_4h` score `8.0032` n `36` status `ready` deltaP `41.8191` edge `0.4074` maxDD `-0.8742`
- `risk_on_and_context->crypto_major_4h` score `8.0032` n `36` status `ready` deltaP `41.8191` edge `0.4074` maxDD `-0.8742`
- `risk_on_high->crypto_alt_4h` score `5.3634` n `36` status `ready` deltaP `31.6227` edge `0.2605` maxDD `-0.9492`
- `risk_on_and_context->crypto_alt_4h` score `5.3634` n `36` status `ready` deltaP `31.6227` edge `0.2605` maxDD `-0.9492`
- `risk_on_high->unknown_4h` score `4.6279` n `36` status `ready` deltaP `15.6504` edge `0.3243` maxDD `-0.4384`
- `risk_on_and_context->unknown_4h` score `4.6279` n `36` status `ready` deltaP `15.6504` edge `0.3243` maxDD `-0.4384`
- `risk_on_high->crypto_major_24h` score `4.1463` n `36` status `ready` deltaP `10.7638` edge `0.3759` maxDD `-5.8371`
- `risk_on_and_context->crypto_major_24h` score `4.1463` n `36` status `ready` deltaP `10.7638` edge `0.3759` maxDD `-5.8371`
- `risk_on_high->crypto_major_1h` score `1.7005` n `36` status `ready` deltaP `24.5509` edge `0.0788` maxDD `-0.957`
- `risk_on_and_context->crypto_major_1h` score `1.7005` n `36` status `ready` deltaP `24.5509` edge `0.0788` maxDD `-0.957`
- `risk_on_high->crypto_alt_24h` score `1.0487` n `36` status `ready` deltaP `11.4584` edge `0.1509` maxDD `-5.0938`
- `risk_on_and_context->crypto_alt_24h` score `1.0487` n `36` status `ready` deltaP `11.4584` edge `0.1509` maxDD `-5.0938`
- `risk_on_high->fx_24h` score `0.9834` n `35` status `ready` deltaP `22.439` edge `0.0221` maxDD `-1.3162`
- `risk_on_and_context->fx_24h` score `0.9834` n `35` status `ready` deltaP `22.439` edge `0.0221` maxDD `-1.3162`
- `risk_on_high->equity_1h` score `0.6135` n `36` status `ready` deltaP `9.6097` edge `0.0523` maxDD `-1.3497`
- `risk_on_and_context->equity_1h` score `0.6135` n `36` status `ready` deltaP `9.6097` edge `0.0523` maxDD `-1.3497`
- `risk_on_high->commodity_1h` score `0.4589` n `36` status `ready` deltaP `5.9309` edge `0.0268` maxDD `-0.2479`
- `risk_on_and_context->commodity_1h` score `0.4589` n `36` status `ready` deltaP `5.9309` edge `0.0268` maxDD `-0.2479`
- `risk_on_high->crypto_alt_1h` score `0.3248` n `36` status `ready` deltaP `3.3766` edge `0.0562` maxDD `-0.9651`
- `risk_on_and_context->crypto_alt_1h` score `0.3248` n `36` status `ready` deltaP `3.3766` edge `0.0562` maxDD `-0.9651`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
