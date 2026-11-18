# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-18T20:22:24.322368+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2292`

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

- `market_context_high->unknown_24h` score `1367.5005` n `98` status `ready` deltaP `4.1667` edge `113.9306` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `13.4629` n `98` status `ready` deltaP `39.594` edge `1.7891` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `11.5399` n `98` status `ready` deltaP `24.4402` edge `1.5289` maxDD `-13.3222`
- `market_context_high->metal_1h` score `-0.3045` n `98` status `ready` deltaP `1.8789` edge `0.0086` maxDD `-2.1461`
- `market_context_high->metal_24h` score `-0.4309` n `98` status `ready` deltaP `15.3557` edge `0.1842` maxDD `-15.7982`
- `market_context_high->crypto_alt_4h` score `-0.5452` n `98` status `ready` deltaP `1.487` edge `0.2012` maxDD `-17.1476`
- `market_context_high->metal_4h` score `-0.5522` n `98` status `ready` deltaP `11.9245` edge `0.0052` maxDD `-6.1238`
- `market_context_high->index_1h` score `-0.8604` n `98` status `ready` deltaP `-1.8759` edge `0.0009` maxDD `-1.2295`
- `market_context_high->crypto_major_4h` score `-0.8926` n `98` status `ready` deltaP `-1.4684` edge `0.2536` maxDD `-22.3259`
- `market_context_high->crypto_alt_1h` score `-1.1346` n `98` status `ready` deltaP `-1.5092` edge `0.0149` maxDD `-7.6911`
- `market_context_high->fx_1h` score `-1.3544` n `98` status `ready` deltaP `-8.5971` edge `-0.0009` maxDD `-0.3721`
- `market_context_high->crypto_major_1h` score `-1.9222` n `98` status `ready` deltaP `0.11` edge `0.0258` maxDD `-10.2705`
- `market_context_high->index_4h` score `-2.4822` n `98` status `ready` deltaP `-8.3873` edge `-0.0166` maxDD `-4.7471`
- `market_context_high->equity_1h` score `-2.8133` n `98` status `ready` deltaP `1.7567` edge `-0.0284` maxDD `-11.0868`
- `market_context_high->commodity_1h` score `-2.9366` n `98` status `ready` deltaP `-15.9721` edge `-0.0335` maxDD `-3.7125`
- `market_context_high->fx_4h` score `-4.4817` n `98` status `ready` deltaP `-23.9298` edge `-0.0097` maxDD `-2.0058`
- `market_context_high->fx_24h` score `-6.754` n `98` status `ready` deltaP `-18.8138` edge `-0.0065` maxDD `-5.8059`
- `market_context_high->commodity_4h` score `-7.3464` n `98` status `ready` deltaP `-23.6` edge `-0.1088` maxDD `-14.6855`
- `market_context_high->index_24h` score `-9.0484` n `98` status `ready` deltaP `-15.9014` edge `-0.1058` maxDD `-20.7114`
- `market_context_high->equity_4h` score `-11.7885` n `98` status `ready` deltaP `-13.8191` edge `-0.2082` maxDD `-44.2305`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
