# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-19T04:07:28.532257+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2450`

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

- `market_context_high->unknown_24h` score `1363.1415` n `98` status `ready` deltaP `5.2083` edge `113.5604` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `13.2375` n `98` status `ready` deltaP `39.594` edge `1.7602` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `11.2337` n `98` status `ready` deltaP `24.2666` edge `1.4908` maxDD `-13.3222`
- `market_context_high->metal_24h` score `-0.2473` n `98` status `ready` deltaP `15.3557` edge `0.1995` maxDD `-15.7982`
- `market_context_high->metal_4h` score `-0.6796` n `98` status `ready` deltaP `10.8574` edge `0.0017` maxDD `-6.1238`
- `market_context_high->metal_1h` score `-0.7066` n `102` status `ready` deltaP `0.27` edge `0.0058` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.8745` n `102` status `ready` deltaP `-2.222` edge `0.0014` maxDD `-1.2295`
- `market_context_high->crypto_alt_4h` score `-1.0247` n `98` status `ready` deltaP `-1.1044` edge `0.157` maxDD `-17.1476`
- `market_context_high->crypto_alt_1h` score `-1.0498` n `102` status `ready` deltaP `-1.3767` edge `0.0249` maxDD `-7.6911`
- `market_context_high->crypto_major_1h` score `-1.0926` n `102` status `ready` deltaP `1.1007` edge `0.0393` maxDD `-10.2705`
- `market_context_high->crypto_major_4h` score `-1.2421` n `98` status `ready` deltaP `-3.4501` edge `0.222` maxDD `-22.3259`
- `market_context_high->fx_1h` score `-1.47` n `102` status `ready` deltaP `-9.9155` edge `-0.0015` maxDD `-0.392`
- `market_context_high->index_4h` score `-2.7164` n `98` status `ready` deltaP `-10.369` edge `-0.0229` maxDD `-4.7471`
- `market_context_high->equity_1h` score `-2.9317` n `102` status `ready` deltaP `0.951` edge `-0.0329` maxDD `-11.0868`
- `market_context_high->commodity_1h` score `-2.986` n `102` status `ready` deltaP `-15.9329` edge `-0.0348` maxDD `-3.9584`
- `market_context_high->fx_4h` score `-4.6336` n `98` status `ready` deltaP `-25.4542` edge `-0.0122` maxDD `-2.0058`
- `market_context_high->fx_24h` score `-6.7408` n `98` status `ready` deltaP `-18.8138` edge `-0.0054` maxDD `-5.8059`
- `market_context_high->commodity_4h` score `-7.5478` n `98` status `ready` deltaP `-25.2768` edge `-0.1144` maxDD `-14.6855`
- `market_context_high->index_24h` score `-9.0086` n `98` status `ready` deltaP `-15.5541` edge `-0.1048` maxDD `-20.7114`
- `market_context_high->equity_4h` score `-12.7602` n `98` status `ready` deltaP `-16.4105` edge `-0.2719` maxDD `-44.2305`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
