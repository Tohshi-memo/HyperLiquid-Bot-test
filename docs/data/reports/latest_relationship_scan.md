# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-13T12:29:58.568934+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11712`

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

- `market_context_high->unknown_24h` score `39.7395` n `161` status `ready` deltaP `-23.6898` edge `3.7608` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `12.0769` n `32` status `ready` deltaP `-42.1875` edge `1.9046` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `12.0769` n `32` status `ready` deltaP `-42.1875` edge `1.9046` maxDD `-1.6689`
- `news_risk_high->equity_4h` score `6.9956` n `36` status `ready` deltaP `37.1951` edge `0.335` maxDD `0.0`
- `risk_on_high->commodity_24h` score `3.5238` n `32` status `ready` deltaP `25.8681` edge `0.1212` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `3.5238` n `32` status `ready` deltaP `25.8681` edge `0.1212` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.5425` n `32` status `ready` deltaP `17.9116` edge `0.1107` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.5425` n `32` status `ready` deltaP `17.9116` edge `0.1107` maxDD `-0.1258`
- `risk_on_high->fx_24h` score `2.085` n `32` status `ready` deltaP `23.2639` edge `0.0371` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `2.085` n `32` status `ready` deltaP `23.2639` edge `0.0371` maxDD `-0.1418`
- `news_risk_high->index_4h` score `1.8727` n `36` status `ready` deltaP `21.2906` edge `0.0273` maxDD `-0.0546`
- `news_risk_high->equity_1h` score `1.5596` n `36` status `ready` deltaP `7.535` edge `0.1116` maxDD `-0.5496`
- `market_context_high->commodity_24h` score `1.5549` n `161` status `ready` deltaP `15.9302` edge `0.1037` maxDD `-2.4263`
- `risk_on_high->crypto_major_24h` score `1.3716` n `32` status `ready` deltaP `12.8472` edge `0.2058` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `1.3716` n `32` status `ready` deltaP `12.8472` edge `0.2058` maxDD `-6.2481`
- `market_context_high->commodity_4h` score `1.3609` n `161` status `ready` deltaP `15.563` edge `0.0735` maxDD `-2.1077`
- `risk_on_high->commodity_1h` score `1.1832` n `32` status `ready` deltaP `12.762` edge `0.0368` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.1832` n `32` status `ready` deltaP `12.762` edge `0.0368` maxDD `-0.1957`
- `risk_on_high->fx_4h` score `0.9707` n `32` status `ready` deltaP `11.2043` edge `0.0203` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `0.9707` n `32` status `ready` deltaP `11.2043` edge `0.0203` maxDD `-0.1285`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
