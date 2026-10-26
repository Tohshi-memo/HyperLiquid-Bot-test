# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-26T04:07:31.022711+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `64`

- Symbol pattern count: `6976`

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

- `market_context_high->unknown_4h` score `27.2186` n `113` status `ready` deltaP `-2.2731` edge `2.3169` maxDD `-1.016`
- `market_context_high->metal_24h` score `0.2569` n `103` status `ready` deltaP `23.8909` edge `0.1407` maxDD `-7.3625`
- `market_context_high->fx_24h` score `0.1092` n `103` status `ready` deltaP `21.3053` edge `0.0292` maxDD `-1.2451`
- `market_context_high->fx_4h` score `-0.0511` n `113` status `ready` deltaP `7.1539` edge `0.0079` maxDD `-0.4545`
- `market_context_high->fx_1h` score `-0.105` n `121` status `ready` deltaP `3.114` edge `0.0016` maxDD `-0.1986`
- `market_context_high->metal_1h` score `-0.3454` n `121` status `ready` deltaP `5.4313` edge `-0.0013` maxDD `-1.6682`
- `market_context_high->commodity_1h` score `-0.4237` n `121` status `ready` deltaP `-1.9882` edge `0.009` maxDD `-1.0053`
- `market_context_high->commodity_4h` score `-0.5502` n `113` status `ready` deltaP `1.268` edge `0.0439` maxDD `-1.165`
- `market_context_high->index_1h` score `-0.6881` n `121` status `ready` deltaP `-2.5994` edge `-0.0057` maxDD `-1.2155`
- `market_context_high->index_24h` score `-0.8385` n `103` status `ready` deltaP `8.8694` edge `-0.0384` maxDD `-4.925`
- `market_context_high->metal_4h` score `-2.0754` n `113` status `ready` deltaP `2.7844` edge `-0.0205` maxDD `-5.3474`
- `market_context_high->index_4h` score `-2.1522` n `113` status `ready` deltaP `-7.7676` edge `-0.0367` maxDD `-4.3282`
- `market_context_high->crypto_major_1h` score `-2.326` n `121` status `ready` deltaP `1.3114` edge `-0.0445` maxDD `-9.3126`
- `market_context_high->crypto_major_24h` score `-3.421` n `103` status `ready` deltaP `-0.5563` edge `-0.0967` maxDD `-20.7214`
- `market_context_high->equity_1h` score `-3.9189` n `121` status `ready` deltaP `-1.4797` edge `-0.0881` maxDD `-12.2891`
- `market_context_high->crypto_alt_1h` score `-4.0465` n `121` status `ready` deltaP `-2.9891` edge `-0.0742` maxDD `-13.113`
- `market_context_high->commodity_24h` score `-5.2382` n `103` status `ready` deltaP `-15.8138` edge `-0.1226` maxDD `-18.1495`
- `market_context_high->equity_24h` score `-7.4286` n `103` status `ready` deltaP `-3.4689` edge `-0.4009` maxDD `-36.6024`
- `market_context_high->crypto_major_4h` score `-10.1324` n `113` status `ready` deltaP `-12.7428` edge `-0.2596` maxDD `-32.9851`
- `market_context_high->crypto_alt_24h` score `-11.6698` n `103` status `ready` deltaP `-11.5443` edge `-0.4451` maxDD `-67.5919`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
