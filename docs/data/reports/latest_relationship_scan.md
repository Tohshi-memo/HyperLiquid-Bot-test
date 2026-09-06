# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-06T22:18:48.032814+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10593`

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

- `risk_on_high->unknown_24h` score `327.6667` n `106` status `ready` deltaP `27.0833` edge `27.125` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `327.6667` n `106` status `ready` deltaP `27.0833` edge `27.125` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `19.7185` n `106` status `ready` deltaP `33.8705` edge `1.4691` maxDD `-1.4687`
- `risk_on_and_context->crypto_major_24h` score `19.7185` n `106` status `ready` deltaP `33.8705` edge `1.4691` maxDD `-1.4687`
- `risk_on_high->crypto_alt_24h` score `13.9192` n `106` status `ready` deltaP `30.0347` edge `0.9597` maxDD `0.0`
- `risk_on_and_context->crypto_alt_24h` score `13.9192` n `106` status `ready` deltaP `30.0347` edge `0.9597` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `8.6594` n `196` status `ready` deltaP `23.9123` edge `0.6197` maxDD `-2.5998`
- `market_context_high->unknown_1h` score `8.1619` n `250` status `ready` deltaP `-4.109` edge `0.78` maxDD `-2.4626`
- `market_context_high->equity_24h` score `6.8164` n `196` status `ready` deltaP `23.0903` edge `0.4141` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `6.5639` n `120` status `ready` deltaP `29.746` edge `0.3543` maxDD `-0.116`
- `risk_on_and_context->crypto_alt_4h` score `6.5639` n `120` status `ready` deltaP `29.746` edge `0.3543` maxDD `-0.116`
- `risk_on_high->equity_24h` score `5.9776` n `106` status `ready` deltaP `23.0903` edge `0.3442` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `5.9776` n `106` status `ready` deltaP `23.0903` edge `0.3442` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `4.3792` n `120` status `ready` deltaP `24.0447` edge `0.2905` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.3792` n `120` status `ready` deltaP `24.0447` edge `0.2905` maxDD `-3.8693`
- `risk_on_high->index_24h` score `2.7821` n `106` status `ready` deltaP `23.0379` edge `0.0825` maxDD `-0.006`
- `risk_on_and_context->index_24h` score `2.7821` n `106` status `ready` deltaP `23.0379` edge `0.0825` maxDD `-0.006`
- `market_context_high->index_24h` score `2.7605` n `196` status `ready` deltaP `22.2967` edge `0.0958` maxDD `-0.1522`
- `risk_on_high->crypto_alt_1h` score `1.1952` n `129` status `ready` deltaP `5.279` edge `0.0943` maxDD `-0.7247`
- `risk_on_and_context->crypto_alt_1h` score `1.1952` n `129` status `ready` deltaP `5.279` edge `0.0943` maxDD `-0.7247`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
