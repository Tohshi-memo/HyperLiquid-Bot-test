# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-27T20:52:25.247315+00:00`
- Price records: `672`
- Market context records: `8128`
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

- `market_context_high->equity_24h` score `22.5408` n `84` status `ready` deltaP `41.3443` edge `1.6938` maxDD `-4.9489`
- `market_context_high->equity_4h` score `10.0352` n `85` status `ready` deltaP `35.8859` edge `0.6205` maxDD `-0.5442`
- `market_context_high->metal_24h` score `8.539` n `84` status `ready` deltaP `35.9375` edge `0.472` maxDD `0.0`
- `news_risk_high->equity_4h` score `7.7616` n `43` status `ready` deltaP `30.1404` edge `0.4664` maxDD `-0.6428`
- `news_risk_high->crypto_major_4h` score `4.1261` n `43` status `ready` deltaP `15.6126` edge `0.3003` maxDD `-2.1767`
- `market_context_high->index_4h` score `3.8929` n `85` status `ready` deltaP `34.3185` edge `0.0999` maxDD `-0.0092`
- `market_context_high->index_24h` score `3.7418` n `84` status `ready` deltaP `23.5863` edge `0.2216` maxDD `-1.3621`
- `news_risk_high->equity_1h` score `3.5389` n `43` status `ready` deltaP `28.0323` edge `0.1389` maxDD `-1.1366`
- `market_context_high->equity_1h` score `3.0349` n `85` status `ready` deltaP `16.0761` edge `0.176` maxDD `-1.088`
- `market_context_high->metal_4h` score `2.5947` n `85` status `ready` deltaP `23.8594` edge `0.1194` maxDD `-0.979`
- `news_risk_high->index_4h` score `2.4045` n `43` status `ready` deltaP `20.4197` edge `0.0833` maxDD `-0.191`
- `market_context_high->crypto_alt_4h` score `2.1231` n `85` status `ready` deltaP `11.4814` edge `0.2121` maxDD `-3.9374`
- `market_context_high->fx_24h` score `2.0783` n `84` status `ready` deltaP `28.5218` edge `0.0534` maxDD `-0.6283`
- `market_context_high->crypto_major_4h` score `1.8053` n `85` status `ready` deltaP `12.8766` edge `0.2364` maxDD `-6.7444`
- `market_context_high->commodity_24h` score `1.4898` n `84` status `ready` deltaP `31.1012` edge `0.2722` maxDD `-15.7497`
- `market_context_high->index_1h` score `1.4618` n `85` status `ready` deltaP `17.1663` edge `0.027` maxDD `-0.2368`
- `news_risk_high->metal_4h` score `1.1845` n `43` status `ready` deltaP `12.4503` edge `0.0625` maxDD `-0.7433`
- `market_context_high->metal_1h` score `1.0132` n `85` status `ready` deltaP `13.466` edge `0.0325` maxDD `-0.6936`
- `news_risk_high->crypto_major_1h` score `0.977` n `43` status `ready` deltaP `4.2369` edge `0.0929` maxDD `-1.1783`
- `market_context_high->crypto_major_1h` score `0.7032` n `85` status `ready` deltaP `11.925` edge `0.0517` maxDD `-1.6171`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
