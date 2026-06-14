# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-14T20:52:27.676894+00:00`
- Price records: `672`
- Market context records: `3927`
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

- `risk_on_high->unknown_4h` score `67.5572` n `54` status `ready` deltaP `1.8971` edge `8.8627` maxDD `-13.467`
- `risk_on_and_context->unknown_4h` score `67.5572` n `54` status `ready` deltaP `1.8971` edge `8.8627` maxDD `-13.467`
- `market_context_high->unknown_4h` score `13.6899` n `190` status `ready` deltaP `-2.6059` edge `1.6991` maxDD `-35.6052`
- `risk_on_high->equity_24h` score `12.7919` n `40` status `ready` deltaP `42.0139` edge `0.7859` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `12.7919` n `40` status `ready` deltaP `42.0139` edge `0.7859` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `6.3812` n `54` status `ready` deltaP `28.0827` edge `0.4111` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `6.3812` n `54` status `ready` deltaP `28.0827` edge `0.4111` maxDD `-2.6576`
- `risk_on_high->equity_4h` score `6.0661` n `54` status `ready` deltaP `38.8268` edge `0.2514` maxDD `-0.0458`
- `risk_on_and_context->equity_4h` score `6.0661` n `54` status `ready` deltaP `38.8268` edge `0.2514` maxDD `-0.0458`
- `risk_on_high->index_24h` score `5.2024` n `40` status `ready` deltaP `30.0347` edge `0.2333` maxDD `0.0`
- `risk_on_and_context->index_24h` score `5.2024` n `40` status `ready` deltaP `30.0347` edge `0.2333` maxDD `0.0`
- `market_context_high->equity_24h` score `4.2648` n `165` status `ready` deltaP `20.8018` edge `0.5197` maxDD `-14.5715`
- `market_context_high->index_24h` score `3.8628` n `165` status `ready` deltaP `25.7923` edge `0.2639` maxDD `-7.1159`
- `risk_on_high->crypto_major_1h` score `2.7919` n `54` status `ready` deltaP `14.216` edge `0.1921` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `2.7919` n `54` status `ready` deltaP `14.216` edge `0.1921` maxDD `-2.3372`
- `market_context_high->crypto_major_4h` score `2.6856` n `190` status `ready` deltaP `18.726` edge `0.2754` maxDD `-9.4488`
- `market_context_high->metal_24h` score `2.4389` n `165` status `ready` deltaP `16.2973` edge `0.2461` maxDD `-9.1203`
- `risk_on_high->commodity_24h` score `1.819` n `40` status `ready` deltaP `4.1667` edge `0.3319` maxDD `-11.9812`
- `risk_on_and_context->commodity_24h` score `1.819` n `40` status `ready` deltaP `4.1667` edge `0.3319` maxDD `-11.9812`
- `market_context_high->equity_4h` score `1.6993` n `190` status `ready` deltaP `16.741` edge `0.2004` maxDD `-8.2982`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
