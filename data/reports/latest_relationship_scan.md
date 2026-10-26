# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-26T15:07:33.418286+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8022`

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

- `market_context_high->unknown_4h` score `131.5163` n `151` status `ready` deltaP `0.499` edge `10.9899` maxDD `-1.016`
- `market_context_high->unknown_1h` score `28.4586` n `153` status `ready` deltaP `1.7468` edge `2.4088` maxDD `-1.5781`
- `market_context_high->metal_24h` score `0.5082` n `113` status `ready` deltaP `27.4474` edge `0.1492` maxDD `-7.3625`
- `market_context_high->fx_4h` score `0.177` n `151` status `ready` deltaP `9.9297` edge `0.0084` maxDD `-0.4545`
- `market_context_high->fx_1h` score `0.1672` n `153` status `ready` deltaP `7.0869` edge `0.0025` maxDD `-0.1986`
- `market_context_high->fx_24h` score `-0.0536` n `113` status `ready` deltaP `18.3095` edge `0.0283` maxDD `-1.2451`
- `market_context_high->metal_1h` score `-0.184` n `153` status `ready` deltaP `7.5002` edge `0.0056` maxDD `-1.6682`
- `market_context_high->commodity_1h` score `-0.345` n `153` status `ready` deltaP `1.5769` edge `0.0108` maxDD `-1.0053`
- `market_context_high->index_24h` score `-0.397` n `113` status `ready` deltaP `11.5689` edge `0.0002` maxDD `-4.925`
- `market_context_high->index_1h` score `-0.505` n `153` status `ready` deltaP `-0.1583` edge `0.0015` maxDD `-1.2155`
- `market_context_high->commodity_4h` score `-0.576` n `151` status `ready` deltaP `5.2647` edge `0.0398` maxDD `-1.165`
- `market_context_high->crypto_major_1h` score `-1.0307` n `153` status `ready` deltaP `3.1097` edge `0.0052` maxDD `-9.3126`
- `market_context_high->metal_4h` score `-1.0409` n `151` status `ready` deltaP `6.1296` edge `-0.0033` maxDD `-5.3474`
- `market_context_high->index_4h` score `-1.7349` n `151` status `ready` deltaP `-3.6731` edge `-0.0105` maxDD `-4.3282`
- `market_context_high->equity_1h` score `-2.0176` n `153` status `ready` deltaP `-0.0821` edge `-0.0295` maxDD `-12.2891`
- `market_context_high->crypto_alt_1h` score `-2.1328` n `153` status `ready` deltaP `-1.4068` edge `-0.0156` maxDD `-13.2099`
- `market_context_high->crypto_major_24h` score `-4.337` n `113` status `ready` deltaP `-1.8159` edge `-0.0582` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-4.8169` n `151` status `ready` deltaP `-1.9908` edge `-0.1003` maxDD `-32.9851`
- `market_context_high->equity_24h` score `-5.9604` n `113` status `ready` deltaP `-2.0445` edge `-0.193` maxDD `-36.6024`
- `market_context_high->commodity_24h` score `-6.3883` n `113` status `ready` deltaP `-17.8632` edge `-0.141` maxDD `-24.0477`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
