# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-14T21:22:28.963149+00:00`
- Price records: `672`
- Market context records: `3929`
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

- `risk_on_high->unknown_4h` score `70.4892` n `52` status `ready` deltaP `0.1877` edge `9.25` maxDD `-13.467`
- `risk_on_and_context->unknown_4h` score `70.4892` n `52` status `ready` deltaP `0.1877` edge `9.25` maxDD `-13.467`
- `market_context_high->unknown_4h` score `14.0251` n `188` status `ready` deltaP `-3.1266` edge `1.7305` maxDD `-35.6052`
- `risk_on_high->equity_24h` score `11.6159` n `40` status `ready` deltaP `42.0139` edge `0.6879` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `11.6159` n `40` status `ready` deltaP `42.0139` edge `0.6879` maxDD `0.0`
- `risk_on_high->equity_4h` score `5.6407` n `52` status `ready` deltaP `38.6843` edge `0.2169` maxDD `-0.0458`
- `risk_on_and_context->equity_4h` score `5.6407` n `52` status `ready` deltaP `38.6843` edge `0.2169` maxDD `-0.0458`
- `risk_on_high->crypto_major_4h` score `5.3144` n `52` status `ready` deltaP `27.228` edge `0.3279` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `5.3144` n `52` status `ready` deltaP `27.228` edge `0.3279` maxDD `-2.6576`
- `risk_on_high->index_24h` score `4.6996` n `40` status `ready` deltaP `30.0347` edge `0.1914` maxDD `0.0`
- `risk_on_and_context->index_24h` score `4.6996` n `40` status `ready` deltaP `30.0347` edge `0.1914` maxDD `0.0`
- `market_context_high->equity_24h` score `4.0464` n `165` status `ready` deltaP `20.8018` edge `0.5015` maxDD `-14.5715`
- `market_context_high->index_24h` score `3.7692` n `165` status `ready` deltaP `25.7923` edge `0.2561` maxDD `-7.1159`
- `risk_on_high->crypto_major_1h` score `2.9323` n `52` status `ready` deltaP `14.6361` edge `0.201` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `2.9323` n `52` status `ready` deltaP `14.6361` edge `0.201` maxDD `-2.3372`
- `market_context_high->metal_24h` score `2.4341` n `165` status `ready` deltaP `16.2973` edge `0.2457` maxDD `-9.1203`
- `market_context_high->crypto_major_4h` score `2.4175` n `188` status `ready` deltaP `18.39` edge `0.2553` maxDD `-9.4488`
- `risk_on_high->commodity_24h` score `2.1047` n `40` status `ready` deltaP `4.1667` edge `0.3326` maxDD `-10.7989`
- `risk_on_and_context->commodity_24h` score `2.1047` n `40` status `ready` deltaP `4.1667` edge `0.3326` maxDD `-10.7989`
- `market_context_high->equity_4h` score `1.5838` n `188` status `ready` deltaP `16.4667` edge `0.1926` maxDD `-8.2982`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
