# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-18T08:22:28.180328+00:00`
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

- `market_context_high->unknown_24h` score `1367.8982` n `98` status `ready` deltaP `2.7778` edge `113.973` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `14.9539` n `98` status `ready` deltaP `43.0662` edge `1.9571` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `13.5944` n `98` status `ready` deltaP `28.9541` edge `1.7622` maxDD `-13.3222`
- `market_context_high->metal_1h` score `-0.2842` n `98` status `ready` deltaP `2.1783` edge `0.0092` maxDD `-2.1461`
- `market_context_high->metal_4h` score `-0.6476` n `98` status `ready` deltaP `10.5525` edge `0.0064` maxDD `-6.1238`
- `market_context_high->metal_24h` score `-0.6601` n `98` status `ready` deltaP `15.3557` edge `0.1651` maxDD `-15.7982`
- `market_context_high->crypto_alt_4h` score `-0.9368` n `98` status `ready` deltaP `-1.4093` edge `0.1703` maxDD `-17.1476`
- `market_context_high->index_1h` score `-0.9935` n `98` status `ready` deltaP `-4.1214` edge `-0.0012` maxDD `-1.2295`
- `market_context_high->crypto_alt_1h` score `-1.2812` n `98` status `ready` deltaP `-2.7068` edge `0.0041` maxDD `-7.6911`
- `market_context_high->fx_1h` score `-1.3544` n `98` status `ready` deltaP `-8.5971` edge `-0.0009` maxDD `-0.3721`
- `market_context_high->crypto_major_4h` score `-1.5932` n `98` status `ready` deltaP `-4.5172` edge `0.1841` maxDD `-22.3259`
- `market_context_high->crypto_major_1h` score `-2.3706` n `98` status `ready` deltaP `-2.4349` edge `0.0054` maxDD `-10.2705`
- `market_context_high->index_4h` score `-2.7396` n `98` status `ready` deltaP `-10.6738` edge `-0.0228` maxDD `-4.7471`
- `market_context_high->commodity_1h` score `-2.8995` n `98` status `ready` deltaP `-15.523` edge `-0.0334` maxDD `-3.7125`
- `market_context_high->equity_1h` score `-3.3163` n `98` status `ready` deltaP `-0.4888` edge `-0.0545` maxDD `-11.1548`
- `market_context_high->fx_4h` score `-4.6546` n `98` status `ready` deltaP `-25.9115` edge `-0.0109` maxDD `-2.0058`
- `market_context_high->fx_24h` score `-6.7948` n `98` status `ready` deltaP `-18.8138` edge `-0.0099` maxDD `-5.8059`
- `market_context_high->commodity_4h` score `-7.4096` n `98` status `ready` deltaP `-24.2098` edge `-0.11` maxDD `-14.6855`
- `market_context_high->index_24h` score `-8.4123` n `98` status `ready` deltaP `-9.825` edge `-0.0933` maxDD `-20.7114`
- `market_context_high->equity_4h` score `-12.9619` n `98` status `ready` deltaP `-16.563` edge `-0.2843` maxDD `-44.5018`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
