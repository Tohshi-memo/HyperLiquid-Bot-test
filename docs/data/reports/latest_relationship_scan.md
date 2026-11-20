# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-20T18:22:34.081956+00:00`
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

- `market_context_high->unknown_1h` score `10163.4064` n `126` status `ready` deltaP `1.7632` edge `846.9586` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `6275.4764` n `125` status `ready` deltaP `0.2695` edge `522.9851` maxDD `-0.7759`
- `market_context_high->crypto_major_24h` score `4.8878` n `107` status `ready` deltaP `27.4257` edge `1.1568` maxDD `-50.7065`
- `market_context_high->crypto_alt_24h` score `1.5767` n `107` status `ready` deltaP `14.3156` edge `0.948` maxDD `-66.63`
- `market_context_high->metal_1h` score `-0.1657` n `126` status `ready` deltaP `4.4007` edge `0.0159` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.2804` n `126` status `ready` deltaP `3.3076` edge `0.0032` maxDD `-1.2295`
- `market_context_high->metal_4h` score `-0.4292` n `125` status `ready` deltaP `12.4817` edge `0.0369` maxDD `-9.6774`
- `market_context_high->fx_1h` score `-1.3963` n `126` status `ready` deltaP `-8.8062` edge `-0.0017` maxDD `-0.4757`
- `market_context_high->equity_1h` score `-1.8275` n `126` status `ready` deltaP `5.988` edge `0.0137` maxDD `-13.1399`
- `market_context_high->fx_4h` score `-1.9852` n `125` status `ready` deltaP `-7.8634` edge `-0.0005` maxDD `-1.794`
- `market_context_high->commodity_1h` score `-2.1697` n `126` status `ready` deltaP `-7.1738` edge `-0.0198` maxDD `-4.3877`
- `market_context_high->index_4h` score `-2.3313` n `125` status `ready` deltaP `-2.8732` edge `-0.0167` maxDD `-6.6736`
- `market_context_high->crypto_major_1h` score `-2.4595` n `126` status `ready` deltaP `2.4094` edge `0.0108` maxDD `-13.8788`
- `market_context_high->crypto_alt_1h` score `-3.1044` n `126` status `ready` deltaP `-3.4455` edge `-0.008` maxDD `-13.8848`
- `market_context_high->crypto_major_4h` score `-3.6943` n `125` status `ready` deltaP `1.3561` edge `0.1617` maxDD `-43.883`
- `market_context_high->metal_24h` score `-5.6614` n `107` status `ready` deltaP `13.2139` edge `0.1131` maxDD `-43.8379`
- `market_context_high->crypto_alt_4h` score `-6.4443` n `125` status `ready` deltaP `2.1183` edge `0.0928` maxDD `-43.8494`
- `market_context_high->fx_24h` score `-6.7656` n `107` status `ready` deltaP `-18.7938` edge `-0.0112` maxDD `-5.5179`
- `market_context_high->commodity_4h` score `-6.9075` n `125` status `ready` deltaP `-20.511` edge `-0.0696` maxDD `-15.5426`
- `market_context_high->index_24h` score `-13.0042` n `107` status `ready` deltaP `-26.3369` edge `-0.1582` maxDD `-30.9921`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
