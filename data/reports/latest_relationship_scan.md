# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-09T07:37:25.138020+00:00`
- Price records: `672`
- Market context records: `3361`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13080`

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

- `risk_on_high->crypto_major_24h` score `57.3063` n `32` status `ready` deltaP `60.7639` edge `4.3747` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `57.3063` n `32` status `ready` deltaP `60.7639` edge `4.3747` maxDD `-0.0083`
- `risk_on_high->crypto_alt_24h` score `53.8168` n `32` status `ready` deltaP `55.5556` edge `4.1295` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `53.8168` n `32` status `ready` deltaP `55.5556` edge `4.1295` maxDD `-0.8779`
- `risk_on_high->equity_24h` score `46.1577` n `32` status `ready` deltaP `56.7708` edge `3.468` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `46.1577` n `32` status `ready` deltaP `56.7708` edge `3.468` maxDD `0.0`
- `risk_on_high->index_24h` score `23.1914` n `32` status `ready` deltaP `50.8681` edge `1.5935` maxDD `0.0`
- `risk_on_and_context->index_24h` score `23.1914` n `32` status `ready` deltaP `50.8681` edge `1.5935` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `15.4874` n `32` status `ready` deltaP `28.5061` edge `1.2128` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `15.4874` n `32` status `ready` deltaP `28.5061` edge `1.2128` maxDD `-5.9781`
- `risk_on_high->metal_24h` score `15.3804` n `32` status `ready` deltaP `33.6806` edge `1.0833` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `15.3804` n `32` status `ready` deltaP `33.6806` edge `1.0833` maxDD `-0.7574`
- `market_context_high->crypto_alt_24h` score `12.498` n `163` status `ready` deltaP `16.9628` edge `2.4384` maxDD `-68.268`
- `market_context_high->index_24h` score `12.1681` n `163` status `ready` deltaP `36.1442` edge `1.0285` maxDD `-16.1026`
- `market_context_high->equity_24h` score `10.7528` n `163` status `ready` deltaP `31.6174` edge `2.0094` maxDD `-53.663`
- `risk_on_high->crypto_alt_4h` score `7.3994` n `32` status `ready` deltaP `8.7652` edge `0.7426` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `7.3994` n `32` status `ready` deltaP `8.7652` edge `0.7426` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `3.5754` n `32` status `ready` deltaP `14.4055` edge `0.4758` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `3.5754` n `32` status `ready` deltaP `14.4055` edge `0.4758` maxDD `-5.7426`
- `risk_on_high->crypto_major_1h` score `1.9933` n `32` status `ready` deltaP `6.2687` edge `0.3207` maxDD `-5.8885`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
