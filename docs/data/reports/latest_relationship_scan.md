# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-03T17:37:39.344700+00:00`
- Price records: `672`
- Market context records: `2785`
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

- `market_context_high->unknown_24h` score `3.2741` n `142` status `ready` deltaP `6.4211` edge `0.2765` maxDD `-1.7175`
- `market_context_high->crypto_alt_24h` score `2.7732` n `142` status `ready` deltaP `4.0909` edge `0.5955` maxDD `-22.6673`
- `market_context_high->unknown_4h` score `0.8556` n `142` status `ready` deltaP `6.1856` edge `0.1354` maxDD `-3.7602`
- `market_context_high->commodity_24h` score `0.5593` n `142` status `ready` deltaP `11.0377` edge `0.2824` maxDD `-12.4171`
- `market_context_high->index_4h` score `0.2845` n `142` status `ready` deltaP `12.8435` edge `0.035` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `-0.0901` n `142` status `ready` deltaP `3.732` edge `0.0407` maxDD `-3.1801`
- `market_context_high->index_1h` score `-0.0906` n `142` status `ready` deltaP `4.198` edge `0.0098` maxDD `-1.2855`
- `market_context_high->fx_1h` score `-0.5622` n `142` status `ready` deltaP `-0.837` edge `0.0031` maxDD `-0.2164`
- `market_context_high->metal_1h` score `-0.6396` n `142` status `ready` deltaP `0.4322` edge `-0.0003` maxDD `-3.0996`
- `market_context_high->commodity_1h` score `-0.688` n `142` status `ready` deltaP `-0.8813` edge `-0.007` maxDD `-4.3601`
- `market_context_high->crypto_alt_1h` score `-0.7287` n `142` status `ready` deltaP `4.7968` edge `0.0506` maxDD `-10.747`
- `market_context_high->crypto_major_1h` score `-0.942` n `142` status `ready` deltaP `3.6266` edge `0.042` maxDD `-9.622`
- `market_context_high->equity_1h` score `-1.019` n `142` status `ready` deltaP `-3.1985` edge `0.0197` maxDD `-2.6634`
- `market_context_high->fx_4h` score `-1.0947` n `142` status `ready` deltaP `-3.1432` edge `0.0076` maxDD `-0.5631`
- `market_context_high->crypto_alt_4h` score `-1.3105` n `142` status `ready` deltaP `14.1854` edge `0.2303` maxDD `-28.7261`
- `market_context_high->equity_4h` score `-1.3263` n `142` status `ready` deltaP `1.5051` edge `0.0174` maxDD `-5.7037`
- `market_context_high->fx_24h` score `-1.4134` n `142` status `ready` deltaP `-1.3644` edge `-0.0215` maxDD `-0.6418`
- `market_context_high->commodity_4h` score `-1.6215` n `142` status `ready` deltaP `-0.2963` edge `-0.0139` maxDD `-10.0279`
- `market_context_high->metal_4h` score `-2.1653` n `142` status `ready` deltaP `-0.9232` edge `-0.0164` maxDD `-11.4038`
- `market_context_high->crypto_major_4h` score `-2.4246` n `142` status `ready` deltaP `5.7347` edge `0.1415` maxDD `-32.2466`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
