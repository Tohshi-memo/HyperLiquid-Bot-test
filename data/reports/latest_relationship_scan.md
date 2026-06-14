# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-14T22:07:33.267860+00:00`
- Price records: `672`
- Market context records: `3932`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11443`

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

- `risk_on_high->unknown_4h` score `75.4271` n `49` status `ready` deltaP `-2.6381` edge `9.9019` maxDD `-13.467`
- `risk_on_and_context->unknown_4h` score `75.4271` n `49` status `ready` deltaP `-2.6381` edge `9.9019` maxDD `-13.467`
- `market_context_high->unknown_4h` score `14.5081` n `185` status `ready` deltaP `-3.9288` edge `1.7761` maxDD `-35.6052`
- `risk_on_high->equity_24h` score `10.6343` n `40` status `ready` deltaP `42.0139` edge `0.6061` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `10.6343` n `40` status `ready` deltaP `42.0139` edge `0.6061` maxDD `0.0`
- `risk_on_high->equity_4h` score `5.3734` n `49` status `ready` deltaP `38.4489` edge `0.1962` maxDD `-0.0458`
- `risk_on_and_context->equity_4h` score `5.3734` n `49` status `ready` deltaP `38.4489` edge `0.1962` maxDD `-0.0458`
- `risk_on_high->index_24h` score `4.15` n `40` status `ready` deltaP `30.0347` edge `0.1456` maxDD `0.0`
- `risk_on_and_context->index_24h` score `4.15` n `40` status `ready` deltaP `30.0347` edge `0.1456` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `3.9582` n `49` status `ready` deltaP `25.8151` edge `0.2243` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `3.9582` n `49` status `ready` deltaP `25.8151` edge `0.2243` maxDD `-2.6576`
- `market_context_high->equity_24h` score `3.864` n `165` status `ready` deltaP `20.8018` edge `0.4863` maxDD `-14.5715`
- `market_context_high->index_24h` score `3.6672` n `165` status `ready` deltaP `25.7923` edge `0.2476` maxDD `-7.1159`
- `market_context_high->metal_24h` score `2.4082` n `165` status `ready` deltaP `15.4325` edge `0.2493` maxDD `-9.1203`
- `market_context_high->crypto_major_4h` score `2.0113` n `185` status `ready` deltaP `17.8725` edge `0.2249` maxDD `-9.4488`
- `risk_on_high->commodity_24h` score `1.8307` n `40` status `ready` deltaP `4.1667` edge `0.3094` maxDD `-11.7697`
- `risk_on_and_context->commodity_24h` score `1.8307` n `40` status `ready` deltaP `4.1667` edge `0.3094` maxDD `-11.7697`
- `market_context_high->unknown_24h` score `1.5607` n `165` status `ready` deltaP `-14.2582` edge `2.041` maxDD `-128.2711`
- `market_context_high->equity_4h` score `1.4552` n `185` status `ready` deltaP `16.044` edge `0.1847` maxDD `-8.2982`
- `risk_on_high->crypto_major_1h` score `1.3012` n `49` status `ready` deltaP `12.5168` edge `0.0792` maxDD `-2.3372`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
