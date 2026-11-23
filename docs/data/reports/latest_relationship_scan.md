# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-23T13:22:26.403353+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4458`

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

- `market_context_high->unknown_1h` score `25475.234` n `56` status `ready` deltaP `-0.5347` edge `2122.9559` maxDD `-0.6271`
- `market_context_high->unknown_4h` score `17228.6468` n `56` status `ready` deltaP `4.3554` edge `1435.7054` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1292.6806` n `31` status `ready` deltaP `3.728` edge `107.7161` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1097.9206` n `31` status `ready` deltaP `4.701` edge `91.4677` maxDD `-0.119`
- `news_risk_high->equity_24h` score `45.0026` n `31` status `ready` deltaP `49.6528` edge `3.4192` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `37.0197` n `31` status `ready` deltaP `48.6111` edge `2.7609` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `32.6668` n `31` status `ready` deltaP `48.7847` edge `2.397` maxDD `0.0`
- `news_risk_high->metal_24h` score `13.3477` n `31` status `ready` deltaP `50.2633` edge `0.8047` maxDD `-0.1986`
- `news_risk_high->equity_4h` score `10.3342` n `31` status `ready` deltaP `32.9564` edge `0.6897` maxDD `-2.1911`
- `news_risk_high->crypto_alt_4h` score `10.215` n `31` status `ready` deltaP `21.8823` edge `0.7924` maxDD `-5.2957`
- `news_risk_high->index_24h` score `7.0354` n `31` status `ready` deltaP `47.7431` edge `0.268` maxDD `0.0`
- `news_risk_high->fx_24h` score `6.2451` n `31` status `ready` deltaP `52.8226` edge `0.1811` maxDD `-0.0262`
- `news_risk_high->crypto_major_4h` score `6.2116` n `31` status `ready` deltaP `11.4427` edge `0.8618` maxDD `-7.6714`
- `news_risk_high->equity_1h` score `3.7039` n `31` status `ready` deltaP `18.7898` edge `0.2021` maxDD `-0.163`
- `news_risk_high->index_4h` score `3.3047` n `31` status `ready` deltaP `34.7856` edge `0.0695` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.6627` n `31` status `ready` deltaP `31.244` edge `0.0221` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.3402` n `31` status `ready` deltaP `8.9627` edge `0.2864` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.9403` n `31` status `ready` deltaP `7.6154` edge `0.2337` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.5329` n `31` status `ready` deltaP `29.1336` edge `0.0302` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `1.424` n `31` status `ready` deltaP `19.9793` edge `0.1051` maxDD `-0.7918`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
