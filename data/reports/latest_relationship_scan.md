# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-27T13:22:31.793149+00:00`
- Price records: `672`
- Market context records: `8095`
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

- `market_context_high->equity_24h` score `20.3533` n `87` status `ready` deltaP `36.9051` edge `1.5411` maxDD `-4.9489`
- `market_context_high->equity_4h` score `8.4241` n `87` status `ready` deltaP `32.7253` edge `0.5318` maxDD `-2.5032`
- `market_context_high->metal_24h` score `8.318` n `87` status `ready` deltaP `35.8752` edge `0.454` maxDD `0.0`
- `news_risk_high->equity_4h` score `7.3034` n `43` status `ready` deltaP `30.2928` edge `0.4272` maxDD `-0.6428`
- `news_risk_high->equity_1h` score `3.5819` n `43` status `ready` deltaP `29.0802` edge `0.1355` maxDD `-1.1366`
- `news_risk_high->crypto_major_4h` score `3.4524` n `43` status `ready` deltaP `14.2407` edge `0.2533` maxDD `-2.1767`
- `market_context_high->index_4h` score `3.3329` n `87` status `ready` deltaP `31.893` edge `0.0839` maxDD `-0.5022`
- `market_context_high->index_24h` score `3.0877` n `87` status `ready` deltaP `19.7454` edge `0.1927` maxDD `-1.3621`
- `news_risk_high->unknown_1h` score `2.7888` n `43` status `ready` deltaP `4.6059` edge `0.2295` maxDD `-0.8909`
- `market_context_high->equity_1h` score `2.4905` n `87` status `ready` deltaP `15.4742` edge `0.1477` maxDD `-2.1322`
- `news_risk_high->index_4h` score `2.3829` n `43` status `ready` deltaP `21.3343` edge `0.0754` maxDD `-0.191`
- `market_context_high->metal_4h` score `2.3034` n `87` status `ready` deltaP `21.1487` edge `0.1132` maxDD `-0.979`
- `market_context_high->fx_24h` score `2.1383` n `87` status `ready` deltaP `29.1221` edge `0.0544` maxDD `-0.6283`
- `market_context_high->index_1h` score `1.2153` n `87` status `ready` deltaP `15.87` edge `0.0222` maxDD `-0.4716`
- `news_risk_high->metal_4h` score `1.2029` n `43` status `ready` deltaP `12.7552` edge `0.062` maxDD `-0.7433`
- `market_context_high->crypto_alt_4h` score `0.9535` n `87` status `ready` deltaP `6.7914` edge `0.1459` maxDD `-3.9374`
- `market_context_high->commodity_24h` score `0.8226` n `87` status `ready` deltaP `26.879` edge `0.2148` maxDD `-15.7497`
- `news_risk_high->crypto_major_1h` score `0.8007` n `43` status `ready` deltaP `3.6381` edge `0.0822` maxDD `-1.1783`
- `market_context_high->metal_1h` score `0.7979` n `87` status `ready` deltaP `11.2241` edge `0.0295` maxDD `-0.6936`
- `market_context_high->crypto_major_4h` score `0.6782` n `87` status `ready` deltaP `8.8678` edge `0.1692` maxDD `-6.7444`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
