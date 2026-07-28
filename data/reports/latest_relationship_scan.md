# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-28T05:37:29.794384+00:00`
- Price records: `672`
- Market context records: `8166`
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

- `news_risk_high->unknown_24h` score `8185.9906` n `35` status `ready` deltaP `37.1528` edge `681.9182` maxDD `0.0`
- `market_context_high->equity_24h` score `19.1192` n `64` status `ready` deltaP `44.4444` edge `1.388` maxDD `-4.9489`
- `market_context_high->equity_4h` score `9.4719` n `65` status `ready` deltaP `38.0394` edge `0.5592` maxDD `-0.5442`
- `news_risk_high->equity_4h` score `9.0411` n `43` status `ready` deltaP `34.1038` edge `0.5466` maxDD `-0.6428`
- `market_context_high->metal_24h` score `8.2057` n `64` status `ready` deltaP `41.1458` edge `0.4095` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `5.4872` n `43` status `ready` deltaP `20.4907` edge `0.3812` maxDD `-2.1767`
- `market_context_high->index_4h` score `4.0351` n `65` status `ready` deltaP `36.6816` edge `0.096` maxDD `-0.0092`
- `market_context_high->equity_1h` score `3.6943` n `65` status `ready` deltaP `21.9415` edge `0.1819` maxDD `-0.6254`
- `news_risk_high->equity_1h` score `3.3775` n `47` status `ready` deltaP `25.2803` edge `0.1438` maxDD `-1.1366`
- `market_context_high->index_24h` score `3.0043` n `64` status `ready` deltaP `19.6181` edge `0.1866` maxDD `-1.3621`
- `news_risk_high->index_4h` score `2.8942` n `43` status `ready` deltaP `24.2307` edge `0.0987` maxDD `-0.191`
- `market_context_high->index_1h` score `1.9462` n `65` status `ready` deltaP `22.4574` edge `0.0263` maxDD `-0.1069`
- `market_context_high->metal_4h` score `1.882` n `65` status `ready` deltaP `22.0309` edge `0.0722` maxDD `-0.979`
- `news_risk_high->metal_4h` score `1.78` n `43` status `ready` deltaP `16.4137` edge `0.0857` maxDD `-0.7433`
- `market_context_high->fx_24h` score `1.657` n `64` status `ready` deltaP `23.0903` edge `0.0545` maxDD `-0.6283`
- `news_risk_high->crypto_major_1h` score `1.4819` n `47` status `ready` deltaP `8.3131` edge `0.1078` maxDD `-1.1783`
- `news_risk_high->crypto_alt_1h` score `1.2457` n `47` status `ready` deltaP `9.361` edge `0.0848` maxDD `-1.1388`
- `market_context_high->commodity_24h` score `1.2148` n `64` status `ready` deltaP `28.9931` edge `0.251` maxDD `-15.7497`
- `news_risk_high->crypto_alt_4h` score `1.1785` n `43` status `ready` deltaP `12.8651` edge `0.2045` maxDD `-5.8012`
- `market_context_high->crypto_major_1h` score `0.8828` n `65` status `ready` deltaP `9.9171` edge `0.0485` maxDD `-1.6171`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
