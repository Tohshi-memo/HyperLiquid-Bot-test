# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-27T05:52:28.736810+00:00`
- Price records: `672`
- Market context records: `8063`
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

- `market_context_high->equity_24h` score `20.0621` n `77` status `ready` deltaP `35.7109` edge `1.5248` maxDD `-4.9489`
- `market_context_high->equity_4h` score `8.3952` n `87` status `ready` deltaP `32.5729` edge `0.5304` maxDD `-2.5032`
- `market_context_high->metal_24h` score `8.3024` n `77` status `ready` deltaP `35.8752` edge `0.4527` maxDD `0.0`
- `news_risk_high->unknown_1h` score `4.8744` n `32` status `ready` deltaP `5.6699` edge `0.3961` maxDD `-0.8826`
- `market_context_high->commodity_24h` score `4.6308` n `77` status `ready` deltaP `33.6357` edge `0.3098` maxDD `-7.8513`
- `news_risk_high->equity_1h` score `3.5872` n `32` status `ready` deltaP `29.7343` edge `0.1323` maxDD `-1.1944`
- `market_context_high->index_4h` score `3.2821` n `87` status `ready` deltaP `31.5881` edge `0.0817` maxDD `-0.5022`
- `market_context_high->index_24h` score `2.6837` n `77` status `ready` deltaP `15.715` edge `0.1859` maxDD `-1.3621`
- `market_context_high->equity_1h` score `2.4305` n `87` status `ready` deltaP `15.4742` edge `0.1427` maxDD `-2.1322`
- `market_context_high->metal_4h` score `2.374` n `87` status `ready` deltaP `21.9109` edge `0.114` maxDD `-0.979`
- `news_risk_high->crypto_alt_1h` score `1.4366` n `32` status `ready` deltaP `9.5247` edge `0.0757` maxDD `-0.2249`
- `market_context_high->fx_24h` score `1.4219` n `77` status `ready` deltaP `29.8432` edge `0.0537` maxDD `-0.6283`
- `news_risk_high->crypto_major_1h` score `1.342` n `32` status `ready` deltaP `5.6512` edge `0.0975` maxDD `-0.5338`
- `market_context_high->index_1h` score `1.1158` n `87` status `ready` deltaP `14.8221` edge `0.0209` maxDD `-0.4716`
- `market_context_high->metal_1h` score `0.8182` n `87` status `ready` deltaP `11.5235` edge `0.0292` maxDD `-0.6936`
- `news_risk_high->index_1h` score `0.7805` n `32` status `ready` deltaP `9.506` edge `0.0222` maxDD `-0.3089`
- `market_context_high->crypto_major_1h` score `0.5063` n `87` status `ready` deltaP `9.1713` edge `0.0221` maxDD `-1.6171`
- `news_risk_high->fx_1h` score `0.4257` n `32` status `ready` deltaP `8.1961` edge `0.0066` maxDD `-0.0611`
- `market_context_high->crypto_major_4h` score `0.2362` n `87` status `ready` deltaP `6.7336` edge `0.1466` maxDD `-6.7444`
- `market_context_high->crypto_alt_4h` score `0.2292` n `87` status `ready` deltaP `3.4378` edge `0.1079` maxDD `-3.9374`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
