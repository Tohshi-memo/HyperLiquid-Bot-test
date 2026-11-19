# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-19T04:22:24.969763+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2452`

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

- `market_context_high->unknown_24h` score `1361.5251` n `98` status `ready` deltaP `5.2083` edge `113.4257` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `13.2087` n `98` status `ready` deltaP `39.594` edge `1.7565` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `11.1966` n `98` status `ready` deltaP `24.093` edge `1.4872` maxDD `-13.3222`
- `market_context_high->metal_24h` score `-0.2449` n `98` status `ready` deltaP `15.3557` edge `0.1997` maxDD `-15.7982`
- `market_context_high->metal_1h` score `-0.6539` n `103` status `ready` deltaP `0.6438` edge `0.0077` maxDD `-2.6517`
- `market_context_high->metal_4h` score `-0.6796` n `98` status `ready` deltaP `10.8574` edge `0.0017` maxDD `-6.1238`
- `market_context_high->index_1h` score `-0.8442` n `103` status `ready` deltaP `-1.8197` edge `0.0026` maxDD `-1.2295`
- `market_context_high->crypto_alt_1h` score `-0.9632` n `103` status `ready` deltaP `-0.8532` edge `0.0325` maxDD `-7.6911`
- `market_context_high->crypto_major_1h` score `-0.9988` n `103` status `ready` deltaP `1.465` edge `0.0489` maxDD `-10.2705`
- `market_context_high->crypto_alt_4h` score `-1.0506` n `98` status `ready` deltaP `-1.2569` edge `0.1547` maxDD `-17.1476`
- `market_context_high->crypto_major_4h` score `-1.2726` n `98` status `ready` deltaP `-3.6025` edge `0.2191` maxDD `-22.3259`
- `market_context_high->fx_1h` score `-1.4294` n `103` status `ready` deltaP `-9.437` edge `-0.0013` maxDD `-0.392`
- `market_context_high->index_4h` score `-2.7334` n `98` status `ready` deltaP `-10.5214` edge `-0.0233` maxDD `-4.7471`
- `market_context_high->equity_1h` score `-2.8138` n `103` status `ready` deltaP `1.3153` edge `-0.0255` maxDD `-11.0868`
- `market_context_high->commodity_1h` score `-2.9363` n `103` status `ready` deltaP `-15.4163` edge `-0.0341` maxDD `-3.9584`
- `market_context_high->fx_4h` score `-4.6336` n `98` status `ready` deltaP `-25.4542` edge `-0.0122` maxDD `-2.0058`
- `market_context_high->fx_24h` score `-6.7396` n `98` status `ready` deltaP `-18.8138` edge `-0.0053` maxDD `-5.8059`
- `market_context_high->commodity_4h` score `-7.5454` n `98` status `ready` deltaP `-25.2768` edge `-0.1142` maxDD `-14.6855`
- `market_context_high->index_24h` score `-9.0098` n `98` status `ready` deltaP `-15.5541` edge `-0.1049` maxDD `-20.7114`
- `market_context_high->equity_4h` score `-12.8036` n `98` status `ready` deltaP `-16.563` edge `-0.2745` maxDD `-44.2305`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
