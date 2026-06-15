# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-15T05:22:31.436085+00:00`
- Price records: `672`
- Market context records: `3962`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11252`

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

- `risk_on_high->unknown_4h` score `148.2092` n `40` status `ready` deltaP `1.7073` edge `12.5206` maxDD `-10.8303`
- `risk_on_and_context->unknown_4h` score `148.2092` n `40` status `ready` deltaP `1.7073` edge `12.5206` maxDD `-10.8303`
- `market_context_high->unknown_24h` score `35.4055` n `145` status `ready` deltaP `-7.318` edge `3.6117` maxDD `-40.9964`
- `market_context_high->unknown_4h` score `22.2938` n `157` status `ready` deltaP `1.5321` edge `2.3885` maxDD `-35.6052`
- `risk_on_high->equity_24h` score `8.8883` n `40` status `ready` deltaP `42.0139` edge `0.4606` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `8.8883` n `40` status `ready` deltaP `42.0139` edge `0.4606` maxDD `0.0`
- `risk_on_high->equity_4h` score `3.387` n `40` status `ready` deltaP `37.439` edge `0.0374` maxDD `-0.0458`
- `risk_on_and_context->equity_4h` score `3.387` n `40` status `ready` deltaP `37.439` edge `0.0374` maxDD `-0.0458`
- `market_context_high->metal_24h` score `3.0413` n `145` status `ready` deltaP `15.9663` edge `0.2985` maxDD `-9.1203`
- `market_context_high->index_24h` score `2.9933` n `145` status `ready` deltaP `25.7232` edge `0.1919` maxDD `-7.1159`
- `risk_on_high->index_24h` score `2.6805` n `40` status `ready` deltaP `29.8611` edge `0.0243` maxDD `0.0`
- `risk_on_and_context->index_24h` score `2.6805` n `40` status `ready` deltaP `29.8611` edge `0.0243` maxDD `0.0`
- `market_context_high->equity_4h` score `2.3402` n `157` status `ready` deltaP `19.5568` edge `0.1949` maxDD `-7.0879`
- `market_context_high->crypto_major_4h` score `2.3221` n `157` status `ready` deltaP `19.8404` edge `0.2179` maxDD `-7.8662`
- `market_context_high->equity_24h` score `1.9776` n `145` status `ready` deltaP `17.876` edge `0.3486` maxDD `-14.5715`
- `risk_on_high->crypto_major_4h` score `1.667` n `40` status `ready` deltaP `20.3659` edge `0.0697` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.667` n `40` status `ready` deltaP `20.3659` edge `0.0697` maxDD `-2.6576`
- `market_context_high->crypto_major_1h` score `1.6214` n `167` status `ready` deltaP `12.5749` edge `0.1055` maxDD `-2.3372`
- `risk_on_high->commodity_24h` score `1.0143` n `40` status `ready` deltaP `4.1667` edge `0.2849` maxDD `-12.9187`
- `risk_on_and_context->commodity_24h` score `1.0143` n `40` status `ready` deltaP `4.1667` edge `0.2849` maxDD `-12.9187`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
