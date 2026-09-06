# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-06T21:37:30.751674+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10545`

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

- `risk_on_high->unknown_24h` score `301.7066` n `105` status `ready` deltaP `27.2569` edge `24.9605` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `301.7066` n `105` status `ready` deltaP `27.2569` edge `24.9605` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `19.9485` n `105` status `ready` deltaP `33.7897` edge `1.4888` maxDD `-1.4687`
- `risk_on_and_context->crypto_major_24h` score `19.9485` n `105` status `ready` deltaP `33.7897` edge `1.4888` maxDD `-1.4687`
- `risk_on_high->crypto_alt_24h` score `13.7329` n `105` status `ready` deltaP `29.4295` edge `0.9565` maxDD `-0.3296`
- `risk_on_and_context->crypto_alt_24h` score `13.7329` n `105` status `ready` deltaP `29.4295` edge `0.9565` maxDD `-0.3296`
- `market_context_high->crypto_alt_24h` score `8.4844` n `196` status `ready` deltaP `23.239` edge `0.6096` maxDD `-2.5998`
- `market_context_high->unknown_1h` score `7.8463` n `250` status `ready` deltaP `-4.109` edge `0.7537` maxDD `-2.4626`
- `market_context_high->equity_24h` score `6.8056` n `196` status `ready` deltaP `23.0903` edge `0.4132` maxDD `0.0`
- `risk_on_high->equity_24h` score `6.0148` n `105` status `ready` deltaP `23.0903` edge `0.3473` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `6.0148` n `105` status `ready` deltaP `23.0903` edge `0.3473` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `5.5499` n `119` status `ready` deltaP `29.1824` edge `0.3261` maxDD `-3.9857`
- `risk_on_and_context->crypto_alt_4h` score `5.5499` n `119` status `ready` deltaP `29.1824` edge `0.3261` maxDD `-3.9857`
- `risk_on_high->crypto_major_4h` score `3.8565` n `119` status `ready` deltaP `23.3552` edge `0.2657` maxDD `-5.0021`
- `risk_on_and_context->crypto_major_4h` score `3.8565` n `119` status `ready` deltaP `23.3552` edge `0.2657` maxDD `-5.0021`
- `risk_on_high->index_24h` score `2.6525` n `105` status `ready` deltaP `22.4058` edge `0.0821` maxDD `-0.1675`
- `risk_on_and_context->index_24h` score `2.6525` n `105` status `ready` deltaP `22.4058` edge `0.0821` maxDD `-0.1675`
- `market_context_high->index_24h` score `2.5075` n `196` status `ready` deltaP `21.6235` edge `0.0948` maxDD `-0.3996`
- `risk_on_high->crypto_alt_1h` score `0.9956` n `128` status `ready` deltaP `5.132` edge `0.0882` maxDD `-1.4894`
- `risk_on_and_context->crypto_alt_1h` score `0.9956` n `128` status `ready` deltaP `5.132` edge `0.0882` maxDD `-1.4894`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
