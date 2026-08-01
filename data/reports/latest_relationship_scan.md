# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-01T22:10:13.932861+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5932`

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

- `news_risk_high->unknown_24h` score `5188.5913` n `60` status `ready` deltaP `31.2882` edge `432.2161` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `17.7719` n `53` status `ready` deltaP `57.9641` edge `1.1343` maxDD `-2.1786`
- `news_risk_high->equity_4h` score `4.8645` n `68` status `ready` deltaP `17.1359` edge `0.3675` maxDD `-3.4427`
- `market_context_high->commodity_24h` score `1.7688` n `53` status `ready` deltaP `27.4844` edge `0.2294` maxDD `-10.2019`
- `news_risk_high->index_4h` score `1.7281` n `68` status `ready` deltaP `16.5261` edge `0.0719` maxDD `-0.3783`
- `market_context_high->crypto_alt_4h` score `0.7884` n `53` status `ready` deltaP `9.9575` edge `0.1304` maxDD `-5.323`
- `news_risk_high->equity_1h` score `0.6708` n `68` status `ready` deltaP `9.4928` edge `0.0749` maxDD `-2.916`
- `market_context_high->fx_4h` score `0.2145` n `53` status `ready` deltaP `13.7109` edge `0.0157` maxDD `-1.3685`
- `news_risk_high->metal_4h` score `0.1281` n `68` status `ready` deltaP `5.165` edge `0.0296` maxDD `-0.8085`
- `news_risk_high->crypto_alt_1h` score `0.1077` n `68` status `ready` deltaP `6.3315` edge `0.0398` maxDD `-3.1233`
- `market_context_high->fx_24h` score `-0.0356` n `53` status `ready` deltaP `7.5798` edge `0.0429` maxDD `-2.506`
- `market_context_high->fx_1h` score `-0.0401` n `53` status `ready` deltaP `6.9032` edge `0.0009` maxDD `-0.6874`
- `news_risk_high->fx_4h` score `-0.0479` n `68` status `ready` deltaP `10.4645` edge `0.022` maxDD `-0.6604`
- `news_risk_high->index_1h` score `-0.0528` n `68` status `ready` deltaP `2.6154` edge `0.0081` maxDD `-0.5845`
- `market_context_high->commodity_1h` score `-0.0675` n `53` status `ready` deltaP `4.3272` edge `0.0166` maxDD `-1.3282`
- `news_risk_high->fx_1h` score `-0.1276` n `68` status `ready` deltaP `1.77` edge `0.0041` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.152` n `68` status `ready` deltaP `2.1663` edge `0.0064` maxDD `-0.5599`
- `news_risk_high->crypto_major_1h` score `-0.2124` n `68` status `ready` deltaP `1.9197` edge `0.032` maxDD `-3.762`
- `market_context_high->commodity_4h` score `-0.3063` n `53` status `ready` deltaP `2.81` edge `0.0295` maxDD `-3.0005`
- `market_context_high->crypto_alt_1h` score `-0.6035` n `53` status `ready` deltaP `-4.2679` edge `0.0138` maxDD `-3.0178`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
