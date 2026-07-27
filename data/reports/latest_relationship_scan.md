# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-27T21:22:31.541805+00:00`
- Price records: `672`
- Market context records: `8130`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11842`

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

- `market_context_high->equity_24h` score `22.7822` n `84` status `ready` deltaP `41.6915` edge `1.7116` maxDD `-4.9489`
- `market_context_high->equity_4h` score `9.9847` n `85` status `ready` deltaP `35.7335` edge `0.6173` maxDD `-0.5442`
- `market_context_high->metal_24h` score `8.563` n `84` status `ready` deltaP `35.9375` edge `0.474` maxDD `0.0`
- `news_risk_high->equity_4h` score `7.711` n `43` status `ready` deltaP `29.988` edge `0.4632` maxDD `-0.6428`
- `news_risk_high->crypto_major_4h` score `4.1601` n `43` status `ready` deltaP `15.9175` edge `0.3011` maxDD `-2.1767`
- `market_context_high->index_4h` score `3.8589` n `85` status `ready` deltaP `34.0136` edge `0.0991` maxDD `-0.0092`
- `market_context_high->index_24h` score `3.8104` n `84` status `ready` deltaP `23.9335` edge `0.225` maxDD `-1.3621`
- `news_risk_high->equity_1h` score `3.5245` n `43` status `ready` deltaP `27.8826` edge `0.1387` maxDD `-1.1366`
- `market_context_high->equity_1h` score `3.0205` n `85` status `ready` deltaP `15.9264` edge `0.1758` maxDD `-1.088`
- `market_context_high->metal_4h` score `2.5801` n `85` status `ready` deltaP `23.707` edge `0.1192` maxDD `-0.979`
- `news_risk_high->index_4h` score `2.3705` n `43` status `ready` deltaP `20.1148` edge `0.0825` maxDD `-0.191`
- `market_context_high->crypto_alt_4h` score `2.1365` n `85` status `ready` deltaP `11.6338` edge `0.2122` maxDD `-3.9374`
- `market_context_high->fx_24h` score `2.1097` n `84` status `ready` deltaP `28.869` edge `0.0537` maxDD `-0.6283`
- `market_context_high->crypto_major_4h` score `1.8393` n `85` status `ready` deltaP `13.1815` edge `0.2372` maxDD `-6.7444`
- `market_context_high->commodity_24h` score `1.55` n `84` status `ready` deltaP `31.4484` edge `0.2776` maxDD `-15.7497`
- `market_context_high->index_1h` score `1.4738` n `85` status `ready` deltaP `17.316` edge `0.027` maxDD `-0.2368`
- `news_risk_high->metal_4h` score `1.1699` n `43` status `ready` deltaP `12.2979` edge `0.0623` maxDD `-0.7433`
- `market_context_high->metal_1h` score `1.0264` n `85` status `ready` deltaP `13.6157` edge `0.0326` maxDD `-0.6936`
- `news_risk_high->crypto_major_1h` score `0.9986` n `43` status `ready` deltaP `4.3866` edge `0.0937` maxDD `-1.1783`
- `market_context_high->crypto_major_1h` score `0.7172` n `85` status `ready` deltaP `12.0747` edge `0.0525` maxDD `-1.6171`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
