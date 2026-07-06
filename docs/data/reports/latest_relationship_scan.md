# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-06T14:07:40.438848+00:00`
- Price records: `672`
- Market context records: `5885`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10248`

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

- `news_risk_high->fx_4h` score `3.7618` n `30` status `ready` deltaP `39.2378` edge `0.0565` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.0501` n `30` status `ready` deltaP `24.8303` edge `0.0192` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.216` n `229` status `ready` deltaP `7.8389` edge `0.1591` maxDD `-4.1352`
- `news_risk_high->crypto_major_1h` score `0.9439` n `30` status `ready` deltaP `11.5369` edge `0.0908` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.27` n `30` status `ready` deltaP `5.1697` edge `0.0463` maxDD `-1.6923`
- `market_context_high->equity_1h` score `-0.1031` n `232` status `ready` deltaP `5.446` edge `0.0431` maxDD `-4.4103`
- `market_context_high->metal_1h` score `-0.308` n `232` status `ready` deltaP `3.376` edge `0.0051` maxDD `-2.0339`
- `news_risk_high->metal_1h` score `-0.4274` n `30` status `ready` deltaP `1.5369` edge `-0.0284` maxDD `-1.2643`
- `market_context_high->crypto_major_1h` score `-0.4606` n `232` status `ready` deltaP `4.2381` edge `0.0448` maxDD `-6.2348`
- `market_context_high->commodity_1h` score `-0.5219` n `232` status `ready` deltaP `-1.2028` edge `-0.0018` maxDD `-1.9006`
- `market_context_high->crypto_alt_1h` score `-0.5352` n `232` status `ready` deltaP `3.2444` edge `0.0432` maxDD `-6.6758`
- `market_context_high->index_1h` score `-0.5507` n `232` status `ready` deltaP `1.3163` edge `0.0054` maxDD `-0.7819`
- `market_context_high->fx_1h` score `-0.7888` n `232` status `ready` deltaP `-2.3823` edge `-0.001` maxDD `-0.5751`
- `news_risk_high->index_1h` score `-1.272` n `30` status `ready` deltaP `-12.994` edge `-0.025` maxDD `-1.1161`
- `market_context_high->crypto_major_4h` score `-1.6256` n `229` status `ready` deltaP `8.9599` edge `0.1691` maxDD `-25.6458`
- `news_risk_high->commodity_4h` score `-1.7873` n `30` status `ready` deltaP `-13.4248` edge `-0.0521` maxDD `-2.3372`
- `market_context_high->fx_24h` score `-1.8891` n `225` status `ready` deltaP `4.125` edge `0.0121` maxDD `-5.5435`
- `market_context_high->index_4h` score `-1.905` n `229` status `ready` deltaP `-0.5279` edge `0.0135` maxDD `-3.165`
- `news_risk_high->index_4h` score `-2.3016` n `30` status `ready` deltaP `-16.8598` edge `-0.0793` maxDD `-2.9371`
- `market_context_high->commodity_4h` score `-2.4283` n `229` status `ready` deltaP `-2.1002` edge `-0.017` maxDD `-6.3754`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
