# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-22T12:52:32.405497+00:00`
- Price records: `672`
- Market context records: `4416`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11123`

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

- `risk_on_high->unknown_4h` score `123.1467` n `49` status `ready` deltaP `3.4159` edge `10.4213` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `123.1467` n `49` status `ready` deltaP `3.4159` edge `10.4213` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `31.2422` n `232` status `ready` deltaP `2.1346` edge `2.7389` maxDD `-9.6361`
- `market_context_high->unknown_4h` score `14.823` n `229` status `ready` deltaP `5.7954` edge `1.7396` maxDD `-35.7719`
- `risk_on_high->unknown_24h` score `4.7776` n `44` status `ready` deltaP `20.0758` edge `0.3434` maxDD `-4.9954`
- `risk_on_and_context->unknown_24h` score `4.7776` n `44` status `ready` deltaP `20.0758` edge `0.3434` maxDD `-4.9954`
- `risk_on_high->equity_4h` score `3.1514` n `49` status `ready` deltaP `33.0202` edge `0.0472` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `3.1514` n `49` status `ready` deltaP `33.0202` edge `0.0472` maxDD `-0.044`
- `risk_on_high->metal_24h` score `3.0576` n `44` status `ready` deltaP `-15.3567` edge `0.5558` maxDD `-1.9133`
- `risk_on_and_context->metal_24h` score `3.0576` n `44` status `ready` deltaP `-15.3567` edge `0.5558` maxDD `-1.9133`
- `risk_on_high->crypto_major_4h` score `2.4129` n `49` status `ready` deltaP `20.4797` edge `0.1311` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `2.4129` n `49` status `ready` deltaP `20.4797` edge `0.1311` maxDD `-2.6576`
- `risk_on_high->index_24h` score `1.7226` n `44` status `ready` deltaP `23.4375` edge `-0.0127` maxDD `0.0`
- `risk_on_and_context->index_24h` score `1.7226` n `44` status `ready` deltaP `23.4375` edge `-0.0127` maxDD `0.0`
- `risk_on_high->equity_24h` score `1.6519` n `44` status `ready` deltaP `20.1389` edge `0.0034` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `1.6519` n `44` status `ready` deltaP `20.1389` edge `0.0034` maxDD `0.0`
- `risk_on_high->metal_4h` score `0.9684` n `49` status `ready` deltaP `8.9037` edge `0.0549` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `0.9684` n `49` status `ready` deltaP `8.9037` edge `0.0549` maxDD `-1.3516`
- `risk_on_high->equity_1h` score `0.6156` n `49` status `ready` deltaP `11.304` edge `0.0149` maxDD `-0.7834`
- `risk_on_and_context->equity_1h` score `0.6156` n `49` status `ready` deltaP `11.304` edge `0.0149` maxDD `-0.7834`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
