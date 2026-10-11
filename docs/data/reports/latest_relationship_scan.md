# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-11T14:22:24.774585+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `7318`

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

- `market_context_high->unknown_24h` score `1002.5911` n `44` status `ready` deltaP `-17.1717` edge `83.7001` maxDD `-1.2425`
- `market_context_high->unknown_4h` score `50.7881` n `76` status `ready` deltaP `-9.4512` edge `4.3534` maxDD `-2.3109`
- `market_context_high->equity_24h` score `8.9029` n `44` status `ready` deltaP `30.2399` edge `0.5832` maxDD `-1.0977`
- `market_context_high->index_24h` score `5.2843` n `44` status `ready` deltaP `44.0341` edge `0.166` maxDD `-0.203`
- `market_context_high->unknown_1h` score `4.1883` n `82` status `ready` deltaP `-5.2285` edge `0.4175` maxDD `-1.0231`
- `market_context_high->crypto_major_24h` score `3.484` n `44` status `ready` deltaP `-13.731` edge `0.6967` maxDD `-17.8526`
- `market_context_high->fx_24h` score `2.6803` n `44` status `ready` deltaP `31.3131` edge `0.0338` maxDD `-0.202`
- `market_context_high->fx_4h` score `1.0384` n `76` status `ready` deltaP `15.8697` edge `0.0091` maxDD `-0.2692`
- `market_context_high->commodity_4h` score `0.44` n `76` status `ready` deltaP `11.5051` edge `0.0133` maxDD `-1.6002`
- `market_context_high->commodity_1h` score `0.1711` n `82` status `ready` deltaP `4.7941` edge `0.0074` maxDD `-0.3417`
- `market_context_high->fx_1h` score `-0.4452` n `82` status `ready` deltaP `-2.052` edge `0.0008` maxDD `-0.271`
- `market_context_high->crypto_alt_1h` score `-0.4766` n `82` status `ready` deltaP `2.3551` edge `0.048` maxDD `-4.9401`
- `market_context_high->metal_4h` score `-0.5045` n `76` status `ready` deltaP `-1.6207` edge `0.0184` maxDD `-1.1153`
- `market_context_high->metal_1h` score `-0.5321` n `82` status `ready` deltaP `1.8621` edge `0.0023` maxDD `-0.7246`
- `market_context_high->crypto_major_1h` score `-1.1153` n `82` status `ready` deltaP `-3.0378` edge `0.0162` maxDD `-3.7778`
- `market_context_high->index_4h` score `-1.1432` n `76` status `ready` deltaP `-11.2885` edge `-0.0001` maxDD `-1.0298`
- `market_context_high->index_1h` score `-1.1434` n `82` status `ready` deltaP `-9.1354` edge `-0.0037` maxDD `-0.5588`
- `market_context_high->equity_1h` score `-1.3314` n `82` status `ready` deltaP `-11.1654` edge `-0.0093` maxDD `-2.2898`
- `market_context_high->crypto_major_4h` score `-1.3966` n `76` status `ready` deltaP `-6.8678` edge `0.0773` maxDD `-11.1784`
- `market_context_high->crypto_alt_4h` score `-2.0533` n `76` status `ready` deltaP `-8.5206` edge `0.0494` maxDD `-13.8008`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
