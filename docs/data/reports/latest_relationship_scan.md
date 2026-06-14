# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-14T20:06:05.239004+00:00`
- Price records: `672`
- Market context records: `3924`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11427`

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

- `risk_on_high->unknown_4h` score `64.8504` n `56` status `ready` deltaP `3.4844` edge `8.5051` maxDD `-13.467`
- `risk_on_and_context->unknown_4h` score `64.8504` n `56` status `ready` deltaP `3.4844` edge `8.5051` maxDD `-13.467`
- `risk_on_high->equity_24h` score `14.2667` n `39` status `ready` deltaP `42.0139` edge `0.9088` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `14.2667` n `39` status `ready` deltaP `42.0139` edge `0.9088` maxDD `0.0`
- `market_context_high->unknown_4h` score `13.2204` n `193` status `ready` deltaP `-1.845` edge `1.6549` maxDD `-35.6052`
- `risk_on_high->crypto_major_4h` score `7.2485` n `56` status `ready` deltaP `28.7238` edge `0.4791` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `7.2485` n `56` status `ready` deltaP `28.7238` edge `0.4791` maxDD `-2.6576`
- `risk_on_high->equity_4h` score `6.5167` n `56` status `ready` deltaP `38.6542` edge `0.2901` maxDD `-0.0458`
- `risk_on_and_context->equity_4h` score `6.5167` n `56` status `ready` deltaP `38.6542` edge `0.2901` maxDD `-0.0458`
- `risk_on_high->index_24h` score `5.7952` n `39` status `ready` deltaP `30.0347` edge `0.2827` maxDD `0.0`
- `risk_on_and_context->index_24h` score `5.7952` n `39` status `ready` deltaP `30.0347` edge `0.2827` maxDD `0.0`
- `market_context_high->equity_24h` score `4.626` n `165` status `ready` deltaP `20.8018` edge `0.5498` maxDD `-14.5715`
- `market_context_high->index_24h` score `3.9996` n `165` status `ready` deltaP `25.7923` edge `0.2753` maxDD `-7.1159`
- `market_context_high->crypto_major_4h` score `3.0114` n `193` status `ready` deltaP `19.0643` edge `0.3003` maxDD `-9.4488`
- `risk_on_high->crypto_major_1h` score `2.5107` n `56` status `ready` deltaP `12.2006` edge `0.1821` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `2.5107` n `56` status `ready` deltaP `12.2006` edge `0.1821` maxDD `-2.3372`
- `market_context_high->metal_24h` score `2.4939` n `165` status `ready` deltaP `16.7298` edge `0.2478` maxDD `-9.1203`
- `market_context_high->equity_4h` score `1.8306` n `193` status `ready` deltaP `16.837` edge `0.2107` maxDD `-8.2982`
- `risk_on_high->equity_1h` score `1.5441` n `56` status `ready` deltaP `11.7194` edge `0.0899` maxDD `-0.8151`
- `risk_on_and_context->equity_1h` score `1.5441` n `56` status `ready` deltaP `11.7194` edge `0.0899` maxDD `-0.8151`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
