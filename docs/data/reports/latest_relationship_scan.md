# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-11T18:22:31.450991+00:00`
- Price records: `672`
- Market context records: `3609`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13138`

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

- `risk_on_high->crypto_major_24h` score `44.835` n `32` status `ready` deltaP `48.4375` edge `3.4176` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `44.835` n `32` status `ready` deltaP `48.4375` edge `3.4176` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `41.6089` n `32` status `ready` deltaP `50.5208` edge `3.1306` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `41.6089` n `32` status `ready` deltaP `50.5208` edge `3.1306` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `37.8239` n `32` status `ready` deltaP `47.5694` edge `2.85` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `37.8239` n `32` status `ready` deltaP `47.5694` edge `2.85` maxDD `-0.8779`
- `risk_on_high->index_24h` score `24.2701` n `32` status `ready` deltaP `50.5208` edge `1.6857` maxDD `0.0`
- `risk_on_and_context->index_24h` score `24.2701` n `32` status `ready` deltaP `50.5208` edge `1.6857` maxDD `0.0`
- `risk_on_high->metal_24h` score `17.2309` n `32` status `ready` deltaP `36.1111` edge `1.2213` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `17.2309` n `32` status `ready` deltaP `36.1111` edge `1.2213` maxDD `-0.7574`
- `market_context_high->equity_24h` score `15.8788` n `158` status `ready` deltaP `27.1031` edge `1.7838` maxDD `-40.9667`
- `risk_on_high->crypto_major_4h` score `13.1915` n `32` status `ready` deltaP `24.5427` edge `1.0479` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `13.1915` n `32` status `ready` deltaP `24.5427` edge `1.0479` maxDD `-5.9781`
- `market_context_high->index_24h` score `12.9202` n `158` status `ready` deltaP `35.3309` edge `1.0628` maxDD `-15.0661`
- `market_context_high->crypto_major_24h` score `9.5124` n `158` status `ready` deltaP `14.2207` edge `1.471` maxDD `-54.8486`
- `market_context_high->metal_24h` score `6.7245` n `158` status `ready` deltaP `30.0193` edge `1.116` maxDD `-25.9879`
- `risk_on_high->crypto_alt_4h` score `4.8975` n `32` status `ready` deltaP `5.1067` edge `0.5585` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `4.8975` n `32` status `ready` deltaP `5.1067` edge `0.5585` maxDD `-11.7537`
- `market_context_high->crypto_alt_24h` score `3.9506` n `158` status `ready` deltaP `8.2893` edge `1.0782` maxDD `-56.6728`
- `risk_on_high->equity_4h` score `3.5512` n `32` status `ready` deltaP `14.4055` edge `0.4727` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
