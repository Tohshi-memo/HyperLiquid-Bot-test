# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-27T19:52:31.787138+00:00`
- Price records: `672`
- Market context records: `8123`
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

- `market_context_high->equity_24h` score `22.1048` n `84` status `ready` deltaP `40.6498` edge `1.6621` maxDD `-4.9489`
- `market_context_high->equity_4h` score `10.116` n `85` status `ready` deltaP `36.1908` edge `0.6252` maxDD `-0.5442`
- `market_context_high->metal_24h` score `8.4934` n `84` status `ready` deltaP `35.9375` edge `0.4682` maxDD `0.0`
- `news_risk_high->equity_4h` score `7.8424` n `43` status `ready` deltaP `30.4453` edge `0.4711` maxDD `-0.6428`
- `news_risk_high->crypto_major_4h` score `4.1199` n `43` status `ready` deltaP `15.4602` edge `0.3008` maxDD `-2.1767`
- `market_context_high->index_4h` score `3.9415` n `85` status `ready` deltaP `34.7758` edge `0.1009` maxDD `-0.0092`
- `market_context_high->index_24h` score `3.6094` n `84` status `ready` deltaP `22.8918` edge `0.2152` maxDD `-1.3621`
- `news_risk_high->equity_1h` score `3.6084` n `43` status `ready` deltaP `28.6311` edge `0.1407` maxDD `-1.1366`
- `market_context_high->equity_1h` score `3.1044` n `85` status `ready` deltaP `16.6749` edge `0.1778` maxDD `-1.088`
- `market_context_high->metal_4h` score `2.5923` n `85` status `ready` deltaP `23.8594` edge `0.1192` maxDD `-0.979`
- `news_risk_high->index_4h` score `2.4531` n `43` status `ready` deltaP `20.877` edge `0.0843` maxDD `-0.191`
- `market_context_high->crypto_alt_4h` score `2.1473` n `85` status `ready` deltaP `11.6338` edge `0.2131` maxDD `-3.9374`
- `market_context_high->fx_24h` score `2.0155` n `84` status `ready` deltaP `27.8274` edge `0.0528` maxDD `-0.6283`
- `market_context_high->crypto_major_4h` score `1.7991` n `85` status `ready` deltaP `12.7242` edge `0.2369` maxDD `-6.7444`
- `market_context_high->index_1h` score `1.5013` n `85` status `ready` deltaP `17.6154` edge `0.0273` maxDD `-0.2368`
- `market_context_high->commodity_24h` score `1.3749` n `84` status `ready` deltaP `30.4067` edge `0.2621` maxDD `-15.7497`
- `news_risk_high->metal_4h` score `1.1821` n `43` status `ready` deltaP `12.4503` edge `0.0623` maxDD `-0.7433`
- `market_context_high->metal_1h` score `1.024` n `85` status `ready` deltaP `13.6157` edge `0.0324` maxDD `-0.6936`
- `news_risk_high->crypto_major_1h` score `0.953` n `43` status `ready` deltaP `4.0872` edge `0.0919` maxDD `-1.1783`
- `market_context_high->crypto_major_1h` score `0.6876` n `85` status `ready` deltaP `11.7753` edge `0.0507` maxDD `-1.6171`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
