# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-27T21:34:13.670078+00:00`
- Price records: `672`
- Market context records: `8131`
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

- `market_context_high->equity_24h` score `22.9065` n `84` status `ready` deltaP `41.8651` edge `1.7208` maxDD `-4.9489`
- `market_context_high->equity_4h` score `9.9726` n `85` status `ready` deltaP `35.7335` edge `0.6163` maxDD `-0.5442`
- `market_context_high->metal_24h` score `8.575` n `84` status `ready` deltaP `35.9375` edge `0.475` maxDD `0.0`
- `news_risk_high->equity_4h` score `7.699` n `43` status `ready` deltaP `29.988` edge `0.4622` maxDD `-0.6428`
- `news_risk_high->crypto_major_4h` score `4.1819` n `43` status `ready` deltaP `16.0699` edge `0.3019` maxDD `-2.1767`
- `market_context_high->index_4h` score `3.8565` n `85` status `ready` deltaP `34.0136` edge `0.0989` maxDD `-0.0092`
- `market_context_high->index_24h` score `3.8447` n `84` status `ready` deltaP `24.1071` edge `0.2267` maxDD `-1.3621`
- `news_risk_high->equity_1h` score `3.5269` n `43` status `ready` deltaP `27.8826` edge `0.1389` maxDD `-1.1366`
- `market_context_high->equity_1h` score `3.0229` n `85` status `ready` deltaP `15.9264` edge `0.176` maxDD `-1.088`
- `market_context_high->metal_4h` score `2.5801` n `85` status `ready` deltaP `23.707` edge `0.1192` maxDD `-0.979`
- `news_risk_high->index_4h` score `2.3681` n `43` status `ready` deltaP `20.1148` edge `0.0823` maxDD `-0.191`
- `market_context_high->crypto_alt_4h` score `2.1535` n `85` status `ready` deltaP `11.7863` edge `0.2126` maxDD `-3.9374`
- `market_context_high->fx_24h` score `2.1272` n `84` status `ready` deltaP `29.0426` edge `0.054` maxDD `-0.6283`
- `market_context_high->crypto_major_4h` score `1.8611` n `85` status `ready` deltaP `13.3339` edge `0.238` maxDD `-6.7444`
- `market_context_high->commodity_24h` score `1.5777` n `84` status `ready` deltaP `31.622` edge `0.28` maxDD `-15.7497`
- `market_context_high->index_1h` score `1.4869` n `85` status `ready` deltaP `17.4657` edge `0.0271` maxDD `-0.2368`
- `news_risk_high->metal_4h` score `1.1699` n `43` status `ready` deltaP `12.2979` edge `0.0623` maxDD `-0.7433`
- `market_context_high->metal_1h` score `1.0264` n `85` status `ready` deltaP `13.6157` edge `0.0326` maxDD `-0.6936`
- `news_risk_high->crypto_major_1h` score `1.0178` n `43` status `ready` deltaP `4.5363` edge `0.0943` maxDD `-1.1783`
- `market_context_high->crypto_major_1h` score `0.7297` n `85` status `ready` deltaP `12.2244` edge `0.0531` maxDD `-1.6171`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
