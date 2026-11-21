# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-21T08:07:35.680783+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2674`

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

- `market_context_high->unknown_1h` score `10061.3165` n `126` status `ready` deltaP `1.1643` edge `838.4551` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `6136.6197` n `126` status `ready` deltaP `-0.3145` edge `511.4176` maxDD `-0.7759`
- `market_context_high->crypto_major_24h` score `3.6916` n `108` status `ready` deltaP `26.794` edge `1.1014` maxDD `-57.8734`
- `market_context_high->metal_1h` score `-0.1805` n `126` status `ready` deltaP `4.251` edge `0.015` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.3232` n `126` status `ready` deltaP `2.4094` edge `0.0037` maxDD `-1.2295`
- `market_context_high->metal_4h` score `-0.5061` n `126` status `ready` deltaP `11.7958` edge `0.0371` maxDD `-10.1161`
- `market_context_high->fx_1h` score `-1.3771` n `126` status `ready` deltaP `-8.6565` edge `-0.0011` maxDD `-0.4757`
- `market_context_high->equity_1h` score `-1.8371` n `126` status `ready` deltaP `5.8383` edge `0.0139` maxDD `-13.1399`
- `market_context_high->crypto_alt_24h` score `-1.8631` n `108` status `ready` deltaP `13.8311` edge `0.7426` maxDD `-72.5383`
- `market_context_high->fx_4h` score `-1.9184` n `126` status `ready` deltaP `-6.8791` edge `0.0015` maxDD `-1.794`
- `market_context_high->commodity_1h` score `-2.1781` n `126` status `ready` deltaP `-7.0241` edge `-0.0215` maxDD `-4.3877`
- `market_context_high->index_4h` score `-2.3629` n `126` status `ready` deltaP `-3.0318` edge `-0.0134` maxDD `-7.0639`
- `market_context_high->crypto_major_1h` score `-2.5315` n `126` status `ready` deltaP `2.8585` edge `0.0018` maxDD `-13.8788`
- `market_context_high->crypto_alt_1h` score `-3.2363` n `126` status `ready` deltaP `-3.8946` edge `-0.016` maxDD `-13.8848`
- `market_context_high->crypto_major_4h` score `-4.221` n `126` status `ready` deltaP `-0.8034` edge `0.1571` maxDD `-47.4317`
- `market_context_high->metal_24h` score `-5.8703` n `108` status `ready` deltaP `12.4422` edge `0.1172` maxDD `-45.1471`
- `market_context_high->fx_24h` score `-6.3883` n `108` status `ready` deltaP `-14.8727` edge `-0.0059` maxDD `-5.5179`
- `market_context_high->commodity_4h` score `-6.8042` n `126` status `ready` deltaP `-17.9007` edge `-0.0784` maxDD `-15.5426`
- `market_context_high->crypto_alt_4h` score `-7.3999` n `126` status `ready` deltaP `-1.1082` edge `0.072` maxDD `-46.5016`
- `market_context_high->index_24h` score `-12.612` n `108` status `ready` deltaP `-26.3888` edge `-0.1121` maxDD `-31.7046`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
