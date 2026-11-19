# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-19T09:52:27.416666+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2572`

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

- `market_context_high->unknown_1h` score `11476.1022` n `112` status `ready` deltaP `1.1175` edge `956.3542` maxDD `-0.9174`
- `market_context_high->unknown_4h` score `7119.6643` n `112` status `ready` deltaP `0.3266` edge `593.3316` maxDD `-0.6067`
- `market_context_high->crypto_major_24h` score `12.2719` n `98` status `ready` deltaP `39.594` edge `1.6364` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `10.4306` n `98` status `ready` deltaP `21.6624` edge `1.4052` maxDD `-13.3222`
- `market_context_high->metal_1h` score `-0.2591` n `112` status `ready` deltaP `3.1437` edge `0.0123` maxDD `-2.6517`
- `market_context_high->metal_4h` score `-0.2747` n `112` status `ready` deltaP `13.6978` edge `0.0168` maxDD `-6.1475`
- `market_context_high->crypto_major_4h` score `-0.3135` n `112` status `ready` deltaP `1.6115` edge `0.3073` maxDD `-22.3259`
- `market_context_high->metal_24h` score `-0.3205` n `98` status `ready` deltaP `15.3557` edge `0.1934` maxDD `-15.7982`
- `market_context_high->crypto_alt_4h` score `-0.5391` n `112` status `ready` deltaP `2.0688` edge `0.1981` maxDD `-17.1476`
- `market_context_high->index_1h` score `-0.8229` n `112` status `ready` deltaP `-1.4703` edge `0.003` maxDD `-1.2295`
- `market_context_high->crypto_major_1h` score `-0.8443` n `112` status `ready` deltaP `2.3952` edge `0.0625` maxDD `-10.2705`
- `market_context_high->crypto_alt_1h` score `-1.0907` n `112` status `ready` deltaP `-2.2241` edge `0.0253` maxDD `-7.6911`
- `market_context_high->index_4h` score `-1.2375` n `112` status `ready` deltaP `-3.5278` edge `-0.0008` maxDD `-4.7471`
- `market_context_high->fx_1h` score `-1.4309` n `112` status `ready` deltaP `-9.5007` edge `-0.001` maxDD `-0.392`
- `market_context_high->fx_4h` score `-2.4073` n `112` status `ready` deltaP `-15.2003` edge `-0.003` maxDD `-2.0104`
- `market_context_high->commodity_1h` score `-2.5187` n `112` status `ready` deltaP `-11.2917` edge `-0.0268` maxDD `-3.9584`
- `market_context_high->equity_1h` score `-2.7516` n `112` status `ready` deltaP `1.358` edge `-0.0206` maxDD `-11.0868`
- `market_context_high->fx_24h` score `-6.7252` n `98` status `ready` deltaP `-18.8138` edge `-0.0041` maxDD `-5.8059`
- `market_context_high->commodity_4h` score `-7.382` n `112` status `ready` deltaP `-23.3667` edge `-0.0975` maxDD `-14.9509`
- `market_context_high->index_24h` score `-9.1659` n `98` status `ready` deltaP `-16.7694` edge `-0.1098` maxDD `-20.7114`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
