# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-19T08:07:37.535667+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2552`

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

- `market_context_high->unknown_1h` score `11500.6938` n `112` status `ready` deltaP `1.1175` edge `958.4035` maxDD `-0.9174`
- `market_context_high->unknown_4h` score `7587.0936` n `106` status `ready` deltaP `0.2272` edge `632.2847` maxDD `-0.6067`
- `market_context_high->crypto_major_24h` score `12.5207` n `98` status `ready` deltaP `39.594` edge `1.6683` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `10.5889` n `98` status `ready` deltaP `22.8777` edge `1.4174` maxDD `-13.3222`
- `market_context_high->metal_1h` score `-0.2435` n `112` status `ready` deltaP `3.2934` edge `0.0133` maxDD `-2.6517`
- `market_context_high->metal_24h` score `-0.2629` n `98` status `ready` deltaP `15.3557` edge `0.1982` maxDD `-15.7982`
- `market_context_high->metal_4h` score `-0.387` n `106` status `ready` deltaP `12.6237` edge `0.0146` maxDD `-6.1475`
- `market_context_high->crypto_major_4h` score `-0.504` n `106` status `ready` deltaP `-0.5062` edge `0.297` maxDD `-22.3259`
- `market_context_high->crypto_alt_4h` score `-0.6799` n `106` status `ready` deltaP `0.742` edge `0.1889` maxDD `-17.1476`
- `market_context_high->crypto_major_1h` score `-0.8163` n `112` status `ready` deltaP `2.6946` edge `0.0641` maxDD `-10.2705`
- `market_context_high->index_1h` score `-0.8222` n `112` status `ready` deltaP `-1.4703` edge `0.0031` maxDD `-1.2295`
- `market_context_high->crypto_alt_1h` score `-1.0299` n `112` status `ready` deltaP `-1.4756` edge `0.0281` maxDD `-7.6911`
- `market_context_high->fx_1h` score `-1.3806` n `112` status `ready` deltaP `-8.9019` edge `-0.0008` maxDD `-0.392`
- `market_context_high->index_4h` score `-2.2578` n `106` status `ready` deltaP `-6.6613` edge `-0.0094` maxDD `-4.7471`
- `market_context_high->commodity_1h` score `-2.5486` n `112` status `ready` deltaP `-11.5911` edge `-0.0273` maxDD `-3.9584`
- `market_context_high->equity_1h` score `-2.754` n `112` status `ready` deltaP `1.358` edge `-0.0208` maxDD `-11.0868`
- `market_context_high->fx_4h` score `-4.0493` n `106` status `ready` deltaP `-18.937` edge `-0.0069` maxDD `-2.0104`
- `market_context_high->fx_24h` score `-6.616` n `98` status `ready` deltaP `-17.5985` edge `-0.0031` maxDD `-5.8059`
- `market_context_high->commodity_4h` score `-7.2712` n `106` status `ready` deltaP `-22.2043` edge `-0.0985` maxDD `-14.7522`
- `market_context_high->index_24h` score `-9.1467` n `98` status `ready` deltaP `-16.7694` edge `-0.1082` maxDD `-20.7114`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
