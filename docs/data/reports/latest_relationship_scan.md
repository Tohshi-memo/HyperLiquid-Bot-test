# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-15T10:07:38.445017+00:00`
- Price records: `672`
- Market context records: `3981`
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

- `risk_on_high->unknown_4h` score `147.6087` n `40` status `ready` deltaP `-0.5793` edge `12.4858` maxDD `-10.8303`
- `risk_on_and_context->unknown_4h` score `147.6087` n `40` status `ready` deltaP `-0.5793` edge `12.4858` maxDD `-10.8303`
- `market_context_high->unknown_24h` score `30.6234` n `152` status `ready` deltaP `-7.1729` edge `3.1376` maxDD `-35.0266`
- `market_context_high->unknown_4h` score `19.5915` n `165` status `ready` deltaP `0.7086` edge `2.1688` maxDD `-35.6052`
- `risk_on_high->equity_24h` score `9.2591` n `40` status `ready` deltaP `42.0139` edge `0.4915` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.2591` n `40` status `ready` deltaP `42.0139` edge `0.4915` maxDD `0.0`
- `risk_on_high->equity_4h` score `3.7123` n `40` status `ready` deltaP `37.439` edge `0.0645` maxDD `-0.0458`
- `risk_on_and_context->equity_4h` score `3.7123` n `40` status `ready` deltaP `37.439` edge `0.0645` maxDD `-0.0458`
- `market_context_high->metal_24h` score `3.6222` n `152` status `ready` deltaP `17.0779` edge `0.3395` maxDD `-9.1203`
- `market_context_high->index_24h` score `3.3805` n `152` status `ready` deltaP `25.9137` edge `0.2229` maxDD `-7.1159`
- `market_context_high->equity_24h` score `3.0085` n `152` status `ready` deltaP `18.9876` edge `0.4271` maxDD `-14.5715`
- `risk_on_high->index_24h` score `2.7945` n `40` status `ready` deltaP `29.8611` edge `0.0338` maxDD `0.0`
- `risk_on_and_context->index_24h` score `2.7945` n `40` status `ready` deltaP `29.8611` edge `0.0338` maxDD `0.0`
- `market_context_high->equity_4h` score `2.5536` n `165` status `ready` deltaP `20.5451` edge `0.2061` maxDD `-7.0879`
- `market_context_high->crypto_major_4h` score `2.2364` n `165` status `ready` deltaP `19.3847` edge `0.2138` maxDD `-7.8662`
- `risk_on_high->crypto_major_4h` score `1.9234` n `40` status `ready` deltaP `20.9756` edge `0.087` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.9234` n `40` status `ready` deltaP `20.9756` edge `0.087` maxDD `-2.6576`
- `market_context_high->crypto_major_1h` score `1.6057` n `165` status `ready` deltaP `12.2891` edge `0.1061` maxDD `-2.3372`
- `market_context_high->equity_1h` score `1.1687` n `165` status `ready` deltaP `9.7805` edge `0.0886` maxDD `-2.1799`
- `market_context_high->crypto_alt_4h` score `1.0049` n `165` status `ready` deltaP `13.7555` edge `0.1225` maxDD `-7.1038`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
