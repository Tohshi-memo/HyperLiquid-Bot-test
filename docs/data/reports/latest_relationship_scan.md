# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-09T05:37:26.215569+00:00`
- Price records: `672`
- Market context records: `3353`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13151`

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

- `risk_on_high->crypto_major_24h` score `58.2094` n `32` status `ready` deltaP `62.1528` edge `4.4407` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `58.2094` n `32` status `ready` deltaP `62.1528` edge `4.4407` maxDD `-0.0083`
- `risk_on_high->crypto_alt_24h` score `54.2699` n `32` status `ready` deltaP `56.9444` edge `4.158` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `54.2699` n `32` status `ready` deltaP `56.9444` edge `4.158` maxDD `-0.8779`
- `risk_on_high->equity_24h` score `46.5225` n `32` status `ready` deltaP `56.7708` edge `3.4984` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `46.5225` n `32` status `ready` deltaP `56.7708` edge `3.4984` maxDD `0.0`
- `risk_on_high->index_24h` score `23.2334` n `32` status `ready` deltaP `50.8681` edge `1.597` maxDD `0.0`
- `risk_on_and_context->index_24h` score `23.2334` n `32` status `ready` deltaP `50.8681` edge `1.597` maxDD `0.0`
- `risk_on_high->metal_24h` score `15.8839` n `32` status `ready` deltaP `35.0694` edge `1.116` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `15.8839` n `32` status `ready` deltaP `35.0694` edge `1.116` maxDD `-0.7574`
- `risk_on_high->crypto_major_4h` score `15.8151` n `32` status `ready` deltaP `29.5732` edge `1.233` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `15.8151` n `32` status `ready` deltaP `29.5732` edge `1.233` maxDD `-5.9781`
- `market_context_high->crypto_alt_24h` score `12.3176` n `165` status `ready` deltaP `17.6452` edge `2.4457` maxDD `-70.3986`
- `market_context_high->index_24h` score `12.306` n `165` status `ready` deltaP `36.3226` edge `1.0388` maxDD `-16.1026`
- `market_context_high->equity_24h` score `11.0097` n `165` status `ready` deltaP `31.9223` edge `2.0403` maxDD `-53.663`
- `risk_on_high->crypto_alt_4h` score `7.6857` n `32` status `ready` deltaP `9.375` edge `0.7624` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `7.6857` n `32` status `ready` deltaP `9.375` edge `0.7624` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `3.6771` n `32` status `ready` deltaP `14.7104` edge `0.4868` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `3.6771` n `32` status `ready` deltaP `14.7104` edge `0.4868` maxDD `-5.7426`
- `risk_on_high->crypto_major_1h` score `2.0066` n `32` status `ready` deltaP `6.2687` edge `0.3224` maxDD `-5.8885`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
