# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-15T15:52:45.898979+00:00`
- Price records: `672`
- Market context records: `4005`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10258`

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

- `risk_on_high->unknown_4h` score `146.7482` n `40` status `ready` deltaP `-3.4756` edge `12.4334` maxDD `-10.8303`
- `risk_on_and_context->unknown_4h` score `146.7482` n `40` status `ready` deltaP `-3.4756` edge `12.4334` maxDD `-10.8303`
- `market_context_high->unknown_24h` score `47.8536` n `136` status `ready` deltaP `-2.9616` edge `4.4094` maxDD `-24.1486`
- `market_context_high->unknown_4h` score `26.2524` n `147` status `ready` deltaP `2.97` edge `2.7088` maxDD `-35.6052`
- `risk_on_high->equity_24h` score `8.6305` n `40` status `ready` deltaP `41.1458` edge `0.4449` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `8.6305` n `40` status `ready` deltaP `41.1458` edge `0.4449` maxDD `0.0`
- `risk_on_high->equity_4h` score `3.9262` n `40` status `ready` deltaP `37.7439` edge `0.0803` maxDD `-0.0458`
- `risk_on_and_context->equity_4h` score `3.9262` n `40` status `ready` deltaP `37.7439` edge `0.0803` maxDD `-0.0458`
- `market_context_high->index_24h` score `3.4998` n `136` status `ready` deltaP `26.6135` edge `0.1961` maxDD `-5.5496`
- `market_context_high->metal_24h` score `2.9521` n `136` status `ready` deltaP `14.9714` edge `0.2865` maxDD `-8.2238`
- `risk_on_high->index_24h` score `2.3548` n `40` status `ready` deltaP `28.8194` edge `0.0041` maxDD `0.0`
- `risk_on_and_context->index_24h` score `2.3548` n `40` status `ready` deltaP `28.8194` edge `0.0041` maxDD `0.0`
- `market_context_high->equity_4h` score `1.9929` n `147` status `ready` deltaP `19.8357` edge `0.1641` maxDD `-7.0879`
- `market_context_high->equity_24h` score `1.8164` n `136` status `ready` deltaP `16.8811` edge `0.3418` maxDD `-14.5715`
- `risk_on_high->crypto_major_4h` score `1.4052` n `40` status `ready` deltaP `20.2134` edge `0.0489` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.4052` n `40` status `ready` deltaP `20.2134` edge `0.0489` maxDD `-2.6576`
- `market_context_high->metal_1h` score `1.1716` n `147` status `ready` deltaP `12.5718` edge `0.0613` maxDD `-1.7983`
- `risk_on_high->commodity_24h` score `1.0479` n `40` status `ready` deltaP `4.1667` edge `0.2877` maxDD `-12.9187`
- `risk_on_and_context->commodity_24h` score `1.0479` n `40` status `ready` deltaP `4.1667` edge `0.2877` maxDD `-12.9187`
- `market_context_high->crypto_major_1h` score `0.9405` n `147` status `ready` deltaP `9.809` edge `0.0672` maxDD `-2.3372`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
