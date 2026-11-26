# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-26T00:22:29.731472+00:00`
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

- `market_context_high->unknown_1h` score `32144.6342` n `45` status `ready` deltaP `1.5668` edge `2678.7185` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `21796.273` n `45` status `ready` deltaP `1.958` edge `1816.3569` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `909.6792` n `31` status `ready` deltaP `1.7819` edge `75.8123` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `543.3255` n `31` status `ready` deltaP `3.1766` edge `45.2616` maxDD `-0.1191`
- `news_risk_high->unknown_24h` score `193.4425` n `31` status `ready` deltaP `6.0764` edge `16.0797` maxDD `0.0`
- `news_risk_high->equity_24h` score `45.3306` n `31` status `ready` deltaP `51.5625` edge `3.4338` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `41.7976` n `31` status `ready` deltaP `52.4306` edge `3.1336` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `37.0189` n `31` status `ready` deltaP `51.7361` edge `2.74` maxDD `0.0`
- `news_risk_high->metal_24h` score `11.3446` n `31` status `ready` deltaP `38.1105` edge `0.7188` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `10.9303` n `31` status `ready` deltaP `26.6079` edge `0.8205` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `10.4011` n `31` status `ready` deltaP `37.682` edge `0.6636` maxDD `-2.178`
- `news_risk_high->index_24h` score `7.4005` n `31` status `ready` deltaP `52.9514` edge `0.2637` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `6.7031` n `31` status `ready` deltaP `17.2354` edge `0.8862` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `5.2424` n `31` status `ready` deltaP `44.4893` edge `0.1531` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.6667` n `31` status `ready` deltaP `19.9874` edge `0.191` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.35` n `31` status `ready` deltaP `36.4625` edge `0.0621` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.6734` n `31` status `ready` deltaP `31.6931` edge `0.02` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.4649` n `31` status `ready` deltaP `10.31` edge `0.2934` maxDD `-1.6897`
- `market_context_high->fx_4h` score `2.3425` n `45` status `ready` deltaP `29.021` edge `0.0302` maxDD `-0.2774`
- `news_risk_high->crypto_alt_1h` score `2.2666` n `31` status `ready` deltaP `13.0046` edge `0.2396` maxDD `-1.5232`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
