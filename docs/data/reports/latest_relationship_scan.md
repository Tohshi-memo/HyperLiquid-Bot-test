# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-26T02:37:33.246218+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3899`

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

- `market_context_high->unknown_1h` score `33791.6538` n `43` status `ready` deltaP `1.1071` edge `2815.9732` maxDD `-0.4209`
- `news_risk_high->unknown_4h` score `3186.9449` n `31` status `ready` deltaP `3.3291` edge `265.5622` maxDD `-0.1191`
- `news_risk_high->unknown_1h` score `889.9033` n `31` status `ready` deltaP `1.6322` edge `74.1653` maxDD `-0.7395`
- `news_risk_high->unknown_24h` score `50.7649` n `31` status `ready` deltaP `6.0764` edge `4.1899` maxDD `0.0`
- `news_risk_high->equity_24h` score `43.9108` n `31` status `ready` deltaP `50.0` edge `3.3259` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `40.9694` n `31` status `ready` deltaP `50.8681` edge `3.075` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `35.8331` n `31` status `ready` deltaP `50.1736` edge `2.6516` maxDD `0.0`
- `news_risk_high->metal_24h` score `10.8752` n `31` status `ready` deltaP `36.548` edge `0.6901` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `10.8331` n `31` status `ready` deltaP `26.6079` edge `0.8124` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `10.1701` n `31` status `ready` deltaP `37.2247` edge `0.6474` maxDD `-2.178`
- `news_risk_high->index_24h` score `7.1687` n `31` status `ready` deltaP `51.3889` edge `0.2548` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `6.746` n `31` status `ready` deltaP `17.2354` edge `0.8917` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `5.3179` n `31` status `ready` deltaP `45.3573` edge `0.1536` maxDD `-0.0262`
- `market_context_high->unknown_4h` score `3.7622` n `43` status `ready` deltaP `1.9037` edge `0.3147` maxDD `-0.7765`
- `news_risk_high->equity_1h` score `3.5491` n `31` status `ready` deltaP `19.688` edge `0.1832` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.3148` n `31` status `ready` deltaP `36.1576` edge `0.0612` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.6375` n `31` status `ready` deltaP `31.3937` edge `0.019` maxDD `-0.0136`
- `market_context_high->fx_4h` score `2.5241` n `43` status `ready` deltaP `30.977` edge `0.0323` maxDD `-0.2774`
- `news_risk_high->crypto_major_1h` score `2.369` n `31` status `ready` deltaP `9.5615` edge `0.2861` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.1723` n `31` status `ready` deltaP `12.2561` edge `0.2325` maxDD `-1.5232`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
