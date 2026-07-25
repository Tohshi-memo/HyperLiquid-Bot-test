# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-25T17:27:10.087404+00:00`
- Price records: `672`
- Market context records: `7901`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14713`

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

- `market_context_high->equity_24h` score `15.118` n `99` status `ready` deltaP `29.6875` edge `1.1961` maxDD `-6.0681`
- `market_context_high->metal_24h` score `6.1483` n `99` status `ready` deltaP `30.2803` edge `0.3515` maxDD `-0.2806`
- `market_context_high->equity_4h` score `5.7079` n `104` status `ready` deltaP `20.8716` edge `0.4258` maxDD `-5.1426`
- `market_context_high->commodity_24h` score `1.9132` n `99` status `ready` deltaP `21.4173` edge `0.175` maxDD `-7.0012`
- `market_context_high->index_4h` score `1.7544` n `104` status `ready` deltaP `20.063` edge `0.0651` maxDD `-0.8791`
- `market_context_high->crypto_alt_4h` score `1.6605` n `104` status `ready` deltaP `12.8987` edge `0.1641` maxDD `-3.9374`
- `market_context_high->metal_4h` score `1.6079` n `104` status `ready` deltaP `15.0797` edge `0.1082` maxDD `-0.979`
- `market_context_high->equity_1h` score `1.5308` n `108` status `ready` deltaP `13.4884` edge `0.1194` maxDD `-4.2072`
- `market_context_high->crypto_major_4h` score `1.494` n `104` status `ready` deltaP `14.7162` edge `0.1982` maxDD `-6.7444`
- `market_context_high->crypto_major_1h` score `1.3055` n `108` status `ready` deltaP `14.6928` edge `0.0517` maxDD `-1.6021`
- `market_context_high->fx_24h` score `1.2945` n `99` status `ready` deltaP `33.9489` edge `0.0484` maxDD `-3.0343`
- `market_context_high->index_24h` score `0.9104` n `99` status `ready` deltaP `4.6243` edge `0.1329` maxDD `-1.3621`
- `market_context_high->index_1h` score `0.6428` n `108` status `ready` deltaP `11.5616` edge `0.0195` maxDD `-0.7743`
- `market_context_high->crypto_alt_1h` score `0.4929` n `108` status `ready` deltaP `6.3041` edge `0.0423` maxDD `-1.4603`
- `market_context_high->metal_1h` score `0.3051` n `108` status `ready` deltaP `5.6498` edge `0.0256` maxDD `-0.6936`
- `market_context_high->commodity_4h` score `0.031` n `104` status `ready` deltaP `6.9307` edge `0.0258` maxDD `-1.8869`
- `market_context_high->fx_1h` score `-0.2277` n `108` status `ready` deltaP `1.0261` edge `0.0007` maxDD `-0.2715`
- `market_context_high->fx_4h` score `-0.3078` n `104` status `ready` deltaP `4.4548` edge `0.0056` maxDD `-0.9813`
- `market_context_high->commodity_1h` score `-0.3992` n `108` status `ready` deltaP `3.028` edge `0.0034` maxDD `-1.5486`
- `market_context_high->unknown_1h` score `-1.4621` n `108` status `ready` deltaP `6.3595` edge `-0.1875` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
