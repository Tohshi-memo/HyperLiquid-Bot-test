# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-12T07:37:27.823119+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11792`

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

- `risk_on_high->equity_24h` score `4.0882` n `32` status `ready` deltaP `10.7639` edge `0.6303` maxDD `-11.2348`
- `risk_on_and_context->equity_24h` score `4.0882` n `32` status `ready` deltaP `10.7639` edge `0.6303` maxDD `-11.2348`
- `risk_on_high->crypto_major_24h` score `3.4109` n `32` status `ready` deltaP `23.2639` edge `0.3978` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `3.4109` n `32` status `ready` deltaP `23.2639` edge `0.3978` maxDD `-6.2481`
- `risk_on_high->index_24h` score `2.1932` n `32` status `ready` deltaP `17.8819` edge `0.094` maxDD `-0.4355`
- `risk_on_and_context->index_24h` score `2.1932` n `32` status `ready` deltaP `17.8819` edge `0.094` maxDD `-0.4355`
- `risk_on_high->commodity_24h` score `2.1115` n `32` status `ready` deltaP `18.9236` edge `0.0498` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `2.1115` n `32` status `ready` deltaP `18.9236` edge `0.0498` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.0534` n `32` status `ready` deltaP `13.6433` edge `0.0984` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.0534` n `32` status `ready` deltaP `13.6433` edge `0.0984` maxDD `-0.1258`
- `risk_on_high->fx_24h` score `1.9468` n `32` status `ready` deltaP `21.7014` edge `0.036` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `1.9468` n `32` status `ready` deltaP `21.7014` edge `0.036` maxDD `-0.1418`
- `risk_on_high->commodity_1h` score `1.0706` n `32` status `ready` deltaP `11.7141` edge `0.0344` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.0706` n `32` status `ready` deltaP `11.7141` edge `0.0344` maxDD `-0.1957`
- `risk_on_high->fx_4h` score `0.8233` n `32` status `ready` deltaP `9.5274` edge `0.0192` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `0.8233` n `32` status `ready` deltaP `9.5274` edge `0.0192` maxDD `-0.1285`
- `market_context_high->commodity_1h` score `0.6638` n `180` status `ready` deltaP `9.6308` edge `0.0233` maxDD `-0.5752`
- `risk_on_high->index_1h` score `0.3654` n `32` status `ready` deltaP `11.003` edge `0.011` maxDD `-0.3343`
- `risk_on_and_context->index_1h` score `0.3654` n `32` status `ready` deltaP `11.003` edge `0.011` maxDD `-0.3343`
- `market_context_high->commodity_4h` score `0.3198` n `180` status `ready` deltaP `7.185` edge `0.0426` maxDD `-2.1077`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
