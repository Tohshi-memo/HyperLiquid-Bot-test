# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-20T18:07:28.144817+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2758`

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

- `market_context_high->unknown_1h` score `10166.2552` n `126` status `ready` deltaP `1.7632` edge `847.196` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `6333.4029` n `124` status `ready` deltaP `0.2114` edge `527.8127` maxDD `-0.7759`
- `market_context_high->crypto_major_24h` score `4.8878` n `107` status `ready` deltaP `27.4257` edge `1.1568` maxDD `-50.7065`
- `market_context_high->crypto_alt_24h` score `1.6019` n `107` status `ready` deltaP `14.3156` edge `0.9501` maxDD `-66.63`
- `market_context_high->metal_1h` score `-0.1571` n `126` status `ready` deltaP `4.5504` edge `0.016` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.2719` n `126` status `ready` deltaP `3.4573` edge `0.0033` maxDD `-1.2295`
- `market_context_high->metal_4h` score `-0.3466` n `124` status `ready` deltaP `12.8688` edge `0.0395` maxDD `-9.2449`
- `market_context_high->fx_1h` score `-1.3963` n `126` status `ready` deltaP `-8.8062` edge `-0.0017` maxDD `-0.4757`
- `market_context_high->equity_1h` score `-1.806` n `126` status `ready` deltaP `6.1377` edge `0.0145` maxDD `-13.1399`
- `market_context_high->fx_4h` score `-2.0067` n `124` status `ready` deltaP `-8.2465` edge `-0.0007` maxDD `-1.794`
- `market_context_high->commodity_1h` score `-2.184` n `126` status `ready` deltaP `-7.3235` edge `-0.02` maxDD `-4.3877`
- `market_context_high->index_4h` score `-2.2294` n `124` status `ready` deltaP `-2.7095` edge `-0.0144` maxDD `-6.2657`
- `market_context_high->crypto_major_1h` score `-2.4523` n `126` status `ready` deltaP `2.4094` edge `0.0114` maxDD `-13.8788`
- `market_context_high->crypto_alt_1h` score `-3.0864` n `126` status `ready` deltaP `-3.4455` edge `-0.0065` maxDD `-13.8848`
- `market_context_high->crypto_major_4h` score `-3.123` n `124` status `ready` deltaP `1.5392` edge `0.1841` maxDD `-40.2461`
- `market_context_high->metal_24h` score `-5.6794` n `107` status `ready` deltaP `13.2139` edge `0.1116` maxDD `-43.8379`
- `market_context_high->crypto_alt_4h` score `-5.768` n `124` status `ready` deltaP `2.4538` edge `0.1087` maxDD `-41.1248`
- `market_context_high->fx_24h` score `-6.7493` n `107` status `ready` deltaP `-18.6202` edge `-0.011` maxDD `-5.5179`
- `market_context_high->commodity_4h` score `-6.9778` n `124` status `ready` deltaP `-21.1497` edge `-0.0712` maxDD `-15.5426`
- `market_context_high->index_24h` score `-13.0174` n `107` status `ready` deltaP `-26.3369` edge `-0.1593` maxDD `-30.9921`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
