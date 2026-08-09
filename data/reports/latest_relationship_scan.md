# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-09T08:07:34.134047+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8841`

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

- `market_context_high->equity_24h` score `3.7248` n `103` status `ready` deltaP `4.5729` edge `0.5859` maxDD `-21.1456`
- `market_context_high->metal_24h` score `2.7175` n `103` status `ready` deltaP `13.2535` edge `0.1957` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.211` n `142` status `ready` deltaP `15.392` edge `0.0656` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.8097` n `143` status `ready` deltaP `10.991` edge `0.0285` maxDD `-0.7439`
- `market_context_high->fx_24h` score `0.7915` n `103` status `ready` deltaP `21.575` edge `0.0443` maxDD `-1.9329`
- `market_context_high->index_24h` score `0.561` n `103` status `ready` deltaP `9.1002` edge `0.1644` maxDD `-5.9181`
- `market_context_high->fx_1h` score `-0.281` n `143` status `ready` deltaP `4.445` edge `-0.0035` maxDD `-0.9639`
- `market_context_high->fx_4h` score `-0.4264` n `142` status `ready` deltaP `6.3595` edge `-0.0026` maxDD `-1.6928`
- `market_context_high->index_1h` score `-0.4408` n `143` status `ready` deltaP `-1.8424` edge `-0.0053` maxDD `-0.7809`
- `market_context_high->metal_1h` score `-0.6908` n `143` status `ready` deltaP `-4.8877` edge `-0.0064` maxDD `-0.9664`
- `market_context_high->index_4h` score `-0.9113` n `142` status `ready` deltaP `-0.9791` edge `-0.0089` maxDD `-1.1743`
- `market_context_high->equity_1h` score `-0.9145` n `143` status `ready` deltaP `-0.1873` edge `0.0079` maxDD `-4.6286`
- `market_context_high->metal_4h` score `-0.9726` n `142` status `ready` deltaP `-1.022` edge `-0.017` maxDD `-2.7373`
- `market_context_high->crypto_alt_1h` score `-1.8785` n `143` status `ready` deltaP `-9.9839` edge `-0.0258` maxDD `-2.4677`
- `market_context_high->equity_4h` score `-2.5317` n `142` status `ready` deltaP `-1.5373` edge `-0.067` maxDD `-7.6983`
- `market_context_high->crypto_major_1h` score `-3.1256` n `143` status `ready` deltaP `-10.5377` edge `-0.058` maxDD `-7.2436`
- `market_context_high->crypto_major_24h` score `-3.233` n `103` status `ready` deltaP `6.0461` edge `-0.0603` maxDD `-14.2873`
- `market_context_high->crypto_alt_4h` score `-3.5923` n `142` status `ready` deltaP `-6.7073` edge `-0.089` maxDD `-6.585`
- `market_context_high->crypto_alt_24h` score `-4.8745` n `103` status `ready` deltaP `-13.1406` edge `-0.1743` maxDD `-4.5445`
- `market_context_high->unknown_1h` score `-7.7957` n `143` status `ready` deltaP `-5.7944` edge `-0.5663` maxDD `-1.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
