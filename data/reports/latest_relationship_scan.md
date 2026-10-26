# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-26T12:22:30.563175+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8396`

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

- `market_context_high->unknown_4h` score `16.5626` n `140` status `ready` deltaP `-0.6228` edge `1.4179` maxDD `-1.016`
- `market_context_high->metal_24h` score `0.5881` n `113` status `ready` deltaP `28.4445` edge `0.1528` maxDD `-7.3625`
- `market_context_high->fx_4h` score `0.1683` n `140` status `ready` deltaP `9.7909` edge `0.0086` maxDD `-0.4545`
- `market_context_high->fx_1h` score `0.0831` n `151` status `ready` deltaP `6.1417` edge `0.0018` maxDD `-0.1986`
- `market_context_high->fx_24h` score `0.0208` n `113` status `ready` deltaP `19.6196` edge `0.0291` maxDD `-1.2451`
- `market_context_high->commodity_1h` score `-0.2684` n `151` status `ready` deltaP `2.2951` edge `0.0124` maxDD `-1.0053`
- `market_context_high->metal_1h` score `-0.2885` n `151` status `ready` deltaP `6.2101` edge `0.0008` maxDD `-1.6682`
- `market_context_high->index_24h` score `-0.4416` n `113` status `ready` deltaP `11.4768` edge `-0.0049` maxDD `-4.925`
- `market_context_high->commodity_4h` score `-0.5267` n `140` status `ready` deltaP `5.3702` edge `0.0432` maxDD `-1.165`
- `market_context_high->index_1h` score `-0.583` n `151` status `ready` deltaP `-1.0568` edge `-0.0025` maxDD `-1.2155`
- `market_context_high->metal_4h` score `-1.0342` n `140` status `ready` deltaP `6.6028` edge `-0.0056` maxDD `-5.3474`
- `market_context_high->crypto_major_1h` score `-1.2608` n `151` status `ready` deltaP `1.8053` edge `-0.0156` maxDD `-9.3126`
- `market_context_high->index_4h` score `-1.9937` n `140` status `ready` deltaP `-6.79` edge `-0.0229` maxDD `-4.3282`
- `market_context_high->equity_1h` score `-2.299` n `151` status `ready` deltaP `-1.4603` edge `-0.0564` maxDD `-12.2891`
- `market_context_high->crypto_alt_1h` score `-2.4055` n `151` status `ready` deltaP `-2.8255` edge `-0.0411` maxDD `-13.2099`
- `market_context_high->crypto_major_24h` score `-4.4829` n `113` status `ready` deltaP `-2.0726` edge `-0.0752` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-5.1964` n `140` status `ready` deltaP `-3.8284` edge `-0.1367` maxDD `-32.9851`
- `market_context_high->equity_24h` score `-6.2835` n `113` status `ready` deltaP `-2.9914` edge `-0.2281` maxDD `-36.6024`
- `market_context_high->commodity_24h` score `-6.477` n `113` status `ready` deltaP `-18.8191` edge `-0.146` maxDD `-24.0477`
- `market_context_high->equity_4h` score `-8.0722` n `140` status `ready` deltaP `-5.7796` edge `-0.2702` maxDD `-45.7601`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
