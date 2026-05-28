# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-28T19:52:25.259653+00:00`
- Price records: `672`
- Market context records: `2173`
- Flow alert records: `8149`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9188`

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

- `market_context_high->crypto_alt_4h` score `12.8407` n `134` status `ready` deltaP `36.4943` edge `0.9204` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `11.7691` n `134` status `ready` deltaP `42.1278` edge `0.7529` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `5.5076` n `134` status `ready` deltaP `22.4518` edge `0.3842` maxDD `-2.6599`
- `news_risk_high->commodity_4h` score `3.816` n `43` status `ready` deltaP `31.8526` edge `0.344` maxDD `-3.0367`
- `market_context_high->equity_4h` score `3.6921` n `134` status `ready` deltaP `24.7087` edge `0.2524` maxDD `-5.0894`
- `market_context_high->crypto_major_1h` score `3.2763` n `134` status `ready` deltaP `17.7652` edge `0.2023` maxDD `-1.817`
- `market_context_high->crypto_alt_1h` score `3.091` n `134` status `ready` deltaP `16.5676` edge `0.2335` maxDD `-4.9097`
- `market_context_high->unknown_24h` score `3.0881` n `134` status `ready` deltaP `28.1846` edge `0.5851` maxDD `-34.9193`
- `market_context_high->index_4h` score `2.7679` n `134` status `ready` deltaP `22.743` edge `0.1474` maxDD `-1.8022`
- `market_context_high->index_24h` score `2.7397` n `134` status `ready` deltaP `11.3469` edge `0.2755` maxDD `-4.1604`
- `market_context_high->crypto_major_24h` score `2.5722` n `134` status `ready` deltaP `20.4498` edge `1.0387` maxDD `-61.2872`
- `news_risk_high->fx_4h` score `2.1416` n `43` status `ready` deltaP `27.2794` edge `0.015` maxDD `-0.1382`
- `market_context_high->equity_24h` score `1.8996` n `134` status `ready` deltaP `23.707` edge `0.4901` maxDD `-33.1875`
- `news_risk_high->unknown_4h` score `1.5417` n `43` status `ready` deltaP `15.8395` edge `0.0952` maxDD `-2.7857`
- `market_context_high->metal_4h` score `1.4984` n `134` status `ready` deltaP `17.8217` edge `0.1448` maxDD `-4.7664`
- `news_risk_high->equity_4h` score `1.3885` n `43` status `ready` deltaP `-2.2264` edge `0.3136` maxDD `-4.6598`
- `news_risk_high->unknown_1h` score `1.3796` n `43` status `ready` deltaP `21.0451` edge `0.0216` maxDD `-1.7548`
- `news_risk_high->commodity_1h` score `0.7284` n `43` status `ready` deltaP `10.3154` edge `0.0926` maxDD `-2.1052`
- `market_context_high->equity_1h` score `0.4653` n `134` status `ready` deltaP `9.9763` edge `0.0511` maxDD `-2.6402`
- `news_risk_high->fx_1h` score `0.4621` n `43` status `ready` deltaP `8.1395` edge `0.0099` maxDD `-0.0524`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
