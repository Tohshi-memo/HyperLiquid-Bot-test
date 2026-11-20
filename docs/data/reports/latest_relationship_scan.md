# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-20T23:07:24.966666+00:00`
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

- `market_context_high->unknown_1h` score `10128.7157` n `126` status `ready` deltaP `1.4638` edge `844.0697` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `6178.7637` n `126` status `ready` deltaP `-0.3145` edge `514.9296` maxDD `-0.7759`
- `market_context_high->crypto_major_24h` score `3.4373` n `108` status `ready` deltaP `26.794` edge `1.0688` maxDD `-57.8734`
- `market_context_high->metal_1h` score `-0.2124` n `126` status `ready` deltaP `3.6522` edge `0.0149` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.2656` n `126` status `ready` deltaP `3.4573` edge `0.0041` maxDD `-1.2295`
- `market_context_high->metal_4h` score `-0.4925` n `126` status `ready` deltaP `12.1007` edge `0.0368` maxDD `-10.1161`
- `market_context_high->crypto_alt_24h` score `-0.8155` n `108` status `ready` deltaP `13.8311` edge `0.8299` maxDD `-72.5383`
- `market_context_high->fx_1h` score `-1.3843` n `126` status `ready` deltaP `-8.6565` edge `-0.0017` maxDD `-0.4757`
- `market_context_high->equity_1h` score `-1.8718` n `126` status `ready` deltaP `5.3892` edge `0.014` maxDD `-13.1399`
- `market_context_high->fx_4h` score `-1.9887` n `126` status `ready` deltaP `-7.9462` edge `-0.0004` maxDD `-1.794`
- `market_context_high->index_4h` score `-2.2608` n `126` status `ready` deltaP `-1.9648` edge `-0.012` maxDD `-7.0639`
- `market_context_high->commodity_1h` score `-2.2619` n `126` status `ready` deltaP `-7.9223` edge `-0.0225` maxDD `-4.3877`
- `market_context_high->crypto_major_1h` score `-2.5411` n `126` status `ready` deltaP `2.4094` edge `0.004` maxDD `-13.8788`
- `market_context_high->crypto_alt_1h` score `-3.2555` n `126` status `ready` deltaP `-3.7449` edge `-0.0186` maxDD `-13.8848`
- `market_context_high->crypto_major_4h` score `-4.2754` n `126` status `ready` deltaP `0.4161` edge `0.142` maxDD `-47.4317`
- `market_context_high->metal_24h` score `-5.6858` n `108` status `ready` deltaP `12.963` edge `0.1291` maxDD `-45.1471`
- `market_context_high->fx_24h` score `-6.8885` n `108` status `ready` deltaP `-20.2546` edge `-0.0117` maxDD `-5.5179`
- `market_context_high->commodity_4h` score `-7.0126` n `126` status `ready` deltaP `-20.3397` edge `-0.0795` maxDD `-15.5426`
- `market_context_high->crypto_alt_4h` score `-7.3544` n `126` status `ready` deltaP `0.721` edge `0.0636` maxDD `-46.5016`
- `market_context_high->index_24h` score `-12.9636` n `108` status `ready` deltaP `-26.3888` edge `-0.1414` maxDD `-31.7046`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
