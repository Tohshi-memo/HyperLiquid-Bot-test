# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-18T16:22:30.262236+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2298`

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

- `market_context_high->unknown_24h` score `1365.2455` n `98` status `ready` deltaP `2.6042` edge `113.7531` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `14.1496` n `98` status `ready` deltaP `40.2884` edge `1.8725` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `12.4683` n `98` status `ready` deltaP `26.3499` edge `1.6352` maxDD `-13.3222`
- `market_context_high->metal_1h` score `-0.2484` n `98` status `ready` deltaP `2.7771` edge `0.0098` maxDD `-2.1461`
- `market_context_high->metal_24h` score `-0.5077` n `98` status `ready` deltaP `15.3557` edge `0.1778` maxDD `-15.7982`
- `market_context_high->crypto_alt_4h` score `-0.5232` n `98` status `ready` deltaP `1.6395` edge `0.203` maxDD `-17.1476`
- `market_context_high->metal_4h` score `-0.5318` n `98` status `ready` deltaP `11.9245` edge `0.0069` maxDD `-6.1238`
- `market_context_high->index_1h` score `-0.9133` n `98` status `ready` deltaP `-2.7741` edge `0.0001` maxDD `-1.2295`
- `market_context_high->crypto_major_4h` score `-1.0246` n `98` status `ready` deltaP `-1.7733` edge `0.2387` maxDD `-22.3259`
- `market_context_high->crypto_alt_1h` score `-1.1105` n `98` status `ready` deltaP `-1.3595` edge `0.017` maxDD `-7.6911`
- `market_context_high->fx_1h` score `-1.3436` n `98` status `ready` deltaP `-8.4474` edge `-0.001` maxDD `-0.3721`
- `market_context_high->crypto_major_1h` score `-1.9929` n `98` status `ready` deltaP `-0.3391` edge `0.0229` maxDD `-10.2705`
- `market_context_high->index_4h` score `-2.493` n `98` status `ready` deltaP `-8.3873` edge `-0.0175` maxDD `-4.7471`
- `market_context_high->commodity_1h` score `-2.812` n `98` status `ready` deltaP `-14.9242` edge `-0.0301` maxDD `-3.7125`
- `market_context_high->equity_1h` score `-2.9332` n `98` status `ready` deltaP `1.1579` edge `-0.0344` maxDD `-11.0868`
- `market_context_high->fx_4h` score `-4.5462` n `98` status `ready` deltaP `-24.692` edge `-0.01` maxDD `-2.0058`
- `market_context_high->fx_24h` score `-6.7732` n `98` status `ready` deltaP `-18.8138` edge `-0.0081` maxDD `-5.8059`
- `market_context_high->commodity_4h` score `-7.2131` n `98` status `ready` deltaP `-22.5329` edge `-0.1048` maxDD `-14.6855`
- `market_context_high->index_24h` score `-8.7686` n `98` status `ready` deltaP `-13.1236` edge `-0.101` maxDD `-20.7114`
- `market_context_high->equity_4h` score `-11.8569` n `98` status `ready` deltaP `-13.8191` edge `-0.2139` maxDD `-44.2305`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
