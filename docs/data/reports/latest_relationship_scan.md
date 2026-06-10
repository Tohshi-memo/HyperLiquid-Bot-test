# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-10T21:52:31.989929+00:00`
- Price records: `672`
- Market context records: `3522`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13196`

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

- `risk_on_high->crypto_major_24h` score `53.7036` n `32` status `ready` deltaP `57.8802` edge `4.0937` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `53.7036` n `32` status `ready` deltaP `57.8802` edge `4.0937` maxDD `-0.0083`
- `risk_on_high->crypto_alt_24h` score `49.6118` n `32` status `ready` deltaP `57.5336` edge `3.7659` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `49.6118` n `32` status `ready` deltaP `57.5336` edge `3.7659` maxDD `-0.8779`
- `risk_on_high->equity_24h` score `44.4954` n `32` status `ready` deltaP `54.5927` edge `3.344` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `44.4954` n `32` status `ready` deltaP `54.5927` edge `3.344` maxDD `0.0`
- `risk_on_high->index_24h` score `24.868` n `32` status `ready` deltaP `52.3397` edge `1.7234` maxDD `0.0`
- `risk_on_and_context->index_24h` score `24.868` n `32` status `ready` deltaP `52.3397` edge `1.7234` maxDD `0.0`
- `market_context_high->equity_24h` score `18.8515` n `156` status `ready` deltaP `31.5158` edge `2.0021` maxDD `-40.9667`
- `market_context_high->crypto_major_24h` score `18.2695` n `156` status `ready` deltaP `23.1847` edge `2.141` maxDD `-54.8486`
- `risk_on_high->metal_24h` score `17.6339` n `32` status `ready` deltaP `34.9545` edge `1.2626` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `17.6339` n `32` status `ready` deltaP `34.9545` edge `1.2626` maxDD `-0.7574`
- `market_context_high->crypto_alt_24h` score `15.5247` n `156` status `ready` deltaP `17.7099` edge `1.9799` maxDD `-56.6728`
- `risk_on_high->crypto_major_4h` score `15.1126` n `32` status `ready` deltaP `28.2012` edge `1.1836` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `15.1126` n `32` status `ready` deltaP `28.2012` edge `1.1836` maxDD `-5.9781`
- `market_context_high->index_24h` score `13.4833` n `156` status `ready` deltaP `36.9551` edge `1.0989` maxDD `-15.0661`
- `risk_on_high->crypto_alt_4h` score `7.5205` n `32` status `ready` deltaP `9.6799` edge `0.7466` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `7.5205` n `32` status `ready` deltaP `9.6799` edge `0.7466` maxDD `-11.7537`
- `market_context_high->metal_24h` score `6.9536` n `156` status `ready` deltaP `29.025` edge `1.152` maxDD `-25.9879`
- `risk_on_high->equity_4h` score `3.8672` n `32` status `ready` deltaP `16.3872` edge `0.5` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
