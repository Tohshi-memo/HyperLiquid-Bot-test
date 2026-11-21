# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-21T05:37:30.336041+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2736`

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

- `market_context_high->unknown_1h` score `10096.1561` n `126` status `ready` deltaP `1.1643` edge `841.3584` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `6140.6181` n `126` status `ready` deltaP `-0.3145` edge `511.7508` maxDD `-0.7759`
- `market_context_high->crypto_major_24h` score `3.2579` n `108` status `ready` deltaP `26.794` edge `1.0458` maxDD `-57.8734`
- `market_context_high->metal_1h` score `-0.1999` n `126` status `ready` deltaP `3.8019` edge `0.0155` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.296` n `126` status `ready` deltaP `2.8585` edge `0.0042` maxDD `-1.2295`
- `market_context_high->metal_4h` score `-0.5432` n `126` status `ready` deltaP `11.1861` edge `0.0364` maxDD `-10.1161`
- `market_context_high->fx_1h` score `-1.407` n `126` status `ready` deltaP `-8.9559` edge `-0.0016` maxDD `-0.4757`
- `market_context_high->equity_1h` score `-1.7927` n `126` status `ready` deltaP `5.6886` edge `0.0186` maxDD `-13.1399`
- `market_context_high->fx_4h` score `-1.9539` n `126` status `ready` deltaP `-7.3364` edge `0.0` maxDD `-1.794`
- `market_context_high->crypto_alt_24h` score `-2.0299` n `108` status `ready` deltaP `13.8311` edge `0.7287` maxDD `-72.5383`
- `market_context_high->commodity_1h` score `-2.232` n `126` status `ready` deltaP `-7.6229` edge `-0.022` maxDD `-4.3877`
- `market_context_high->crypto_major_1h` score `-2.3551` n `126` status `ready` deltaP `2.7088` edge `0.0175` maxDD `-13.8788`
- `market_context_high->index_4h` score `-2.3873` n `126` status `ready` deltaP `-3.3367` edge `-0.0134` maxDD `-7.0639`
- `market_context_high->crypto_alt_1h` score `-3.0767` n `126` status `ready` deltaP `-3.7449` edge `-0.0037` maxDD `-13.8848`
- `market_context_high->crypto_major_4h` score `-4.2956` n `126` status `ready` deltaP `-0.4985` edge `0.1455` maxDD `-47.4317`
- `market_context_high->metal_24h` score `-5.8343` n `108` status `ready` deltaP `12.4422` edge `0.1202` maxDD `-45.1471`
- `market_context_high->fx_24h` score `-6.5632` n `108` status `ready` deltaP `-16.6088` edge `-0.0089` maxDD `-5.5179`
- `market_context_high->commodity_4h` score `-6.8968` n `126` status `ready` deltaP `-18.9677` edge `-0.079` maxDD `-15.5426`
- `market_context_high->crypto_alt_4h` score `-7.4125` n `126` status `ready` deltaP `-0.6509` edge `0.0679` maxDD `-46.5016`
- `market_context_high->index_24h` score `-12.7068` n `108` status `ready` deltaP `-26.3888` edge `-0.12` maxDD `-31.7046`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
