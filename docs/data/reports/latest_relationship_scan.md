# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-14T02:07:28.040674+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9807`

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

- `market_context_high->crypto_alt_4h` score `6.7708` n `117` status `ready` deltaP `16.8482` edge `0.5968` maxDD `-9.2574`
- `risk_on_high->commodity_24h` score `6.2944` n `52` status `ready` deltaP `32.0` edge `0.3112` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.2944` n `52` status `ready` deltaP `32.0` edge `0.3112` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `6.1811` n `117` status `ready` deltaP `21.3441` edge `0.5287` maxDD `-7.4722`
- `risk_on_high->crypto_alt_4h` score `5.3597` n `54` status `ready` deltaP `19.1274` edge `0.3639` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `5.3597` n `54` status `ready` deltaP `19.1274` edge `0.3639` maxDD `-1.9151`
- `risk_on_high->crypto_major_4h` score `4.5575` n `54` status `ready` deltaP `34.4495` edge `0.4399` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.5575` n `54` status `ready` deltaP `34.4495` edge `0.4399` maxDD `-4.1548`
- `market_context_high->unknown_4h` score `4.3749` n `117` status `ready` deltaP `-3.7934` edge `0.4545` maxDD `-1.8373`
- `market_context_high->crypto_alt_1h` score `1.9354` n `117` status `ready` deltaP `14.315` edge `0.1726` maxDD `-5.8734`
- `market_context_high->crypto_major_1h` score `1.4252` n `117` status `ready` deltaP `7.1588` edge `0.1516` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.3528` n `117` status `ready` deltaP `14.6002` edge `0.0366` maxDD `-1.6961`
- `risk_on_high->crypto_major_1h` score `-0.23` n `54` status `ready` deltaP `2.6004` edge `0.0254` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.23` n `54` status `ready` deltaP `2.6004` edge `0.0254` maxDD `-3.7781`
- `market_context_high->fx_1h` score `-0.3179` n `117` status `ready` deltaP `1.3976` edge `0.0022` maxDD `-0.3742`
- `market_context_high->metal_1h` score `-0.3338` n `117` status `ready` deltaP `7.7141` edge `0.0077` maxDD `-0.9556`
- `risk_on_high->metal_1h` score `-0.4313` n `54` status `ready` deltaP `2.301` edge `0.0025` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.4313` n `54` status `ready` deltaP `2.301` edge `0.0025` maxDD `-0.8513`
- `risk_on_high->crypto_alt_1h` score `-0.4752` n `54` status `ready` deltaP `4.0586` edge `0.0146` maxDD `-5.8734`
- `risk_on_and_context->crypto_alt_1h` score `-0.4752` n `54` status `ready` deltaP `4.0586` edge `0.0146` maxDD `-5.8734`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
