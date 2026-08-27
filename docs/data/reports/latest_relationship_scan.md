# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-27T01:07:23.770684+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14792`

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

- `news_risk_high->unknown_24h` score `49.0973` n `50` status `ready` deltaP `11.5717` edge `4.0143` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `13.8695` n `50` status `ready` deltaP `36.5872` edge `0.956` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `12.2619` n `50` status `ready` deltaP `25.4024` edge `0.8624` maxDD `-0.1274`
- `news_risk_high->equity_24h` score `6.6521` n `50` status `ready` deltaP `30.2867` edge `0.4462` maxDD `-4.8351`
- `news_risk_high->fx_4h` score `3.7412` n `50` status `ready` deltaP `43.8293` edge `0.0286` maxDD `-0.0559`
- `news_risk_high->index_24h` score `3.659` n `50` status `ready` deltaP `37.0501` edge `0.0731` maxDD `-0.2147`
- `market_context_high->unknown_4h` score `3.1166` n `137` status `ready` deltaP `24.1031` edge `0.1397` maxDD `-0.5871`
- `news_risk_high->unknown_1h` score `2.7206` n `50` status `ready` deltaP `15.6287` edge `0.1581` maxDD `-0.8463`
- `news_risk_high->metal_24h` score `2.7126` n `50` status `ready` deltaP `36.342` edge `-0.012` maxDD `-0.0053`
- `news_risk_high->fx_1h` score `1.4294` n `50` status `ready` deltaP `19.3054` edge `0.0074` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `1.3663` n `50` status `ready` deltaP `17.7126` edge `0.0237` maxDD `-0.2338`
- `market_context_high->unknown_1h` score `1.354` n `137` status `ready` deltaP `13.001` edge `0.0711` maxDD `-1.5954`
- `news_risk_high->equity_4h` score `1.2142` n `50` status `ready` deltaP `19.2927` edge `0.0493` maxDD `-2.1389`
- `market_context_high->unknown_24h` score `0.6128` n `133` status `ready` deltaP `5.5567` edge `0.0871` maxDD `-3.1794`
- `news_risk_high->commodity_1h` score `0.5347` n `50` status `ready` deltaP `14.5988` edge `0.0025` maxDD `-0.5024`
- `news_risk_high->index_1h` score `0.1349` n `50` status `ready` deltaP `7.3593` edge `0.0022` maxDD `-0.0505`
- `news_risk_high->index_4h` score `0.0894` n `50` status `ready` deltaP `6.628` edge `0.003` maxDD `-0.1788`
- `news_risk_high->metal_1h` score `0.0337` n `50` status `ready` deltaP `4.3533` edge `-0.0021` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `-0.2079` n `50` status `ready` deltaP `6.8537` edge `-0.0099` maxDD `-0.249`
- `market_context_high->fx_1h` score `-0.35` n `137` status `ready` deltaP `4.2397` edge `0.0001` maxDD `-0.8587`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
