# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-23T15:37:35.733327+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9888`

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

- `market_context_high->unknown_1h` score `80.5028` n `47` status `ready` deltaP `9.2178` edge `6.6542` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `30.8333` n `46` status `ready` deltaP `16.3119` edge `2.4763` maxDD `-0.5817`
- `market_context_high->equity_24h` score `17.4747` n `46` status `ready` deltaP `13.7078` edge `1.3749` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `13.1416` n `46` status `ready` deltaP `11.2847` edge `1.0199` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `6.1397` n `96` status `ready` deltaP `-6.4236` edge `1.2403` maxDD `-46.1999`
- `market_context_high->index_24h` score `5.9155` n `46` status `ready` deltaP `22.7355` edge `0.3501` maxDD `-0.03`
- `news_risk_high->crypto_major_4h` score `3.5477` n `103` status `ready` deltaP `15.1463` edge `0.2524` maxDD `-2.619`
- `news_risk_high->commodity_24h` score `3.239` n `96` status `ready` deltaP `29.3403` edge `0.1922` maxDD `-2.431`
- `news_risk_high->crypto_alt_4h` score `2.8287` n `103` status `ready` deltaP `9.9633` edge `0.2691` maxDD `-5.9838`
- `market_context_high->index_4h` score `2.5128` n `46` status `ready` deltaP `29.1092` edge `0.0287` maxDD `-0.0692`
- `news_risk_high->crypto_alt_1h` score `2.1492` n `103` status `ready` deltaP `11.8104` edge `0.1494` maxDD `-1.5895`
- `news_risk_high->crypto_major_1h` score `1.8394` n `103` status `ready` deltaP `14.9541` edge `0.0971` maxDD `-1.8141`
- `market_context_high->equity_4h` score `1.3435` n `46` status `ready` deltaP `9.6633` edge `0.0782` maxDD `-0.4529`
- `news_risk_high->fx_4h` score `1.2129` n `103` status `ready` deltaP `18.9557` edge `0.0383` maxDD `-0.421`
- `news_risk_high->fx_24h` score `1.1673` n `96` status `ready` deltaP `28.125` edge `0.1211` maxDD `-1.7159`
- `market_context_high->index_1h` score `0.6828` n `47` status `ready` deltaP `11.4664` edge `0.0083` maxDD `-0.2275`
- `news_risk_high->metal_1h` score `0.6674` n `103` status `ready` deltaP `15.3523` edge `0.0126` maxDD `-0.7468`
- `market_context_high->metal_24h` score `0.4227` n `46` status `ready` deltaP `16.712` edge `-0.0528` maxDD `-0.2042`
- `market_context_high->equity_1h` score `0.3924` n `47` status `ready` deltaP `7.1251` edge `0.0256` maxDD `-1.5655`
- `news_risk_high->crypto_alt_24h` score `0.2506` n `96` status `ready` deltaP `-8.507` edge `0.5657` maxDD `-32.7147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
