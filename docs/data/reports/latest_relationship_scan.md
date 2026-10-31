# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-31T19:15:15.679517+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7669`

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

- `market_context_high->unknown_24h` score `3011.1788` n `97` status `ready` deltaP `-9.7133` edge `251.0393` maxDD `-1.1049`
- `market_context_high->unknown_4h` score `96.5489` n `97` status `ready` deltaP `0.7103` edge `8.0543` maxDD `-0.3966`
- `news_risk_high->unknown_1h` score `77.74` n `108` status `ready` deltaP `-5.0454` edge `6.5406` maxDD `-0.9571`
- `news_risk_high->crypto_alt_24h` score `19.5165` n `71` status `ready` deltaP `45.7942` edge `1.3262` maxDD `-0.0763`
- `market_context_high->equity_24h` score `10.7976` n `97` status `ready` deltaP `25.4421` edge `1.0059` maxDD `-14.0571`
- `news_risk_high->crypto_alt_4h` score `5.1433` n `108` status `ready` deltaP `19.2073` edge `0.4392` maxDD `-7.4246`
- `market_context_high->index_24h` score `4.8574` n `97` status `ready` deltaP `43.1845` edge `0.1352` maxDD `-0.1315`
- `market_context_high->metal_4h` score `1.6181` n `97` status `ready` deltaP `20.0591` edge `0.0436` maxDD `-0.7323`
- `market_context_high->metal_1h` score `0.7891` n `97` status `ready` deltaP `11.4405` edge `0.0185` maxDD `-0.3209`
- `news_risk_high->crypto_alt_1h` score `0.7521` n `108` status `ready` deltaP `8.4276` edge `0.1019` maxDD `-3.9659`
- `market_context_high->equity_4h` score `0.6746` n `97` status `ready` deltaP `4.9079` edge `0.1931` maxDD `-4.48`
- `market_context_high->equity_1h` score `0.4291` n `97` status `ready` deltaP `6.4016` edge `0.0999` maxDD `-2.3383`
- `market_context_high->fx_4h` score `0.3663` n `97` status `ready` deltaP `10.2951` edge `0.001` maxDD `-0.1285`
- `market_context_high->commodity_4h` score `0.2964` n `97` status `ready` deltaP `13.6771` edge `0.0585` maxDD `-0.9349`
- `market_context_high->fx_1h` score `0.2809` n `97` status `ready` deltaP `9.4605` edge `-0.0003` maxDD `-0.1407`
- `market_context_high->crypto_major_1h` score `0.2781` n `97` status `ready` deltaP `8.3138` edge `0.083` maxDD `-5.2213`
- `market_context_high->metal_24h` score `-0.079` n `97` status `ready` deltaP `11.8002` edge `0.1759` maxDD `-10.5088`
- `market_context_high->crypto_major_4h` score `-0.2365` n `97` status `ready` deltaP `15.7185` edge `0.1389` maxDD `-14.5879`
- `market_context_high->index_1h` score `-0.2403` n `97` status `ready` deltaP `3.4416` edge `0.0021` maxDD `-1.1344`
- `market_context_high->commodity_1h` score `-0.3075` n `97` status `ready` deltaP `-0.3148` edge `0.0141` maxDD `-0.4475`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
