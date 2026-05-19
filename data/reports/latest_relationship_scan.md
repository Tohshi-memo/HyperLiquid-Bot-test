# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-19T04:21:54.987182+00:00`
- Price records: `672`
- Market context records: `1185`
- Flow alert records: `5316`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8768`

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

- `market_context_high->crypto_major_24h` score `18.6213` n `143` status `ready` deltaP `44.4105` edge `1.3689` maxDD `-8.0553`
- `market_context_high->crypto_alt_24h` score `8.159` n `143` status `ready` deltaP `22.2077` edge `0.7335` maxDD `-15.1306`
- `market_context_high->metal_24h` score `4.3203` n `143` status `ready` deltaP `-2.9332` edge `0.5463` maxDD `-6.3373`
- `market_context_high->equity_4h` score `2.7255` n `143` status `ready` deltaP `14.6629` edge `0.1957` maxDD `-3.6396`
- `market_context_high->unknown_4h` score `2.7238` n `143` status `ready` deltaP `4.9399` edge `0.3157` maxDD `-6.7322`
- `market_context_high->index_24h` score `2.4685` n `143` status `ready` deltaP `15.0362` edge `0.2141` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.3917` n `143` status `ready` deltaP `15.3737` edge `0.3295` maxDD `-14.2815`
- `market_context_high->index_4h` score `1.0836` n `143` status `ready` deltaP `10.4405` edge `0.089` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.674` n `143` status `ready` deltaP `9.6541` edge `0.0235` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.2762` n `143` status `ready` deltaP `2.7124` edge `0.0427` maxDD `-1.3546`
- `market_context_high->fx_1h` score `-0.0483` n `143` status `ready` deltaP `5.9975` edge `-0.0006` maxDD `-0.3124`
- `market_context_high->crypto_major_4h` score `-0.1612` n `143` status `ready` deltaP `6.9216` edge `0.1253` maxDD `-8.3693`
- `market_context_high->crypto_major_1h` score `-0.2932` n `143` status `ready` deltaP `3.8975` edge `0.013` maxDD `-4.1256`
- `market_context_high->metal_1h` score `-0.2969` n `143` status `ready` deltaP `7.349` edge `-0.0127` maxDD `-2.2164`
- `market_context_high->crypto_alt_1h` score `-0.472` n `143` status `ready` deltaP `-0.3946` edge `0.0264` maxDD `-3.4088`
- `market_context_high->fx_24h` score `-0.7016` n `143` status `ready` deltaP `6.2488` edge `0.0297` maxDD `-7.9051`
- `market_context_high->fx_4h` score `-1.0066` n `143` status `ready` deltaP `-4.5912` edge `-0.0055` maxDD `-1.1026`
- `market_context_high->commodity_1h` score `-1.0095` n `143` status `ready` deltaP `-3.5468` edge `0.001` maxDD `-2.252`
- `market_context_high->crypto_alt_4h` score `-1.3641` n `143` status `ready` deltaP `3.0019` edge `0.1016` maxDD `-16.7194`
- `market_context_high->commodity_24h` score `-1.4536` n `143` status `ready` deltaP `-4.9643` edge `0.4328` maxDD `-41.8856`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
