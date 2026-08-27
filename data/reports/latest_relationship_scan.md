# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-27T03:26:02.542738+00:00`
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

- `news_risk_high->unknown_24h` score `49.5269` n `50` status `ready` deltaP `11.5717` edge `4.0501` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `14.7132` n `50` status `ready` deltaP `36.9326` edge `1.024` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `12.2463` n `50` status `ready` deltaP `25.4024` edge `0.8611` maxDD `-0.1276`
- `news_risk_high->equity_24h` score `6.0739` n `50` status `ready` deltaP `28.7323` edge `0.4079` maxDD `-4.7964`
- `news_risk_high->fx_4h` score `3.8543` n `50` status `ready` deltaP `45.0488` edge `0.0299` maxDD `-0.0559`
- `news_risk_high->index_24h` score `3.4627` n `50` status `ready` deltaP `35.4957` edge `0.0671` maxDD `-0.2147`
- `market_context_high->unknown_4h` score `3.0889` n `137` status `ready` deltaP `24.1031` edge `0.1374` maxDD `-0.5878`
- `news_risk_high->metal_24h` score `2.9497` n `50` status `ready` deltaP `37.8964` edge `-0.0026` maxDD `-0.0053`
- `news_risk_high->unknown_1h` score `2.6844` n `50` status `ready` deltaP `15.6287` edge `0.1551` maxDD `-0.8474`
- `news_risk_high->fx_1h` score `1.4306` n `50` status `ready` deltaP `19.3054` edge `0.0075` maxDD `-0.0257`
- `market_context_high->unknown_1h` score `1.3165` n `137` status `ready` deltaP `13.001` edge `0.068` maxDD `-1.5974`
- `news_risk_high->equity_4h` score `1.3017` n `50` status `ready` deltaP `20.0549` edge `0.0513` maxDD `-2.1218`
- `news_risk_high->equity_1h` score `1.2456` n `50` status `ready` deltaP `16.6647` edge `0.0206` maxDD `-0.2319`
- `market_context_high->unknown_24h` score `0.8522` n `134` status `ready` deltaP `5.6016` edge `0.1068` maxDD `-3.1835`
- `news_risk_high->commodity_1h` score `0.5261` n `50` status `ready` deltaP `14.4491` edge `0.0024` maxDD `-0.5024`
- `news_risk_high->index_4h` score `0.177` n `50` status `ready` deltaP `7.5427` edge `0.0042` maxDD `-0.1788`
- `news_risk_high->index_1h` score `0.1186` n `50` status `ready` deltaP `7.0599` edge `0.0021` maxDD `-0.0505`
- `news_risk_high->metal_1h` score `0.0345` n `50` status `ready` deltaP `4.503` edge `-0.003` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `-0.3134` n `50` status `ready` deltaP `5.939` edge `-0.0126` maxDD `-0.249`
- `market_context_high->fx_1h` score `-0.3492` n `137` status `ready` deltaP `4.2397` edge `0.0002` maxDD `-0.8587`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
