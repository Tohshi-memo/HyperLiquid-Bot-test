# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-12T04:07:31.421167+00:00`
- Price records: `672`
- Market context records: `3651`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13163`

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

- `risk_on_high->crypto_major_24h` score `36.5305` n `32` status `ready` deltaP `41.6667` edge `2.7707` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `36.5305` n `32` status `ready` deltaP `41.6667` edge `2.7707` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `32.63` n `32` status `ready` deltaP `43.75` edge `2.4275` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `32.63` n `32` status `ready` deltaP `43.75` edge `2.4275` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `28.6818` n `32` status `ready` deltaP `40.7986` edge `2.1333` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `28.6818` n `32` status `ready` deltaP `40.7986` edge `2.1333` maxDD `-0.8779`
- `risk_on_high->index_24h` score `18.5408` n `32` status `ready` deltaP `43.75` edge `1.2534` maxDD `0.0`
- `risk_on_and_context->index_24h` score `18.5408` n `32` status `ready` deltaP `43.75` edge `1.2534` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `11.4694` n `32` status `ready` deltaP `20.7317` edge `0.9298` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `11.4694` n `32` status `ready` deltaP `20.7317` edge `0.9298` maxDD `-5.9781`
- `risk_on_high->metal_24h` score `10.382` n `32` status `ready` deltaP `29.3403` edge `0.6957` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `10.382` n `32` status `ready` deltaP `29.3403` edge `0.6957` maxDD `-0.7574`
- `market_context_high->equity_24h` score `8.342` n `157` status `ready` deltaP `20.8201` edge `1.1228` maxDD `-35.3144`
- `market_context_high->index_24h` score `8.1448` n `157` status `ready` deltaP `29.1003` edge `0.6563` maxDD `-11.3924`
- `market_context_high->metal_24h` score `2.9674` n `157` status `ready` deltaP `23.6476` edge `0.618` maxDD `-21.6171`
- `risk_on_high->crypto_alt_4h` score `2.828` n `32` status `ready` deltaP `0.8384` edge `0.4145` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `2.828` n `32` status `ready` deltaP `0.8384` edge `0.4145` maxDD `-11.7537`
- `market_context_high->crypto_major_24h` score `2.5255` n `157` status `ready` deltaP `7.849` edge `0.8648` maxDD `-49.5335`
- `risk_on_high->equity_4h` score `2.4526` n `32` status `ready` deltaP `9.2226` edge `0.3664` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `2.4526` n `32` status `ready` deltaP `9.2226` edge `0.3664` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
