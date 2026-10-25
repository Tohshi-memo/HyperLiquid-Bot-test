# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-25T17:07:27.147641+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5378`

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

- `market_context_high->unknown_4h` score `31.1061` n `113` status `ready` deltaP `-0.7487` edge `2.6307` maxDD `-1.016`
- `market_context_high->fx_4h` score `-0.0427` n `113` status `ready` deltaP `7.1539` edge `0.0086` maxDD `-0.4545`
- `market_context_high->fx_1h` score `-0.0498` n `113` status `ready` deltaP `3.8591` edge `0.0028` maxDD `-0.1258`
- `market_context_high->commodity_24h` score `-0.377` n `66` status `ready` deltaP `4.3245` edge `0.0304` maxDD `-3.6055`
- `market_context_high->commodity_1h` score `-0.4655` n `113` status `ready` deltaP `0.2663` edge `0.0095` maxDD `-1.0053`
- `market_context_high->metal_1h` score `-0.6527` n `113` status `ready` deltaP `4.4844` edge `-0.0051` maxDD `-1.6682`
- `market_context_high->index_1h` score `-0.7095` n `113` status `ready` deltaP `-2.9344` edge `-0.0062` maxDD `-1.2155`
- `market_context_high->commodity_4h` score `-0.785` n `113` status `ready` deltaP `-1.4759` edge `0.0321` maxDD `-1.165`
- `market_context_high->crypto_major_24h` score `-0.9284` n `66` status `ready` deltaP `-2.4779` edge `0.0417` maxDD `-4.5369`
- `market_context_high->fx_24h` score `-1.2601` n `66` status `ready` deltaP `6.108` edge `0.0115` maxDD `-1.2451`
- `market_context_high->crypto_major_1h` score `-1.362` n `113` status `ready` deltaP `2.6482` edge `-0.0342` maxDD `-9.3126`
- `market_context_high->index_24h` score `-1.8444` n `66` status `ready` deltaP `0.805` edge `-0.1136` maxDD `-4.925`
- `market_context_high->metal_4h` score `-1.8964` n `113` status `ready` deltaP `4.7661` edge `-0.0188` maxDD `-5.3474`
- `market_context_high->index_4h` score `-2.206` n `113` status `ready` deltaP `-8.6822` edge `-0.0375` maxDD `-4.3282`
- `market_context_high->metal_24h` score `-3.1184` n `66` status `ready` deltaP `-4.9558` edge `0.0402` maxDD `-7.3625`
- `market_context_high->crypto_alt_1h` score `-3.2158` n `113` status `ready` deltaP `-2.1594` edge `-0.0662` maxDD `-11.3243`
- `market_context_high->equity_1h` score `-3.9578` n `113` status `ready` deltaP `-1.2877` edge `-0.0939` maxDD `-12.1865`
- `market_context_high->crypto_alt_24h` score `-6.938` n `66` status `ready` deltaP `-1.3416` edge `-0.2349` maxDD `-42.3182`
- `market_context_high->crypto_major_4h` score `-10.0188` n `113` status `ready` deltaP `-13.0477` edge `-0.2481` maxDD `-32.9851`
- `market_context_high->equity_24h` score `-10.9178` n `66` status `ready` deltaP `-14.0783` edge `-0.7775` maxDD `-36.6024`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
