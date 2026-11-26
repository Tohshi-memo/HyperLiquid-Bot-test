# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-26T01:07:28.512045+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3887`

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

- `market_context_high->unknown_1h` score `32140.481` n `45` status `ready` deltaP `1.5668` edge `2678.3724` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `21784.3414` n `45` status `ready` deltaP `1.958` edge `1815.3626` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `905.526` n `31` status `ready` deltaP `1.7819` edge `75.4662` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `531.3939` n `31` status `ready` deltaP `3.1766` edge `44.2673` maxDD `-0.1191`
- `news_risk_high->unknown_24h` score `146.0485` n `31` status `ready` deltaP `6.0764` edge `12.1302` maxDD `0.0`
- `news_risk_high->equity_24h` score `44.8569` n `31` status `ready` deltaP `51.0417` edge `3.3978` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `41.5736` n `31` status `ready` deltaP `51.9097` edge `3.1184` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `36.6736` n `31` status `ready` deltaP `51.2153` edge `2.7147` maxDD `0.0`
- `news_risk_high->metal_24h` score `11.1986` n `31` status `ready` deltaP `37.5896` edge `0.7101` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `10.8991` n `31` status `ready` deltaP `26.6079` edge `0.8179` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `10.2699` n `31` status `ready` deltaP `37.3771` edge `0.6547` maxDD `-2.178`
- `news_risk_high->index_24h` score `7.3204` n `31` status `ready` deltaP `52.4306` edge `0.2605` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `6.7094` n `31` status `ready` deltaP `17.2354` edge `0.887` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `5.2877` n `31` status `ready` deltaP `45.0101` edge `0.1534` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.5431` n `31` status `ready` deltaP `19.5383` edge `0.1837` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.316` n `31` status `ready` deltaP `36.1576` edge `0.0613` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.6267` n `31` status `ready` deltaP `31.244` edge `0.0191` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.4064` n `31` status `ready` deltaP `9.8609` edge `0.2889` maxDD `-1.6897`
- `market_context_high->fx_4h` score `2.3693` n `45` status `ready` deltaP `29.3259` edge `0.0304` maxDD `-0.2774`
- `news_risk_high->crypto_alt_1h` score `2.2027` n `31` status `ready` deltaP `12.5555` edge `0.2344` maxDD `-1.5232`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
