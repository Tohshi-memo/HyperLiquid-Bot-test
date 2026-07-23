# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-23T14:07:39.142128+00:00`
- Price records: `672`
- Market context records: `7675`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14675`

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

- `market_context_high->index_1h` score `0.032` n `146` status `ready` deltaP `6.0616` edge `0.0116` maxDD `-0.8324`
- `market_context_high->crypto_major_1h` score `-0.1004` n `146` status `ready` deltaP `8.6047` edge `0.0258` maxDD `-4.0162`
- `market_context_high->crypto_alt_1h` score `-0.1679` n `146` status `ready` deltaP `2.8033` edge `0.023` maxDD `-2.7243`
- `market_context_high->fx_24h` score `-0.3184` n `145` status `ready` deltaP `9.4545` edge `0.0192` maxDD `-3.0343`
- `market_context_high->commodity_1h` score `-0.4428` n `146` status `ready` deltaP `0.6273` edge `-0.0039` maxDD `-1.5641`
- `market_context_high->equity_1h` score `-0.572` n `146` status `ready` deltaP `4.4758` edge `0.0482` maxDD `-7.7764`
- `market_context_high->metal_1h` score `-0.6294` n `146` status `ready` deltaP `1.2386` edge `0.0156` maxDD `-1.0307`
- `market_context_high->index_4h` score `-0.7342` n `146` status `ready` deltaP `7.3813` edge `0.0268` maxDD `-3.2774`
- `market_context_high->fx_1h` score `-0.741` n `146` status `ready` deltaP `-1.4727` edge `-0.002` maxDD `-0.6615`
- `market_context_high->commodity_4h` score `-0.9191` n `146` status `ready` deltaP `0.0775` edge `-0.0026` maxDD `-2.2943`
- `market_context_high->crypto_alt_4h` score `-0.9253` n `146` status `ready` deltaP `3.197` edge `0.059` maxDD `-9.5815`
- `market_context_high->crypto_major_4h` score `-1.0999` n `146` status `ready` deltaP `9.7414` edge `0.0618` maxDD `-14.4206`
- `market_context_high->commodity_24h` score `-1.3197` n `145` status `ready` deltaP `7.3159` edge `-0.0004` maxDD `-7.0012`
- `market_context_high->unknown_1h` score `-1.5062` n `146` status `ready` deltaP `-1.2837` edge `-0.0546` maxDD `-1.3217`
- `market_context_high->metal_4h` score `-1.6872` n `146` status `ready` deltaP `-2.5852` edge `0.0466` maxDD `-4.6535`
- `market_context_high->equity_4h` score `-1.9646` n `146` status `ready` deltaP `-0.6912` edge `0.1671` maxDD `-20.4824`
- `market_context_high->metal_24h` score `-2.2863` n `146` status `ready` deltaP `-3.2772` edge `0.0544` maxDD `-7.3868`
- `market_context_high->fx_4h` score `-2.6654` n `146` status `ready` deltaP `-7.2703` edge `-0.0052` maxDD `-2.1425`
- `market_context_high->equity_24h` score `-3.037` n `145` status `ready` deltaP `11.9248` edge `0.0217` maxDD `-34.5784`
- `market_context_high->index_24h` score `-3.7087` n `145` status `ready` deltaP `-21.7818` edge `-0.0455` maxDD `-8.114`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
