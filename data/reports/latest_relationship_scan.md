# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-11T09:52:29.565685+00:00`
- Price records: `672`
- Market context records: `3573`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13114`

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

- `risk_on_high->crypto_major_24h` score `49.2877` n `32` status `ready` deltaP `53.5474` edge `3.7546` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `49.2877` n `32` status `ready` deltaP `53.5474` edge `3.7546` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `43.9973` n `32` status `ready` deltaP `52.6863` edge `3.3152` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `43.9973` n `32` status `ready` deltaP `52.6863` edge `3.3152` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `43.4956` n `32` status `ready` deltaP `53.2008` edge `3.2851` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `43.4956` n `32` status `ready` deltaP `53.2008` edge `3.2851` maxDD `-0.8779`
- `risk_on_high->index_24h` score `25.467` n `32` status `ready` deltaP `53.0329` edge `1.7687` maxDD `0.0`
- `risk_on_and_context->index_24h` score `25.467` n `32` status `ready` deltaP `53.0329` edge `1.7687` maxDD `0.0`
- `risk_on_high->metal_24h` score `18.6385` n `32` status `ready` deltaP `36.8609` edge `1.3336` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `18.6385` n `32` status `ready` deltaP `36.8609` edge `1.3336` maxDD `-0.7574`
- `market_context_high->equity_24h` score `18.3533` n `156` status `ready` deltaP `29.6094` edge `1.9733` maxDD `-40.9667`
- `market_context_high->index_24h` score `14.0823` n `156` status `ready` deltaP `37.6483` edge `1.1442` maxDD `-15.0661`
- `market_context_high->crypto_major_24h` score `13.8537` n `156` status `ready` deltaP `18.8519` edge `1.8019` maxDD `-54.8486`
- `risk_on_high->crypto_major_4h` score `13.1269` n `32` status `ready` deltaP `24.6951` edge `1.0415` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `13.1269` n `32` status `ready` deltaP `24.6951` edge `1.0415` maxDD `-5.9781`
- `market_context_high->crypto_alt_24h` score `9.4084` n `156` status `ready` deltaP `13.3771` edge `1.4991` maxDD `-56.6728`
- `market_context_high->metal_24h` score `7.6065` n `156` status `ready` deltaP `30.9314` edge `1.223` maxDD `-25.9879`
- `risk_on_high->crypto_alt_4h` score `4.6781` n `32` status `ready` deltaP `5.2591` edge `0.5392` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `4.6781` n `32` status `ready` deltaP `5.2591` edge `0.5392` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `3.4206` n `32` status `ready` deltaP `13.9482` edge `0.459` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
