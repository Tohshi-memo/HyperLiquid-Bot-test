# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-18T21:37:25.458726+00:00`
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

- `market_context_high->unknown_24h` score `1368.9474` n `98` status `ready` deltaP `4.6875` edge `114.0477` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `13.3537` n `98` status `ready` deltaP `39.594` edge `1.7751` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `11.4065` n `98` status `ready` deltaP `24.4402` edge `1.5118` maxDD `-13.3222`
- `market_context_high->metal_1h` score `-0.3473` n `98` status `ready` deltaP `1.1304` edge `0.0081` maxDD `-2.1461`
- `market_context_high->metal_24h` score `-0.3937` n `98` status `ready` deltaP `15.3557` edge `0.1873` maxDD `-15.7982`
- `market_context_high->metal_4h` score `-0.5886` n `98` status `ready` deltaP `11.6196` edge `0.0042` maxDD `-6.1238`
- `market_context_high->crypto_alt_4h` score `-0.6579` n `98` status `ready` deltaP `1.0297` edge `0.1898` maxDD `-17.1476`
- `market_context_high->index_1h` score `-0.9032` n `98` status `ready` deltaP `-2.6244` edge `0.0004` maxDD `-1.2295`
- `market_context_high->crypto_major_4h` score `-0.9739` n `98` status `ready` deltaP `-1.7733` edge `0.2452` maxDD `-22.3259`
- `market_context_high->crypto_alt_1h` score `-1.1292` n `98` status `ready` deltaP `-1.5092` edge `0.0156` maxDD `-7.6911`
- `market_context_high->fx_1h` score `-1.3544` n `98` status `ready` deltaP `-8.5971` edge `-0.0009` maxDD `-0.3721`
- `market_context_high->crypto_major_1h` score `-1.873` n `98` status `ready` deltaP `0.4094` edge `0.0279` maxDD `-10.2705`
- `market_context_high->index_4h` score `-2.5234` n `98` status `ready` deltaP `-8.6921` edge `-0.018` maxDD `-4.7471`
- `market_context_high->equity_1h` score `-2.9188` n `98` status `ready` deltaP `1.1579` edge `-0.0332` maxDD `-11.0868`
- `market_context_high->commodity_1h` score `-2.9283` n `98` status `ready` deltaP `-15.8224` edge `-0.0338` maxDD `-3.7125`
- `market_context_high->fx_4h` score `-4.5206` n `98` status `ready` deltaP `-24.3871` edge `-0.0099` maxDD `-2.0058`
- `market_context_high->fx_24h` score `-6.7516` n `98` status `ready` deltaP `-18.8138` edge `-0.0063` maxDD `-5.8059`
- `market_context_high->commodity_4h` score `-7.4154` n `98` status `ready` deltaP `-24.0573` edge `-0.1115` maxDD `-14.6855`
- `market_context_high->index_24h` score `-9.0954` n `98` status `ready` deltaP `-16.2486` edge `-0.1074` maxDD `-20.7114`
- `market_context_high->equity_4h` score `-12.0135` n `98` status `ready` deltaP `-14.2764` edge `-0.2239` maxDD `-44.2305`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
