# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-24T17:37:37.149722+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4272`

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

- `market_context_high->unknown_1h` score `32290.0442` n `45` status `ready` deltaP `1.5668` edge `2690.836` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `22100.0577` n `45` status `ready` deltaP `2.8727` edge `1841.6662` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `1055.0892` n `31` status `ready` deltaP `1.7819` edge `87.9298` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `847.1102` n `31` status `ready` deltaP `4.0913` edge `70.5709` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `37.7786` n `31` status `ready` deltaP `49.6528` edge `2.8172` maxDD `0.0`
- `news_risk_high->equity_24h` score `35.7304` n `31` status `ready` deltaP `41.8403` edge `2.6986` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `33.0208` n `31` status `ready` deltaP `47.5694` edge `2.4346` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `11.2571` n `31` status `ready` deltaP `25.0836` edge `0.8579` maxDD `-5.2957`
- `news_risk_high->metal_24h` score `11.1002` n `31` status `ready` deltaP `41.2355` edge `0.6776` maxDD `-0.1986`
- `news_risk_high->equity_4h` score `9.6446` n `31` status `ready` deltaP `33.5661` edge `0.628` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `6.9847` n `31` status `ready` deltaP `16.3208` edge `0.9284` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `6.2962` n `31` status `ready` deltaP `52.9962` edge `0.1842` maxDD `-0.0262`
- `news_risk_high->index_24h` score `5.3003` n `31` status `ready` deltaP `39.5833` edge `0.1778` maxDD `0.0`
- `news_risk_high->equity_1h` score `3.4965` n `31` status `ready` deltaP `18.7898` edge `0.1848` maxDD `-0.1621`
- `news_risk_high->index_4h` score `2.9801` n `31` status `ready` deltaP `32.499` edge `0.0577` maxDD `-0.4146`
- `market_context_high->fx_4h` score `2.8597` n `45` status `ready` deltaP `34.6612` edge `0.0357` maxDD `-0.2774`
- `news_risk_high->crypto_major_1h` score `2.6106` n `31` status `ready` deltaP `11.6573` edge `0.3031` maxDD `-1.6897`
- `news_risk_high->index_1h` score `2.5512` n `31` status `ready` deltaP `30.3458` edge `0.0188` maxDD `-0.0136`
- `news_risk_high->crypto_alt_1h` score `2.2512` n `31` status `ready` deltaP `11.2082` edge `0.2496` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.6521` n `31` status `ready` deltaP `30.93` edge `0.0335` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
