# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-13T16:52:29.581066+00:00`
- Price records: `672`
- Market context records: `3809`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13464`

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

- `risk_on_high->crypto_major_24h` score `31.3559` n `32` status `ready` deltaP `33.1597` edge `2.3962` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `31.3559` n `32` status `ready` deltaP `33.1597` edge `2.3962` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `25.6952` n `32` status `ready` deltaP `41.3194` edge `1.8658` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `25.6952` n `32` status `ready` deltaP `41.3194` edge `1.8658` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `23.3511` n `32` status `ready` deltaP `31.9444` edge `1.7481` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `23.3511` n `32` status `ready` deltaP `31.9444` edge `1.7481` maxDD `-0.8779`
- `risk_on_high->index_24h` score `11.398` n `32` status `ready` deltaP `31.25` edge `0.7415` maxDD `0.0`
- `risk_on_and_context->index_24h` score `11.398` n `32` status `ready` deltaP `31.25` edge `0.7415` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `9.2662` n `32` status `ready` deltaP `14.1768` edge `0.7899` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `9.2662` n `32` status `ready` deltaP `14.1768` edge `0.7899` maxDD `-5.9781`
- `market_context_high->equity_24h` score `7.2439` n `151` status `ready` deltaP `20.1273` edge `0.7511` maxDD `-13.8632`
- `market_context_high->crypto_major_24h` score `5.5809` n `151` status `ready` deltaP `7.1456` edge `0.8638` maxDD `-31.0425`
- `market_context_high->index_24h` score `5.3482` n `151` status `ready` deltaP `26.6142` edge `0.3822` maxDD `-7.1159`
- `market_context_high->metal_24h` score `4.2976` n `151` status `ready` deltaP `26.2808` edge `0.3261` maxDD `-9.1203`
- `market_context_high->crypto_major_4h` score `2.6498` n `186` status `ready` deltaP `13.7064` edge `0.3195` maxDD `-10.5381`
- `risk_on_high->equity_4h` score `1.4482` n `32` status `ready` deltaP `7.6982` edge `0.2478` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `1.4482` n `32` status `ready` deltaP `7.6982` edge `0.2478` maxDD `-5.7426`
- `risk_on_high->commodity_4h` score `1.4147` n `32` status `ready` deltaP `16.997` edge `0.0913` maxDD `-3.6044`
- `risk_on_and_context->commodity_4h` score `1.4147` n `32` status `ready` deltaP `16.997` edge `0.0913` maxDD `-3.6044`
- `risk_on_high->metal_24h` score `1.3317` n `32` status `ready` deltaP `14.2361` edge `0.0422` maxDD `-0.7574`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
