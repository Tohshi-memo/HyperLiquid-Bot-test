# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-23T19:52:41.268563+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9883`

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

- `market_context_high->unknown_1h` score `82.2451` n `47` status `ready` deltaP `9.8166` edge `6.7954` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `33.119` n `46` status `ready` deltaP `19.2633` edge `2.6471` maxDD `-0.5817`
- `market_context_high->equity_24h` score `18.9072` n `46` status `ready` deltaP `16.6591` edge `1.4746` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `16.0549` n `46` status `ready` deltaP `14.2361` edge `1.243` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `8.4254` n `96` status `ready` deltaP `-3.4722` edge `1.4111` maxDD `-46.1999`
- `market_context_high->index_24h` score `6.3917` n `46` status `ready` deltaP `25.6869` edge `0.3701` maxDD `-0.03`
- `news_risk_high->crypto_major_4h` score `4.4344` n `103` status `ready` deltaP `16.9755` edge `0.3141` maxDD `-2.619`
- `news_risk_high->crypto_alt_4h` score `4.19` n `103` status `ready` deltaP `12.2499` edge `0.3673` maxDD `-5.9838`
- `news_risk_high->crypto_alt_24h` score `3.1639` n `96` status `ready` deltaP `-5.5556` edge `0.7888` maxDD `-32.7147`
- `news_risk_high->commodity_24h` score `2.8573` n `96` status `ready` deltaP `26.9097` edge `0.1766` maxDD `-2.431`
- `news_risk_high->crypto_alt_1h` score `2.4167` n `103` status `ready` deltaP `12.7086` edge `0.1657` maxDD `-1.5895`
- `market_context_high->index_4h` score `2.3363` n `47` status `ready` deltaP `27.9288` edge `0.0239` maxDD `-0.2323`
- `news_risk_high->crypto_major_1h` score `2.0397` n `103` status `ready` deltaP `15.8523` edge `0.1078` maxDD `-1.8141`
- `news_risk_high->fx_4h` score `1.432` n `103` status `ready` deltaP `21.3948` edge `0.0403` maxDD `-0.421`
- `news_risk_high->fx_24h` score `1.2406` n `96` status `ready` deltaP `29.3403` edge `0.1224` maxDD `-1.7159`
- `market_context_high->metal_24h` score `1.0356` n `46` status `ready` deltaP `19.6634` edge `-0.0214` maxDD `-0.2042`
- `market_context_high->equity_4h` score `0.9598` n `47` status `ready` deltaP `8.6079` edge `0.0644` maxDD `-1.3444`
- `market_context_high->index_1h` score `0.672` n `47` status `ready` deltaP `11.4664` edge `0.0074` maxDD `-0.2275`
- `news_risk_high->metal_1h` score `0.605` n `103` status `ready` deltaP `15.0529` edge `0.0094` maxDD `-0.7468`
- `news_risk_high->metal_24h` score `0.5041` n `96` status `ready` deltaP `16.4931` edge `0.0391` maxDD `-2.4203`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
