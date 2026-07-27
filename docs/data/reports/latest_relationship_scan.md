# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-27T23:07:26.307829+00:00`
- Price records: `672`
- Market context records: `8139`
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

- `market_context_high->equity_24h` score `23.7446` n `84` status `ready` deltaP `42.9068` edge `1.7837` maxDD `-4.9489`
- `market_context_high->equity_4h` score `9.9812` n `85` status `ready` deltaP `35.8859` edge `0.616` maxDD `-0.5442`
- `market_context_high->metal_24h` score `8.7368` n `84` status `ready` deltaP `36.8056` edge `0.4827` maxDD `0.0`
- `news_risk_high->equity_4h` score `7.7076` n `43` status `ready` deltaP `30.1404` edge `0.4619` maxDD `-0.6428`
- `news_risk_high->crypto_major_4h` score `4.3365` n `43` status `ready` deltaP `16.8321` edge `0.3097` maxDD `-2.1767`
- `market_context_high->index_24h` score `4.0672` n `84` status `ready` deltaP `25.1488` edge `0.2383` maxDD `-1.3621`
- `market_context_high->index_4h` score `3.8723` n `85` status `ready` deltaP `34.1661` edge `0.0992` maxDD `-0.0092`
- `news_risk_high->equity_1h` score `3.5797` n `43` status `ready` deltaP `28.182` edge `0.1413` maxDD `-1.1366`
- `market_context_high->equity_1h` score `3.0757` n `85` status `ready` deltaP `16.2258` edge `0.1784` maxDD `-1.088`
- `market_context_high->metal_4h` score `2.6031` n `85` status `ready` deltaP `23.8594` edge `0.1201` maxDD `-0.979`
- `news_risk_high->index_4h` score `2.3839` n `43` status `ready` deltaP `20.2673` edge `0.0826` maxDD `-0.191`
- `market_context_high->crypto_alt_4h` score `2.2815` n `85` status `ready` deltaP `12.396` edge `0.2192` maxDD `-3.9374`
- `market_context_high->fx_24h` score `2.2213` n `84` status `ready` deltaP `30.0843` edge `0.0549` maxDD `-0.6283`
- `market_context_high->crypto_major_4h` score `2.0156` n `85` status `ready` deltaP `14.0961` edge `0.2458` maxDD `-6.7444`
- `market_context_high->commodity_24h` score `1.7255` n `84` status `ready` deltaP `32.6637` edge `0.292` maxDD `-15.7497`
- `market_context_high->index_1h` score `1.4989` n `85` status `ready` deltaP `17.6154` edge `0.0271` maxDD `-0.2368`
- `news_risk_high->metal_4h` score `1.1929` n `43` status `ready` deltaP `12.4503` edge `0.0632` maxDD `-0.7433`
- `news_risk_high->crypto_major_1h` score `1.0825` n `43` status `ready` deltaP `4.686` edge `0.0987` maxDD `-1.1783`
- `market_context_high->metal_1h` score `1.0132` n `85` status `ready` deltaP `13.466` edge `0.0325` maxDD `-0.6936`
- `market_context_high->crypto_major_1h` score `0.7718` n `85` status `ready` deltaP `12.3741` edge `0.0575` maxDD `-1.6171`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
