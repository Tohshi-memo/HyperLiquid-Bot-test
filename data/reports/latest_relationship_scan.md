# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-24T11:22:32.061543+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9968`

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

- `market_context_high->unknown_1h` score `65.9442` n `47` status `ready` deltaP `10.2657` edge `5.434` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `42.8013` n `46` status `ready` deltaP `30.0272` edge `3.3822` maxDD `-0.5817`
- `market_context_high->crypto_alt_24h` score `28.484` n `46` status `ready` deltaP `25.0` edge `2.207` maxDD `0.0`
- `market_context_high->equity_24h` score `24.7627` n `46` status `ready` deltaP `27.423` edge `1.8908` maxDD `-0.1382`
- `news_risk_high->crypto_major_24h` score `9.0602` n `103` status `ready` deltaP `2.3362` edge `1.6437` maxDD `-63.6743`
- `market_context_high->index_24h` score `8.1396` n `46` status `ready` deltaP `36.4508` edge `0.444` maxDD `-0.03`
- `news_risk_high->crypto_alt_24h` score `6.2219` n `103` status `ready` deltaP `-0.2427` edge `1.2214` maxDD `-49.7699`
- `market_context_high->metal_24h` score `3.4724` n `46` status `ready` deltaP `30.4273` edge `0.1099` maxDD `-0.2042`
- `market_context_high->index_4h` score `3.0263` n `47` status `ready` deltaP `34.4837` edge `0.0377` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.5549` n `47` status `ready` deltaP `17.2969` edge `0.1394` maxDD `-1.3444`
- `news_risk_high->crypto_alt_1h` score `2.4909` n `114` status `ready` deltaP `13.3969` edge `0.1673` maxDD `-1.5895`
- `news_risk_high->crypto_major_1h` score `2.0961` n `114` status `ready` deltaP `15.343` edge `0.1159` maxDD `-1.8141`
- `news_risk_high->fx_4h` score `1.7119` n `114` status `ready` deltaP `25.0134` edge `0.0395` maxDD `-0.421`
- `news_risk_high->commodity_24h` score `1.3905` n `103` status `ready` deltaP `17.8448` edge `0.1148` maxDD `-2.431`
- `news_risk_high->fx_24h` score `1.3019` n `103` status `ready` deltaP `30.1847` edge `0.1288` maxDD `-1.7159`
- `market_context_high->index_1h` score `0.9966` n `47` status `ready` deltaP `15.0592` edge `0.0105` maxDD `-0.2275`
- `news_risk_high->metal_24h` score `0.9238` n `103` status `ready` deltaP `22.3015` edge `0.1146` maxDD `-7.2536`
- `market_context_high->equity_1h` score `0.8875` n `47` status `ready` deltaP `10.8676` edge `0.0418` maxDD `-1.5564`
- `news_risk_high->metal_1h` score `0.7115` n `114` status `ready` deltaP `15.5741` edge `0.0148` maxDD `-0.7468`
- `news_risk_high->crypto_major_4h` score `0.6127` n `114` status `ready` deltaP `12.4813` edge `0.181` maxDD `-13.719`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
