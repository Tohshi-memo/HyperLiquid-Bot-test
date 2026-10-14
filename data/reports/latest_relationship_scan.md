# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-14T16:07:31.863595+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9280`

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

- `market_context_high->crypto_alt_4h` score `6.9303` n `117` status `ready` deltaP `18.1364` edge `0.6015` maxDD `-9.2574`
- `risk_on_high->commodity_24h` score `6.279` n `54` status `ready` deltaP `32.3478` edge `0.3076` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.279` n `54` status `ready` deltaP `32.3478` edge `0.3076` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `6.091` n `117` status `ready` deltaP `20.9676` edge `0.5237` maxDD `-7.4722`
- `risk_on_high->crypto_alt_4h` score `5.5192` n `54` status `ready` deltaP `20.4156` edge `0.3686` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `5.5192` n `54` status `ready` deltaP `20.4156` edge `0.3686` maxDD `-1.9151`
- `risk_on_high->crypto_major_4h` score `4.4989` n `54` status `ready` deltaP `34.073` edge `0.4349` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.4989` n `54` status `ready` deltaP `34.073` edge `0.4349` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.7603` n `117` status `ready` deltaP `13.5665` edge `0.163` maxDD `-5.8734`
- `market_context_high->crypto_major_1h` score `1.2406` n `117` status `ready` deltaP `5.8115` edge `0.1452` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.304` n `117` status `ready` deltaP `13.7652` edge `0.0381` maxDD `-1.6961`
- `market_context_high->metal_1h` score `-0.3146` n `117` status `ready` deltaP `7.8638` edge `0.0083` maxDD `-0.9556`
- `risk_on_high->crypto_major_1h` score `-0.35` n `54` status `ready` deltaP `1.2531` edge `0.019` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.35` n `54` status `ready` deltaP `1.2531` edge `0.019` maxDD `-3.7781`
- `market_context_high->fx_1h` score `-0.378` n `117` status `ready` deltaP `0.6468` edge `0.0022` maxDD `-0.3742`
- `risk_on_high->metal_1h` score `-0.4189` n `54` status `ready` deltaP `2.4507` edge `0.0031` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.4189` n `54` status `ready` deltaP `2.4507` edge `0.0031` maxDD `-0.8513`
- `risk_on_high->metal_4h` score `-0.5833` n `54` status `ready` deltaP `1.372` edge `0.0206` maxDD `-1.6961`
- `risk_on_and_context->metal_4h` score `-0.5833` n `54` status `ready` deltaP `1.372` edge `0.0206` maxDD `-1.6961`
- `risk_on_high->crypto_alt_1h` score `-0.589` n `54` status `ready` deltaP `3.3101` edge `0.005` maxDD `-5.8734`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
