# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-03T16:52:25.579358+00:00`
- Price records: `672`
- Market context records: `2782`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9237`

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

- `market_context_high->unknown_24h` score `3.5713` n `140` status `ready` deltaP `7.3015` edge `0.2954` maxDD `-1.7175`
- `market_context_high->crypto_alt_24h` score `3.1215` n `140` status `ready` deltaP `4.3651` edge `0.6227` maxDD `-22.6673`
- `market_context_high->unknown_4h` score `0.8856` n `142` status `ready` deltaP `6.1856` edge `0.1379` maxDD `-3.7602`
- `market_context_high->commodity_24h` score `0.3161` n `140` status `ready` deltaP `10.6051` edge `0.2792` maxDD `-12.4171`
- `market_context_high->index_4h` score `0.2334` n `142` status `ready` deltaP `12.3862` edge `0.0315` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `-0.0733` n `142` status `ready` deltaP `3.732` edge `0.0421` maxDD `-3.1801`
- `market_context_high->index_1h` score `-0.1194` n `142` status `ready` deltaP `3.7489` edge `0.0091` maxDD `-1.2855`
- `market_context_high->fx_1h` score `-0.5622` n `142` status `ready` deltaP `-0.837` edge `0.0031` maxDD `-0.2164`
- `market_context_high->metal_1h` score `-0.6396` n `142` status `ready` deltaP `0.4322` edge `-0.0003` maxDD `-3.0996`
- `market_context_high->commodity_1h` score `-0.6686` n `142` status `ready` deltaP `-0.7316` edge `-0.0055` maxDD `-4.3601`
- `market_context_high->crypto_alt_1h` score `-0.6882` n `142` status `ready` deltaP `5.0962` edge `0.0538` maxDD `-10.747`
- `market_context_high->crypto_major_1h` score `-0.9092` n `142` status `ready` deltaP `3.926` edge `0.0442` maxDD `-9.622`
- `market_context_high->equity_1h` score `-1.0561` n `142` status `ready` deltaP `-3.4979` edge `0.0186` maxDD `-2.6634`
- `market_context_high->fx_4h` score `-1.1081` n `142` status `ready` deltaP `-3.2957` edge `0.0075` maxDD `-0.5631`
- `market_context_high->crypto_alt_4h` score `-1.3925` n `142` status `ready` deltaP `13.8805` edge `0.2255` maxDD `-28.7261`
- `market_context_high->fx_24h` score `-1.3935` n `140` status `ready` deltaP `-1.1756` edge `-0.0211` maxDD `-0.6418`
- `market_context_high->equity_4h` score `-1.4865` n `142` status `ready` deltaP `1.0477` edge `0.0071` maxDD `-5.7037`
- `market_context_high->commodity_4h` score `-1.572` n `142` status `ready` deltaP `0.161` edge `-0.0106` maxDD `-10.0279`
- `market_context_high->metal_4h` score `-2.2234` n `142` status `ready` deltaP `-1.3805` edge `-0.0208` maxDD `-11.4038`
- `market_context_high->crypto_major_4h` score `-2.4951` n `142` status `ready` deltaP `5.4298` edge `0.1345` maxDD `-32.2466`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
