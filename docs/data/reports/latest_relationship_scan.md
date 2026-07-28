# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-28T04:22:27.440126+00:00`
- Price records: `672`
- Market context records: `8161`
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

- `news_risk_high->unknown_24h` score `7484.2078` n `30` status `ready` deltaP `37.1528` edge `623.4363` maxDD `0.0`
- `market_context_high->equity_24h` score `19.9766` n `69` status `ready` deltaP `44.4822` edge `1.4592` maxDD `-4.9489`
- `market_context_high->equity_4h` score `9.4861` n `70` status `ready` deltaP `37.8266` edge `0.5618` maxDD `-0.5442`
- `news_risk_high->equity_4h` score `8.8517` n `43` status `ready` deltaP `33.3416` edge `0.5359` maxDD `-0.6428`
- `market_context_high->metal_24h` score `8.3942` n `69` status `ready` deltaP `40.2778` edge `0.431` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `5.405` n `43` status `ready` deltaP `20.0334` edge `0.3774` maxDD `-2.1767`
- `market_context_high->index_4h` score `3.9625` n `70` status `ready` deltaP `36.3589` edge `0.0921` maxDD `-0.0092`
- `news_risk_high->equity_1h` score `3.8063` n `45` status `ready` deltaP `28.4797` edge `0.1582` maxDD `-1.1366`
- `market_context_high->equity_1h` score `3.2846` n `70` status `ready` deltaP `19.1146` edge `0.1666` maxDD `-0.6254`
- `market_context_high->index_24h` score `3.2743` n `69` status `ready` deltaP `21.8071` edge `0.1945` maxDD `-1.3621`
- `news_risk_high->index_4h` score `2.8176` n `43` status `ready` deltaP `23.4685` edge `0.0974` maxDD `-0.191`
- `market_context_high->metal_4h` score `2.1777` n `70` status `ready` deltaP `23.027` edge `0.0902` maxDD `-0.979`
- `market_context_high->fx_24h` score `1.8989` n `69` status `ready` deltaP `25.6189` edge `0.0578` maxDD `-0.6283`
- `news_risk_high->metal_4h` score `1.6722` n `43` status `ready` deltaP `15.6515` edge `0.0818` maxDD `-0.7433`
- `news_risk_high->crypto_major_1h` score `1.5392` n `45` status `ready` deltaP `8.3999` edge `0.112` maxDD `-1.1783`
- `market_context_high->index_1h` score `1.5166` n `70` status `ready` deltaP `18.5714` edge `0.0222` maxDD `-0.2368`
- `market_context_high->commodity_24h` score `1.456` n `69` status `ready` deltaP `30.6159` edge `0.2711` maxDD `-15.7497`
- `market_context_high->crypto_major_4h` score `1.4507` n `70` status `ready` deltaP `9.7344` edge `0.2278` maxDD `-6.7444`
- `news_risk_high->crypto_alt_4h` score `1.1509` n `43` status `ready` deltaP `12.5602` edge `0.203` maxDD `-5.8012`
- `market_context_high->crypto_major_1h` score `1.0339` n `70` status `ready` deltaP `11.4157` edge `0.0511` maxDD `-1.6171`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
