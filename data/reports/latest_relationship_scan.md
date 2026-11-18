# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-18T02:37:35.114303+00:00`
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

- `market_context_high->unknown_24h` score `1489.803` n `98` status `ready` deltaP `3.4722` edge `124.1271` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `15.3835` n `98` status `ready` deltaP `46.0176` edge `1.9925` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `14.2507` n `98` status `ready` deltaP `31.211` edge `1.8313` maxDD `-13.3222`
- `market_context_high->metal_1h` score `-0.4275` n `98` status `ready` deltaP `0.0825` edge `0.0048` maxDD `-2.1461`
- `market_context_high->crypto_alt_4h` score `-0.8176` n `98` status `ready` deltaP `-0.6471` edge `0.1805` maxDD `-17.1476`
- `market_context_high->metal_24h` score `-0.8809` n `98` status `ready` deltaP `15.3557` edge `0.1467` maxDD `-15.7982`
- `market_context_high->index_1h` score `-1.0013` n `98` status `ready` deltaP `-4.2711` edge `-0.0012` maxDD `-1.2295`
- `market_context_high->metal_4h` score `-1.1513` n `98` status `ready` deltaP `7.0464` edge `-0.0122` maxDD `-6.1238`
- `market_context_high->crypto_alt_1h` score `-1.1705` n `98` status `ready` deltaP `-1.6589` edge `0.0113` maxDD `-7.6911`
- `market_context_high->fx_1h` score `-1.2933` n `98` status `ready` deltaP `-7.8486` edge `-0.0008` maxDD `-0.3721`
- `market_context_high->crypto_major_4h` score `-1.5576` n `98` status `ready` deltaP `-3.9074` edge `0.1846` maxDD `-22.3259`
- `market_context_high->crypto_major_1h` score `-2.271` n `98` status `ready` deltaP `-1.9858` edge `0.0107` maxDD `-10.2705`
- `market_context_high->index_4h` score `-2.8377` n `98` status `ready` deltaP `-11.436` edge `-0.0259` maxDD `-4.7471`
- `market_context_high->commodity_1h` score `-2.9798` n `98` status `ready` deltaP `-16.2715` edge `-0.0351` maxDD `-3.7125`
- `market_context_high->equity_1h` score `-3.3391` n `98` status `ready` deltaP `-0.4888` edge `-0.0564` maxDD `-11.1548`
- `market_context_high->fx_4h` score `-4.6108` n `98` status `ready` deltaP `-25.4542` edge `-0.0103` maxDD `-2.0058`
- `market_context_high->fx_24h` score `-6.7552` n `98` status `ready` deltaP `-18.8138` edge `-0.0066` maxDD `-5.8059`
- `market_context_high->commodity_4h` score `-7.7381` n `98` status `ready` deltaP `-26.8012` edge `-0.1201` maxDD `-14.6855`
- `market_context_high->index_24h` score `-8.4411` n `98` status `ready` deltaP `-9.825` edge `-0.0957` maxDD `-20.7114`
- `market_context_high->equity_4h` score `-13.5822` n `98` status `ready` deltaP `-18.3922` edge `-0.3238` maxDD `-44.5018`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
