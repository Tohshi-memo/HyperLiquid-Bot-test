# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-29T07:52:18.054367+00:00`
- Price records: `672`
- Market context records: `2225`
- Flow alert records: `8297`
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

- `news_risk_high->crypto_alt_24h` score `26.5757` n `33` status `ready` deltaP `57.4811` edge `1.8903` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `14.9311` n `33` status `ready` deltaP `47.8378` edge `0.9693` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `13.3473` n `33` status `ready` deltaP `38.81` edge `0.885` maxDD `-2.1831`
- `market_context_high->crypto_alt_4h` score `12.9125` n `132` status `ready` deltaP `37.3014` edge `0.921` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `11.6822` n `132` status `ready` deltaP `41.6713` edge `0.7487` maxDD `-1.9063`
- `news_risk_high->unknown_24h` score `10.0511` n `33` status `ready` deltaP `38.3838` edge `0.6043` maxDD `-1.4744`
- `news_risk_high->crypto_major_24h` score `7.9299` n `33` status `ready` deltaP `20.3283` edge `0.9392` maxDD `-3.3119`
- `market_context_high->unknown_4h` score `5.432` n `132` status `ready` deltaP `21.069` edge `0.3801` maxDD `-2.4317`
- `news_risk_high->commodity_4h` score `3.9409` n `43` status `ready` deltaP `32.9197` edge `0.3529` maxDD `-3.0367`
- `market_context_high->equity_4h` score `3.3073` n `132` status `ready` deltaP `22.9583` edge `0.232` maxDD `-5.0894`
- `market_context_high->index_4h` score `3.215` n `132` status `ready` deltaP `26.6214` edge `0.1588` maxDD `-1.8022`
- `market_context_high->crypto_major_1h` score `3.1199` n `138` status `ready` deltaP `16.9661` edge `0.1946` maxDD `-1.817`
- `news_risk_high->fx_24h` score `2.9736` n `33` status `ready` deltaP `31.0606` edge `0.0592` maxDD `-0.1442`
- `market_context_high->crypto_alt_1h` score `2.9533` n `138` status `ready` deltaP `16.2414` edge `0.2242` maxDD `-4.9097`
- `news_risk_high->commodity_24h` score `2.505` n `33` status `ready` deltaP `-1.0733` edge `0.2976` maxDD `-3.202`
- `news_risk_high->fx_4h` score `2.2024` n `43` status `ready` deltaP `27.8892` edge `0.016` maxDD `-0.1382`
- `market_context_high->unknown_24h` score `1.7441` n `132` status `ready` deltaP `23.9899` edge `0.4669` maxDD `-32.8525`
- `market_context_high->index_24h` score `1.7056` n `132` status `ready` deltaP `8.9962` edge `0.205` maxDD `-4.1604`
- `news_risk_high->index_24h` score `1.6337` n `33` status `ready` deltaP `11.269` edge `0.1029` maxDD `-1.3507`
- `news_risk_high->unknown_1h` score `1.3664` n `43` status `ready` deltaP `20.8954` edge `0.0215` maxDD `-1.7548`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
