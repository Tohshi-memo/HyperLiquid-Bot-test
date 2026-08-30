# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-30T22:22:26.672540+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11736`

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

- `risk_on_high->crypto_alt_24h` score `24.162` n `49` status `ready` deltaP `49.3056` edge `1.6848` maxDD `0.0`
- `risk_on_and_context->crypto_alt_24h` score `24.162` n `49` status `ready` deltaP `49.3056` edge `1.6848` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `12.7739` n `49` status `ready` deltaP `35.7603` edge `0.8461` maxDD `-0.9343`
- `risk_on_and_context->crypto_major_24h` score `12.7739` n `49` status `ready` deltaP `35.7603` edge `0.8461` maxDD `-0.9343`
- `risk_on_high->unknown_4h` score `8.6928` n `79` status `ready` deltaP `29.8723` edge `0.5681` maxDD `-1.0945`
- `risk_on_and_context->unknown_4h` score `8.6928` n `79` status `ready` deltaP `29.8723` edge `0.5681` maxDD `-1.0945`
- `risk_on_high->fx_24h` score `6.2169` n `49` status `ready` deltaP `69.7917` edge `0.0528` maxDD `0.0`
- `risk_on_and_context->fx_24h` score `6.2169` n `49` status `ready` deltaP `69.7917` edge `0.0528` maxDD `0.0`
- `risk_on_high->metal_24h` score `5.3579` n `49` status `ready` deltaP `47.697` edge `0.1444` maxDD `-0.2712`
- `risk_on_and_context->metal_24h` score `5.3579` n `49` status `ready` deltaP `47.697` edge `0.1444` maxDD `-0.2712`
- `market_context_high->unknown_4h` score `5.0333` n `149` status `ready` deltaP `21.054` edge `0.3261` maxDD `-1.0945`
- `market_context_high->metal_24h` score `4.3455` n `117` status `ready` deltaP `35.016` edge `0.2306` maxDD `-3.1535`
- `market_context_high->crypto_major_24h` score `4.1915` n `117` status `ready` deltaP `17.4279` edge `0.4947` maxDD `-17.2607`
- `risk_on_high->equity_24h` score `4.0633` n `49` status `ready` deltaP `28.5112` edge `0.1641` maxDD `-0.2456`
- `risk_on_and_context->equity_24h` score `4.0633` n `49` status `ready` deltaP `28.5112` edge `0.1641` maxDD `-0.2456`
- `risk_on_high->unknown_1h` score `4.0002` n `89` status `ready` deltaP `10.9786` edge `0.2846` maxDD `-0.2885`
- `risk_on_and_context->unknown_1h` score `4.0002` n `89` status `ready` deltaP `10.9786` edge `0.2846` maxDD `-0.2885`
- `market_context_high->crypto_alt_24h` score `3.2941` n `117` status `ready` deltaP `15.9723` edge `0.7348` maxDD `-27.517`
- `market_context_high->unknown_1h` score `2.6159` n `161` status `ready` deltaP `9.4014` edge `0.1962` maxDD `-0.9372`
- `risk_on_high->index_24h` score `2.2629` n `49` status `ready` deltaP `27.5156` edge `0.0146` maxDD `-0.0906`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
