# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-16T17:52:25.021438+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11830`

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

- `market_context_high->unknown_24h` score `225.3493` n `88` status `ready` deltaP `-21.512` edge `29.3027` maxDD `-7.8016`
- `market_context_high->commodity_24h` score `7.9657` n `88` status `ready` deltaP `41.3037` edge `0.3942` maxDD `-0.1266`
- `market_context_high->commodity_4h` score `1.4596` n `125` status `ready` deltaP `14.2268` edge `0.0739` maxDD `-0.7687`
- `market_context_high->commodity_1h` score `-0.0758` n `127` status `ready` deltaP `2.3127` edge `0.0194` maxDD `-0.624`
- `market_context_high->fx_4h` score `-0.2902` n `125` status `ready` deltaP `4.5122` edge `0.0062` maxDD `-0.504`
- `market_context_high->fx_1h` score `-0.2975` n `127` status `ready` deltaP `0.9206` edge `0.0014` maxDD `-0.2527`
- `market_context_high->metal_1h` score `-0.4951` n `127` status `ready` deltaP `2.0852` edge `-0.0058` maxDD `-1.7257`
- `market_context_high->index_1h` score `-0.7953` n `127` status `ready` deltaP `-7.0194` edge `-0.003` maxDD `-0.5064`
- `market_context_high->metal_4h` score `-0.8808` n `125` status `ready` deltaP `8.5902` edge `-0.0128` maxDD `-4.5909`
- `market_context_high->fx_24h` score `-1.3473` n `88` status `ready` deltaP `-6.6288` edge `0.0322` maxDD `-1.8596`
- `market_context_high->equity_1h` score `-1.6594` n `127` status `ready` deltaP `-9.5643` edge `-0.045` maxDD `-4.9849`
- `market_context_high->metal_24h` score `-1.8845` n `88` status `ready` deltaP `-9.0909` edge `0.0702` maxDD `-7.0954`
- `market_context_high->crypto_alt_1h` score `-1.9268` n `127` status `ready` deltaP `-1.2919` edge `-0.018` maxDD `-7.0497`
- `market_context_high->index_4h` score `-2.0338` n `125` status `ready` deltaP `-11.8707` edge `-0.0091` maxDD `-0.8328`
- `market_context_high->crypto_major_1h` score `-2.0696` n `127` status `ready` deltaP `-5.4175` edge `-0.031` maxDD `-5.4277`
- `market_context_high->index_24h` score `-2.1337` n `88` status `ready` deltaP `-7.4495` edge `-0.0699` maxDD `-2.3194`
- `market_context_high->crypto_major_4h` score `-3.7226` n `125` status `ready` deltaP `-1.3902` edge `-0.0652` maxDD `-13.1929`
- `market_context_high->crypto_major_24h` score `-5.0623` n `88` status `ready` deltaP `-6.392` edge `-0.0207` maxDD `-35.189`
- `market_context_high->unknown_1h` score `-7.147` n `127` status `ready` deltaP `0.4715` edge `-0.553` maxDD `-1.3246`
- `market_context_high->crypto_alt_4h` score `-7.9693` n `125` status `ready` deltaP `-11.6` edge `-0.0989` maxDD `-26.3633`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
