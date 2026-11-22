# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-22T07:37:28.447421+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `40`

- Symbol pattern count: `4562`

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

- `market_context_high->unknown_1h` score `11142.1432` n `113` status `ready` deltaP `0.9074` edge `928.5257` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `6884.8398` n `113` status `ready` deltaP `-1.5325` edge `573.7774` maxDD `-0.7759`
- `market_context_high->metal_1h` score `-0.1809` n `113` status `ready` deltaP `4.7838` edge `0.0114` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.2636` n `113` status `ready` deltaP `3.5597` edge `0.003` maxDD `-1.2295`
- `market_context_high->fx_1h` score `-1.313` n `113` status `ready` deltaP `-9.6749` edge `-0.0017` maxDD `-0.4573`
- `market_context_high->crypto_major_1h` score `-1.4988` n `113` status `ready` deltaP `3.5597` edge `-0.0049` maxDD `-13.8788`
- `market_context_high->metal_4h` score `-1.6523` n `113` status `ready` deltaP `5.2234` edge `0.0081` maxDD `-10.1161`
- `market_context_high->fx_4h` score `-1.6572` n `113` status `ready` deltaP `-2.3136` edge `0.0024` maxDD `-1.6217`
- `market_context_high->equity_1h` score `-1.7625` n `113` status `ready` deltaP `6.8266` edge `0.0052` maxDD `-13.1399`
- `market_context_high->crypto_alt_1h` score `-2.2824` n `113` status `ready` deltaP `-5.0037` edge `-0.0482` maxDD `-13.8848`
- `market_context_high->commodity_1h` score `-2.4786` n `113` status `ready` deltaP `-10.287` edge `-0.0253` maxDD `-4.3472`
- `market_context_high->index_4h` score `-3.0336` n `113` status `ready` deltaP `-9.6307` edge `-0.0253` maxDD `-7.0639`
- `market_context_high->fx_24h` score `-5.2506` n `113` status `ready` deltaP `-7.7157` edge `-0.0022` maxDD `-6.3799`
- `market_context_high->crypto_major_4h` score `-6.0959` n `113` status `ready` deltaP `-5.299` edge `-0.0533` maxDD `-47.4317`
- `market_context_high->commodity_4h` score `-6.7862` n `113` status `ready` deltaP `-17.5102` edge `-0.0853` maxDD `-15.0788`
- `market_context_high->metal_24h` score `-9.389` n `113` status `ready` deltaP `-3.7226` edge `0.052` maxDD `-52.1012`
- `market_context_high->crypto_alt_4h` score `-10.0539` n `113` status `ready` deltaP `-5.6038` edge `-0.1192` maxDD `-46.5016`
- `market_context_high->commodity_24h` score `-12.9648` n `113` status `ready` deltaP `-27.4398` edge `-0.3385` maxDD `-64.2582`
- `market_context_high->crypto_major_24h` score `-14.3702` n `113` status `ready` deltaP `10.0756` edge `0.1505` maxDD `-152.134`
- `market_context_high->index_24h` score `-15.6364` n `113` status `ready` deltaP `-30.6954` edge `-0.1583` maxDD `-39.8743`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
