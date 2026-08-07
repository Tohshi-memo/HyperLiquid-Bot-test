# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-07T17:22:29.452275+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11773`

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

- `market_context_high->metal_24h` score `2.7076` n `100` status `ready` deltaP `11.7648` edge `0.2048` maxDD `-2.2743`
- `market_context_high->fx_24h` score `0.7277` n `100` status `ready` deltaP `23.2521` edge `0.0494` maxDD `-3.5557`
- `market_context_high->commodity_4h` score `0.5243` n `109` status `ready` deltaP `11.0078` edge `0.0738` maxDD `-2.7309`
- `market_context_high->commodity_1h` score `0.3333` n `121` status `ready` deltaP `8.8991` edge `0.025` maxDD `-1.3282`
- `market_context_high->index_24h` score `0.2059` n `100` status `ready` deltaP `5.4552` edge `0.1321` maxDD `-5.7715`
- `market_context_high->fx_4h` score `0.1082` n `109` status `ready` deltaP `9.3113` edge `0.0056` maxDD `-1.6928`
- `market_context_high->fx_1h` score `-0.2101` n `121` status `ready` deltaP `5.1443` edge `-0.0052` maxDD `-1.0616`
- `market_context_high->index_1h` score `-0.7872` n `121` status `ready` deltaP `-1.8978` edge `-0.0108` maxDD `-1.3721`
- `market_context_high->index_4h` score `-0.788` n `109` status `ready` deltaP `-2.4349` edge `-0.0144` maxDD `-1.9645`
- `market_context_high->crypto_alt_1h` score `-0.8498` n `121` status `ready` deltaP `-5.2098` edge `-0.0113` maxDD `-2.3669`
- `market_context_high->metal_4h` score `-0.8586` n `109` status `ready` deltaP `2.9397` edge `0.0046` maxDD `-2.3265`
- `market_context_high->metal_1h` score `-0.9223` n `121` status `ready` deltaP `-3.5507` edge `-0.0078` maxDD `-0.9646`
- `market_context_high->equity_24h` score `-1.0985` n `100` status `ready` deltaP `-6.22` edge `0.3662` maxDD `-26.6355`
- `market_context_high->equity_1h` score `-1.2361` n `121` status `ready` deltaP `2.9173` edge `-0.0329` maxDD `-9.6016`
- `market_context_high->crypto_alt_4h` score `-1.8557` n `109` status `ready` deltaP `1.3874` edge `-0.0249` maxDD `-5.7857`
- `market_context_high->crypto_major_1h` score `-2.8406` n `121` status `ready` deltaP `-6.7254` edge `-0.0555` maxDD `-7.5769`
- `market_context_high->equity_4h` score `-2.9338` n `109` status `ready` deltaP `3.9956` edge `-0.1436` maxDD `-17.7337`
- `market_context_high->crypto_major_24h` score `-3.92` n `100` status `ready` deltaP `-1.3909` edge `-0.2061` maxDD `-16.3088`
- `market_context_high->crypto_alt_24h` score `-4.1319` n `100` status `ready` deltaP `-13.7733` edge `-0.1082` maxDD `-4.5445`
- `market_context_high->crypto_major_4h` score `-4.434` n `109` status `ready` deltaP `-7.6485` edge `-0.1831` maxDD `-20.4169`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
