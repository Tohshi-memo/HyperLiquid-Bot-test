# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-24T15:22:30.926809+00:00`
- Price records: `672`
- Market context records: `4634`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9996`

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

- `market_context_high->unknown_1h` score `70.0044` n `146` status `ready` deltaP `8.3094` edge `5.8242` maxDD `-2.0052`
- `market_context_high->unknown_4h` score `4.4283` n `146` status `ready` deltaP `9.5807` edge `0.4262` maxDD `-4.6834`
- `market_context_high->commodity_1h` score `-0.3101` n `146` status `ready` deltaP `3.398` edge `0.0311` maxDD `-2.0345`
- `market_context_high->fx_1h` score `-0.5645` n `146` status `ready` deltaP `-1.9502` edge `-0.0039` maxDD `-1.1038`
- `market_context_high->fx_4h` score `-0.7428` n `146` status `ready` deltaP `1.9066` edge `0.0003` maxDD `-1.9927`
- `market_context_high->equity_1h` score `-0.8507` n `146` status `ready` deltaP `-2.2455` edge `0.0046` maxDD `-5.5624`
- `market_context_high->index_4h` score `-0.9038` n `146` status `ready` deltaP `1.5912` edge `-0.0142` maxDD `-5.9823`
- `market_context_high->commodity_4h` score `-0.9904` n `146` status `ready` deltaP `5.9534` edge `0.0441` maxDD `-9.1941`
- `market_context_high->unknown_24h` score `-1.3139` n `146` status `ready` deltaP `5.0015` edge `-0.0505` maxDD `-4.7201`
- `market_context_high->equity_4h` score `-1.5882` n `146` status `ready` deltaP `-0.3884` edge `-0.0241` maxDD `-8.8203`
- `market_context_high->index_1h` score `-1.7394` n `146` status `ready` deltaP `-4.6633` edge `-0.013` maxDD `-2.7358`
- `market_context_high->metal_1h` score `-2.9642` n `146` status `ready` deltaP `-4.5402` edge `-0.0846` maxDD `-17.8795`
- `market_context_high->fx_24h` score `-4.9905` n `146` status `ready` deltaP `-8.5117` edge `-0.0079` maxDD `-6.0982`
- `market_context_high->commodity_24h` score `-5.1493` n `146` status `ready` deltaP `11.2847` edge `0.0461` maxDD `-30.7016`
- `market_context_high->crypto_alt_1h` score `-5.6063` n `146` status `ready` deltaP `-2.5449` edge `-0.1215` maxDD `-22.2982`
- `market_context_high->crypto_major_1h` score `-6.8055` n `146` status `ready` deltaP `-6.1418` edge `-0.1509` maxDD `-27.356`
- `market_context_high->index_24h` score `-7.9586` n `146` status `ready` deltaP `-7.6104` edge `-0.075` maxDD `-29.3321`
- `market_context_high->crypto_alt_4h` score `-9.0521` n `146` status `ready` deltaP `-2.8963` edge `-0.2755` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-10.1622` n `146` status `ready` deltaP `-6.2333` edge `-0.3399` maxDD `-67.3775`
- `market_context_high->crypto_major_4h` score `-12.1966` n `146` status `ready` deltaP `-4.9491` edge `-0.4363` maxDD `-82.2164`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
