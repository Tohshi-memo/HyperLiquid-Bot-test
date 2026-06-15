# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-15T09:52:32.212032+00:00`
- Price records: `672`
- Market context records: `3980`
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

- `risk_on_high->unknown_4h` score `147.6653` n `40` status `ready` deltaP `-0.4268` edge `12.4895` maxDD `-10.8303`
- `risk_on_and_context->unknown_4h` score `147.6653` n `40` status `ready` deltaP `-0.4268` edge `12.4895` maxDD `-10.8303`
- `market_context_high->unknown_24h` score `30.7309` n `152` status `ready` deltaP `-6.9993` edge `3.1454` maxDD `-35.0266`
- `market_context_high->unknown_4h` score `19.6481` n `165` status `ready` deltaP `0.8611` edge `2.1725` maxDD `-35.6052`
- `risk_on_high->equity_24h` score `9.2423` n `40` status `ready` deltaP `42.0139` edge `0.4901` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.2423` n `40` status `ready` deltaP `42.0139` edge `0.4901` maxDD `0.0`
- `risk_on_high->equity_4h` score `3.6943` n `40` status `ready` deltaP `37.439` edge `0.063` maxDD `-0.0458`
- `risk_on_and_context->equity_4h` score `3.6943` n `40` status `ready` deltaP `37.439` edge `0.063` maxDD `-0.0458`
- `market_context_high->metal_24h` score `3.6498` n `152` status `ready` deltaP `17.0779` edge `0.3418` maxDD `-9.1203`
- `market_context_high->index_24h` score `3.3769` n `152` status `ready` deltaP `25.9137` edge `0.2226` maxDD `-7.1159`
- `market_context_high->equity_24h` score `2.9917` n `152` status `ready` deltaP `18.9876` edge `0.4257` maxDD `-14.5715`
- `risk_on_high->index_24h` score `2.7909` n `40` status `ready` deltaP `29.8611` edge `0.0335` maxDD `0.0`
- `risk_on_and_context->index_24h` score `2.7909` n `40` status `ready` deltaP `29.8611` edge `0.0335` maxDD `0.0`
- `market_context_high->equity_4h` score `2.5356` n `165` status `ready` deltaP `20.5451` edge `0.2046` maxDD `-7.0879`
- `market_context_high->crypto_major_4h` score `2.2196` n `165` status `ready` deltaP `19.3847` edge `0.2124` maxDD `-7.8662`
- `risk_on_high->crypto_major_4h` score `1.9066` n `40` status `ready` deltaP `20.9756` edge `0.0856` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.9066` n `40` status `ready` deltaP `20.9756` edge `0.0856` maxDD `-2.6576`
- `market_context_high->crypto_major_1h` score `1.6249` n `165` status `ready` deltaP `12.4388` edge `0.1067` maxDD `-2.3372`
- `market_context_high->equity_1h` score `1.1531` n `165` status `ready` deltaP `9.6308` edge `0.0883` maxDD `-2.1799`
- `market_context_high->metal_1h` score `0.9936` n `165` status `ready` deltaP `11.9534` edge `0.0625` maxDD `-2.751`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
