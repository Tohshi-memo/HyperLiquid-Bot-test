# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-19T06:37:26.510776+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2636`

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

- `market_context_high->unknown_1h` score `11504.0082` n `112` status `ready` deltaP `0.9678` edge `958.6807` maxDD `-0.9174`
- `market_context_high->unknown_4h` score `8141.7549` n `100` status `ready` deltaP `-0.2256` edge `678.5095` maxDD `-0.6067`
- `market_context_high->crypto_major_24h` score `12.7812` n `98` status `ready` deltaP `39.594` edge `1.7017` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `10.7837` n `98` status `ready` deltaP `23.3985` edge `1.4389` maxDD `-13.3222`
- `market_context_high->metal_24h` score `-0.2329` n `98` status `ready` deltaP `15.3557` edge `0.2007` maxDD `-15.7982`
- `market_context_high->metal_1h` score `-0.2342` n `112` status `ready` deltaP `3.4431` edge `0.0135` maxDD `-2.6517`
- `market_context_high->metal_4h` score `-0.7048` n `100` status `ready` deltaP `10.4817` edge `0.0024` maxDD `-6.1475`
- `market_context_high->index_1h` score `-0.77` n `112` status `ready` deltaP `-0.5721` edge `0.0038` maxDD `-1.2295`
- `market_context_high->crypto_major_1h` score `-0.7874` n `112` status `ready` deltaP `2.994` edge `0.0658` maxDD `-10.2705`
- `market_context_high->crypto_alt_1h` score `-0.9995` n `112` status `ready` deltaP `-1.1762` edge `0.03` maxDD `-7.6911`
- `market_context_high->crypto_alt_4h` score `-1.051` n `100` status `ready` deltaP `-1.4451` edge `0.1559` maxDD `-17.1476`
- `market_context_high->crypto_major_4h` score `-1.1984` n `100` status `ready` deltaP `-3.75` edge `0.2296` maxDD `-22.3259`
- `market_context_high->fx_1h` score `-1.3937` n `112` status `ready` deltaP `-9.0516` edge `-0.0009` maxDD `-0.392`
- `market_context_high->commodity_1h` score `-2.6134` n `112` status `ready` deltaP `-12.1899` edge `-0.0287` maxDD `-3.9584`
- `market_context_high->index_4h` score `-2.6825` n `100` status `ready` deltaP `-10.1707` edge `-0.0214` maxDD `-4.7471`
- `market_context_high->equity_1h` score `-2.7144` n `112` status `ready` deltaP `1.358` edge `-0.0175` maxDD `-11.0868`
- `market_context_high->fx_4h` score `-4.4844` n `100` status `ready` deltaP `-23.8049` edge `-0.0107` maxDD `-2.0104`
- `market_context_high->fx_24h` score `-6.6799` n `98` status `ready` deltaP `-18.293` edge `-0.0038` maxDD `-5.8059`
- `market_context_high->commodity_4h` score `-7.5218` n `100` status `ready` deltaP `-24.75` edge `-0.1072` maxDD `-14.7029`
- `market_context_high->index_24h` score `-9.0985` n `98` status `ready` deltaP `-16.4222` edge `-0.1065` maxDD `-20.7114`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
