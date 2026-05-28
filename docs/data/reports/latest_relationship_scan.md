# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-28T11:22:22.159714+00:00`
- Price records: `672`
- Market context records: `2136`
- Flow alert records: `8046`
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

- `market_context_high->crypto_alt_4h` score `13.1603` n `158` status `ready` deltaP `36.7687` edge `0.9452` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `11.7876` n `158` status `ready` deltaP `41.0698` edge `0.7615` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `6.3356` n `158` status `ready` deltaP `24.5079` edge `0.4395` maxDD `-2.6599`
- `news_risk_high->commodity_4h` score `6.106` n `33` status `ready` deltaP `28.0442` edge `0.389` maxDD `-3.0367`
- `market_context_high->equity_4h` score `5.0154` n `158` status `ready` deltaP `26.6247` edge `0.3499` maxDD `-5.0894`
- `market_context_high->index_24h` score `3.572` n `157` status `ready` deltaP `14.5505` edge `0.3235` maxDD `-4.1604`
- `market_context_high->crypto_major_1h` score `3.211` n `158` status `ready` deltaP `17.5851` edge `0.2025` maxDD `-2.1721`
- `market_context_high->metal_4h` score `3.0869` n `158` status `ready` deltaP `21.4032` edge `0.2533` maxDD `-4.7664`
- `market_context_high->crypto_alt_1h` score `3.0406` n `158` status `ready` deltaP `15.7887` edge `0.2345` maxDD `-4.9097`
- `market_context_high->index_4h` score `3.0401` n `158` status `ready` deltaP `22.0651` edge `0.1746` maxDD `-1.8022`
- `market_context_high->equity_24h` score `2.9188` n `157` status `ready` deltaP `25.9769` edge `0.5599` maxDD `-33.1875`
- `news_risk_high->unknown_1h` score `2.8029` n `33` status `ready` deltaP `30.1715` edge `0.0627` maxDD `-1.7548`
- `market_context_high->unknown_24h` score `2.5176` n `157` status `ready` deltaP `26.5114` edge `0.5651` maxDD `-35.8966`
- `news_risk_high->fx_4h` score `2.4455` n `33` status `ready` deltaP `31.6473` edge `0.0112` maxDD `-0.1382`
- `market_context_high->crypto_major_24h` score `1.8686` n `157` status `ready` deltaP `21.6373` edge `0.9539` maxDD `-62.3533`
- `news_risk_high->unknown_4h` score `1.2725` n `33` status `ready` deltaP `17.124` edge `0.1213` maxDD `-2.7857`
- `market_context_high->equity_1h` score `0.825` n `158` status `ready` deltaP `10.1683` edge `0.0798` maxDD `-2.6402`
- `news_risk_high->commodity_1h` score `0.7707` n `33` status `ready` deltaP `7.7255` edge `0.0807` maxDD `-2.1052`
- `market_context_high->metal_1h` score `0.5775` n `158` status `ready` deltaP `8.7925` edge `0.0565` maxDD `-2.3594`
- `market_context_high->metal_24h` score `0.4567` n `157` status `ready` deltaP `12.4446` edge `0.3657` maxDD `-23.2095`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
