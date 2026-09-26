# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-26T06:52:30.921010+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11840`

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

- `news_risk_high->unknown_24h` score `3407.038` n `102` status `ready` deltaP `-0.6332` edge `283.9285` maxDD `-0.0226`
- `market_context_high->unknown_1h` score `69.9129` n `47` status `ready` deltaP `8.7687` edge `5.7747` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `48.2961` n `47` status `ready` deltaP `24.1726` edge `3.9028` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `29.6668` n `47` status `ready` deltaP `22.3515` edge `2.3612` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.3503` n `47` status `ready` deltaP `33.3739` edge `1.9256` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.249` n `47` status `ready` deltaP `31.117` edge `0.4096` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.4329` n `47` status `ready` deltaP `28.982` edge `0.1167` maxDD `-0.2401`
- `market_context_high->equity_4h` score `2.7265` n `47` status `ready` deltaP `17.2969` edge `0.1537` maxDD `-1.3444`
- `market_context_high->index_4h` score `2.5054` n `47` status `ready` deltaP `28.8434` edge `0.0319` maxDD `-0.2323`
- `market_context_high->crypto_alt_4h` score `1.3345` n `47` status `ready` deltaP `11.5172` edge `0.1012` maxDD `-3.3417`
- `news_risk_high->metal_24h` score `1.2289` n `102` status `ready` deltaP `28.0433` edge `0.1367` maxDD `-6.9545`
- `market_context_high->equity_1h` score `1.0637` n `47` status `ready` deltaP `12.2149` edge `0.0475` maxDD `-1.5564`
- `market_context_high->index_1h` score `0.7702` n `47` status `ready` deltaP `12.3646` edge `0.0096` maxDD `-0.2275`
- `market_context_high->fx_1h` score `0.5584` n `47` status `ready` deltaP `11.1574` edge `0.0078` maxDD `-0.1854`
- `market_context_high->crypto_major_4h` score `0.4758` n `47` status `ready` deltaP `4.9948` edge `0.0968` maxDD `-5.2359`
- `news_risk_high->index_24h` score `0.39` n `102` status `ready` deltaP `13.9706` edge `0.0395` maxDD `-2.344`
- `market_context_high->crypto_major_1h` score `0.3494` n `47` status `ready` deltaP `5.351` edge `0.0752` maxDD `-4.5405`
- `news_risk_high->index_1h` score `0.1381` n `132` status `ready` deltaP `5.4981` edge `0.0041` maxDD `-0.3395`
- `market_context_high->fx_4h` score `0.0737` n `47` status `ready` deltaP `9.7788` edge `0.0077` maxDD `-0.6736`
- `market_context_high->metal_1h` score `0.004` n `47` status `ready` deltaP `3.2775` edge `0.0103` maxDD `-0.1976`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
