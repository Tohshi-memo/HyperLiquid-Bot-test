# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-18T06:07:28.177762+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4215`

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

- `market_context_high->unknown_24h` score `1422.9342` n `98` status `ready` deltaP `3.4722` edge `118.5547` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `15.2208` n `98` status `ready` deltaP `44.6287` edge `1.9809` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `13.9447` n `98` status `ready` deltaP `30.5166` edge `1.7967` maxDD `-13.3222`
- `market_context_high->metal_1h` score `-0.3574` n `98` status `ready` deltaP `1.1304` edge `0.0068` maxDD `-2.1461`
- `market_context_high->metal_24h` score `-0.7357` n `98` status `ready` deltaP `15.3557` edge `0.1588` maxDD `-15.7982`
- `market_context_high->crypto_alt_4h` score `-0.7941` n `98` status `ready` deltaP `-0.4947` edge `0.1825` maxDD `-17.1476`
- `market_context_high->metal_4h` score `-0.8101` n `98` status `ready` deltaP `9.1806` edge `0.002` maxDD `-6.1238`
- `market_context_high->index_1h` score `-0.9842` n `98` status `ready` deltaP `-3.9717` edge `-0.001` maxDD `-1.2295`
- `market_context_high->crypto_alt_1h` score `-1.1736` n `98` status `ready` deltaP `-1.6589` edge `0.0109` maxDD `-7.6911`
- `market_context_high->fx_1h` score `-1.3568` n `98` status `ready` deltaP `-8.5971` edge `-0.0011` maxDD `-0.3721`
- `market_context_high->crypto_major_4h` score `-1.4753` n `98` status `ready` deltaP `-3.4501` edge `0.1921` maxDD `-22.3259`
- `market_context_high->crypto_major_1h` score `-2.3262` n `98` status `ready` deltaP `-2.2852` edge `0.0081` maxDD `-10.2705`
- `market_context_high->index_4h` score `-2.6496` n `98` status `ready` deltaP `-9.7592` edge `-0.0214` maxDD `-4.7471`
- `market_context_high->commodity_1h` score `-2.9331` n `98` status `ready` deltaP `-15.8224` edge `-0.0342` maxDD `-3.7125`
- `market_context_high->equity_1h` score `-3.2804` n `98` status `ready` deltaP `-0.1894` edge `-0.0535` maxDD `-11.1548`
- `market_context_high->fx_4h` score `-4.6132` n `98` status `ready` deltaP `-25.4542` edge `-0.0105` maxDD `-2.0058`
- `market_context_high->fx_24h` score `-6.7804` n `98` status `ready` deltaP `-18.8138` edge `-0.0087` maxDD `-5.8059`
- `market_context_high->commodity_4h` score `-7.5708` n `98` status `ready` deltaP `-25.4293` edge `-0.1153` maxDD `-14.6855`
- `market_context_high->index_24h` score `-8.2657` n `98` status `ready` deltaP `-8.2625` edge `-0.0915` maxDD `-20.7114`
- `market_context_high->equity_4h` score `-12.9379` n `98` status `ready` deltaP `-16.563` edge `-0.2823` maxDD `-44.5018`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
