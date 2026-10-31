# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-31T07:37:36.400672+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7667`

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

- `market_context_high->unknown_24h` score `1644.4794` n `132` status `ready` deltaP `-5.0663` edge `137.1167` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `112.2834` n `98` status `ready` deltaP `-5.3433` edge `9.4212` maxDD `-0.9571`
- `market_context_high->unknown_4h` score `39.6654` n `132` status `ready` deltaP `2.1665` edge `3.3043` maxDD `-0.3966`
- `market_context_high->equity_24h` score `8.5285` n `132` status `ready` deltaP `21.2279` edge `0.8449` maxDD `-14.0571`
- `news_risk_high->crypto_alt_4h` score `6.824` n `93` status `ready` deltaP `22.5331` edge `0.4962` maxDD `-4.2201`
- `market_context_high->index_24h` score `4.2179` n `132` status `ready` deltaP `40.2147` edge `0.1017` maxDD `-0.1315`
- `news_risk_high->crypto_alt_1h` score `0.9176` n `98` status `ready` deltaP `8.2457` edge `0.1044` maxDD `-3.9659`
- `market_context_high->metal_1h` score `0.4854` n `132` status `ready` deltaP `11.4861` edge `0.0149` maxDD `-0.3392`
- `market_context_high->commodity_4h` score `0.3518` n `132` status `ready` deltaP `14.2646` edge `0.0561` maxDD `-1.0837`
- `market_context_high->metal_4h` score `0.3225` n `132` status `ready` deltaP `14.7311` edge `0.0318` maxDD `-1.7598`
- `market_context_high->equity_1h` score `0.2206` n `132` status `ready` deltaP `4.237` edge `0.0777` maxDD `-2.3383`
- `market_context_high->crypto_major_1h` score `0.0569` n `132` status `ready` deltaP `7.5758` edge `0.057` maxDD `-5.2213`
- `market_context_high->equity_4h` score `-0.0756` n `132` status `ready` deltaP `1.5059` edge `0.1387` maxDD `-6.008`
- `market_context_high->fx_1h` score `-0.0893` n `132` status `ready` deltaP `3.806` edge `-0.001` maxDD `-0.1986`
- `market_context_high->commodity_1h` score `-0.2311` n `132` status `ready` deltaP `2.5449` edge `0.0152` maxDD `-0.4475`
- `market_context_high->metal_24h` score `-0.4733` n `132` status `ready` deltaP `4.5928` edge `0.1734` maxDD `-10.5088`
- `market_context_high->fx_4h` score `-0.4966` n `132` status `ready` deltaP `-0.1524` edge `-0.0028` maxDD `-0.4545`
- `market_context_high->index_1h` score `-0.6934` n `132` status `ready` deltaP `-0.44` edge `0.001` maxDD `-1.1344`
- `news_risk_high->index_1h` score `-0.8562` n `98` status `ready` deltaP `1.8636` edge `-0.0038` maxDD `-1.3981`
- `market_context_high->crypto_alt_1h` score `-0.9003` n `132` status `ready` deltaP `2.3861` edge `0.0462` maxDD `-7.536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
