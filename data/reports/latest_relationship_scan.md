# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-25T15:37:24.188269+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5252`

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

- `market_context_high->unknown_4h` score `33.5113` n `113` status `ready` deltaP `-0.4439` edge `2.8291` maxDD `-1.016`
- `market_context_high->commodity_24h` score `0.0941` n `62` status `ready` deltaP `7.9413` edge `0.0458` maxDD `-3.6055`
- `market_context_high->fx_4h` score `-0.0305` n `113` status `ready` deltaP `7.3063` edge `0.0086` maxDD `-0.4545`
- `market_context_high->fx_1h` score `-0.042` n `113` status `ready` deltaP `4.0088` edge `0.0028` maxDD `-0.1258`
- `market_context_high->commodity_1h` score `-0.5326` n `113` status `ready` deltaP `-0.4822` edge `0.0089` maxDD `-1.0053`
- `market_context_high->metal_1h` score `-0.6383` n `113` status `ready` deltaP `4.6341` edge `-0.0049` maxDD `-1.6682`
- `market_context_high->index_1h` score `-0.6775` n `113` status `ready` deltaP `-2.3356` edge `-0.0061` maxDD `-1.2155`
- `market_context_high->commodity_4h` score `-0.8316` n `113` status `ready` deltaP `-2.2381` edge `0.0312` maxDD `-1.165`
- `market_context_high->crypto_major_24h` score `-1.3527` n `62` status `ready` deltaP `-5.606` edge `-0.0335` maxDD `-4.5369`
- `market_context_high->crypto_major_1h` score `-1.3652` n `113` status `ready` deltaP `2.6482` edge `-0.0346` maxDD `-9.3126`
- `market_context_high->fx_24h` score `-1.5583` n `62` status `ready` deltaP `2.621` edge `0.0099` maxDD `-1.2451`
- `market_context_high->metal_4h` score `-1.8916` n `113` status `ready` deltaP `4.7661` edge `-0.0184` maxDD `-5.3474`
- `market_context_high->index_24h` score `-2.1115` n `62` status `ready` deltaP `-1.9321` edge `-0.1296` maxDD `-4.925`
- `market_context_high->index_4h` score `-2.1878` n `113` status `ready` deltaP `-8.3774` edge `-0.0372` maxDD `-4.3282`
- `market_context_high->crypto_alt_1h` score `-3.1582` n `113` status `ready` deltaP `-1.86` edge `-0.0634` maxDD `-11.3243`
- `market_context_high->metal_24h` score `-3.7465` n `62` status `ready` deltaP `-10.1367` edge `0.0224` maxDD `-7.3625`
- `market_context_high->equity_1h` score `-3.8967` n `113` status `ready` deltaP `-0.6889` edge `-0.0928` maxDD `-12.1865`
- `market_context_high->crypto_alt_24h` score `-7.4802` n `62` status `ready` deltaP `-3.6234` edge `-0.2892` maxDD `-42.3182`
- `market_context_high->crypto_major_4h` score `-9.962` n `113` status `ready` deltaP `-12.7428` edge `-0.2454` maxDD `-32.9851`
- `market_context_high->equity_24h` score `-11.9019` n `62` status `ready` deltaP `-17.9883` edge `-0.8776` maxDD `-36.6024`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
