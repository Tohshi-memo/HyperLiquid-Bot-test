# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-18T20:37:28.990349+00:00`
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

- `market_context_high->unknown_24h` score `1367.6793` n `98` status `ready` deltaP `4.1667` edge `113.9455` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `13.438` n `98` status `ready` deltaP `39.594` edge `1.7859` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `11.5103` n `98` status `ready` deltaP `24.4402` edge `1.5251` maxDD `-13.3222`
- `market_context_high->metal_1h` score `-0.313` n `98` status `ready` deltaP `1.7292` edge `0.0085` maxDD `-2.1461`
- `market_context_high->metal_24h` score `-0.4249` n `98` status `ready` deltaP `15.3557` edge `0.1847` maxDD `-15.7982`
- `market_context_high->metal_4h` score `-0.5668` n `98` status `ready` deltaP `11.7721` edge `0.005` maxDD `-6.1238`
- `market_context_high->crypto_alt_4h` score `-0.5719` n `98` status `ready` deltaP `1.3346` edge `0.1988` maxDD `-17.1476`
- `market_context_high->index_1h` score `-0.869` n `98` status `ready` deltaP `-2.0256` edge `0.0008` maxDD `-1.2295`
- `market_context_high->crypto_major_4h` score `-0.9176` n `98` status `ready` deltaP `-1.6208` edge `0.2514` maxDD `-22.3259`
- `market_context_high->crypto_alt_1h` score `-1.1331` n `98` status `ready` deltaP `-1.5092` edge `0.0151` maxDD `-7.6911`
- `market_context_high->fx_1h` score `-1.3544` n `98` status `ready` deltaP `-8.5971` edge `-0.0009` maxDD `-0.3721`
- `market_context_high->crypto_major_1h` score `-1.9186` n `98` status `ready` deltaP `0.11` edge `0.0261` maxDD `-10.2705`
- `market_context_high->index_4h` score `-2.4992` n `98` status `ready` deltaP `-8.5397` edge `-0.017` maxDD `-4.7471`
- `market_context_high->equity_1h` score `-2.8397` n `98` status `ready` deltaP `1.607` edge `-0.0296` maxDD `-11.0868`
- `market_context_high->commodity_1h` score `-2.9402` n `98` status `ready` deltaP `-15.9721` edge `-0.0338` maxDD `-3.7125`
- `market_context_high->fx_4h` score `-4.4939` n `98` status `ready` deltaP `-24.0823` edge `-0.0097` maxDD `-2.0058`
- `market_context_high->fx_24h` score `-6.754` n `98` status `ready` deltaP `-18.8138` edge `-0.0065` maxDD `-5.8059`
- `market_context_high->commodity_4h` score `-7.3658` n `98` status `ready` deltaP `-23.7524` edge `-0.1094` maxDD `-14.6855`
- `market_context_high->index_24h` score `-9.0683` n `98` status `ready` deltaP `-16.075` edge `-0.1063` maxDD `-20.7114`
- `market_context_high->equity_4h` score `-11.8475` n `98` status `ready` deltaP `-13.9715` edge `-0.2121` maxDD `-44.2305`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
