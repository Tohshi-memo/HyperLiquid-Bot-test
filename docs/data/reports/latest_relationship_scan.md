# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-14T21:52:25.575355+00:00`
- Price records: `672`
- Market context records: `3931`
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

- `risk_on_high->unknown_4h` score `73.7176` n `50` status `ready` deltaP `-1.6585` edge `9.6762` maxDD `-13.467`
- `risk_on_and_context->unknown_4h` score `73.7176` n `50` status `ready` deltaP `-1.6585` edge `9.6762` maxDD `-13.467`
- `market_context_high->unknown_4h` score `14.3521` n `186` status `ready` deltaP `-3.6585` edge `1.7613` maxDD `-35.6052`
- `risk_on_high->equity_24h` score `10.9439` n `40` status `ready` deltaP `42.0139` edge `0.6319` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `10.9439` n `40` status `ready` deltaP `42.0139` edge `0.6319` maxDD `0.0`
- `risk_on_high->equity_4h` score `5.4928` n `50` status `ready` deltaP `38.5305` edge `0.2056` maxDD `-0.0458`
- `risk_on_and_context->equity_4h` score `5.4928` n `50` status `ready` deltaP `38.5305` edge `0.2056` maxDD `-0.0458`
- `risk_on_high->crypto_major_4h` score `4.4678` n `50` status `ready` deltaP `26.3049` edge `0.2635` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `4.4678` n `50` status `ready` deltaP `26.3049` edge `0.2635` maxDD `-2.6576`
- `risk_on_high->index_24h` score `4.3528` n `40` status `ready` deltaP `30.0347` edge `0.1625` maxDD `0.0`
- `risk_on_and_context->index_24h` score `4.3528` n `40` status `ready` deltaP `30.0347` edge `0.1625` maxDD `0.0`
- `market_context_high->equity_24h` score `3.9216` n `165` status `ready` deltaP `20.8018` edge `0.4911` maxDD `-14.5715`
- `market_context_high->index_24h` score `3.7044` n `165` status `ready` deltaP `25.7923` edge `0.2507` maxDD `-7.1159`
- `market_context_high->metal_24h` score `2.311` n `165` status `ready` deltaP `15.4325` edge `0.2412` maxDD `-9.1203`
- `market_context_high->crypto_major_4h` score `2.1548` n `186` status `ready` deltaP `18.0468` edge `0.2357` maxDD `-9.4488`
- `risk_on_high->crypto_major_1h` score `1.8819` n `50` status `ready` deltaP `13.2515` edge `0.1227` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `1.8819` n `50` status `ready` deltaP `13.2515` edge `0.1227` maxDD `-2.3372`
- `risk_on_high->commodity_24h` score `1.8032` n `40` status `ready` deltaP `4.1667` edge `0.3106` maxDD `-11.7153`
- `risk_on_and_context->commodity_24h` score `1.8032` n `40` status `ready` deltaP `4.1667` edge `0.3106` maxDD `-11.7153`
- `market_context_high->equity_4h` score `1.5062` n `186` status `ready` deltaP `16.1864` edge `0.188` maxDD `-8.2982`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
