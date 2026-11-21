# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-21T14:22:24.283598+00:00`
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

- `market_context_high->unknown_1h` score `10010.6766` n `126` status `ready` deltaP `0.8649` edge `834.2371` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `6081.6819` n `126` status `ready` deltaP `-0.7719` edge `506.8425` maxDD `-0.7759`
- `market_context_high->metal_1h` score `-0.2288` n `126` status `ready` deltaP `3.5025` edge `0.0138` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.3598` n `126` status `ready` deltaP `1.8106` edge `0.003` maxDD `-1.2295`
- `market_context_high->metal_4h` score `-0.6772` n `126` status `ready` deltaP `9.5092` edge `0.0304` maxDD `-10.1161`
- `market_context_high->fx_1h` score `-1.4166` n `126` status `ready` deltaP `-9.1056` edge `-0.0014` maxDD `-0.4757`
- `market_context_high->fx_4h` score `-1.8614` n `126` status `ready` deltaP `-5.812` edge `0.0017` maxDD `-1.794`
- `market_context_high->equity_1h` score `-1.9942` n `126` status `ready` deltaP `4.7904` edge `0.0078` maxDD `-13.1399`
- `market_context_high->commodity_1h` score `-2.3074` n `126` status `ready` deltaP `-8.5211` edge `-0.0223` maxDD `-4.3877`
- `market_context_high->index_4h` score `-2.6342` n `126` status `ready` deltaP `-5.9282` edge `-0.0167` maxDD `-7.0639`
- `market_context_high->crypto_major_1h` score `-2.9753` n `126` status `ready` deltaP `1.0621` edge `-0.0232` maxDD `-13.8788`
- `market_context_high->crypto_alt_1h` score `-3.6272` n `126` status `ready` deltaP `-5.5413` edge `-0.0376` maxDD `-13.8848`
- `market_context_high->crypto_major_4h` score `-5.3916` n `126` status `ready` deltaP `-3.3948` edge `0.0243` maxDD `-47.4317`
- `market_context_high->fx_24h` score `-6.4641` n `125` status `ready` deltaP `-13.0681` edge `-0.0069` maxDD `-6.9055`
- `market_context_high->commodity_4h` score `-6.977` n `126` status `ready` deltaP `-19.7299` edge `-0.0806` maxDD `-15.5426`
- `market_context_high->metal_24h` score `-7.5139` n `125` status `ready` deltaP `8.7903` edge `0.1175` maxDD `-51.8475`
- `market_context_high->crypto_alt_4h` score `-9.011` n `126` status `ready` deltaP `-4.4619` edge `-0.0399` maxDD `-46.5016`
- `market_context_high->crypto_major_24h` score `-11.518` n `125` status `ready` deltaP `17.6014` edge `0.4317` maxDD `-149.7231`
- `market_context_high->crypto_alt_24h` score `-14.7561` n `125` status `ready` deltaP `6.7792` edge `0.1519` maxDD `-154.7791`
- `market_context_high->index_24h` score `-14.8229` n `125` status `ready` deltaP `-27.1444` edge `-0.1197` maxDD `-39.766`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
