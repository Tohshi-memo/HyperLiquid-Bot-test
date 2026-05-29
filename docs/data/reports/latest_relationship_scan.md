# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-29T05:07:17.606816+00:00`
- Price records: `672`
- Market context records: `2214`
- Flow alert records: `8264`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9188`

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

- `market_context_high->crypto_alt_4h` score `12.9957` n `132` status `ready` deltaP `37.6063` edge `0.9259` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `11.8949` n `132` status `ready` deltaP `42.8908` edge `0.7583` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `5.5081` n `132` status `ready` deltaP `21.5263` edge `0.3834` maxDD `-2.4317`
- `news_risk_high->commodity_4h` score `3.8379` n `43` status `ready` deltaP `32.0051` edge `0.3458` maxDD `-3.0367`
- `market_context_high->equity_4h` score `3.429` n `132` status `ready` deltaP `23.4156` edge `0.2391` maxDD `-5.0894`
- `market_context_high->crypto_major_1h` score `3.2518` n `132` status `ready` deltaP `17.7146` edge `0.2006` maxDD `-1.817`
- `market_context_high->index_4h` score `3.2318` n `132` status `ready` deltaP `26.6214` edge `0.1602` maxDD `-1.8022`
- `market_context_high->crypto_alt_1h` score `3.0058` n `132` status `ready` deltaP `16.2085` edge `0.2288` maxDD `-4.9097`
- `market_context_high->unknown_24h` score `2.6013` n `132` status `ready` deltaP `25.8997` edge `0.5256` maxDD `-32.8525`
- `news_risk_high->fx_4h` score `2.2316` n `43` status `ready` deltaP `28.1941` edge `0.0164` maxDD `-0.1382`
- `market_context_high->index_24h` score `2.0943` n `132` status `ready` deltaP `9.8642` edge `0.2316` maxDD `-4.1604`
- `news_risk_high->unknown_1h` score `1.5139` n `43` status `ready` deltaP `21.7936` edge `0.0278` maxDD `-1.7548`
- `market_context_high->crypto_major_24h` score `1.4859` n `132` status `ready` deltaP `16.9349` edge `0.9058` maxDD `-60.2561`
- `news_risk_high->unknown_4h` score `1.3445` n `43` status `ready` deltaP `14.62` edge `0.0869` maxDD `-2.7857`
- `market_context_high->metal_4h` score `1.3001` n `132` status `ready` deltaP `16.8283` edge `0.1349` maxDD `-4.7664`
- `news_risk_high->equity_4h` score `1.2464` n `43` status `ready` deltaP `-3.2934` edge `0.3025` maxDD `-4.6598`
- `news_risk_high->commodity_1h` score `0.744` n `43` status `ready` deltaP `10.6148` edge `0.0926` maxDD `-2.1052`
- `news_risk_high->fx_1h` score `0.4897` n `43` status `ready` deltaP `8.4389` edge `0.0102` maxDD `-0.0524`
- `market_context_high->equity_1h` score `0.2621` n `132` status `ready` deltaP `8.8913` edge `0.0414` maxDD `-2.6402`
- `news_risk_high->equity_1h` score `0.1441` n `43` status `ready` deltaP `4.2578` edge `0.0421` maxDD `-1.8278`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
