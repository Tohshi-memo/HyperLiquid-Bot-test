# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-14T20:37:30.097008+00:00`
- Price records: `672`
- Market context records: `3926`
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

- `risk_on_high->unknown_4h` score `66.1913` n `55` status `ready` deltaP `2.7051` edge `8.6822` maxDD `-13.467`
- `risk_on_and_context->unknown_4h` score `66.1913` n `55` status `ready` deltaP `2.7051` edge `8.6822` maxDD `-13.467`
- `market_context_high->unknown_4h` score `13.5293` n `191` status `ready` deltaP `-2.3496` edge `1.684` maxDD `-35.6052`
- `risk_on_high->equity_24h` score `13.4267` n `40` status `ready` deltaP `42.0139` edge `0.8388` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `13.4267` n `40` status `ready` deltaP `42.0139` edge `0.8388` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `6.9583` n `55` status `ready` deltaP `28.4867` edge `0.4565` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `6.9583` n `55` status `ready` deltaP `28.4867` edge `0.4565` maxDD `-2.6576`
- `risk_on_high->equity_4h` score `6.3715` n `55` status `ready` deltaP `38.8941` edge `0.2764` maxDD `-0.0458`
- `risk_on_and_context->equity_4h` score `6.3715` n `55` status `ready` deltaP `38.8941` edge `0.2764` maxDD `-0.0458`
- `risk_on_high->index_24h` score `5.4508` n `40` status `ready` deltaP `30.0347` edge `0.254` maxDD `0.0`
- `risk_on_and_context->index_24h` score `5.4508` n `40` status `ready` deltaP `30.0347` edge `0.254` maxDD `0.0`
- `market_context_high->equity_24h` score `4.3836` n `165` status `ready` deltaP `20.8018` edge `0.5296` maxDD `-14.5715`
- `market_context_high->index_24h` score `3.9084` n `165` status `ready` deltaP `25.7923` edge `0.2677` maxDD `-7.1159`
- `market_context_high->crypto_major_4h` score `2.8284` n `191` status `ready` deltaP `18.8913` edge `0.2862` maxDD `-9.4488`
- `risk_on_high->crypto_major_1h` score `2.6436` n `55` status `ready` deltaP `13.1873` edge `0.1866` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `2.6436` n `55` status `ready` deltaP `13.1873` edge `0.1866` maxDD `-2.3372`
- `market_context_high->metal_24h` score `2.4831` n `165` status `ready` deltaP `16.7298` edge `0.2469` maxDD `-9.1203`
- `market_context_high->equity_4h` score `1.775` n `191` status `ready` deltaP `16.876` edge `0.2058` maxDD `-8.2982`
- `risk_on_high->equity_1h` score `1.5093` n `55` status `ready` deltaP `11.2847` edge `0.0899` maxDD `-0.8151`
- `risk_on_and_context->equity_1h` score `1.5093` n `55` status `ready` deltaP `11.2847` edge `0.0899` maxDD `-0.8151`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
