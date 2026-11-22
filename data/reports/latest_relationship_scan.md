# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-22T06:22:25.870930+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `40`

- Symbol pattern count: `4564`

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

- `market_context_high->unknown_1h` score `10569.4822` n `118` status `ready` deltaP `0.6597` edge `880.8056` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `6473.8722` n `118` status `ready` deltaP `-1.1575` edge `539.5276` maxDD `-0.7759`
- `market_context_high->metal_1h` score `-0.1388` n `118` status `ready` deltaP `5.3385` edge `0.0131` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.3249` n `118` status `ready` deltaP `2.7936` edge `0.003` maxDD `-1.2295`
- `market_context_high->metal_4h` score `-0.9094` n `118` status `ready` deltaP `7.1285` edge `0.0165` maxDD `-10.1161`
- `market_context_high->fx_1h` score `-1.5768` n `118` status `ready` deltaP `-11.0626` edge `-0.0017` maxDD `-0.4757`
- `market_context_high->crypto_major_1h` score `-1.6506` n `118` status `ready` deltaP `1.9461` edge `-0.0136` maxDD `-13.8788`
- `market_context_high->fx_4h` score `-1.7359` n `118` status `ready` deltaP `-3.5836` edge `0.002` maxDD `-1.7192`
- `market_context_high->equity_1h` score `-1.7919` n `118` status `ready` deltaP `6.2341` edge `0.0067` maxDD `-13.1399`
- `market_context_high->commodity_1h` score `-2.4763` n `118` status `ready` deltaP `-10.3167` edge `-0.0244` maxDD `-4.3877`
- `market_context_high->index_4h` score `-2.8042` n `118` status `ready` deltaP `-7.2732` edge `-0.0219` maxDD `-7.0639`
- `market_context_high->crypto_alt_1h` score `-3.6663` n `118` status `ready` deltaP `-6.5792` edge `-0.0506` maxDD `-13.8848`
- `market_context_high->fx_24h` score `-5.5197` n `118` status `ready` deltaP `-7.4476` edge `-0.0014` maxDD `-6.7139`
- `market_context_high->crypto_major_4h` score `-5.5809` n `118` status `ready` deltaP `-3.5112` edge `0.0008` maxDD `-47.4317`
- `market_context_high->crypto_alt_4h` score `-6.1401` n `118` status `ready` deltaP `-3.6637` edge `-0.0815` maxDD `-46.5016`
- `market_context_high->commodity_4h` score `-6.8837` n `118` status `ready` deltaP `-18.4477` edge `-0.0833` maxDD `-15.3888`
- `market_context_high->metal_24h` score `-8.8167` n `118` status `ready` deltaP `-0.259` edge `0.0766` maxDD `-52.1012`
- `market_context_high->crypto_major_24h` score `-13.802` n `118` status `ready` deltaP `11.3141` edge `0.2151` maxDD `-152.134`
- `market_context_high->index_24h` score `-15.4382` n `118` status `ready` deltaP `-29.9023` edge `-0.144` maxDD `-40.1203`
- `market_context_high->crypto_alt_24h` score `-16.3605` n `118` status `ready` deltaP `3.4222` edge `-0.0021` maxDD `-156.7906`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
