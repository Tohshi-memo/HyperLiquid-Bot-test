# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-20T17:37:32.074049+00:00`
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

- `market_context_high->unknown_1h` score `10166.2612` n `126` status `ready` deltaP `1.7632` edge `847.1965` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `6410.0829` n `123` status `ready` deltaP `0.6605` edge `534.1976` maxDD `-0.6076`
- `market_context_high->crypto_major_24h` score `4.8683` n `107` status `ready` deltaP `27.4257` edge `1.1543` maxDD `-50.7065`
- `market_context_high->crypto_alt_24h` score `1.6343` n `107` status `ready` deltaP `14.3156` edge `0.9528` maxDD `-66.63`
- `market_context_high->metal_1h` score `-0.168` n `126` status `ready` deltaP `4.4007` edge `0.0156` maxDD `-2.6517`
- `market_context_high->metal_4h` score `-0.2704` n `123` status `ready` deltaP `13.2622` edge `0.0415` maxDD `-8.8336`
- `market_context_high->index_1h` score `-0.2905` n `126` status `ready` deltaP `3.1579` edge `0.0029` maxDD `-1.2295`
- `market_context_high->fx_1h` score `-1.3963` n `126` status `ready` deltaP `-8.8062` edge `-0.0017` maxDD `-0.4757`
- `market_context_high->equity_1h` score `-1.8407` n `126` status `ready` deltaP `5.988` edge `0.0126` maxDD `-13.1399`
- `market_context_high->fx_4h` score `-2.0271` n `123` status `ready` deltaP `-8.6382` edge `-0.0007` maxDD `-1.794`
- `market_context_high->index_4h` score `-2.1497` n `123` status `ready` deltaP `-2.6931` edge `-0.013` maxDD `-5.8552`
- `market_context_high->commodity_1h` score `-2.1828` n `126` status `ready` deltaP `-7.3235` edge `-0.0199` maxDD `-4.3877`
- `market_context_high->crypto_major_1h` score `-2.4954` n `126` status `ready` deltaP `2.2597` edge `0.0088` maxDD `-13.8788`
- `market_context_high->crypto_major_4h` score `-2.5644` n `123` status `ready` deltaP `1.5752` edge `0.2014` maxDD `-36.254`
- `market_context_high->crypto_alt_1h` score `-3.09` n `126` status `ready` deltaP `-3.4455` edge `-0.0068` maxDD `-13.8848`
- `market_context_high->crypto_alt_4h` score `-3.269` n `123` status `ready` deltaP `2.6423` edge `0.1235` maxDD `-37.8171`
- `market_context_high->metal_24h` score `-5.7202` n `107` status `ready` deltaP `13.2139` edge `0.1082` maxDD `-43.8379`
- `market_context_high->fx_24h` score `-6.7318` n `107` status `ready` deltaP `-18.4466` edge `-0.0107` maxDD `-5.5179`
- `market_context_high->commodity_4h` score `-6.984` n `123` status `ready` deltaP `-21.1382` edge `-0.0718` maxDD `-15.5426`
- `market_context_high->index_24h` score `-13.0474` n `107` status `ready` deltaP `-26.3369` edge `-0.1618` maxDD `-30.9921`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
