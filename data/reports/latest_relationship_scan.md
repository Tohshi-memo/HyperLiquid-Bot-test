# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-11T08:07:29.546426+00:00`
- Price records: `672`
- Market context records: `3565`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13076`

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

- `risk_on_high->crypto_major_24h` score `50.1516` n `32` status `ready` deltaP `54.7606` edge `3.8185` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `50.1516` n `32` status `ready` deltaP `54.7606` edge `3.8185` maxDD `-0.0083`
- `risk_on_high->crypto_alt_24h` score `44.5898` n `32` status `ready` deltaP `54.414` edge `3.3682` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `44.5898` n `32` status `ready` deltaP `54.414` edge `3.3682` maxDD `-0.8779`
- `risk_on_high->equity_24h` score `44.3397` n `32` status `ready` deltaP `53.7262` edge `3.3368` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `44.3397` n `32` status `ready` deltaP `53.7262` edge `3.3368` maxDD `0.0`
- `risk_on_high->index_24h` score `25.582` n `32` status `ready` deltaP `53.8995` edge `1.7725` maxDD `0.0`
- `risk_on_and_context->index_24h` score `25.582` n `32` status `ready` deltaP `53.8995` edge `1.7725` maxDD `0.0`
- `market_context_high->equity_24h` score `18.6957` n `156` status `ready` deltaP `30.6493` edge `1.9949` maxDD `-40.9667`
- `risk_on_high->metal_24h` score `18.6613` n `32` status `ready` deltaP `36.8609` edge `1.3355` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `18.6613` n `32` status `ready` deltaP `36.8609` edge `1.3355` maxDD `-0.7574`
- `market_context_high->crypto_major_24h` score `14.7175` n `156` status `ready` deltaP `20.0651` edge `1.8658` maxDD `-54.8486`
- `market_context_high->index_24h` score `14.1973` n `156` status `ready` deltaP `38.5149` edge `1.148` maxDD `-15.0661`
- `risk_on_high->crypto_major_4h` score `13.2029` n `32` status `ready` deltaP `25.0` edge `1.0458` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `13.2029` n `32` status `ready` deltaP `25.0` edge `1.0458` maxDD `-5.9781`
- `market_context_high->crypto_alt_24h` score `10.5027` n `156` status `ready` deltaP `14.5903` edge `1.5822` maxDD `-56.6728`
- `market_context_high->metal_24h` score `7.6213` n `156` status `ready` deltaP `30.9314` edge `1.2249` maxDD `-25.9879`
- `risk_on_high->crypto_alt_4h` score `4.6973` n `32` status `ready` deltaP `5.2591` edge `0.5408` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `4.6973` n `32` status `ready` deltaP `5.2591` edge `0.5408` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `3.5076` n `32` status `ready` deltaP `14.4055` edge `0.4671` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
