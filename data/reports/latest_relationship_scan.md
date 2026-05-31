# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-31T17:52:16.887950+00:00`
- Price records: `672`
- Market context records: `2480`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9248`

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

- `market_context_high->unknown_24h` score `5.1979` n `124` status `ready` deltaP `19.8869` edge `0.3334` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `4.2774` n `136` status `ready` deltaP `21.5028` edge `0.481` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `4.0144` n `136` status `ready` deltaP `18.7858` edge `0.3903` maxDD `-10.1468`
- `market_context_high->crypto_major_24h` score `1.7853` n `124` status `ready` deltaP `10.1758` edge `0.5503` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `1.5323` n `136` status `ready` deltaP `9.8458` edge `0.1641` maxDD `-3.4972`
- `market_context_high->crypto_major_1h` score `0.5917` n `143` status `ready` deltaP `8.0441` edge `0.1151` maxDD `-4.2199`
- `market_context_high->crypto_alt_1h` score `0.4656` n `143` status `ready` deltaP `6.3953` edge `0.1149` maxDD `-6.1656`
- `market_context_high->index_24h` score `0.0136` n `124` status `ready` deltaP `4.3514` edge `0.0702` maxDD `-2.5127`
- `market_context_high->equity_24h` score `-0.1617` n `124` status `ready` deltaP `18.4084` edge `0.0165` maxDD `-6.8828`
- `market_context_high->index_4h` score `-0.2166` n `136` status `ready` deltaP `5.4878` edge `0.0198` maxDD `-2.3986`
- `market_context_high->fx_1h` score `-0.3144` n `143` status `ready` deltaP `1.2992` edge `0.0045` maxDD `-0.278`
- `market_context_high->unknown_1h` score `-0.3501` n `143` status `ready` deltaP `2.5481` edge `0.0258` maxDD `-3.0902`
- `market_context_high->crypto_alt_24h` score `-0.414` n `124` status `ready` deltaP `0.2352` edge `0.6411` maxDD `-43.6595`
- `market_context_high->metal_1h` score `-0.4904` n `143` status `ready` deltaP `0.8971` edge `0.0071` maxDD `-3.0759`
- `market_context_high->index_1h` score `-0.6039` n `143` status `ready` deltaP `-0.694` edge `0.0037` maxDD `-1.2855`
- `market_context_high->fx_4h` score `-0.6215` n `136` status `ready` deltaP `-0.3318` edge `0.0085` maxDD `-0.8774`
- `market_context_high->commodity_1h` score `-0.625` n `143` status `ready` deltaP `1.5002` edge `-0.0023` maxDD `-4.3601`
- `market_context_high->metal_4h` score `-0.9088` n `136` status `ready` deltaP `3.5868` edge `0.0391` maxDD `-4.7664`
- `market_context_high->fx_24h` score `-0.9116` n `124` status `ready` deltaP `2.677` edge `0.0038` maxDD `-2.7484`
- `market_context_high->equity_1h` score `-0.9224` n `143` status `ready` deltaP `-0.8866` edge `0.0129` maxDD `-2.7085`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
