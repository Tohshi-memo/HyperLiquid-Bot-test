# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-15T15:52:28.222722+00:00`
- Price records: `672`
- Market context records: `6831`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11748`

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

- `market_context_high->unknown_24h` score `0.9264` n `176` status `ready` deltaP `-1.5467` edge `0.5043` maxDD `-12.3511`
- `market_context_high->commodity_24h` score `0.1901` n `176` status `ready` deltaP `9.8801` edge `0.1368` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `-0.2404` n `209` status `ready` deltaP `5.4673` edge `0.0295` maxDD `-4.2122`
- `market_context_high->fx_1h` score `-0.3441` n `209` status `ready` deltaP `0.5386` edge `0.0008` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.3567` n `209` status `ready` deltaP `3.254` edge `0.025` maxDD `-3.7803`
- `market_context_high->index_1h` score `-0.8557` n `209` status `ready` deltaP `-2.931` edge `-0.005` maxDD `-1.8127`
- `market_context_high->metal_1h` score `-0.9573` n `209` status `ready` deltaP `-5.978` edge `-0.009` maxDD `-1.9098`
- `market_context_high->fx_4h` score `-1.1681` n `199` status `ready` deltaP `8.2516` edge `0.0016` maxDD `-2.1765`
- `market_context_high->commodity_1h` score `-1.2085` n `209` status `ready` deltaP `-3.5004` edge `-0.0089` maxDD `-2.1443`
- `market_context_high->unknown_1h` score `-1.6129` n `209` status `ready` deltaP `-3.706` edge `-0.0196` maxDD `-3.2083`
- `market_context_high->index_4h` score `-1.9853` n `199` status `ready` deltaP `0.9912` edge `-0.0321` maxDD `-8.9892`
- `market_context_high->commodity_4h` score `-2.3` n `199` status `ready` deltaP `-4.1075` edge `-0.0153` maxDD `-5.5853`
- `market_context_high->equity_1h` score `-2.5689` n `209` status `ready` deltaP `-0.2127` edge `-0.038` maxDD `-9.6393`
- `market_context_high->metal_4h` score `-2.6519` n `199` status `ready` deltaP `-2.5892` edge `-0.0244` maxDD `-5.5324`
- `market_context_high->crypto_major_4h` score `-2.8897` n `199` status `ready` deltaP `0.5171` edge `-0.0412` maxDD `-16.9508`
- `market_context_high->crypto_alt_4h` score `-3.0613` n `199` status `ready` deltaP `0.6863` edge `-0.0387` maxDD `-20.6678`
- `market_context_high->unknown_4h` score `-3.2242` n `199` status `ready` deltaP `-10.3245` edge `0.0367` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.4528` n `176` status `ready` deltaP `-9.7853` edge `-0.0022` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-6.3734` n `199` status `ready` deltaP `-1.3521` edge `-0.1963` maxDD `-41.9427`
- `market_context_high->metal_24h` score `-9.4264` n `176` status `ready` deltaP `-20.2336` edge `-0.2251` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
