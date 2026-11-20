# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-20T17:22:42.800073+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2756`

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

- `market_context_high->unknown_1h` score `10166.1616` n `126` status `ready` deltaP `1.7632` edge `847.1882` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `6409.9857` n `123` status `ready` deltaP `0.6605` edge `534.1895` maxDD `-0.6076`
- `market_context_high->crypto_major_24h` score `4.8449` n `107` status `ready` deltaP `27.4257` edge `1.1513` maxDD `-50.7065`
- `market_context_high->crypto_alt_24h` score `1.6283` n `107` status `ready` deltaP `14.3156` edge `0.9523` maxDD `-66.63`
- `market_context_high->metal_1h` score `-0.1696` n `126` status `ready` deltaP `4.4007` edge `0.0154` maxDD `-2.6517`
- `market_context_high->metal_4h` score `-0.2728` n `123` status `ready` deltaP `13.2622` edge `0.0412` maxDD `-8.8336`
- `market_context_high->index_1h` score `-0.2999` n `126` status `ready` deltaP `3.0082` edge `0.0027` maxDD `-1.2295`
- `market_context_high->fx_1h` score `-1.3831` n `126` status `ready` deltaP `-8.6565` edge `-0.0016` maxDD `-0.4757`
- `market_context_high->equity_1h` score `-1.8767` n `126` status `ready` deltaP `5.8383` edge `0.0106` maxDD `-13.1399`
- `market_context_high->fx_4h` score `-2.0184` n `123` status `ready` deltaP `-8.4858` edge `-0.0006` maxDD `-1.794`
- `market_context_high->commodity_1h` score `-2.1685` n `126` status `ready` deltaP `-7.1738` edge `-0.0197` maxDD `-4.3877`
- `market_context_high->index_4h` score `-2.1703` n `123` status `ready` deltaP `-2.8455` edge `-0.0137` maxDD `-5.8552`
- `market_context_high->crypto_major_1h` score `-2.5266` n `126` status `ready` deltaP `2.11` edge `0.0072` maxDD `-13.8788`
- `market_context_high->crypto_major_4h` score `-2.6246` n `123` status `ready` deltaP `1.4227` edge `0.1947` maxDD `-36.254`
- `market_context_high->crypto_alt_1h` score `-3.0996` n `126` status `ready` deltaP `-3.4455` edge `-0.0076` maxDD `-13.8848`
- `market_context_high->crypto_alt_4h` score `-3.3198` n `123` status `ready` deltaP `2.4898` edge `0.118` maxDD `-37.8171`
- `market_context_high->metal_24h` score `-5.7406` n `107` status `ready` deltaP `13.2139` edge `0.1065` maxDD `-43.8379`
- `market_context_high->fx_24h` score `-6.7167` n `107` status `ready` deltaP `-18.273` edge `-0.0106` maxDD `-5.5179`
- `market_context_high->commodity_4h` score `-6.9852` n `123` status `ready` deltaP `-21.1382` edge `-0.0719` maxDD `-15.5426`
- `market_context_high->index_24h` score `-13.0642` n `107` status `ready` deltaP `-26.3369` edge `-0.1632` maxDD `-30.9921`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
