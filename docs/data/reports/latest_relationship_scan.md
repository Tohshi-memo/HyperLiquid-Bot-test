# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-29T08:22:21.679977+00:00`
- Price records: `672`
- Market context records: `2227`
- Flow alert records: `8303`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9178`

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

- `news_risk_high->crypto_alt_24h` score `26.3163` n `33` status `ready` deltaP `57.1338` edge `1.871` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `14.8001` n `33` status `ready` deltaP `47.4905` edge `0.9607` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `13.0868` n `33` status `ready` deltaP `38.4628` edge `0.8656` maxDD `-2.1831`
- `market_context_high->crypto_alt_4h` score `12.8643` n `132` status `ready` deltaP `37.149` edge `0.918` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `11.6546` n `132` status `ready` deltaP `41.6713` edge `0.7464` maxDD `-1.9063`
- `news_risk_high->unknown_24h` score `9.8578` n `33` status `ready` deltaP `38.0366` edge `0.5905` maxDD `-1.4744`
- `news_risk_high->crypto_major_24h` score `7.7793` n `33` status `ready` deltaP `19.9811` edge `0.9222` maxDD `-3.3119`
- `market_context_high->unknown_4h` score `5.3452` n `132` status `ready` deltaP `20.7641` edge `0.3749` maxDD `-2.4317`
- `news_risk_high->commodity_4h` score `3.9416` n `43` status `ready` deltaP `32.9197` edge `0.353` maxDD `-3.0367`
- `market_context_high->equity_4h` score `3.2529` n `132` status `ready` deltaP `22.6534` edge `0.2295` maxDD `-5.0894`
- `market_context_high->index_4h` score `3.1858` n `132` status `ready` deltaP `26.3165` edge `0.1584` maxDD `-1.8022`
- `market_context_high->crypto_major_1h` score `3.1089` n `140` status `ready` deltaP `17.1429` edge `0.1925` maxDD `-1.817`
- `news_risk_high->fx_24h` score `2.9688` n `33` status `ready` deltaP `31.0606` edge `0.0588` maxDD `-0.1442`
- `market_context_high->crypto_alt_1h` score `2.8143` n `140` status `ready` deltaP `15.2994` edge `0.2189` maxDD `-4.9097`
- `news_risk_high->commodity_24h` score `2.481` n `33` status `ready` deltaP `-1.0733` edge `0.2956` maxDD `-3.202`
- `news_risk_high->fx_4h` score `2.189` n `43` status `ready` deltaP `27.7368` edge `0.0159` maxDD `-0.1382`
- `market_context_high->index_24h` score `1.6215` n `132` status `ready` deltaP `8.6489` edge `0.2003` maxDD `-4.1604`
- `market_context_high->unknown_24h` score `1.5507` n `132` status `ready` deltaP `23.6427` edge `0.4531` maxDD `-32.8525`
- `news_risk_high->index_24h` score `1.5495` n `33` status `ready` deltaP `10.9217` edge `0.0982` maxDD `-1.3507`
- `news_risk_high->unknown_1h` score `1.3124` n `43` status `ready` deltaP `20.7457` edge `0.018` maxDD `-1.7548`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
