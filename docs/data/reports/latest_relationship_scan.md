# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-23T16:22:31.198367+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9846`

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

- `market_context_high->unknown_1h` score `80.5892` n `47` status `ready` deltaP `9.3675` edge `6.6604` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `31.2278` n `46` status `ready` deltaP `16.8328` edge `2.5057` maxDD `-0.5817`
- `market_context_high->equity_24h` score `17.6724` n `46` status `ready` deltaP `14.2286` edge `1.3879` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `13.6152` n `46` status `ready` deltaP `11.8056` edge `1.0559` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `6.5342` n `96` status `ready` deltaP `-5.9027` edge `1.2697` maxDD `-46.1999`
- `market_context_high->index_24h` score `5.986` n `46` status `ready` deltaP `23.2564` edge `0.3525` maxDD `-0.03`
- `news_risk_high->crypto_major_4h` score `3.7906` n `103` status `ready` deltaP `15.6036` edge `0.2696` maxDD `-2.619`
- `news_risk_high->commodity_24h` score `3.1613` n `96` status `ready` deltaP `28.8194` edge `0.1892` maxDD `-2.431`
- `news_risk_high->crypto_alt_4h` score `3.1461` n `103` status `ready` deltaP `10.4206` edge `0.2925` maxDD `-5.9838`
- `market_context_high->index_4h` score `2.5092` n `46` status `ready` deltaP `29.1092` edge `0.0284` maxDD `-0.0692`
- `news_risk_high->crypto_alt_1h` score `2.2476` n `103` status `ready` deltaP `12.1098` edge `0.1556` maxDD `-1.5895`
- `news_risk_high->crypto_major_1h` score `1.9054` n `103` status `ready` deltaP `15.2535` edge `0.1006` maxDD `-1.8141`
- `market_context_high->equity_4h` score `1.3351` n `46` status `ready` deltaP `9.6633` edge `0.0775` maxDD `-0.4529`
- `news_risk_high->fx_4h` score `1.2531` n `103` status `ready` deltaP `19.4131` edge `0.0386` maxDD `-0.421`
- `news_risk_high->fx_24h` score `1.1673` n `96` status `ready` deltaP `28.125` edge `0.1211` maxDD `-1.7159`
- `news_risk_high->crypto_alt_24h` score `0.7243` n `96` status `ready` deltaP `-7.9861` edge `0.6017` maxDD `-32.7147`
- `market_context_high->index_1h` score `0.684` n `47` status `ready` deltaP `11.4664` edge `0.0084` maxDD `-0.2275`
- `news_risk_high->metal_1h` score `0.6698` n `103` status `ready` deltaP `15.3523` edge `0.0128` maxDD `-0.7468`
- `market_context_high->metal_24h` score `0.5088` n `46` status `ready` deltaP `17.2328` edge `-0.0491` maxDD `-0.2042`
- `market_context_high->equity_1h` score `0.4009` n `47` status `ready` deltaP `7.1251` edge `0.0262` maxDD `-1.5564`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
