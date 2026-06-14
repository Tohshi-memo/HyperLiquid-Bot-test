# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-14T17:22:29.798708+00:00`
- Price records: `672`
- Market context records: `3913`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11409`

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

- `risk_on_high->unknown_4h` score `52.3799` n `67` status `ready` deltaP `6.6208` edge `6.8854` maxDD `-13.467`
- `risk_on_and_context->unknown_4h` score `52.3799` n `67` status `ready` deltaP `6.6208` edge `6.8854` maxDD `-13.467`
- `risk_on_high->equity_24h` score `20.2667` n `40` status `ready` deltaP `42.0139` edge `1.4088` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `20.2667` n `40` status `ready` deltaP `42.0139` edge `1.4088` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `17.2429` n `40` status `ready` deltaP `5.4514` edge `1.5688` maxDD `-8.7923`
- `risk_on_and_context->crypto_major_24h` score `17.2429` n `40` status `ready` deltaP `5.4514` edge `1.5688` maxDD `-8.7923`
- `risk_on_high->index_24h` score `8.1112` n `40` status `ready` deltaP `30.0347` edge `0.4757` maxDD `0.0`
- `risk_on_and_context->index_24h` score `8.1112` n `40` status `ready` deltaP `30.0347` edge `0.4757` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `7.5246` n `67` status `ready` deltaP `25.8145` edge `0.5313` maxDD `-3.441`
- `risk_on_and_context->crypto_major_4h` score `7.5246` n `67` status `ready` deltaP `25.8145` edge `0.5313` maxDD `-3.441`
- `market_context_high->unknown_4h` score `7.4175` n `203` status `ready` deltaP `-1.3712` edge `1.501` maxDD `-35.6052`
- `market_context_high->equity_24h` score `5.7924` n `165` status `ready` deltaP `20.8018` edge `0.647` maxDD `-14.5715`
- `risk_on_high->equity_4h` score `4.6039` n `67` status `ready` deltaP `31.1681` edge `0.226` maxDD `-2.3439`
- `risk_on_and_context->equity_4h` score `4.6039` n `67` status `ready` deltaP `31.1681` edge `0.226` maxDD `-2.3439`
- `market_context_high->index_24h` score `4.4448` n `165` status `ready` deltaP `25.7923` edge `0.3124` maxDD `-7.1159`
- `risk_on_high->crypto_alt_24h` score `3.4653` n `40` status `ready` deltaP `3.3681` edge `0.7066` maxDD `-18.1166`
- `risk_on_and_context->crypto_alt_24h` score `3.4653` n `40` status `ready` deltaP `3.3681` edge `0.7066` maxDD `-18.1166`
- `market_context_high->crypto_major_4h` score `3.1723` n `203` status `ready` deltaP `18.6606` edge `0.3164` maxDD `-9.4488`
- `market_context_high->metal_24h` score `2.6063` n `165` status `ready` deltaP `17.5947` edge `0.2514` maxDD `-9.1203`
- `market_context_high->equity_4h` score `1.5431` n `203` status `ready` deltaP `15.5075` edge `0.1956` maxDD `-8.2982`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
