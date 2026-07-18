# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-18T13:07:25.714650+00:00`
- Price records: `672`
- Market context records: `7142`
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

- `market_context_high->fx_4h` score `0.6362` n `144` status `ready` deltaP `16.2771` edge `0.0145` maxDD `-0.9333`
- `market_context_high->fx_1h` score `-0.1426` n `156` status `ready` deltaP `4.5947` edge `0.0026` maxDD `-0.276`
- `market_context_high->unknown_1h` score `-0.4314` n `156` status `ready` deltaP `-1.3435` edge `0.0372` maxDD `-1.4688`
- `market_context_high->crypto_alt_1h` score `-0.6443` n `156` status `ready` deltaP `-0.5336` edge `0.024` maxDD `-5.91`
- `market_context_high->crypto_major_1h` score `-0.6629` n `156` status `ready` deltaP `3.3548` edge `0.0337` maxDD `-7.6171`
- `market_context_high->commodity_1h` score `-0.6974` n `156` status `ready` deltaP `-1.6697` edge `-0.0162` maxDD `-1.9668`
- `market_context_high->index_1h` score `-0.7941` n `156` status `ready` deltaP `0.7945` edge `-0.005` maxDD `-2.3175`
- `market_context_high->metal_1h` score `-1.4273` n `156` status `ready` deltaP `-5.6579` edge `-0.0051` maxDD `-2.0897`
- `market_context_high->unknown_4h` score `-1.4997` n `144` status `ready` deltaP `-5.6233` edge `0.0176` maxDD `-5.4574`
- `market_context_high->commodity_4h` score `-2.0596` n `144` status `ready` deltaP `-4.5901` edge `-0.0375` maxDD `-2.9494`
- `market_context_high->metal_4h` score `-2.8452` n `144` status `ready` deltaP `-8.6721` edge `-0.0121` maxDD `-5.2551`
- `market_context_high->equity_1h` score `-3.5999` n `156` status `ready` deltaP `-0.9558` edge `-0.0444` maxDD `-15.2709`
- `market_context_high->index_4h` score `-3.9272` n `144` status `ready` deltaP `-1.3889` edge `-0.0481` maxDD `-12.2591`
- `market_context_high->commodity_24h` score `-4.4988` n `133` status `ready` deltaP `-13.4581` edge `-0.1543` maxDD `-4.4704`
- `market_context_high->fx_24h` score `-4.9887` n `133` status `ready` deltaP `-16.0518` edge `-0.026` maxDD `-3.9503`
- `market_context_high->crypto_major_4h` score `-5.2298` n `144` status `ready` deltaP `0.254` edge `-0.0043` maxDD `-24.9898`
- `market_context_high->crypto_alt_4h` score `-5.6022` n `144` status `ready` deltaP `-4.0312` edge `-0.0417` maxDD `-23.8619`
- `market_context_high->unknown_24h` score `-10.1227` n `133` status `ready` deltaP `-32.8765` edge `-0.1097` maxDD `-23.5076`
- `market_context_high->equity_4h` score `-14.212` n `144` status `ready` deltaP `-2.9641` edge `-0.2464` maxDD `-65.1204`
- `market_context_high->metal_24h` score `-14.5302` n `133` status `ready` deltaP `-30.2135` edge `-0.1913` maxDD `-40.7836`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
