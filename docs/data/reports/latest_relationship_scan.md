# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-28T10:37:27.812847+00:00`
- Price records: `672`
- Market context records: `2133`
- Flow alert records: `8037`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9158`

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

- `market_context_high->crypto_alt_4h` score `13.1927` n `158` status `ready` deltaP `36.7687` edge `0.9479` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `11.8416` n `158` status `ready` deltaP `41.0698` edge `0.766` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `6.2815` n `158` status `ready` deltaP `24.3555` edge `0.436` maxDD `-2.6599`
- `news_risk_high->commodity_4h` score `6.0789` n `30` status `ready` deltaP `25.6199` edge `0.4029` maxDD `-3.0367`
- `market_context_high->equity_4h` score `5.0312` n `158` status `ready` deltaP `26.7771` edge `0.3502` maxDD `-5.0894`
- `market_context_high->index_24h` score `3.4069` n `157` status `ready` deltaP `14.0315` edge `0.3132` maxDD `-4.1604`
- `news_risk_high->fx_4h` score `3.3288` n `30` status `ready` deltaP `39.8272` edge `0.0162` maxDD `-0.0117`
- `market_context_high->crypto_major_1h` score `3.1834` n `158` status `ready` deltaP `17.4354` edge `0.2012` maxDD `-2.1721`
- `market_context_high->metal_4h` score `3.0845` n `158` status `ready` deltaP `21.4032` edge `0.2531` maxDD `-4.7664`
- `market_context_high->index_4h` score `3.0449` n `158` status `ready` deltaP `22.0651` edge `0.175` maxDD `-1.8022`
- `market_context_high->crypto_alt_1h` score `2.9663` n `158` status `ready` deltaP `15.3396` edge `0.2313` maxDD `-4.9097`
- `news_risk_high->unknown_1h` score `2.8137` n `33` status `ready` deltaP `30.1715` edge `0.0636` maxDD `-1.7548`
- `market_context_high->equity_24h` score `2.6625` n `157` status `ready` deltaP `25.4579` edge `0.542` maxDD `-33.1875`
- `market_context_high->unknown_24h` score `2.3009` n `157` status `ready` deltaP `25.9924` edge `0.5505` maxDD `-35.8966`
- `market_context_high->crypto_major_24h` score `1.7173` n `157` status `ready` deltaP `21.6373` edge `0.9345` maxDD `-62.3533`
- `news_risk_high->unknown_4h` score `1.3925` n `30` status `ready` deltaP `16.9716` edge `0.1377` maxDD `-2.7857`
- `news_risk_high->commodity_1h` score `0.8438` n `33` status `ready` deltaP `8.1746` edge `0.0838` maxDD `-2.1052`
- `market_context_high->equity_1h` score `0.7627` n `158` status `ready` deltaP `9.7192` edge `0.0776` maxDD `-2.6402`
- `market_context_high->metal_1h` score `0.5092` n `158` status `ready` deltaP `8.3434` edge `0.0538` maxDD `-2.3594`
- `market_context_high->metal_24h` score `0.3563` n `157` status `ready` deltaP `11.9256` edge `0.3563` maxDD `-23.2095`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
