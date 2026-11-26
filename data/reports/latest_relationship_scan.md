# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-26T09:52:28.623012+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3455`

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

- `news_risk_high->unknown_4h` score `3256.1707` n `31` status `ready` deltaP `3.4815` edge `271.33` maxDD `-0.1191`
- `news_risk_high->unknown_1h` score `3233.1577` n `31` status `ready` deltaP `1.6322` edge `269.4365` maxDD `-0.7395`
- `market_context_high->unknown_1h` score `102.8658` n `31` status `ready` deltaP `1.6322` edge `8.5707` maxDD `-0.4209`
- `news_risk_high->equity_24h` score `38.0396` n `31` status `ready` deltaP `44.9653` edge `2.8702` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `37.2379` n `31` status `ready` deltaP `45.8333` edge `2.7976` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `31.5915` n `31` status `ready` deltaP `45.1389` edge `2.3317` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `11.0472` n `31` status `ready` deltaP `27.9799` edge `0.8211` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `10.8186` n `31` status `ready` deltaP `39.5112` edge `0.6862` maxDD `-2.178`
- `news_risk_high->metal_24h` score `9.1285` n `31` status `ready` deltaP `31.5133` edge `0.5781` maxDD `-0.1986`
- `news_risk_high->crypto_major_4h` score `7.0202` n `31` status `ready` deltaP `19.522` edge `0.9116` maxDD `-7.6714`
- `news_risk_high->index_24h` score `6.3003` n `31` status `ready` deltaP `46.3542` edge `0.216` maxDD `0.0`
- `news_risk_high->fx_24h` score `5.1791` n `31` status `ready` deltaP `43.9684` edge `0.1513` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.8034` n `31` status `ready` deltaP `20.7359` edge `0.1974` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.5975` n `31` status `ready` deltaP `38.5966` edge `0.0685` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.7764` n `31` status `ready` deltaP `32.741` edge `0.0216` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.4673` n `31` status `ready` deltaP `9.7112` edge `0.2977` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.2635` n `31` status `ready` deltaP `12.8549` edge `0.2402` maxDD `-1.5232`
- `market_context_high->fx_4h` score `2.0568` n `31` status `ready` deltaP `26.1999` edge `0.0252` maxDD `-0.2774`
- `news_risk_high->metal_1h` score `1.5118` n `31` status `ready` deltaP `29.5827` edge `0.0245` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `1.1078` n `31` status `ready` deltaP `16.7781` edge `0.0859` maxDD `-0.7918`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
