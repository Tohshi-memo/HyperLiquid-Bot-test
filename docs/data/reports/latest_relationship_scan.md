# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-18T04:22:43.328969+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4179`

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

- `market_context_high->unknown_24h` score `1474.8306` n `98` status `ready` deltaP `3.4722` edge `122.8794` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `15.3229` n `98` status `ready` deltaP `45.4967` edge `1.9882` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `14.1063` n `98` status `ready` deltaP `30.8638` edge `1.8151` maxDD `-13.3222`
- `market_context_high->metal_1h` score `-0.3683` n `98` status `ready` deltaP `0.9807` edge `0.0064` maxDD `-2.1461`
- `market_context_high->crypto_alt_4h` score `-0.7196` n `98` status `ready` deltaP `-0.0374` edge `0.189` maxDD `-17.1476`
- `market_context_high->metal_24h` score `-0.8029` n `98` status `ready` deltaP `15.3557` edge `0.1532` maxDD `-15.7982`
- `market_context_high->metal_4h` score `-0.9603` n `98` status `ready` deltaP `8.1135` edge `-0.0034` maxDD `-6.1238`
- `market_context_high->index_1h` score `-1.0099` n `98` status `ready` deltaP `-4.4208` edge `-0.0013` maxDD `-1.2295`
- `market_context_high->crypto_alt_1h` score `-1.1674` n `98` status `ready` deltaP `-1.6589` edge `0.0117` maxDD `-7.6911`
- `market_context_high->fx_1h` score `-1.3436` n `98` status `ready` deltaP `-8.4474` edge `-0.001` maxDD `-0.3721`
- `market_context_high->crypto_major_4h` score `-1.4297` n `98` status `ready` deltaP `-2.9928` edge `0.1949` maxDD `-22.3259`
- `market_context_high->crypto_major_1h` score `-2.271` n `98` status `ready` deltaP `-1.9858` edge `0.0107` maxDD `-10.2705`
- `market_context_high->index_4h` score `-2.7092` n `98` status `ready` deltaP `-10.369` edge `-0.0223` maxDD `-4.7471`
- `market_context_high->commodity_1h` score `-2.9343` n `98` status `ready` deltaP `-15.8224` edge `-0.0343` maxDD `-3.7125`
- `market_context_high->equity_1h` score `-3.3079` n `98` status `ready` deltaP `-0.3391` edge `-0.0548` maxDD `-11.1548`
- `market_context_high->fx_4h` score `-4.6096` n `98` status `ready` deltaP `-25.4542` edge `-0.0102` maxDD `-2.0058`
- `market_context_high->fx_24h` score `-6.7624` n `98` status `ready` deltaP `-18.8138` edge `-0.0072` maxDD `-5.8059`
- `market_context_high->commodity_4h` score `-7.6314` n `98` status `ready` deltaP `-25.8866` edge `-0.1173` maxDD `-14.6855`
- `market_context_high->index_24h` score `-8.3206` n `98` status `ready` deltaP `-8.7833` edge `-0.0926` maxDD `-20.7114`
- `market_context_high->equity_4h` score `-13.1489` n `98` status `ready` deltaP `-17.3252` edge `-0.2948` maxDD `-44.5018`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
