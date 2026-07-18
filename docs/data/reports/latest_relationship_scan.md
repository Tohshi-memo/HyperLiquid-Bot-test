# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-18T13:22:25.787152+00:00`
- Price records: `672`
- Market context records: `7143`
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

- `market_context_high->fx_4h` score `0.6008` n `145` status `ready` deltaP `15.8652` edge `0.0143` maxDD `-0.9333`
- `market_context_high->fx_1h` score `-0.1546` n `156` status `ready` deltaP `4.445` edge `0.0026` maxDD `-0.276`
- `market_context_high->unknown_1h` score `-0.4194` n `156` status `ready` deltaP `-1.1938` edge `0.0372` maxDD `-1.4688`
- `market_context_high->crypto_alt_1h` score `-0.6326` n `156` status `ready` deltaP `-0.3839` edge `0.0245` maxDD `-5.91`
- `market_context_high->crypto_major_1h` score `-0.652` n `156` status `ready` deltaP `3.5045` edge `0.0341` maxDD `-7.6171`
- `market_context_high->commodity_1h` score `-0.6974` n `156` status `ready` deltaP `-1.6697` edge `-0.0162` maxDD `-1.9668`
- `market_context_high->index_1h` score `-0.7941` n `156` status `ready` deltaP `0.7945` edge `-0.005` maxDD `-2.3175`
- `market_context_high->metal_1h` score `-1.4153` n `156` status `ready` deltaP `-5.5082` edge `-0.0051` maxDD `-2.0897`
- `market_context_high->unknown_4h` score `-1.5133` n `145` status `ready` deltaP `-5.696` edge `0.017` maxDD `-5.5096`
- `market_context_high->commodity_4h` score `-2.0433` n `145` status `ready` deltaP `-4.4313` edge `-0.0372` maxDD `-2.9494`
- `market_context_high->metal_4h` score `-2.8539` n `145` status `ready` deltaP `-8.8541` edge `-0.012` maxDD `-5.2551`
- `market_context_high->equity_1h` score `-3.5999` n `156` status `ready` deltaP `-0.9558` edge `-0.0444` maxDD `-15.2709`
- `market_context_high->index_4h` score `-3.9336` n `145` status `ready` deltaP `-1.5286` edge `-0.0477` maxDD `-12.2591`
- `market_context_high->commodity_24h` score `-4.4988` n `133` status `ready` deltaP `-13.4581` edge `-0.1543` maxDD `-4.4704`
- `market_context_high->fx_24h` score `-4.9887` n `133` status `ready` deltaP `-16.0518` edge `-0.026` maxDD `-3.9503`
- `market_context_high->crypto_major_4h` score `-5.2483` n `145` status `ready` deltaP `0.0904` edge `-0.004` maxDD `-25.0503`
- `market_context_high->crypto_alt_4h` score `-5.61` n `145` status `ready` deltaP `-4.1422` edge `-0.0408` maxDD `-23.9269`
- `market_context_high->unknown_24h` score `-10.1215` n `133` status `ready` deltaP `-32.8765` edge `-0.1096` maxDD `-23.5076`
- `market_context_high->equity_4h` score `-14.2799` n `145` status `ready` deltaP `-3.2275` edge `-0.2443` maxDD `-65.2676`
- `market_context_high->metal_24h` score `-14.5549` n `133` status `ready` deltaP `-30.3871` edge `-0.1922` maxDD `-40.7836`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
