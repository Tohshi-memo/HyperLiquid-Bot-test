# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-25T06:07:26.525272+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7768`

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

- `market_context_high->unknown_4h` score `51.1634` n `96` status `ready` deltaP `0.1271` edge `4.2963` maxDD `-1.016`
- `market_context_high->unknown_1h` score `17.5112` n `108` status `ready` deltaP `3.9089` edge `1.4821` maxDD `-1.5781`
- `market_context_high->crypto_alt_24h` score `11.6745` n `35` status `ready` deltaP `31.7361` edge `0.8221` maxDD `-4.1975`
- `market_context_high->crypto_major_24h` score `3.4085` n `35` status `ready` deltaP `20.2926` edge `0.2547` maxDD `-5.8084`
- `market_context_high->commodity_24h` score `0.5903` n `35` status `ready` deltaP `12.1627` edge `0.0855` maxDD `-3.6055`
- `market_context_high->fx_24h` score `-0.0219` n `35` status `ready` deltaP `9.7917` edge `0.0061` maxDD `-0.9352`
- `market_context_high->fx_1h` score `-0.1017` n `108` status `ready` deltaP `2.8443` edge `0.0029` maxDD `-0.1258`
- `market_context_high->fx_4h` score `-0.1962` n `96` status `ready` deltaP `3.9888` edge `0.0081` maxDD `-0.4545`
- `market_context_high->commodity_1h` score `-0.4823` n `108` status `ready` deltaP `-2.6946` edge `0.0062` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.5526` n `108` status `ready` deltaP `-0.0832` edge `-0.0051` maxDD `-1.2155`
- `market_context_high->metal_1h` score `-0.5697` n `108` status `ready` deltaP `5.4169` edge `-0.0044` maxDD `-1.6682`
- `market_context_high->commodity_4h` score `-0.9803` n `96` status `ready` deltaP `-5.4878` edge `0.0338` maxDD `-1.165`
- `market_context_high->crypto_major_1h` score `-1.227` n `108` status `ready` deltaP `3.3101` edge `-0.0213` maxDD `-9.3126`
- `market_context_high->metal_4h` score `-1.8781` n `96` status `ready` deltaP `5.6402` edge `-0.0231` maxDD `-5.3474`
- `market_context_high->index_4h` score `-2.0325` n `96` status `ready` deltaP `-5.0305` edge `-0.0396` maxDD `-4.3282`
- `market_context_high->equity_1h` score `-2.3223` n `108` status `ready` deltaP `2.3397` edge `-0.086` maxDD `-12.1865`
- `market_context_high->metal_24h` score `-2.3336` n `35` status `ready` deltaP `-2.6637` edge `-0.0374` maxDD `-6.1446`
- `market_context_high->crypto_alt_1h` score `-2.7001` n `108` status `ready` deltaP `0.0665` edge `-0.0464` maxDD `-11.3243`
- `market_context_high->crypto_major_4h` score `-5.6826` n `96` status `ready` deltaP `-7.8506` edge `-0.1765` maxDD `-33.3092`
- `market_context_high->index_24h` score `-6.5916` n `35` status `ready` deltaP `-32.6042` edge `-0.2018` maxDD `-5.078`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
