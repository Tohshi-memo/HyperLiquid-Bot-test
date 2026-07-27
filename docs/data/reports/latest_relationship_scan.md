# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-27T05:37:31.083687+00:00`
- Price records: `672`
- Market context records: `8062`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11848`

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

- `market_context_high->equity_24h` score `20.1028` n `76` status `ready` deltaP `35.5742` edge `1.5291` maxDD `-4.9489`
- `market_context_high->equity_4h` score `8.4277` n `87` status `ready` deltaP `32.7253` edge `0.5321` maxDD `-2.5032`
- `market_context_high->metal_24h` score `8.3312` n `76` status `ready` deltaP `35.8752` edge `0.4551` maxDD `0.0`
- `market_context_high->commodity_24h` score `5.0057` n `76` status `ready` deltaP `34.7464` edge `0.3223` maxDD `-7.2777`
- `news_risk_high->unknown_1h` score `4.9238` n `31` status `ready` deltaP `4.1578` edge `0.4103` maxDD `-0.8826`
- `news_risk_high->equity_1h` score `3.5576` n `31` status `ready` deltaP `29.38` edge `0.1322` maxDD `-1.1944`
- `market_context_high->index_4h` score `3.2991` n `87` status `ready` deltaP `31.7406` edge `0.0821` maxDD `-0.5022`
- `market_context_high->index_24h` score `2.648` n `76` status `ready` deltaP `15.2536` edge `0.186` maxDD `-1.3621`
- `market_context_high->equity_1h` score `2.4557` n `87` status `ready` deltaP `15.6239` edge `0.1438` maxDD `-2.1322`
- `market_context_high->metal_4h` score `2.3582` n `87` status `ready` deltaP `21.7585` edge `0.1137` maxDD `-0.979`
- `market_context_high->fx_24h` score `1.4012` n `76` status `ready` deltaP `29.5038` edge `0.0533` maxDD `-0.6283`
- `news_risk_high->crypto_alt_1h` score `1.3654` n `31` status `ready` deltaP `8.3639` edge `0.0775` maxDD `-0.2249`
- `news_risk_high->crypto_major_1h` score `1.2567` n `31` status `ready` deltaP `4.3896` edge `0.0988` maxDD `-0.5338`
- `market_context_high->index_1h` score `1.1314` n `87` status `ready` deltaP `14.9718` edge `0.0212` maxDD `-0.4716`
- `market_context_high->metal_1h` score `0.8338` n `87` status `ready` deltaP `11.6732` edge `0.0295` maxDD `-0.6936`
- `news_risk_high->index_1h` score `0.6897` n `31` status `ready` deltaP `8.446` edge `0.0217` maxDD `-0.3089`
- `market_context_high->crypto_major_1h` score `0.5303` n `87` status `ready` deltaP `9.321` edge `0.0231` maxDD `-1.6171`
- `news_risk_high->fx_1h` score `0.3248` n `31` status `ready` deltaP `6.9345` edge `0.0066` maxDD `-0.0611`
- `market_context_high->crypto_major_4h` score `0.2616` n `87` status `ready` deltaP `6.8861` edge `0.1477` maxDD `-6.7444`
- `market_context_high->crypto_alt_4h` score `0.2426` n `87` status `ready` deltaP `3.5902` edge `0.108` maxDD `-3.9374`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
