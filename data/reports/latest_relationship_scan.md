# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-19T03:37:22.683753+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2450`

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

- `market_context_high->unknown_24h` score `1364.6355` n `98` status `ready` deltaP `5.2083` edge `113.6849` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `13.2906` n `98` status `ready` deltaP `39.594` edge `1.767` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `11.2973` n `98` status `ready` deltaP `24.4402` edge `1.4978` maxDD `-13.3222`
- `market_context_high->metal_24h` score `-0.2569` n `98` status `ready` deltaP `15.3557` edge `0.1987` maxDD `-15.7982`
- `market_context_high->metal_1h` score `-0.486` n `100` status `ready` deltaP `0.0419` edge `0.0035` maxDD `-2.6199`
- `market_context_high->metal_4h` score `-0.682` n `98` status `ready` deltaP `10.8574` edge `0.0015` maxDD `-6.1238`
- `market_context_high->crypto_alt_4h` score `-0.9761` n `98` status `ready` deltaP `-0.7996` edge `0.1612` maxDD `-17.1476`
- `market_context_high->crypto_major_4h` score `-1.2045` n `98` status `ready` deltaP `-3.2977` edge `0.2258` maxDD `-22.3259`
- `market_context_high->crypto_alt_1h` score `-1.226` n `100` status `ready` deltaP `-2.1557` edge `0.0075` maxDD `-7.6911`
- `market_context_high->crypto_major_1h` score `-1.2686` n `100` status `ready` deltaP `0.3413` edge `0.0218` maxDD `-10.2705`
- `market_context_high->index_1h` score `-1.434` n `100` status `ready` deltaP `-3.0599` edge `-0.0004` maxDD `-1.2295`
- `market_context_high->fx_1h` score `-1.4798` n `100` status `ready` deltaP `-10.0599` edge `-0.0014` maxDD `-0.3883`
- `market_context_high->index_4h` score `-2.6836` n `98` status `ready` deltaP `-10.0641` edge `-0.0222` maxDD `-4.7471`
- `market_context_high->commodity_1h` score `-2.9974` n `100` status `ready` deltaP `-16.1557` edge `-0.0349` maxDD `-3.9077`
- `market_context_high->equity_1h` score `-3.1257` n `100` status `ready` deltaP `0.1916` edge `-0.044` maxDD `-11.0868`
- `market_context_high->fx_4h` score `-4.6324` n `98` status `ready` deltaP `-25.4542` edge `-0.0121` maxDD `-2.0058`
- `market_context_high->fx_24h` score `-6.7432` n `98` status `ready` deltaP `-18.8138` edge `-0.0056` maxDD `-5.8059`
- `market_context_high->commodity_4h` score `-7.549` n `98` status `ready` deltaP `-25.2768` edge `-0.1145` maxDD `-14.6855`
- `market_context_high->index_24h` score `-9.0062` n `98` status `ready` deltaP `-15.5541` edge `-0.1046` maxDD `-20.7114`
- `market_context_high->equity_4h` score `-12.6734` n `98` status `ready` deltaP `-16.1057` edge `-0.2667` maxDD `-44.2305`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
