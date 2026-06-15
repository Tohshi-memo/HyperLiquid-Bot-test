# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-15T07:52:36.961897+00:00`
- Price records: `672`
- Market context records: `3972`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10092`

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

- `risk_on_high->unknown_4h` score `148.0965` n `40` status `ready` deltaP `0.7927` edge `12.5173` maxDD `-10.8303`
- `risk_on_and_context->unknown_4h` score `148.0965` n `40` status `ready` deltaP `0.7927` edge `12.5173` maxDD `-10.8303`
- `market_context_high->unknown_24h` score `31.3458` n `151` status `ready` deltaP `-6.5558` edge `3.2301` maxDD `-37.9399`
- `market_context_high->unknown_4h` score `19.852` n `165` status `ready` deltaP `1.4745` edge `2.1854` maxDD `-35.6052`
- `risk_on_high->equity_24h` score `9.1559` n `40` status `ready` deltaP `42.0139` edge `0.4829` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.1559` n `40` status `ready` deltaP `42.0139` edge `0.4829` maxDD `0.0`
- `market_context_high->metal_24h` score `3.6472` n `151` status `ready` deltaP `16.9254` edge `0.3426` maxDD `-9.1203`
- `risk_on_high->equity_4h` score `3.5419` n `40` status `ready` deltaP `37.439` edge `0.0503` maxDD `-0.0458`
- `risk_on_and_context->equity_4h` score `3.5419` n `40` status `ready` deltaP `37.439` edge `0.0503` maxDD `-0.0458`
- `market_context_high->index_24h` score `3.3244` n `151` status `ready` deltaP `25.8876` edge `0.2184` maxDD `-7.1159`
- `market_context_high->equity_24h` score `2.8499` n `151` status `ready` deltaP `18.8351` edge `0.4149` maxDD `-14.5715`
- `risk_on_high->index_24h` score `2.7633` n `40` status `ready` deltaP `29.8611` edge `0.0312` maxDD `0.0`
- `risk_on_and_context->index_24h` score `2.7633` n `40` status `ready` deltaP `29.8611` edge `0.0312` maxDD `0.0`
- `market_context_high->equity_4h` score `2.4228` n `165` status `ready` deltaP `20.5451` edge `0.1952` maxDD `-7.0879`
- `market_context_high->crypto_major_4h` score `2.2041` n `165` status `ready` deltaP `19.6859` edge `0.2091` maxDD `-7.8662`
- `risk_on_high->crypto_major_4h` score `1.7598` n `40` status `ready` deltaP `20.6707` edge `0.0754` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.7598` n `40` status `ready` deltaP `20.6707` edge `0.0754` maxDD `-2.6576`
- `market_context_high->crypto_major_1h` score `1.6316` n `166` status `ready` deltaP `12.6578` edge `0.1058` maxDD `-2.3372`
- `market_context_high->equity_1h` score `1.1775` n `166` status `ready` deltaP `9.9813` edge `0.088` maxDD `-2.1799`
- `market_context_high->metal_1h` score `1.0869` n `166` status `ready` deltaP `12.6398` edge `0.0657` maxDD `-2.751`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
