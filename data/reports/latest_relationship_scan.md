# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-14T18:52:29.623020+00:00`
- Price records: `672`
- Market context records: `3919`
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

- `risk_on_high->unknown_4h` score `58.9674` n `61` status `ready` deltaP `6.5398` edge `7.7305` maxDD `-13.467`
- `risk_on_and_context->unknown_4h` score `58.9674` n `61` status `ready` deltaP `6.5398` edge `7.7305` maxDD `-13.467`
- `risk_on_high->equity_24h` score `17.4923` n `39` status `ready` deltaP `42.0139` edge `1.1776` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `17.4923` n `39` status `ready` deltaP `42.0139` edge `1.1776` maxDD `0.0`
- `market_context_high->unknown_4h` score `12.6069` n `197` status `ready` deltaP `-1.324` edge `1.6003` maxDD `-35.6052`
- `risk_on_high->crypto_major_4h` score `8.8584` n `61` status `ready` deltaP `30.023` edge `0.6046` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `8.8584` n `61` status `ready` deltaP `30.023` edge `0.6046` maxDD `-2.6576`
- `risk_on_high->index_24h` score `6.9808` n `39` status `ready` deltaP `30.0347` edge `0.3815` maxDD `0.0`
- `risk_on_and_context->index_24h` score `6.9808` n `39` status `ready` deltaP `30.0347` edge `0.3815` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `6.8085` n `39` status `ready` deltaP `-7.2248` edge `1.1463` maxDD `-11.687`
- `risk_on_and_context->crypto_major_24h` score `6.8085` n `39` status `ready` deltaP `-7.2248` edge `1.1463` maxDD `-11.687`
- `risk_on_high->equity_4h` score `6.4587` n `61` status `ready` deltaP `38.1847` edge `0.2884` maxDD `-0.0458`
- `risk_on_and_context->equity_4h` score `6.4587` n `61` status `ready` deltaP `38.1847` edge `0.2884` maxDD `-0.0458`
- `market_context_high->equity_24h` score `5.2104` n `165` status `ready` deltaP `20.8018` edge `0.5985` maxDD `-14.5715`
- `market_context_high->index_24h` score `4.2144` n `165` status `ready` deltaP `25.7923` edge `0.2932` maxDD `-7.1159`
- `market_context_high->crypto_major_4h` score `3.4656` n `197` status `ready` deltaP `19.7459` edge `0.3336` maxDD `-9.4488`
- `market_context_high->metal_24h` score `2.5967` n `165` status `ready` deltaP `17.5947` edge `0.2506` maxDD `-9.1203`
- `risk_on_high->crypto_major_1h` score `2.4774` n `61` status `ready` deltaP `12.2951` edge `0.1787` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `2.4774` n `61` status `ready` deltaP `12.2951` edge `0.1787` maxDD `-2.3372`
- `risk_on_high->crypto_alt_4h` score `2.389` n `61` status `ready` deltaP `2.0792` edge `0.2671` maxDD `-3.8835`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
