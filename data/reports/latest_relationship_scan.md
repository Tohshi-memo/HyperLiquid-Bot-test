# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-05T22:07:28.040311+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7928`

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

- `market_context_high->crypto_major_24h` score `10.5532` n `78` status `ready` deltaP `27.8483` edge `0.7074` maxDD `-0.423`
- `news_risk_high->crypto_major_4h` score `9.3393` n `65` status `ready` deltaP `32.64` edge `0.581` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `5.7999` n `65` status `ready` deltaP `20.0302` edge `0.4842` maxDD `-6.4195`
- `market_context_high->crypto_alt_24h` score `5.4853` n `78` status `ready` deltaP `25.8261` edge `0.3469` maxDD `-2.9571`
- `news_risk_high->index_24h` score `3.2436` n `65` status `ready` deltaP `22.6804` edge `0.1191` maxDD `0.0`
- `news_risk_high->equity_24h` score `3.2285` n `65` status `ready` deltaP `9.6538` edge `0.2147` maxDD `-0.1344`
- `news_risk_high->index_4h` score `2.6651` n `65` status `ready` deltaP `29.7142` edge `0.0502` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.439` n `65` status `ready` deltaP `9.2676` edge `0.177` maxDD `-1.5096`
- `market_context_high->crypto_major_4h` score `2.2299` n `117` status `ready` deltaP `12.1272` edge `0.2014` maxDD `-4.047`
- `news_risk_high->equity_4h` score `2.1251` n `65` status `ready` deltaP `17.9712` edge `0.1183` maxDD `-2.881`
- `news_risk_high->index_1h` score `1.9117` n `65` status `ready` deltaP `23.8208` edge `0.0155` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.7509` n `65` status `ready` deltaP `16.6628` edge `0.0764` maxDD `-0.993`
- `market_context_high->fx_4h` score `1.5609` n `117` status `ready` deltaP `26.887` edge `0.0265` maxDD `-0.3868`
- `market_context_high->commodity_4h` score `1.2682` n `117` status `ready` deltaP `16.8733` edge `0.0632` maxDD `-1.6002`
- `news_risk_high->crypto_alt_1h` score `1.1205` n `65` status `ready` deltaP `3.3717` edge `0.1228` maxDD `-2.4854`
- `market_context_high->fx_1h` score `1.021` n `117` status `ready` deltaP `15.986` edge `0.0069` maxDD `-0.271`
- `market_context_high->commodity_1h` score `0.7837` n `117` status `ready` deltaP `12.6542` edge `0.0206` maxDD `-0.5059`
- `market_context_high->metal_24h` score `0.7226` n `78` status `ready` deltaP `24.5308` edge `0.0666` maxDD `-5.6663`
- `market_context_high->equity_24h` score `0.6276` n `78` status `ready` deltaP `13.2435` edge `-0.0299` maxDD `-0.1536`
- `news_risk_high->commodity_24h` score `0.3557` n `65` status `ready` deltaP `25.4005` edge `0.0794` maxDD `-10.9169`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
