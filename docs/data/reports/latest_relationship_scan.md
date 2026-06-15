# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-15T13:37:36.671834+00:00`
- Price records: `672`
- Market context records: `3996`
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

- `risk_on_high->unknown_4h` score `146.9982` n `40` status `ready` deltaP `-2.2561` edge `12.4461` maxDD `-10.8303`
- `risk_on_and_context->unknown_4h` score `146.9982` n `40` status `ready` deltaP `-2.2561` edge `12.4461` maxDD `-10.8303`
- `market_context_high->unknown_24h` score `42.7718` n `141` status `ready` deltaP `-4.429` edge `3.9957` maxDD `-24.1486`
- `market_context_high->unknown_4h` score `23.9798` n `153` status `ready` deltaP `1.6818` edge `2.528` maxDD `-35.6052`
- `risk_on_high->equity_24h` score `9.2663` n `40` status `ready` deltaP `42.0139` edge `0.4921` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.2663` n `40` status `ready` deltaP `42.0139` edge `0.4921` maxDD `0.0`
- `risk_on_high->equity_4h` score `4.0204` n `40` status `ready` deltaP `38.2012` edge `0.0851` maxDD `-0.0458`
- `risk_on_and_context->equity_4h` score `4.0204` n `40` status `ready` deltaP `38.2012` edge `0.0851` maxDD `-0.0458`
- `market_context_high->metal_24h` score `3.0225` n `141` status `ready` deltaP `15.2815` edge `0.3015` maxDD `-9.1203`
- `market_context_high->index_24h` score `3.0211` n `141` status `ready` deltaP `25.6058` edge `0.195` maxDD `-7.1159`
- `risk_on_high->index_24h` score `2.7537` n `40` status `ready` deltaP `29.8611` edge `0.0304` maxDD `0.0`
- `risk_on_and_context->index_24h` score `2.7537` n `40` status `ready` deltaP `29.8611` edge `0.0304` maxDD `0.0`
- `market_context_high->equity_4h` score `2.226` n `153` status `ready` deltaP `20.4398` edge `0.1795` maxDD `-7.0879`
- `market_context_high->equity_24h` score `2.062` n `141` status `ready` deltaP `17.1912` edge `0.3602` maxDD `-14.5715`
- `risk_on_high->crypto_major_4h` score `1.7238` n `40` status `ready` deltaP `20.6707` edge `0.0724` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.7238` n `40` status `ready` deltaP `20.6707` edge `0.0724` maxDD `-2.6576`
- `market_context_high->crypto_major_4h` score `1.2773` n `153` status `ready` deltaP `18.1053` edge `0.1424` maxDD `-7.8662`
- `market_context_high->crypto_major_1h` score `1.2209` n `153` status `ready` deltaP `11.3029` edge `0.0806` maxDD `-2.3372`
- `market_context_high->metal_1h` score `1.1635` n `153` status `ready` deltaP `12.3361` edge `0.0622` maxDD `-1.7983`
- `market_context_high->equity_1h` score `1.1398` n `153` status `ready` deltaP `9.9302` edge `0.0852` maxDD `-2.1799`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
