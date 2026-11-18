# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-18T00:07:43.062736+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4173`

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

- `market_context_high->unknown_24h` score `1490.7294` n `98` status `ready` deltaP `3.4722` edge `124.2043` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `15.5851` n `98` status `ready` deltaP `47.0592` edge `2.0114` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `14.6109` n `98` status `ready` deltaP `32.9472` edge `1.8659` maxDD `-13.3222`
- `market_context_high->metal_1h` score `-0.5109` n `98` status `ready` deltaP `-0.9654` edge `0.0011` maxDD `-2.1461`
- `market_context_high->crypto_alt_4h` score `-0.8696` n `98` status `ready` deltaP `-1.2569` edge `0.1779` maxDD `-17.1476`
- `market_context_high->metal_24h` score `-0.9253` n `98` status `ready` deltaP `15.3557` edge `0.143` maxDD `-15.7982`
- `market_context_high->index_1h` score `-1.0901` n `98` status `ready` deltaP `-5.6184` edge `-0.0036` maxDD `-1.2295`
- `market_context_high->crypto_alt_1h` score `-1.3045` n `98` status `ready` deltaP `-2.8565` edge `0.0021` maxDD `-7.6911`
- `market_context_high->fx_1h` score `-1.3304` n `98` status `ready` deltaP `-8.2977` edge `-0.0009` maxDD `-0.3721`
- `market_context_high->metal_4h` score `-1.357` n `98` status `ready` deltaP `5.6745` edge `-0.0202` maxDD `-6.1238`
- `market_context_high->crypto_major_4h` score `-1.5211` n `98` status `ready` deltaP `-4.0599` edge `0.1903` maxDD `-22.3259`
- `market_context_high->crypto_major_1h` score `-2.4377` n `98` status `ready` deltaP `-3.0337` edge `0.0038` maxDD `-10.2705`
- `market_context_high->index_4h` score `-2.9275` n `98` status `ready` deltaP `-12.1982` edge `-0.0283` maxDD `-4.7471`
- `market_context_high->commodity_1h` score `-3.0421` n `98` status `ready` deltaP `-16.8703` edge `-0.0363` maxDD `-3.7125`
- `market_context_high->equity_1h` score `-3.6701` n `98` status `ready` deltaP `-1.8361` edge `-0.075` maxDD `-11.1548`
- `market_context_high->fx_4h` score `-4.6132` n `98` status `ready` deltaP `-25.4542` edge `-0.0105` maxDD `-2.0058`
- `market_context_high->fx_24h` score `-6.7372` n `98` status `ready` deltaP `-18.8138` edge `-0.0051` maxDD `-5.8059`
- `market_context_high->commodity_4h` score `-7.8451` n `98` status `ready` deltaP `-27.8683` edge `-0.1219` maxDD `-14.6855`
- `market_context_high->index_24h` score `-8.5892` n `98` status `ready` deltaP `-10.8666` edge `-0.1011` maxDD `-20.7114`
- `market_context_high->equity_4h` score `-13.7424` n `98` status `ready` deltaP `-18.8496` edge `-0.3341` maxDD `-44.5018`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
