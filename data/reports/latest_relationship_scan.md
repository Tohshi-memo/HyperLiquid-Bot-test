# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-20T15:07:53.178288+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2662`

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

- `market_context_high->unknown_1h` score `10356.6402` n `124` status `ready` deltaP `1.8834` edge `863.0606` maxDD `-0.9181`
- `market_context_high->unknown_4h` score `6747.2151` n `118` status `ready` deltaP `1.1471` edge `562.2887` maxDD `-0.6072`
- `market_context_high->crypto_major_24h` score `4.7661` n `107` status `ready` deltaP `27.4257` edge `1.1412` maxDD `-50.7065`
- `market_context_high->crypto_alt_24h` score `1.5647` n `107` status `ready` deltaP `14.3156` edge `0.947` maxDD `-66.63`
- `market_context_high->metal_4h` score `0.0706` n `118` status `ready` deltaP `15.3292` edge `0.0514` maxDD `-7.2302`
- `market_context_high->crypto_major_4h` score `0.0211` n `118` status `ready` deltaP `2.6044` edge `0.2958` maxDD `-18.5787`
- `market_context_high->metal_1h` score `-0.1165` n `124` status `ready` deltaP `5.0318` edge `0.018` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.2646` n `124` status `ready` deltaP `3.4769` edge `0.0041` maxDD `-1.2295`
- `market_context_high->crypto_alt_4h` score `-0.7257` n `118` status `ready` deltaP `3.6715` edge `0.2109` maxDD `-20.94`
- `market_context_high->crypto_major_1h` score `-1.1077` n `124` status `ready` deltaP `3.0278` edge `0.0441` maxDD `-7.8611`
- `market_context_high->fx_1h` score `-1.2834` n `124` status `ready` deltaP `-7.4561` edge `-0.0013` maxDD `-0.4757`
- `market_context_high->equity_1h` score `-1.359` n `124` status `ready` deltaP `6.3454` edge `0.0306` maxDD `-11.559`
- `market_context_high->crypto_alt_1h` score `-1.8473` n `124` status `ready` deltaP `-2.6174` edge `0.0231` maxDD `-8.4343`
- `market_context_high->index_4h` score `-1.8865` n `118` status `ready` deltaP `-1.9197` edge `-0.0088` maxDD `-4.8491`
- `market_context_high->commodity_1h` score `-1.9734` n `124` status `ready` deltaP `-5.4858` edge `-0.0147` maxDD `-4.3877`
- `market_context_high->fx_4h` score `-2.0628` n `118` status `ready` deltaP `-9.4305` edge `0.0` maxDD `-1.794`
- `market_context_high->metal_24h` score `-5.8954` n `107` status `ready` deltaP `13.2139` edge `0.0936` maxDD `-43.8379`
- `market_context_high->fx_24h` score `-6.642` n `107` status `ready` deltaP `-17.5785` edge `-0.009` maxDD `-5.5179`
- `market_context_high->commodity_4h` score `-6.9477` n `118` status `ready` deltaP `-20.8195` edge `-0.0709` maxDD `-15.5426`
- `market_context_high->equity_4h` score `-10.5761` n `118` status `ready` deltaP `-5.1261` edge `-0.0853` maxDD `-50.6163`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
