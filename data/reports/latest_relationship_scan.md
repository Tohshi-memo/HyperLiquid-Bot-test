# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-15T10:22:32.710256+00:00`
- Price records: `672`
- Market context records: `3982`
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

- `risk_on_high->unknown_4h` score `147.5449` n `40` status `ready` deltaP `-0.7317` edge `12.4815` maxDD `-10.8303`
- `risk_on_and_context->unknown_4h` score `147.5449` n `40` status `ready` deltaP `-0.7317` edge `12.4815` maxDD `-10.8303`
- `market_context_high->unknown_24h` score `30.5171` n `152` status `ready` deltaP `-7.3465` edge `3.1299` maxDD `-35.0266`
- `market_context_high->unknown_4h` score `19.5277` n `165` status `ready` deltaP `0.5562` edge `2.1645` maxDD `-35.6052`
- `risk_on_high->equity_24h` score `9.2735` n `40` status `ready` deltaP `42.0139` edge `0.4927` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.2735` n `40` status `ready` deltaP `42.0139` edge `0.4927` maxDD `0.0`
- `risk_on_high->equity_4h` score `3.7267` n `40` status `ready` deltaP `37.439` edge `0.0657` maxDD `-0.0458`
- `risk_on_and_context->equity_4h` score `3.7267` n `40` status `ready` deltaP `37.439` edge `0.0657` maxDD `-0.0458`
- `market_context_high->metal_24h` score `3.5934` n `152` status `ready` deltaP `17.0779` edge `0.3371` maxDD `-9.1203`
- `market_context_high->index_24h` score `3.3865` n `152` status `ready` deltaP `25.9137` edge `0.2234` maxDD `-7.1159`
- `market_context_high->equity_24h` score `3.0229` n `152` status `ready` deltaP `18.9876` edge `0.4283` maxDD `-14.5715`
- `risk_on_high->index_24h` score `2.8005` n `40` status `ready` deltaP `29.8611` edge `0.0343` maxDD `0.0`
- `risk_on_and_context->index_24h` score `2.8005` n `40` status `ready` deltaP `29.8611` edge `0.0343` maxDD `0.0`
- `market_context_high->equity_4h` score `2.568` n `165` status `ready` deltaP `20.5451` edge `0.2073` maxDD `-7.0879`
- `market_context_high->crypto_major_4h` score `2.2472` n `165` status `ready` deltaP `19.3847` edge `0.2147` maxDD `-7.8662`
- `risk_on_high->crypto_major_4h` score `1.9342` n `40` status `ready` deltaP `20.9756` edge `0.0879` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.9342` n `40` status `ready` deltaP `20.9756` edge `0.0879` maxDD `-2.6576`
- `market_context_high->crypto_major_1h` score `1.5854` n `165` status `ready` deltaP `12.1394` edge `0.1054` maxDD `-2.3372`
- `market_context_high->equity_1h` score `1.1699` n `165` status `ready` deltaP `9.7805` edge `0.0887` maxDD `-2.1799`
- `market_context_high->crypto_alt_4h` score `1.0181` n `165` status `ready` deltaP `13.7555` edge `0.1236` maxDD `-7.1038`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
