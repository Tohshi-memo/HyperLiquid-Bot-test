# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-26T09:22:37.107590+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11866`

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

- `news_risk_high->unknown_24h` score `3593.4155` n `97` status `ready` deltaP `-0.6837` edge `299.4603` maxDD `-0.0226`
- `market_context_high->unknown_1h` score `69.9249` n `47` status `ready` deltaP `8.7687` edge `5.7757` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `47.657` n `47` status `ready` deltaP `22.7837` edge `3.8588` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `28.7635` n `47` status `ready` deltaP `20.6154` edge `2.2975` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.4607` n `47` status `ready` deltaP `33.3739` edge `1.9348` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.1326` n `47` status `ready` deltaP `29.9017` edge `0.408` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.3939` n `47` status `ready` deltaP `28.8084` edge `0.1146` maxDD `-0.2401`
- `market_context_high->equity_4h` score `2.7253` n `47` status `ready` deltaP `17.2969` edge `0.1536` maxDD `-1.3444`
- `market_context_high->index_4h` score `2.5554` n `47` status `ready` deltaP `29.4532` edge `0.032` maxDD `-0.2323`
- `market_context_high->crypto_alt_4h` score `1.4269` n `47` status `ready` deltaP `11.5172` edge `0.1089` maxDD `-3.3417`
- `news_risk_high->metal_24h` score `1.1482` n `97` status `ready` deltaP `26.5052` edge `0.1366` maxDD `-6.9545`
- `market_context_high->equity_1h` score `1.0386` n `47` status `ready` deltaP `11.9155` edge `0.0474` maxDD `-1.5564`
- `news_risk_high->index_24h` score `0.9691` n `97` status `ready` deltaP `16.6971` edge `0.0473` maxDD `-2.2287`
- `market_context_high->index_1h` score `0.7822` n `47` status `ready` deltaP `12.5143` edge `0.0096` maxDD `-0.2275`
- `market_context_high->crypto_major_4h` score `0.6744` n `47` status `ready` deltaP `6.3667` edge `0.1042` maxDD `-5.2359`
- `market_context_high->fx_1h` score `0.5584` n `47` status `ready` deltaP `11.1574` edge `0.0078` maxDD `-0.1854`
- `market_context_high->crypto_major_1h` score `0.3183` n `47` status `ready` deltaP `5.0516` edge `0.0746` maxDD `-4.5405`
- `news_risk_high->index_1h` score `0.0905` n `137` status `ready` deltaP `4.9511` edge `0.0037` maxDD `-0.3331`
- `market_context_high->fx_4h` score `0.0225` n `47` status `ready` deltaP `9.1691` edge `0.0075` maxDD `-0.6736`
- `market_context_high->metal_1h` score `0.004` n `47` status `ready` deltaP `3.2775` edge `0.0103` maxDD `-0.1976`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
