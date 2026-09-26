# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-26T13:07:24.961462+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11822`

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

- `news_risk_high->unknown_24h` score `4454.8615` n `85` status `ready` deltaP `0.1736` edge `371.2373` maxDD `0.0`
- `market_context_high->unknown_1h` score `69.2698` n `47` status `ready` deltaP `7.8704` edge `5.7271` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `47.1768` n `47` status `ready` deltaP `22.4364` edge `3.8211` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `27.2951` n `47` status `ready` deltaP `18.0112` edge `2.1925` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.6503` n `47` status `ready` deltaP `33.3739` edge `1.9506` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.0058` n `47` status `ready` deltaP `28.5128` edge `0.4067` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.4059` n `47` status `ready` deltaP `28.8084` edge `0.1156` maxDD `-0.2401`
- `news_risk_high->crypto_alt_24h` score `3.0561` n `85` status `ready` deltaP `11.9036` edge `0.5705` maxDD `-29.2814`
- `market_context_high->equity_4h` score `2.7533` n `47` status `ready` deltaP `17.6018` edge `0.1539` maxDD `-1.3444`
- `market_context_high->index_4h` score `2.7187` n `47` status `ready` deltaP `31.4349` edge `0.0324` maxDD `-0.2323`
- `news_risk_high->index_24h` score `2.3005` n `85` status `ready` deltaP `26.6605` edge `0.071` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `1.5177` n `85` status `ready` deltaP `31.9874` edge `0.1461` maxDD `-6.8481`
- `market_context_high->crypto_alt_4h` score `1.3037` n `47` status `ready` deltaP `10.9075` edge `0.1027` maxDD `-3.3417`
- `market_context_high->equity_1h` score `1.0374` n `47` status `ready` deltaP `11.9155` edge `0.0473` maxDD `-1.5564`
- `market_context_high->crypto_major_4h` score `0.8627` n `47` status `ready` deltaP `7.2814` edge `0.1138` maxDD `-5.2359`
- `market_context_high->index_1h` score `0.8193` n `47` status `ready` deltaP `12.9634` edge `0.0097` maxDD `-0.2275`
- `market_context_high->fx_1h` score `0.4817` n `47` status `ready` deltaP `10.2592` edge `0.0074` maxDD `-0.1854`
- `market_context_high->crypto_major_1h` score `0.4034` n `47` status `ready` deltaP `5.6504` edge `0.0777` maxDD `-4.5405`
- `market_context_high->metal_1h` score `0.0367` n `47` status `ready` deltaP `3.8763` edge `0.0105` maxDD `-0.1976`
- `news_risk_high->index_1h` score `-0.0591` n `139` status `ready` deltaP `3.1211` edge `0.0034` maxDD `-0.3305`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
