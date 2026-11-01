# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-01T07:07:27.607521+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6337`

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

- `market_context_high->unknown_24h` score `7033.2529` n `55` status `ready` deltaP `4.8611` edge `586.072` maxDD `0.0`
- `market_context_high->unknown_4h` score `372.5715` n `55` status `ready` deltaP `5.3464` edge `31.0163` maxDD `-0.0124`
- `news_risk_high->unknown_1h` score `78.1924` n `108` status `ready` deltaP `-5.1951` edge `6.5793` maxDD `-0.9571`
- `market_context_high->unknown_1h` score `48.9005` n `55` status `ready` deltaP `2.4143` edge `4.07` maxDD `-0.2178`
- `market_context_high->equity_24h` score `21.7697` n `55` status `ready` deltaP `46.4457` edge `1.5281` maxDD `-1.5546`
- `news_risk_high->crypto_alt_24h` score `13.1726` n `98` status `ready` deltaP `30.6796` edge `1.0288` maxDD `-6.8493`
- `market_context_high->index_24h` score `7.3094` n `55` status `ready` deltaP `60.2431` edge `0.2075` maxDD `0.0`
- `market_context_high->commodity_24h` score `6.756` n `55` status `ready` deltaP `46.4836` edge `0.2842` maxDD `-0.8203`
- `market_context_high->crypto_alt_4h` score `5.7993` n `55` status `ready` deltaP `23.4451` edge `0.3564` maxDD `-1.6876`
- `market_context_high->crypto_major_4h` score `5.4729` n `55` status `ready` deltaP `30.4352` edge `0.2868` maxDD `-1.6901`
- `news_risk_high->crypto_alt_4h` score `4.8843` n `108` status `ready` deltaP `18.4451` edge `0.4227` maxDD `-7.4246`
- `market_context_high->commodity_4h` score `3.3901` n `55` status `ready` deltaP `31.6768` edge `0.0964` maxDD `-0.3387`
- `market_context_high->equity_4h` score `3.3722` n `55` status `ready` deltaP `6.0477` edge `0.3109` maxDD `-2.283`
- `market_context_high->crypto_major_24h` score `2.6338` n `55` status `ready` deltaP `11.9003` edge `0.326` maxDD `-3.0799`
- `market_context_high->crypto_alt_24h` score `1.9867` n `55` status `ready` deltaP `-4.1256` edge `0.434` maxDD `-8.8096`
- `market_context_high->metal_4h` score `1.5644` n `55` status `ready` deltaP `18.5033` edge `0.0495` maxDD `-0.7323`
- `market_context_high->equity_1h` score `1.4303` n `55` status `ready` deltaP `1.9788` edge `0.1585` maxDD `-1.5336`
- `market_context_high->crypto_major_1h` score `1.4108` n `55` status `ready` deltaP `8.1818` edge `0.124` maxDD `-2.2118`
- `market_context_high->crypto_alt_1h` score `1.3727` n `55` status `ready` deltaP `4.0746` edge `0.1543` maxDD `-2.3659`
- `market_context_high->metal_1h` score `0.8612` n `55` status `ready` deltaP `10.7267` edge `0.0251` maxDD `-0.3209`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
