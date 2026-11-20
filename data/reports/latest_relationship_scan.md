# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-20T16:52:26.744276+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2726`

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

- `market_context_high->unknown_1h` score `10173.3412` n `126` status `ready` deltaP `1.7632` edge `847.7865` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `6532.5415` n `121` status `ready` deltaP `0.553` edge `544.4032` maxDD `-0.6076`
- `market_context_high->crypto_major_24h` score `4.8254` n `107` status `ready` deltaP `27.4257` edge `1.1488` maxDD `-50.7065`
- `market_context_high->crypto_alt_24h` score `1.6211` n `107` status `ready` deltaP `14.3156` edge `0.9517` maxDD `-66.63`
- `market_context_high->metal_4h` score `-0.1273` n `121` status `ready` deltaP `14.0685` edge `0.0457` maxDD `-8.1314`
- `market_context_high->metal_1h` score `-0.1797` n `126` status `ready` deltaP `4.251` edge `0.0151` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.3116` n `126` status `ready` deltaP `2.8585` edge `0.0022` maxDD `-1.2295`
- `market_context_high->fx_1h` score `-1.3579` n `126` status `ready` deltaP `-8.3571` edge `-0.0015` maxDD `-0.4757`
- `market_context_high->crypto_major_4h` score `-1.4788` n `121` status `ready` deltaP `1.8167` edge `0.2405` maxDD `-29.0423`
- `market_context_high->equity_1h` score `-1.9547` n `126` status `ready` deltaP `5.6886` edge `0.0051` maxDD `-13.1399`
- `market_context_high->index_4h` score `-2.0166` n `121` status `ready` deltaP `-2.4919` edge `-0.0107` maxDD `-5.2589`
- `market_context_high->fx_4h` score `-2.0247` n `121` status `ready` deltaP `-8.6223` edge `-0.0005` maxDD `-1.794`
- `market_context_high->commodity_1h` score `-2.1313` n `126` status `ready` deltaP `-6.8744` edge `-0.0186` maxDD `-4.3877`
- `market_context_high->crypto_alt_4h` score `-2.2347` n `121` status `ready` deltaP `2.8837` edge `0.1602` maxDD `-30.9406`
- `market_context_high->crypto_major_1h` score `-2.541` n `126` status `ready` deltaP `2.11` edge `0.006` maxDD `-13.8788`
- `market_context_high->crypto_alt_1h` score `-3.1116` n `126` status `ready` deltaP `-3.4455` edge `-0.0086` maxDD `-13.8848`
- `market_context_high->metal_24h` score `-5.7754` n `107` status `ready` deltaP `13.2139` edge `0.1036` maxDD `-43.8379`
- `market_context_high->fx_24h` score `-6.6841` n `107` status `ready` deltaP `-17.9257` edge `-0.0102` maxDD `-5.5179`
- `market_context_high->commodity_4h` score `-7.0315` n `121` status `ready` deltaP `-21.4763` edge `-0.0735` maxDD `-15.5426`
- `market_context_high->equity_4h` score `-11.8209` n `121` status `ready` deltaP `-5.5092` edge `-0.1108` maxDD `-56.6707`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
