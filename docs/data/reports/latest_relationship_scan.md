# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-27T05:07:27.148703+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14779`

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

- `news_risk_high->unknown_24h` score `49.8629` n `50` status `ready` deltaP `11.5717` edge `4.0781` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `15.5262` n `50` status `ready` deltaP `37.1054` edge `1.0906` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `12.3322` n `50` status `ready` deltaP `26.0122` edge `0.8642` maxDD `-0.1276`
- `news_risk_high->equity_24h` score `5.748` n `50` status `ready` deltaP `27.5233` edge `0.3888` maxDD `-4.7964`
- `news_risk_high->fx_4h` score `3.8945` n `50` status `ready` deltaP `45.5061` edge `0.0302` maxDD `-0.0559`
- `news_risk_high->index_24h` score `3.3311` n `50` status `ready` deltaP `34.2867` edge `0.0642` maxDD `-0.2147`
- `market_context_high->unknown_4h` score `3.1749` n `137` status `ready` deltaP `24.7129` edge `0.1405` maxDD `-0.5878`
- `news_risk_high->metal_24h` score `3.1556` n `50` status `ready` deltaP `39.1054` edge `0.0065` maxDD `-0.0053`
- `news_risk_high->unknown_1h` score `2.7467` n `50` status `ready` deltaP `16.0778` edge `0.1573` maxDD `-0.8474`
- `news_risk_high->fx_1h` score `1.4557` n `50` status `ready` deltaP `19.6048` edge `0.0076` maxDD `-0.0257`
- `market_context_high->unknown_1h` score `1.3788` n `137` status `ready` deltaP `13.4501` edge `0.0702` maxDD `-1.5974`
- `news_risk_high->equity_4h` score `1.3163` n `50` status `ready` deltaP `20.2073` edge `0.0515` maxDD `-2.1218`
- `news_risk_high->equity_1h` score `1.3127` n `50` status `ready` deltaP `17.2635` edge `0.0222` maxDD `-0.2319`
- `market_context_high->unknown_24h` score `0.8436` n `136` status `ready` deltaP `5.6893` edge `0.1055` maxDD `-3.1835`
- `news_risk_high->commodity_1h` score `0.5175` n `50` status `ready` deltaP `14.2994` edge `0.0023` maxDD `-0.5024`
- `news_risk_high->index_4h` score `0.2062` n `50` status `ready` deltaP `7.8476` edge `0.0046` maxDD `-0.1788`
- `news_risk_high->index_1h` score `0.152` n `50` status `ready` deltaP `7.6587` edge `0.0024` maxDD `-0.0505`
- `news_risk_high->metal_1h` score `0.0532` n `50` status `ready` deltaP `4.8024` edge `-0.0026` maxDD `-0.1413`
- `market_context_high->fx_1h` score `-0.3329` n `137` status `ready` deltaP `4.5391` edge `0.0003` maxDD `-0.8587`
- `news_risk_high->metal_4h` score `-0.4022` n `50` status `ready` deltaP `5.0244` edge `-0.0139` maxDD `-0.249`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
