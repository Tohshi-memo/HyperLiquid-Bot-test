# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-24T23:52:26.064873+00:00`
- Price records: `672`
- Market context records: `4670`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9870`

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

- `market_context_high->unknown_1h` score `72.483` n `143` status `ready` deltaP `9.9944` edge `6.0184` maxDD `-1.916`
- `market_context_high->unknown_4h` score `4.293` n `143` status `ready` deltaP `10.0941` edge `0.4115` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `1.4731` n `143` status `ready` deltaP `9.3884` edge `0.1525` maxDD `-4.7201`
- `market_context_high->commodity_1h` score `-0.4486` n `143` status `ready` deltaP `2.3428` edge `0.0266` maxDD `-2.0345`
- `market_context_high->fx_1h` score `-0.5414` n `143` status `ready` deltaP `-1.5515` edge `-0.0036` maxDD `-1.1038`
- `market_context_high->fx_4h` score `-0.7373` n `143` status `ready` deltaP `1.8473` edge `0.0014` maxDD `-1.9927`
- `market_context_high->index_4h` score `-0.7549` n `143` status `ready` deltaP `3.81` edge `-0.0099` maxDD `-5.9823`
- `market_context_high->equity_1h` score `-0.8453` n `143` status `ready` deltaP `-2.0969` edge `0.0043` maxDD `-5.5624`
- `market_context_high->commodity_4h` score `-1.2837` n `143` status `ready` deltaP `4.4218` edge `0.0167` maxDD `-9.1941`
- `market_context_high->equity_4h` score `-1.3162` n `143` status `ready` deltaP `1.4072` edge `-0.0012` maxDD `-8.8203`
- `market_context_high->index_1h` score `-1.6946` n `143` status `ready` deltaP `-4.1927` edge `-0.0124` maxDD `-2.7358`
- `market_context_high->metal_1h` score `-2.9187` n `143` status `ready` deltaP `-4.6994` edge `-0.0777` maxDD `-17.8795`
- `market_context_high->commodity_24h` score `-4.7238` n `143` status `ready` deltaP `13.7079` edge `0.0654` maxDD `-30.7016`
- `market_context_high->fx_24h` score `-5.0096` n `143` status `ready` deltaP `-10.5842` edge `-0.0106` maxDD `-5.9042`
- `market_context_high->crypto_alt_1h` score `-5.4061` n `143` status `ready` deltaP `-1.9472` edge `-0.1088` maxDD `-22.2982`
- `market_context_high->crypto_major_1h` score `-6.6518` n `143` status `ready` deltaP `-5.7944` edge `-0.1404` maxDD `-27.356`
- `market_context_high->index_24h` score `-7.6224` n `143` status `ready` deltaP `-7.4872` edge `-0.0478` maxDD `-29.3321`
- `market_context_high->crypto_alt_4h` score `-8.2619` n `143` status `ready` deltaP `-1.049` edge `-0.1865` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-9.5885` n `143` status `ready` deltaP `-3.6117` edge `-0.2873` maxDD `-67.0999`
- `market_context_high->crypto_major_4h` score `-11.4242` n `143` status `ready` deltaP `-3.326` edge `-0.3481` maxDD `-82.2164`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
