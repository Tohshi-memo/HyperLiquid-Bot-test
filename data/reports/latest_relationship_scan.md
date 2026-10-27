# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-27T00:07:27.054069+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7985`

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

- `market_context_high->unknown_4h` score `90.1251` n `153` status `ready` deltaP `1.0172` edge `7.5372` maxDD `-1.0178`
- `market_context_high->unknown_1h` score `20.8908` n `153` status `ready` deltaP `1.6242` edge `1.779` maxDD `-1.5807`
- `market_context_high->fx_1h` score `0.2782` n `153` status `ready` deltaP `8.4145` edge `0.0029` maxDD `-0.1986`
- `market_context_high->metal_24h` score `0.2166` n `112` status `ready` deltaP `23.4154` edge `0.1343` maxDD `-7.0108`
- `market_context_high->fx_4h` score `0.2054` n `153` status `ready` deltaP `10.2393` edge `0.0087` maxDD `-0.4545`
- `market_context_high->index_24h` score `-0.0613` n `112` status `ready` deltaP `15.9585` edge `0.0096` maxDD `-4.5747`
- `market_context_high->fx_24h` score `-0.1289` n `112` status `ready` deltaP `17.1453` edge `0.0264` maxDD `-1.2451`
- `market_context_high->metal_1h` score `-0.1338` n `153` status `ready` deltaP `8.3304` edge `0.0065` maxDD `-1.6682`
- `market_context_high->commodity_1h` score `-0.2306` n `153` status `ready` deltaP `2.452` edge `0.0145` maxDD `-1.0053`
- `market_context_high->commodity_4h` score `-0.3717` n `153` status `ready` deltaP `6.3636` edge `0.0495` maxDD `-1.165`
- `market_context_high->index_1h` score `-0.6179` n `153` status `ready` deltaP `-0.5861` edge `-0.0016` maxDD `-1.8971`
- `market_context_high->crypto_major_1h` score `-0.8475` n `153` status `ready` deltaP `4.8325` edge `0.0172` maxDD `-9.3126`
- `market_context_high->metal_4h` score `-0.921` n `153` status `ready` deltaP `7.9697` edge `-0.0002` maxDD `-5.3474`
- `market_context_high->equity_1h` score `-1.8509` n `153` status `ready` deltaP `0.7064` edge `-0.0144` maxDD `-12.2088`
- `market_context_high->crypto_alt_1h` score `-1.9757` n `153` status `ready` deltaP `-0.2759` edge `-0.003` maxDD `-13.2099`
- `market_context_high->index_4h` score `-3.3837` n `153` status `ready` deltaP `-6.0796` edge `-0.0238` maxDD `-6.7447`
- `market_context_high->crypto_major_4h` score `-4.5355` n `153` status `ready` deltaP `0.1514` edge `-0.0785` maxDD `-32.9851`
- `market_context_high->crypto_major_24h` score `-4.5945` n `112` status `ready` deltaP `-3.1381` edge `-0.0824` maxDD `-29.1905`
- `market_context_high->commodity_24h` score `-5.9471` n `112` status `ready` deltaP `-12.9178` edge `-0.1174` maxDD `-24.0477`
- `market_context_high->equity_24h` score `-6.9142` n `112` status `ready` deltaP `-7.5498` edge `-0.2928` maxDD `-35.4638`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
