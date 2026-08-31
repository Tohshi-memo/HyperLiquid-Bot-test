# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-31T03:22:23.382718+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11636`

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

- `risk_on_high->crypto_alt_24h` score `21.037` n `55` status `ready` deltaP `46.19` edge `1.4932` maxDD `-3.1772`
- `risk_on_and_context->crypto_alt_24h` score `21.037` n `55` status `ready` deltaP `46.19` edge `1.4932` maxDD `-3.1772`
- `risk_on_high->unknown_4h` score `10.4687` n `92` status `ready` deltaP `31.356` edge `0.7062` maxDD `-1.0945`
- `risk_on_and_context->unknown_4h` score `10.4687` n `92` status `ready` deltaP `31.356` edge `0.7062` maxDD `-1.0945`
- `risk_on_high->crypto_major_24h` score `8.5792` n `55` status `ready` deltaP `27.3043` edge `0.6747` maxDD `-9.0103`
- `risk_on_and_context->crypto_major_24h` score `8.5792` n `55` status `ready` deltaP `27.3043` edge `0.6747` maxDD `-9.0103`
- `market_context_high->unknown_4h` score `7.4127` n `149` status `ready` deltaP `22.0914` edge `0.5133` maxDD `-1.0945`
- `risk_on_high->fx_24h` score `6.1209` n `55` status `ready` deltaP `68.5764` edge `0.0529` maxDD `0.0`
- `risk_on_and_context->fx_24h` score `6.1209` n `55` status `ready` deltaP `68.5764` edge `0.0529` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `4.8499` n `103` status `ready` deltaP `22.6419` edge `0.8898` maxDD `-27.517`
- `market_context_high->crypto_major_24h` score `4.8188` n `103` status `ready` deltaP `20.2434` edge `0.5157` maxDD `-17.2607`
- `risk_on_high->metal_24h` score `4.3708` n `55` status `ready` deltaP `40.5808` edge `0.1409` maxDD `-0.7767`
- `risk_on_and_context->metal_24h` score `4.3708` n `55` status `ready` deltaP `40.5808` edge `0.1409` maxDD `-0.7767`
- `market_context_high->metal_24h` score `4.1071` n `103` status `ready` deltaP `31.7017` edge `0.2229` maxDD `-3.0253`
- `risk_on_high->unknown_1h` score `2.9199` n `102` status `ready` deltaP `8.1866` edge `0.2464` maxDD `-1.9453`
- `risk_on_and_context->unknown_1h` score `2.9199` n `102` status `ready` deltaP `8.1866` edge `0.2464` maxDD `-1.9453`
- `market_context_high->unknown_1h` score `2.3065` n `161` status `ready` deltaP `6.5729` edge `0.2114` maxDD `-2.041`
- `market_context_high->fx_24h` score `1.0545` n `103` status `ready` deltaP `37.5084` edge `0.031` maxDD `-1.6688`
- `risk_on_high->commodity_24h` score `0.8561` n `55` status `ready` deltaP `9.6528` edge `0.1442` maxDD `-0.5706`
- `risk_on_and_context->commodity_24h` score `0.8561` n `55` status `ready` deltaP `9.6528` edge `0.1442` maxDD `-0.5706`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
