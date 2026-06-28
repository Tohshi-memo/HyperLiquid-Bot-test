# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-28T04:07:27.434996+00:00`
- Price records: `672`
- Market context records: `5004`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10290`

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

- `market_context_high->unknown_1h` score `15.1915` n `93` status `ready` deltaP `3.9679` edge `1.2896` maxDD `-1.674`
- `market_context_high->unknown_4h` score `9.8586` n `92` status `ready` deltaP `22.541` edge `0.7735` maxDD `-5.5109`
- `market_context_high->crypto_major_4h` score `5.8237` n `92` status `ready` deltaP `18.2463` edge `0.5221` maxDD `-8.3416`
- `market_context_high->crypto_alt_4h` score `5.211` n `92` status `ready` deltaP `13.746` edge `0.482` maxDD `-7.8181`
- `market_context_high->unknown_24h` score `5.0797` n `74` status `ready` deltaP `29.8142` edge `0.2588` maxDD `-1.4072`
- `market_context_high->metal_4h` score `1.2855` n `92` status `ready` deltaP `13.5339` edge `0.1248` maxDD `-1.9651`
- `market_context_high->equity_1h` score `0.8644` n `93` status `ready` deltaP `8.0371` edge `0.0758` maxDD `-2.5875`
- `market_context_high->crypto_major_1h` score `0.8189` n `93` status `ready` deltaP `6.2536` edge `0.1183` maxDD `-4.6734`
- `market_context_high->equity_4h` score `0.5342` n `92` status `ready` deltaP `4.1159` edge `0.1792` maxDD `-6.3852`
- `market_context_high->metal_1h` score `0.3365` n `93` status `ready` deltaP `5.9542` edge `0.038` maxDD `-1.3057`
- `market_context_high->crypto_alt_1h` score `0.1469` n `93` status `ready` deltaP `4.8113` edge `0.089` maxDD `-5.5126`
- `market_context_high->index_4h` score `0.0093` n `92` status `ready` deltaP `4.6859` edge `0.0411` maxDD `-1.0586`
- `market_context_high->fx_24h` score `-0.162` n `74` status `ready` deltaP `7.4747` edge `0.0056` maxDD `-1.7626`
- `market_context_high->commodity_1h` score `-0.2691` n `93` status `ready` deltaP `2.4564` edge `0.0151` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.5694` n `93` status `ready` deltaP `2.062` edge `0.0129` maxDD `-0.5946`
- `market_context_high->commodity_4h` score `-0.7676` n `92` status `ready` deltaP `4.4937` edge `-0.0031` maxDD `-5.021`
- `market_context_high->fx_4h` score `-0.9556` n `92` status `ready` deltaP `-3.2609` edge `-0.0021` maxDD `-1.2274`
- `market_context_high->fx_1h` score `-1.7342` n `93` status `ready` deltaP `-11.6992` edge `-0.0055` maxDD `-0.5482`
- `market_context_high->metal_24h` score `-4.116` n `74` status `ready` deltaP `0.8681` edge `0.012` maxDD `-32.9721`
- `market_context_high->commodity_24h` score `-4.1785` n `74` status `ready` deltaP `5.6212` edge `-0.0623` maxDD `-27.5371`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
