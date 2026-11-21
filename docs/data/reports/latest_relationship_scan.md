# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-21T14:37:29.227263+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2590`

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

- `market_context_high->unknown_1h` score `10010.241` n `126` status `ready` deltaP `0.8649` edge `834.2008` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `6084.6027` n `126` status `ready` deltaP `-0.7719` edge `507.0859` maxDD `-0.7759`
- `market_context_high->metal_1h` score `-0.2288` n `126` status `ready` deltaP `3.5025` edge `0.0138` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.3598` n `126` status `ready` deltaP `1.8106` edge `0.003` maxDD `-1.2295`
- `market_context_high->metal_4h` score `-0.689` n `126` status `ready` deltaP `9.3568` edge `0.0299` maxDD `-10.1161`
- `market_context_high->fx_1h` score `-1.4286` n `126` status `ready` deltaP `-9.2553` edge `-0.0014` maxDD `-0.4757`
- `market_context_high->fx_4h` score `-1.8614` n `126` status `ready` deltaP `-5.812` edge `0.0017` maxDD `-1.794`
- `market_context_high->equity_1h` score `-1.9978` n `126` status `ready` deltaP `4.7904` edge `0.0075` maxDD `-13.1399`
- `market_context_high->commodity_1h` score `-2.3074` n `126` status `ready` deltaP `-8.5211` edge `-0.0223` maxDD `-4.3877`
- `market_context_high->index_4h` score `-2.65` n `126` status `ready` deltaP `-6.0806` edge `-0.017` maxDD `-7.0639`
- `market_context_high->crypto_major_1h` score `-2.9945` n `126` status `ready` deltaP `1.0621` edge `-0.0248` maxDD `-13.8788`
- `market_context_high->crypto_alt_1h` score `-3.674` n `126` status `ready` deltaP `-5.691` edge `-0.0405` maxDD `-13.8848`
- `market_context_high->crypto_major_4h` score `-5.476` n `126` status `ready` deltaP `-3.5473` edge `0.0145` maxDD `-47.4317`
- `market_context_high->fx_24h` score `-6.4913` n `126` status `ready` deltaP `-13.1697` edge `-0.0072` maxDD `-7.0088`
- `market_context_high->commodity_4h` score `-6.9916` n `126` status `ready` deltaP `-19.8824` edge `-0.0808` maxDD `-15.5426`
- `market_context_high->metal_24h` score `-7.6047` n `126` status `ready` deltaP `8.6062` edge `0.1185` maxDD `-52.1012`
- `market_context_high->crypto_alt_4h` score `-9.1336` n `126` status `ready` deltaP `-4.6143` edge `-0.0491` maxDD `-46.5016`
- `market_context_high->crypto_major_24h` score `-11.9048` n `126` status `ready` deltaP `17.1379` edge `0.4195` maxDD `-152.134`
- `market_context_high->index_24h` score `-14.9377` n `126` status `ready` deltaP `-27.1825` edge `-0.1198` maxDD `-40.1698`
- `market_context_high->crypto_alt_24h` score `-15.0781` n `126` status `ready` deltaP `6.4236` edge `0.1423` maxDD `-156.7906`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
