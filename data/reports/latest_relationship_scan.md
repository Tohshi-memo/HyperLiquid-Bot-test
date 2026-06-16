# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-16T01:37:29.758557+00:00`
- Price records: `672`
- Market context records: `4046`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10528`

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

- `risk_on_high->unknown_4h` score `144.8879` n `40` status `ready` deltaP `-8.2012` edge `12.3103` maxDD `-10.864`
- `risk_on_and_context->unknown_4h` score `144.8879` n `40` status `ready` deltaP `-8.2012` edge `12.3103` maxDD `-10.864`
- `market_context_high->unknown_24h` score `44.6206` n `136` status `ready` deltaP `-7.9582` edge `4.1743` maxDD `-24.2289`
- `market_context_high->unknown_4h` score `22.1739` n `156` status `ready` deltaP `1.6065` edge `2.3794` maxDD `-35.7161`
- `risk_on_high->equity_24h` score `4.2159` n `40` status `ready` deltaP `34.4887` edge `0.1214` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `4.2159` n `40` status `ready` deltaP `34.4887` edge `0.1214` maxDD `0.0`
- `risk_on_high->equity_4h` score `3.5204` n `40` status `ready` deltaP `37.439` edge `0.0485` maxDD `-0.0446`
- `risk_on_and_context->equity_4h` score `3.5204` n `40` status `ready` deltaP `37.439` edge `0.0485` maxDD `-0.0446`
- `market_context_high->index_24h` score `2.359` n `136` status `ready` deltaP `21.4484` edge `0.0748` maxDD `-1.3629`
- `market_context_high->equity_4h` score `1.8006` n `156` status `ready` deltaP `16.2211` edge `0.17` maxDD `-6.9137`
- `risk_on_high->crypto_major_4h` score `1.0283` n `40` status `ready` deltaP `19.1463` edge `0.0246` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.0283` n `40` status `ready` deltaP `19.1463` edge `0.0246` maxDD `-2.6576`
- `market_context_high->metal_24h` score `0.8812` n `136` status `ready` deltaP `9.5308` edge `0.1086` maxDD `-4.8962`
- `market_context_high->equity_1h` score `0.7996` n `166` status `ready` deltaP `5.9105` edge `0.0832` maxDD `-2.144`
- `risk_on_high->equity_1h` score `0.4615` n `40` status `ready` deltaP `11.3623` edge `0.0018` maxDD `-0.7937`
- `risk_on_and_context->equity_1h` score `0.4615` n `40` status `ready` deltaP `11.3623` edge `0.0018` maxDD `-0.7937`
- `market_context_high->crypto_major_1h` score `0.28` n `166` status `ready` deltaP `7.6961` edge `0.0442` maxDD `-3.7739`
- `risk_on_high->commodity_24h` score `0.2169` n `40` status `ready` deltaP `1.0832` edge `0.239` maxDD `-12.9187`
- `risk_on_and_context->commodity_24h` score `0.2169` n `40` status `ready` deltaP `1.0832` edge `0.239` maxDD `-12.9187`
- `risk_on_high->crypto_major_1h` score `0.185` n `40` status `ready` deltaP `12.4551` edge `-0.0051` maxDD `-2.3372`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
