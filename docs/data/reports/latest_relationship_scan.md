# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-18T13:37:23.718722+00:00`
- Price records: `672`
- Market context records: `7144`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11692`

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

- `market_context_high->fx_4h` score `0.5659` n `146` status `ready` deltaP `15.459` edge `0.0141` maxDD `-0.9333`
- `market_context_high->fx_1h` score `-0.1546` n `156` status `ready` deltaP `4.445` edge `0.0026` maxDD `-0.276`
- `market_context_high->unknown_1h` score `-0.4062` n `156` status `ready` deltaP `-1.0441` edge `0.0373` maxDD `-1.4688`
- `market_context_high->crypto_alt_1h` score `-0.6193` n `156` status `ready` deltaP `-0.2342` edge `0.0252` maxDD `-5.91`
- `market_context_high->crypto_major_1h` score `-0.641` n `156` status `ready` deltaP `3.6542` edge `0.0345` maxDD `-7.6171`
- `market_context_high->commodity_1h` score `-0.706` n `156` status `ready` deltaP `-1.8194` edge `-0.0163` maxDD `-1.9668`
- `market_context_high->index_1h` score `-0.7941` n `156` status `ready` deltaP `0.7945` edge `-0.005` maxDD `-2.3175`
- `market_context_high->metal_1h` score `-1.4033` n `156` status `ready` deltaP `-5.3585` edge `-0.0051` maxDD `-2.0897`
- `market_context_high->unknown_4h` score `-1.5637` n `146` status `ready` deltaP `-5.7655` edge `0.0163` maxDD `-5.6`
- `market_context_high->commodity_4h` score `-2.0273` n `146` status `ready` deltaP `-4.2766` edge `-0.0369` maxDD `-2.9494`
- `market_context_high->metal_4h` score `-2.8624` n `146` status `ready` deltaP `-9.0336` edge `-0.0119` maxDD `-5.2551`
- `market_context_high->equity_1h` score `-3.5999` n `156` status `ready` deltaP `-0.9558` edge `-0.0444` maxDD `-15.2709`
- `market_context_high->index_4h` score `-3.8946` n `146` status `ready` deltaP `-1.1318` edge `-0.0471` maxDD `-12.2591`
- `market_context_high->commodity_24h` score `-4.5012` n `133` status `ready` deltaP `-13.4581` edge `-0.1545` maxDD `-4.4704`
- `market_context_high->fx_24h` score `-4.9887` n `133` status `ready` deltaP `-16.0518` edge `-0.026` maxDD `-3.9503`
- `market_context_high->crypto_major_4h` score `-5.2077` n `146` status `ready` deltaP `0.4636` edge `-0.0031` maxDD `-25.0503`
- `market_context_high->crypto_alt_4h` score `-5.616` n `146` status `ready` deltaP `-4.2495` edge `-0.0398` maxDD `-23.9893`
- `market_context_high->unknown_24h` score `-10.1203` n `133` status `ready` deltaP `-32.8765` edge `-0.1095` maxDD `-23.5076`
- `market_context_high->equity_4h` score `-14.3401` n `146` status `ready` deltaP `-3.4873` edge `-0.242` maxDD `-65.3809`
- `market_context_high->metal_24h` score `-14.5796` n `133` status `ready` deltaP `-30.5607` edge `-0.1931` maxDD `-40.7836`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
