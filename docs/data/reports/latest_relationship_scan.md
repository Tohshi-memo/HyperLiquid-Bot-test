# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-24T23:52:31.709783+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7158`

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

- `market_context_high->unknown_4h` score `21.9797` n `97` status `ready` deltaP `2.0666` edge `1.8514` maxDD `-1.016`
- `market_context_high->commodity_24h` score `1.7444` n `59` status `ready` deltaP `23.3198` edge `0.0808` maxDD `-3.6055`
- `market_context_high->commodity_4h` score `0.8624` n `97` status `ready` deltaP `11.4141` edge `0.052` maxDD `-1.165`
- `market_context_high->commodity_1h` score `-0.0347` n `107` status `ready` deltaP `5.4718` edge `0.0107` maxDD `-1.0053`
- `market_context_high->fx_1h` score `-0.3131` n `107` status `ready` deltaP `0.957` edge `0.003` maxDD `-0.1712`
- `market_context_high->fx_4h` score `-0.8831` n `97` status `ready` deltaP `-2.6653` edge `0.0048` maxDD `-0.5168`
- `market_context_high->index_1h` score `-1.0236` n `107` status `ready` deltaP `-1.9965` edge `-0.0068` maxDD `-1.2155`
- `market_context_high->metal_1h` score `-1.0524` n `107` status `ready` deltaP `-0.3862` edge `-0.0057` maxDD `-1.6873`
- `market_context_high->fx_24h` score `-2.0093` n `59` status `ready` deltaP `-6.4795` edge `-0.0028` maxDD `-1.7158`
- `market_context_high->crypto_major_1h` score `-2.6875` n `107` status `ready` deltaP `-0.88` edge `-0.0439` maxDD `-10.6022`
- `market_context_high->crypto_major_24h` score `-2.9732` n `59` status `ready` deltaP `-3.6253` edge `-0.0858` maxDD `-17.0302`
- `market_context_high->metal_4h` score `-3.4957` n `97` status `ready` deltaP `-12.0757` edge `-0.0319` maxDD `-5.979`
- `market_context_high->metal_24h` score `-3.6021` n `59` status `ready` deltaP `-11.9615` edge `0.0129` maxDD `-7.3331`
- `market_context_high->crypto_alt_1h` score `-3.627` n `107` status `ready` deltaP `-1.8468` edge `-0.0645` maxDD `-14.7016`
- `market_context_high->equity_1h` score `-4.0291` n `107` status `ready` deltaP `-1.1347` edge `-0.0953` maxDD `-12.6316`
- `market_context_high->index_4h` score `-5.0641` n `97` status `ready` deltaP `-25.3819` edge `-0.0531` maxDD `-5.3093`
- `market_context_high->index_24h` score `-7.8912` n `59` status `ready` deltaP `-37.7884` edge `-0.1727` maxDD `-6.9714`
- `market_context_high->unknown_1h` score `-8.1865` n `107` status `ready` deltaP `-0.1973` edge `-0.632` maxDD `-1.5781`
- `market_context_high->crypto_alt_24h` score `-9.6303` n `59` status `ready` deltaP `-0.8063` edge `-0.3867` maxDD `-58.7397`
- `market_context_high->crypto_major_4h` score `-14.48` n `97` status `ready` deltaP `-25.5344` edge `-0.3675` maxDD `-45.1819`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
