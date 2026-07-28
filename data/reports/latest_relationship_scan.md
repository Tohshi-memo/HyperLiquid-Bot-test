# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-28T03:52:30.156242+00:00`
- Price records: `672`
- Market context records: `8159`
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

- `market_context_high->equity_24h` score `20.4406` n `71` status `ready` deltaP `44.4616` edge `1.498` maxDD `-4.9489`
- `market_context_high->equity_4h` score `9.5868` n `72` status `ready` deltaP `37.7202` edge `0.5709` maxDD `-0.5442`
- `news_risk_high->equity_4h` score `8.7505` n `43` status `ready` deltaP `33.0367` edge `0.5295` maxDD `-0.6428`
- `market_context_high->metal_24h` score `8.502` n `71` status `ready` deltaP `39.9306` edge `0.4423` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `5.353` n `43` status `ready` deltaP `19.7285` edge `0.3751` maxDD `-2.1767`
- `market_context_high->index_4h` score `3.9544` n `72` status `ready` deltaP `36.2127` edge `0.0924` maxDD `-0.0092`
- `news_risk_high->equity_1h` score `3.9094` n `43` status `ready` deltaP `29.8287` edge `0.1578` maxDD `-1.1366`
- `market_context_high->equity_1h` score `3.4709` n `72` status `ready` deltaP `19.7189` edge `0.1781` maxDD `-0.6254`
- `market_context_high->index_24h` score `3.3959` n `71` status `ready` deltaP `22.5621` edge `0.1996` maxDD `-1.3621`
- `news_risk_high->index_4h` score `2.7824` n `43` status `ready` deltaP `23.1636` edge `0.0965` maxDD `-0.191`
- `market_context_high->metal_4h` score `2.2989` n `72` status `ready` deltaP `23.3571` edge `0.0981` maxDD `-0.979`
- `market_context_high->fx_24h` score `1.9763` n `71` status `ready` deltaP `26.4965` edge `0.0584` maxDD `-0.6283`
- `market_context_high->crypto_alt_4h` score `1.626` n `72` status `ready` deltaP `8.2826` edge `0.192` maxDD `-3.9374`
- `news_risk_high->metal_4h` score `1.625` n `43` status `ready` deltaP `15.3467` edge `0.0799` maxDD `-0.7433`
- `market_context_high->crypto_major_4h` score `1.6007` n `72` status `ready` deltaP `10.6199` edge `0.2344` maxDD `-6.7444`
- `market_context_high->index_1h` score `1.5985` n `72` status `ready` deltaP `19.2947` edge `0.0242` maxDD `-0.2368`
- `market_context_high->commodity_24h` score `1.5369` n `71` status `ready` deltaP `31.1669` edge `0.2778` maxDD `-15.7497`
- `news_risk_high->crypto_major_1h` score `1.3571` n `43` status `ready` deltaP `6.3327` edge `0.1106` maxDD `-1.1783`
- `market_context_high->crypto_major_1h` score `1.144` n `72` status `ready` deltaP `12.5665` edge `0.0526` maxDD `-1.6171`
- `news_risk_high->crypto_alt_4h` score `1.1187` n `43` status `ready` deltaP `12.2554` edge `0.2009` maxDD `-5.8012`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
