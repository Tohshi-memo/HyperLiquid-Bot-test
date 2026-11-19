# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-19T00:07:25.383565+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2262`

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

- `market_context_high->unknown_24h` score `1369.1847` n `98` status `ready` deltaP `5.2083` edge `114.064` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `13.275` n `98` status `ready` deltaP `39.594` edge `1.765` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `11.3262` n `98` status `ready` deltaP `24.4402` edge `1.5015` maxDD `-13.3222`
- `market_context_high->metal_24h` score `-0.3109` n `98` status `ready` deltaP `15.3557` edge `0.1942` maxDD `-15.7982`
- `market_context_high->metal_1h` score `-0.3738` n `98` status `ready` deltaP `0.831` edge `0.0067` maxDD `-2.1461`
- `market_context_high->metal_4h` score `-0.6116` n `98` status `ready` deltaP `11.4672` edge `0.0033` maxDD `-6.1238`
- `market_context_high->crypto_alt_4h` score `-0.7728` n `98` status `ready` deltaP `0.7248` edge `0.1771` maxDD `-17.1476`
- `market_context_high->index_1h` score `-0.9515` n `98` status `ready` deltaP `-3.3729` edge `-0.0008` maxDD `-1.2295`
- `market_context_high->crypto_major_4h` score `-1.0514` n `98` status `ready` deltaP `-2.0782` edge `0.2373` maxDD `-22.3259`
- `market_context_high->crypto_alt_1h` score `-1.2578` n `98` status `ready` deltaP `-2.2577` edge `0.0041` maxDD `-7.6911`
- `market_context_high->fx_1h` score `-1.4286` n `98` status `ready` deltaP `-9.4953` edge `-0.0011` maxDD `-0.3721`
- `market_context_high->crypto_major_1h` score `-2.0553` n `98` status `ready` deltaP `-0.1894` edge `0.0167` maxDD `-10.2705`
- `market_context_high->index_4h` score `-2.5816` n `98` status `ready` deltaP `-9.1494` edge `-0.0198` maxDD `-4.7471`
- `market_context_high->commodity_1h` score `-2.9259` n `98` status `ready` deltaP `-15.8224` edge `-0.0336` maxDD `-3.7125`
- `market_context_high->equity_1h` score `-3.1407` n `98` status `ready` deltaP `0.4094` edge `-0.0467` maxDD `-11.0868`
- `market_context_high->fx_4h` score `-4.6034` n `98` status `ready` deltaP `-25.3018` edge `-0.0107` maxDD `-2.0058`
- `market_context_high->fx_24h` score `-6.748` n `98` status `ready` deltaP `-18.8138` edge `-0.006` maxDD `-5.8059`
- `market_context_high->commodity_4h` score `-7.453` n `98` status `ready` deltaP `-24.3622` edge `-0.1126` maxDD `-14.6855`
- `market_context_high->index_24h` score `-9.0858` n `98` status `ready` deltaP `-16.2486` edge `-0.1066` maxDD `-20.7114`
- `market_context_high->equity_4h` score `-12.2649` n `98` status `ready` deltaP `-14.7337` edge `-0.2418` maxDD `-44.2305`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
