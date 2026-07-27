# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-27T12:37:27.786566+00:00`
- Price records: `672`
- Market context records: `8092`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11784`

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

- `market_context_high->equity_24h` score `20.3305` n `87` status `ready` deltaP `36.9051` edge `1.5392` maxDD `-4.9489`
- `market_context_high->equity_4h` score `8.3902` n `87` status `ready` deltaP `32.4205` edge `0.531` maxDD `-2.5032`
- `market_context_high->metal_24h` score `8.2976` n `87` status `ready` deltaP `35.8752` edge `0.4523` maxDD `0.0`
- `news_risk_high->equity_4h` score `7.8427` n `42` status `ready` deltaP `32.0921` edge `0.4501` maxDD `-0.1727`
- `news_risk_high->crypto_major_4h` score `3.682` n `42` status `ready` deltaP `15.5415` edge `0.2583` maxDD `-2.0729`
- `news_risk_high->equity_1h` score `3.5625` n `43` status `ready` deltaP `28.9305` edge `0.1356` maxDD `-1.1944`
- `market_context_high->index_4h` score `3.3037` n `87` status `ready` deltaP `31.5881` edge `0.0835` maxDD `-0.5022`
- `market_context_high->index_24h` score `3.0829` n `87` status `ready` deltaP `19.7454` edge `0.1923` maxDD `-1.3621`
- `news_risk_high->unknown_1h` score `2.7985` n `43` status `ready` deltaP `4.7556` edge `0.2292` maxDD `-0.8826`
- `news_risk_high->index_4h` score `2.5483` n `42` status `ready` deltaP `22.9674` edge `0.0783` maxDD `-0.191`
- `market_context_high->equity_1h` score `2.4773` n `87` status `ready` deltaP `15.3245` edge `0.1476` maxDD `-2.1322`
- `market_context_high->metal_4h` score `2.2707` n `87` status `ready` deltaP `20.8438` edge `0.1125` maxDD `-0.979`
- `market_context_high->fx_24h` score `2.1895` n `87` status `ready` deltaP `29.642` edge `0.0552` maxDD `-0.6283`
- `news_risk_high->metal_4h` score `1.3486` n `42` status `ready` deltaP `14.1115` edge `0.0651` maxDD `-0.7433`
- `market_context_high->index_1h` score `1.2153` n `87` status `ready` deltaP `15.87` edge `0.0222` maxDD `-0.4716`
- `market_context_high->crypto_alt_4h` score `0.8931` n `87` status `ready` deltaP `6.4866` edge `0.1429` maxDD `-3.9374`
- `news_risk_high->crypto_major_1h` score `0.8223` n `43` status `ready` deltaP `3.7878` edge `0.083` maxDD `-1.1783`
- `market_context_high->metal_1h` score `0.7991` n `87` status `ready` deltaP `11.2241` edge `0.0296` maxDD `-0.6936`
- `market_context_high->commodity_24h` score `0.7596` n `87` status `ready` deltaP `26.359` edge `0.2102` maxDD `-15.7497`
- `market_context_high->crypto_major_1h` score `0.6694` n `87` status `ready` deltaP `10.0695` edge `0.0297` maxDD `-1.6171`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
