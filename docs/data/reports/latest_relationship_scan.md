# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-15T12:37:36.745574+00:00`
- Price records: `672`
- Market context records: `3992`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10098`

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

- `risk_on_high->unknown_4h` score `147.0526` n `40` status `ready` deltaP `-1.9512` edge `12.4486` maxDD `-10.8303`
- `risk_on_and_context->unknown_4h` score `147.0526` n `40` status `ready` deltaP `-1.9512` edge `12.4486` maxDD `-10.8303`
- `market_context_high->unknown_24h` score `39.068` n `145` status `ready` deltaP `-5.4561` edge `3.6939` maxDD `-24.1486`
- `market_context_high->unknown_4h` score `22.6332` n `157` status `ready` deltaP `1.6953` edge `2.4157` maxDD `-35.6052`
- `risk_on_high->equity_24h` score `9.3347` n `40` status `ready` deltaP `42.0139` edge `0.4978` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.3347` n `40` status `ready` deltaP `42.0139` edge `0.4978` maxDD `0.0`
- `risk_on_high->equity_4h` score `3.9854` n `40` status `ready` deltaP `38.0488` edge `0.0832` maxDD `-0.0458`
- `risk_on_and_context->equity_4h` score `3.9854` n `40` status `ready` deltaP `38.0488` edge `0.0832` maxDD `-0.0458`
- `market_context_high->metal_24h` score `3.2561` n `145` status `ready` deltaP `15.9663` edge `0.3164` maxDD `-9.1203`
- `market_context_high->index_24h` score `3.1037` n `145` status `ready` deltaP `25.7232` edge `0.2011` maxDD `-7.1159`
- `risk_on_high->index_24h` score `2.7957` n `40` status `ready` deltaP `29.8611` edge `0.0339` maxDD `0.0`
- `risk_on_and_context->index_24h` score `2.7957` n `40` status `ready` deltaP `29.8611` edge `0.0339` maxDD `0.0`
- `market_context_high->equity_24h` score `2.3232` n `145` status `ready` deltaP `17.876` edge `0.3774` maxDD `-14.5715`
- `market_context_high->equity_4h` score `2.2053` n `157` status `ready` deltaP `20.1666` edge `0.1796` maxDD `-7.0879`
- `risk_on_high->crypto_major_4h` score `1.927` n `40` status `ready` deltaP `20.9756` edge `0.0873` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.927` n `40` status `ready` deltaP `20.9756` edge `0.0873` maxDD `-2.6576`
- `market_context_high->crypto_major_4h` score `1.4291` n `157` status `ready` deltaP `17.9024` edge `0.1564` maxDD `-7.8662`
- `market_context_high->crypto_major_1h` score `1.2643` n `157` status `ready` deltaP `11.2609` edge `0.0845` maxDD `-2.3372`
- `market_context_high->metal_1h` score `0.9578` n `157` status `ready` deltaP `11.8569` edge `0.0549` maxDD `-2.3301`
- `risk_on_high->commodity_24h` score `0.9399` n `40` status `ready` deltaP `4.1667` edge `0.2787` maxDD `-12.9187`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
