# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-25T00:37:25.838908+00:00`
- Price records: `672`
- Market context records: `4674`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9870`

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

- `market_context_high->unknown_1h` score `74.7828` n `140` status `ready` deltaP `10.8084` edge `6.2016` maxDD `-1.674`
- `market_context_high->unknown_4h` score `4.5133` n `140` status `ready` deltaP `9.8171` edge `0.4317` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `1.4488` n `140` status `ready` deltaP `9.4147` edge `0.1503` maxDD `-4.7201`
- `market_context_high->commodity_1h` score `-0.5029` n `140` status `ready` deltaP `1.7836` edge `0.0258` maxDD `-2.0345`
- `market_context_high->fx_1h` score `-0.5767` n `140` status `ready` deltaP `-2.1557` edge `-0.0041` maxDD `-1.1038`
- `market_context_high->index_4h` score `-0.788` n `140` status `ready` deltaP `3.4277` edge `-0.0116` maxDD `-5.9823`
- `market_context_high->fx_4h` score `-0.8004` n `140` status `ready` deltaP `0.7534` edge `0.0006` maxDD `-1.9927`
- `market_context_high->equity_1h` score `-0.9007` n `140` status `ready` deltaP `-2.8914` edge `0.0025` maxDD `-5.5624`
- `market_context_high->equity_4h` score `-1.4019` n `140` status `ready` deltaP `0.4181` edge `-0.0056` maxDD `-8.8203`
- `market_context_high->index_1h` score `-1.7582` n `140` status `ready` deltaP `-4.8375` edge `-0.0134` maxDD `-2.7358`
- `market_context_high->commodity_4h` score `-2.0643` n `140` status `ready` deltaP `3.7848` edge `0.0135` maxDD `-9.1941`
- `market_context_high->metal_1h` score `-2.8161` n `140` status `ready` deltaP `-4.1146` edge `-0.0765` maxDD `-17.2348`
- `market_context_high->fx_24h` score `-4.8247` n `140` status `ready` deltaP `-10.5506` edge `-0.0107` maxDD `-5.6816`
- `market_context_high->commodity_24h` score `-4.9136` n `140` status `ready` deltaP `13.1349` edge `0.0534` maxDD `-30.7016`
- `market_context_high->crypto_alt_1h` score `-5.5608` n `140` status `ready` deltaP `-2.8914` edge `-0.1154` maxDD `-22.2982`
- `market_context_high->crypto_major_1h` score `-6.7137` n `140` status `ready` deltaP `-5.7143` edge `-0.1461` maxDD `-27.356`
- `market_context_high->index_24h` score `-7.8839` n `140` status `ready` deltaP `-8.626` edge `-0.062` maxDD `-29.3321`
- `market_context_high->crypto_alt_4h` score `-8.4592` n `140` status `ready` deltaP `-2.1429` edge `-0.2045` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-9.4019` n `140` status `ready` deltaP `-3.0923` edge `-0.2874` maxDD `-65.4549`
- `market_context_high->crypto_major_4h` score `-11.5798` n `140` status `ready` deltaP `-3.9329` edge `-0.364` maxDD `-82.2164`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
