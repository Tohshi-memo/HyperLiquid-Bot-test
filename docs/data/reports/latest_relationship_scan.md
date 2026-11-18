# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-18T03:52:27.315968+00:00`
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

- `market_context_high->unknown_24h` score `1479.8178` n `98` status `ready` deltaP `3.4722` edge `123.295` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `15.306` n `98` status `ready` deltaP `45.3231` edge `1.9872` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `14.1266` n `98` status `ready` deltaP `30.8638` edge `1.8177` maxDD `-13.3222`
- `market_context_high->metal_1h` score `-0.3785` n `98` status `ready` deltaP `0.831` edge `0.0061` maxDD `-2.1461`
- `market_context_high->crypto_alt_4h` score `-0.7424` n `98` status `ready` deltaP `-0.1898` edge `0.1871` maxDD `-17.1476`
- `market_context_high->metal_24h` score `-0.8221` n `98` status `ready` deltaP `15.3557` edge `0.1516` maxDD `-15.7982`
- `market_context_high->index_1h` score `-1.0099` n `98` status `ready` deltaP `-4.4208` edge `-0.0013` maxDD `-1.2295`
- `market_context_high->metal_4h` score `-1.0135` n `98` status `ready` deltaP `7.8086` edge `-0.0058` maxDD `-6.1238`
- `market_context_high->crypto_alt_1h` score `-1.1775` n `98` status `ready` deltaP `-1.6589` edge `0.0104` maxDD `-7.6911`
- `market_context_high->fx_1h` score `-1.3316` n `98` status `ready` deltaP `-8.2977` edge `-0.001` maxDD `-0.3721`
- `market_context_high->crypto_major_4h` score `-1.4728` n `98` status `ready` deltaP `-3.2977` edge `0.1914` maxDD `-22.3259`
- `market_context_high->crypto_major_1h` score `-2.2998` n `98` status `ready` deltaP `-2.1355` edge `0.0093` maxDD `-10.2705`
- `market_context_high->index_4h` score `-2.7444` n `98` status `ready` deltaP `-10.6738` edge `-0.0232` maxDD `-4.7471`
- `market_context_high->commodity_1h` score `-2.9486` n `98` status `ready` deltaP `-15.9721` edge `-0.0345` maxDD `-3.7125`
- `market_context_high->equity_1h` score `-3.3151` n `98` status `ready` deltaP `-0.3391` edge `-0.0554` maxDD `-11.1548`
- `market_context_high->fx_4h` score `-4.6084` n `98` status `ready` deltaP `-25.4542` edge `-0.0101` maxDD `-2.0058`
- `market_context_high->fx_24h` score `-6.7588` n `98` status `ready` deltaP `-18.8138` edge `-0.0069` maxDD `-5.8059`
- `market_context_high->commodity_4h` score `-7.6665` n `98` status `ready` deltaP `-26.1915` edge `-0.1182` maxDD `-14.6855`
- `market_context_high->index_24h` score `-8.3429` n `98` status `ready` deltaP `-8.9569` edge `-0.0933` maxDD `-20.7114`
- `market_context_high->equity_4h` score `-13.2681` n `98` status `ready` deltaP `-17.63` edge `-0.3027` maxDD `-44.5018`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
