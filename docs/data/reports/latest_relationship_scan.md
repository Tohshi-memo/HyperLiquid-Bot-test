# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-14T18:07:29.642069+00:00`
- Price records: `672`
- Market context records: `3916`
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

- `risk_on_high->unknown_4h` score `55.514` n `64` status `ready` deltaP `6.5168` edge `7.2879` maxDD `-13.467`
- `risk_on_and_context->unknown_4h` score `55.514` n `64` status `ready` deltaP `6.5168` edge `7.2879` maxDD `-13.467`
- `risk_on_high->equity_24h` score `18.9611` n `40` status `ready` deltaP `42.0139` edge `1.3` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `18.9611` n `40` status `ready` deltaP `42.0139` edge `1.3` maxDD `0.0`
- `market_context_high->unknown_4h` score `11.9884` n `200` status `ready` deltaP `-1.4207` edge `1.5494` maxDD `-35.6052`
- `risk_on_high->crypto_major_24h` score `8.9095` n `40` status `ready` deltaP `-1.5278` edge `1.3528` maxDD `-10.3631`
- `risk_on_and_context->crypto_major_24h` score `8.9095` n `40` status `ready` deltaP `-1.5278` edge `1.3528` maxDD `-10.3631`
- `risk_on_high->crypto_major_4h` score `8.7496` n `64` status `ready` deltaP `29.3826` edge `0.5998` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `8.7496` n `64` status `ready` deltaP `29.3826` edge `0.5998` maxDD `-2.6576`
- `risk_on_high->index_24h` score `7.6144` n `40` status `ready` deltaP `30.0347` edge `0.4343` maxDD `0.0`
- `risk_on_and_context->index_24h` score `7.6144` n `40` status `ready` deltaP `30.0347` edge `0.4343` maxDD `0.0`
- `risk_on_high->equity_4h` score `5.8138` n `64` status `ready` deltaP `35.3659` edge `0.2648` maxDD `-0.6204`
- `risk_on_and_context->equity_4h` score `5.8138` n `64` status `ready` deltaP `35.3659` edge `0.2648` maxDD `-0.6204`
- `market_context_high->equity_24h` score `5.5512` n `165` status `ready` deltaP `20.8018` edge `0.6269` maxDD `-14.5715`
- `market_context_high->index_24h` score `4.3536` n `165` status `ready` deltaP `25.7923` edge `0.3048` maxDD `-7.1159`
- `market_context_high->crypto_major_4h` score `3.4651` n `200` status `ready` deltaP `19.6951` edge `0.3339` maxDD `-9.4488`
- `market_context_high->metal_24h` score `2.6039` n `165` status `ready` deltaP `17.5947` edge `0.2512` maxDD `-9.1203`
- `risk_on_high->crypto_alt_4h` score `2.4516` n `64` status `ready` deltaP `2.5915` edge `0.2689` maxDD `-3.8835`
- `risk_on_and_context->crypto_alt_4h` score `2.4516` n `64` status `ready` deltaP `2.5915` edge `0.2689` maxDD `-3.8835`
- `market_context_high->equity_4h` score `1.7577` n `200` status `ready` deltaP `16.6159` edge `0.2061` maxDD `-8.2982`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
