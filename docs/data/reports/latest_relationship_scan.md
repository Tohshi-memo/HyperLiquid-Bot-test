# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-24T14:52:32.920951+00:00`
- Price records: `672`
- Market context records: `4631`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9851`

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

- `market_context_high->unknown_1h` score `70.02` n `146` status `ready` deltaP `8.3094` edge `5.8255` maxDD `-2.0052`
- `market_context_high->unknown_4h` score `4.4031` n `146` status `ready` deltaP `9.5807` edge `0.4241` maxDD `-4.6834`
- `market_context_high->commodity_1h` score `-0.3137` n `146` status `ready` deltaP `3.398` edge `0.0308` maxDD `-2.0345`
- `market_context_high->fx_1h` score `-0.5567` n `146` status `ready` deltaP `-1.8005` edge `-0.0039` maxDD `-1.1038`
- `market_context_high->fx_4h` score `-0.7515` n `146` status `ready` deltaP `1.7541` edge `0.0002` maxDD `-1.9927`
- `market_context_high->equity_1h` score `-0.8211` n `146` status `ready` deltaP `-1.9461` edge `0.0064` maxDD `-5.5624`
- `market_context_high->index_4h` score `-0.9133` n `146` status `ready` deltaP `1.4388` edge `-0.0144` maxDD `-5.9823`
- `market_context_high->commodity_4h` score `-0.9826` n `146` status `ready` deltaP `5.9534` edge `0.0451` maxDD `-9.1941`
- `market_context_high->unknown_24h` score `-1.2533` n `144` status `ready` deltaP `5.7291` edge `-0.0503` maxDD `-4.7201`
- `market_context_high->equity_4h` score `-1.6422` n `146` status `ready` deltaP `-0.6933` edge `-0.029` maxDD `-8.8203`
- `market_context_high->index_1h` score `-1.7131` n `146` status `ready` deltaP `-4.3639` edge `-0.0128` maxDD `-2.7358`
- `market_context_high->metal_1h` score `-2.9673` n `146` status `ready` deltaP `-4.5402` edge `-0.085` maxDD `-17.8795`
- `market_context_high->commodity_24h` score `-4.7009` n `144` status `ready` deltaP `11.9791` edge `0.0533` maxDD `-29.3255`
- `market_context_high->fx_24h` score `-5.0854` n `144` status `ready` deltaP `-9.5486` edge `-0.0089` maxDD `-6.0982`
- `market_context_high->crypto_alt_1h` score `-5.5823` n `146` status `ready` deltaP `-2.3952` edge `-0.1205` maxDD `-22.2982`
- `market_context_high->crypto_major_1h` score `-6.7912` n `146` status `ready` deltaP `-5.9921` edge `-0.1507` maxDD `-27.356`
- `market_context_high->index_24h` score `-8.1113` n `144` status `ready` deltaP `-8.3334` edge `-0.0829` maxDD `-29.3321`
- `market_context_high->crypto_alt_4h` score `-9.1296` n `146` status `ready` deltaP `-3.2012` edge `-0.2834` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-10.2014` n `146` status `ready` deltaP `-6.5382` edge `-0.3429` maxDD `-67.3775`
- `market_context_high->crypto_major_4h` score `-12.2795` n `146` status `ready` deltaP `-5.254` edge `-0.4449` maxDD `-82.2164`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
