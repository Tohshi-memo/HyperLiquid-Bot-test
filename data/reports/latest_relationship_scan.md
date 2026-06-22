# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-22T11:22:33.335417+00:00`
- Price records: `672`
- Market context records: `4410`
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

- `risk_on_high->unknown_4h` score `122.9735` n `49` status `ready` deltaP `4.0256` edge `10.4028` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `122.9735` n `49` status `ready` deltaP `4.0256` edge `10.4028` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `31.3542` n `231` status `ready` deltaP `2.2754` edge `2.7473` maxDD `-9.6361`
- `market_context_high->unknown_4h` score `15.1583` n `225` status `ready` deltaP `5.8306` edge `1.7673` maxDD `-35.7719`
- `risk_on_high->unknown_24h` score `4.4668` n `44` status `ready` deltaP `20.0758` edge `0.3175` maxDD `-4.9954`
- `risk_on_and_context->unknown_24h` score `4.4668` n `44` status `ready` deltaP `20.0758` edge `0.3175` maxDD `-4.9954`
- `risk_on_high->equity_4h` score `3.2216` n `49` status `ready` deltaP `33.4775` edge `0.05` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `3.2216` n `49` status `ready` deltaP `33.4775` edge `0.05` maxDD `-0.044`
- `risk_on_high->metal_24h` score `3.0116` n `44` status `ready` deltaP `-15.3567` edge `0.5499` maxDD `-1.9133`
- `risk_on_and_context->metal_24h` score `3.0116` n `44` status `ready` deltaP `-15.3567` edge `0.5499` maxDD `-1.9133`
- `risk_on_high->crypto_major_4h` score `2.5239` n `49` status `ready` deltaP `20.937` edge `0.1373` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `2.5239` n `49` status `ready` deltaP `20.937` edge `0.1373` maxDD `-2.6576`
- `risk_on_high->equity_24h` score `1.6881` n `44` status `ready` deltaP `20.4861` edge `0.0041` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `1.6881` n `44` status `ready` deltaP `20.4861` edge `0.0041` maxDD `0.0`
- `risk_on_high->index_24h` score `1.635` n `44` status `ready` deltaP `23.4375` edge `-0.02` maxDD `0.0`
- `risk_on_and_context->index_24h` score `1.635` n `44` status `ready` deltaP `23.4375` edge `-0.02` maxDD `0.0`
- `risk_on_high->metal_4h` score `0.882` n `49` status `ready` deltaP `8.9037` edge `0.0477` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `0.882` n `49` status `ready` deltaP `8.9037` edge `0.0477` maxDD `-1.3516`
- `risk_on_high->equity_1h` score `0.6575` n `49` status `ready` deltaP `11.7531` edge `0.0154` maxDD `-0.7834`
- `risk_on_and_context->equity_1h` score `0.6575` n `49` status `ready` deltaP `11.7531` edge `0.0154` maxDD `-0.7834`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
