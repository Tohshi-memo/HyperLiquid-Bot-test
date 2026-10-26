# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-26T04:22:24.229593+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `64`

- Symbol pattern count: `7054`

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

- `market_context_high->unknown_4h` score `27.192` n `113` status `ready` deltaP `-2.4256` edge `2.3157` maxDD `-1.016`
- `market_context_high->metal_24h` score `0.2952` n `104` status `ready` deltaP `24.3857` edge `0.1423` maxDD `-7.3625`
- `market_context_high->fx_24h` score `0.1217` n `104` status `ready` deltaP `21.5144` edge `0.0294` maxDD `-1.2451`
- `market_context_high->fx_4h` score `-0.0511` n `113` status `ready` deltaP `7.1539` edge `0.0079` maxDD `-0.4545`
- `market_context_high->fx_1h` score `-0.0845` n `122` status `ready` deltaP `3.5069` edge `0.0016` maxDD `-0.1986`
- `market_context_high->metal_1h` score `-0.3703` n `122` status `ready` deltaP `5.0113` edge `-0.0017` maxDD `-1.6682`
- `market_context_high->commodity_1h` score `-0.4019` n `122` status `ready` deltaP `-1.5682` edge `0.009` maxDD `-1.0053`
- `market_context_high->commodity_4h` score `-0.5407` n `113` status `ready` deltaP `1.4205` edge `0.0441` maxDD `-1.165`
- `market_context_high->index_1h` score `-0.6703` n `122` status `ready` deltaP `-2.302` edge `-0.0054` maxDD `-1.2155`
- `market_context_high->index_24h` score `-0.8135` n `104` status `ready` deltaP `9.2148` edge `-0.0375` maxDD `-4.925`
- `market_context_high->crypto_major_1h` score `-1.5063` n `122` status `ready` deltaP `1.5682` edge `-0.0455` maxDD `-9.3126`
- `market_context_high->metal_4h` score `-2.0888` n `113` status `ready` deltaP `2.6319` edge `-0.0206` maxDD `-5.3474`
- `market_context_high->index_4h` score `-2.153` n `113` status `ready` deltaP `-7.7676` edge `-0.0368` maxDD `-4.3282`
- `market_context_high->crypto_major_24h` score `-3.6978` n `104` status `ready` deltaP `-0.8681` edge `-0.1076` maxDD `-22.1881`
- `market_context_high->equity_1h` score `-3.8814` n `122` status `ready` deltaP `-1.1755` edge `-0.087` maxDD `-12.2891`
- `market_context_high->crypto_alt_1h` score `-4.1621` n `122` status `ready` deltaP `-3.3278` edge `-0.0762` maxDD `-13.2099`
- `market_context_high->commodity_24h` score `-5.3804` n `104` status `ready` deltaP `-16.1592` edge `-0.1265` maxDD `-18.7786`
- `market_context_high->equity_24h` score `-7.4255` n `104` status `ready` deltaP `-3.7527` edge `-0.3986` maxDD `-36.6024`
- `market_context_high->crypto_major_4h` score `-10.1456` n `113` status `ready` deltaP `-12.7428` edge `-0.2607` maxDD `-32.9851`
- `market_context_high->crypto_alt_24h` score `-11.9721` n `104` status `ready` deltaP `-11.899` edge `-0.4556` maxDD `-69.3303`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
