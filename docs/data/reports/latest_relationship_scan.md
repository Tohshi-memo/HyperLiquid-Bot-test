# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-28T04:37:25.117590+00:00`
- Price records: `672`
- Market context records: `8162`
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

- `news_risk_high->unknown_24h` score `7645.807` n `31` status `ready` deltaP `37.1528` edge `636.9029` maxDD `0.0`
- `market_context_high->equity_24h` score `19.7945` n `68` status `ready` deltaP `44.4853` edge `1.444` maxDD `-4.9489`
- `market_context_high->equity_4h` score `9.4972` n `69` status `ready` deltaP `37.8756` edge `0.5624` maxDD `-0.5442`
- `news_risk_high->equity_4h` score `8.8963` n `43` status `ready` deltaP `33.4941` edge `0.5386` maxDD `-0.6428`
- `market_context_high->metal_24h` score `8.3493` n `68` status `ready` deltaP `40.4514` edge `0.4261` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `5.4352` n `43` status `ready` deltaP `20.1858` edge `0.3789` maxDD `-2.1767`
- `market_context_high->index_4h` score `3.9741` n `69` status `ready` deltaP `36.4285` edge `0.0926` maxDD `-0.0092`
- `news_risk_high->equity_1h` score `3.5925` n `46` status `ready` deltaP `26.842` edge `0.1513` maxDD `-1.1366`
- `market_context_high->equity_1h` score `3.2675` n `69` status `ready` deltaP `18.871` edge `0.1668` maxDD `-0.6254`
- `market_context_high->index_24h` score `3.2181` n `68` status `ready` deltaP `21.4052` edge `0.1925` maxDD `-1.3621`
- `news_risk_high->index_4h` score `2.8346` n `43` status `ready` deltaP `23.6209` edge `0.0978` maxDD `-0.191`
- `market_context_high->metal_4h` score `2.1118` n `69` status `ready` deltaP `22.8482` edge `0.0859` maxDD `-0.979`
- `market_context_high->fx_24h` score `1.8568` n `68` status `ready` deltaP `25.1532` edge `0.0574` maxDD `-0.6283`
- `news_risk_high->metal_4h` score `1.6964` n `43` status `ready` deltaP `15.804` edge `0.0828` maxDD `-0.7433`
- `market_context_high->index_1h` score `1.4873` n `69` status `ready` deltaP `18.2656` edge `0.0218` maxDD `-0.2368`
- `news_risk_high->crypto_major_1h` score `1.4138` n `46` status `ready` deltaP `7.3418` edge `0.1086` maxDD `-1.1783`
- `market_context_high->commodity_24h` score `1.4126` n `68` status `ready` deltaP `30.3207` edge `0.2675` maxDD `-15.7497`
- `market_context_high->crypto_major_4h` score `1.3568` n `69` status `ready` deltaP `9.2656` edge `0.2231` maxDD `-6.7444`
- `news_risk_high->crypto_alt_4h` score `1.1705` n `43` status `ready` deltaP `12.7127` edge `0.2045` maxDD `-5.8012`
- `market_context_high->crypto_major_1h` score `1.0014` n `69` status `ready` deltaP `10.965` edge `0.0514` maxDD `-1.6171`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
