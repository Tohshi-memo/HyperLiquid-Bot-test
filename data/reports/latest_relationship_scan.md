# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-01T21:52:28.392658+00:00`
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

- `news_risk_high->unknown_24h` score `5188.6075` n `60` status `ready` deltaP `31.4615` edge `432.2163` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `17.7353` n `53` status `ready` deltaP `57.7908` edge `1.1324` maxDD `-2.1786`
- `news_risk_high->equity_4h` score `4.8645` n `68` status `ready` deltaP `17.1359` edge `0.3675` maxDD `-3.4427`
- `market_context_high->commodity_24h` score `1.7712` n `53` status `ready` deltaP `27.4844` edge `0.2297` maxDD `-10.2019`
- `news_risk_high->index_4h` score `1.7281` n `68` status `ready` deltaP `16.5261` edge `0.0719` maxDD `-0.3783`
- `market_context_high->crypto_alt_4h` score `0.7781` n `53` status `ready` deltaP `9.805` edge `0.1301` maxDD `-5.323`
- `news_risk_high->equity_1h` score `0.6768` n `68` status `ready` deltaP `9.4928` edge `0.0754` maxDD `-2.916`
- `market_context_high->fx_4h` score `0.2224` n `53` status `ready` deltaP `13.8633` edge `0.0157` maxDD `-1.3685`
- `news_risk_high->metal_4h` score `0.1289` n `68` status `ready` deltaP `5.165` edge `0.0297` maxDD `-0.8085`
- `news_risk_high->crypto_alt_1h` score `0.1186` n `68` status `ready` deltaP `6.4812` edge `0.0402` maxDD `-3.1233`
- `market_context_high->fx_1h` score `-0.0281` n `53` status `ready` deltaP `7.0529` edge `0.0009` maxDD `-0.6874`
- `news_risk_high->fx_4h` score `-0.0357` n `68` status `ready` deltaP `10.6169` edge `0.022` maxDD `-0.6604`
- `market_context_high->fx_24h` score `-0.0454` n `53` status `ready` deltaP `7.4065` edge `0.0428` maxDD `-2.506`
- `news_risk_high->index_1h` score `-0.052` n `68` status `ready` deltaP `2.6154` edge `0.0082` maxDD `-0.5845`
- `market_context_high->commodity_1h` score `-0.0683` n `53` status `ready` deltaP `4.3272` edge `0.0165` maxDD `-1.3282`
- `news_risk_high->fx_1h` score `-0.1198` n `68` status `ready` deltaP `1.9197` edge `0.0041` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.1435` n `68` status `ready` deltaP `2.316` edge `0.0065` maxDD `-0.5599`
- `news_risk_high->crypto_major_1h` score `-0.2015` n `68` status `ready` deltaP `2.0694` edge `0.0324` maxDD `-3.762`
- `market_context_high->commodity_4h` score `-0.3079` n `53` status `ready` deltaP `2.81` edge `0.0293` maxDD `-3.0005`
- `market_context_high->crypto_alt_1h` score `-0.5926` n `53` status `ready` deltaP `-4.1182` edge `0.0142` maxDD `-3.0178`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
