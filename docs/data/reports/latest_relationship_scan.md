# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-27T20:37:33.865115+00:00`
- Price records: `672`
- Market context records: `8127`
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

- `market_context_high->equity_24h` score `22.4273` n `84` status `ready` deltaP `41.1706` edge `1.6855` maxDD `-4.9489`
- `market_context_high->equity_4h` score `10.0618` n `85` status `ready` deltaP `36.0383` edge `0.6217` maxDD `-0.5442`
- `market_context_high->metal_24h` score `8.527` n `84` status `ready` deltaP `35.9375` edge `0.471` maxDD `0.0`
- `news_risk_high->equity_4h` score `7.7882` n `43` status `ready` deltaP `30.2928` edge `0.4676` maxDD `-0.6428`
- `news_risk_high->crypto_major_4h` score `4.1115` n `43` status `ready` deltaP `15.4602` edge `0.3001` maxDD `-2.1767`
- `market_context_high->index_4h` score `3.9099` n `85` status `ready` deltaP `34.4709` edge `0.1003` maxDD `-0.0092`
- `market_context_high->index_24h` score `3.7087` n `84` status `ready` deltaP `23.4127` edge `0.22` maxDD `-1.3621`
- `news_risk_high->equity_1h` score `3.5569` n `43` status `ready` deltaP `28.182` edge `0.1394` maxDD `-1.1366`
- `market_context_high->equity_1h` score `3.0529` n `85` status `ready` deltaP `16.2258` edge `0.1765` maxDD `-1.088`
- `market_context_high->metal_4h` score `2.5947` n `85` status `ready` deltaP `23.8594` edge `0.1194` maxDD `-0.979`
- `news_risk_high->index_4h` score `2.4215` n `43` status `ready` deltaP `20.5721` edge `0.0837` maxDD `-0.191`
- `market_context_high->crypto_alt_4h` score `2.1243` n `85` status `ready` deltaP `11.4814` edge `0.2122` maxDD `-3.9374`
- `market_context_high->fx_24h` score `2.062` n `84` status `ready` deltaP `28.3482` edge `0.0532` maxDD `-0.6283`
- `market_context_high->crypto_major_4h` score `1.7907` n `85` status `ready` deltaP `12.7242` edge `0.2362` maxDD `-6.7444`
- `market_context_high->index_1h` score `1.475` n `85` status `ready` deltaP `17.316` edge `0.0271` maxDD `-0.2368`
- `market_context_high->commodity_24h` score `1.4605` n `84` status `ready` deltaP `30.9276` edge `0.2696` maxDD `-15.7497`
- `news_risk_high->metal_4h` score `1.1845` n `43` status `ready` deltaP `12.4503` edge `0.0625` maxDD `-0.7433`
- `market_context_high->metal_1h` score `1.0132` n `85` status `ready` deltaP `13.466` edge `0.0325` maxDD `-0.6936`
- `news_risk_high->crypto_major_1h` score `0.9614` n `43` status `ready` deltaP `4.0872` edge `0.0926` maxDD `-1.1783`
- `market_context_high->crypto_major_1h` score `0.6931` n `85` status `ready` deltaP `11.7753` edge `0.0514` maxDD `-1.6171`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
