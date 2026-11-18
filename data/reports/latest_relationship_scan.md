# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-18T04:37:29.627724+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4185`

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

- `market_context_high->unknown_24h` score `1469.9118` n `98` status `ready` deltaP `3.4722` edge `122.4695` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `15.3107` n `98` status `ready` deltaP `45.3231` edge `1.9878` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `14.0915` n `98` status `ready` deltaP `30.8638` edge `1.8132` maxDD `-13.3222`
- `market_context_high->metal_1h` score `-0.359` n `98` status `ready` deltaP `1.1304` edge `0.0066` maxDD `-2.1461`
- `market_context_high->crypto_alt_4h` score `-0.7212` n `98` status `ready` deltaP `-0.0374` edge `0.1888` maxDD `-17.1476`
- `market_context_high->metal_24h` score `-0.7921` n `98` status `ready` deltaP `15.3557` edge `0.1541` maxDD `-15.7982`
- `market_context_high->metal_4h` score `-0.9361` n `98` status `ready` deltaP `8.266` edge `-0.0024` maxDD `-6.1238`
- `market_context_high->index_1h` score `-1.0091` n `98` status `ready` deltaP `-4.4208` edge `-0.0012` maxDD `-1.2295`
- `market_context_high->crypto_alt_1h` score `-1.1526` n `98` status `ready` deltaP `-1.5092` edge `0.0126` maxDD `-7.6911`
- `market_context_high->fx_1h` score `-1.3436` n `98` status `ready` deltaP `-8.4474` edge `-0.001` maxDD `-0.3721`
- `market_context_high->crypto_major_4h` score `-1.4258` n `98` status `ready` deltaP `-2.9928` edge `0.1954` maxDD `-22.3259`
- `market_context_high->crypto_major_1h` score `-2.2531` n `98` status `ready` deltaP `-1.8361` edge `0.0112` maxDD `-10.2705`
- `market_context_high->index_4h` score `-2.6922` n `98` status `ready` deltaP `-10.2165` edge `-0.0219` maxDD `-4.7471`
- `market_context_high->commodity_1h` score `-2.9343` n `98` status `ready` deltaP `-15.8224` edge `-0.0343` maxDD `-3.7125`
- `market_context_high->equity_1h` score `-3.3007` n `98` status `ready` deltaP `-0.3391` edge `-0.0542` maxDD `-11.1548`
- `market_context_high->fx_4h` score `-4.6108` n `98` status `ready` deltaP `-25.4542` edge `-0.0103` maxDD `-2.0058`
- `market_context_high->fx_24h` score `-6.7648` n `98` status `ready` deltaP `-18.8138` edge `-0.0074` maxDD `-5.8059`
- `market_context_high->commodity_4h` score `-7.6156` n `98` status `ready` deltaP `-25.7342` edge `-0.117` maxDD `-14.6855`
- `market_context_high->index_24h` score `-8.3019` n `98` status `ready` deltaP `-8.6097` edge `-0.0922` maxDD `-20.7114`
- `market_context_high->equity_4h` score `-13.0947` n `98` status `ready` deltaP `-17.1727` edge `-0.2913` maxDD `-44.5018`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
