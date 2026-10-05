# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-05T22:22:31.538718+00:00`
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

- `market_context_high->crypto_major_24h` score `10.5323` n `78` status `ready` deltaP `27.6764` edge `0.7068` maxDD `-0.423`
- `news_risk_high->crypto_major_4h` score `9.3261` n `65` status `ready` deltaP `32.64` edge `0.5799` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `5.7927` n `65` status `ready` deltaP `20.0302` edge `0.4836` maxDD `-6.4195`
- `market_context_high->crypto_alt_24h` score `5.4901` n `78` status `ready` deltaP `25.8261` edge `0.3473` maxDD `-2.9571`
- `news_risk_high->index_24h` score `3.2424` n `65` status `ready` deltaP `22.6804` edge `0.119` maxDD `0.0`
- `news_risk_high->equity_24h` score `3.2369` n `65` status `ready` deltaP `9.6538` edge `0.2154` maxDD `-0.1344`
- `news_risk_high->index_4h` score `2.6651` n `65` status `ready` deltaP `29.7142` edge `0.0502` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.4162` n `65` status `ready` deltaP `9.1179` edge `0.1761` maxDD `-1.5096`
- `market_context_high->crypto_major_4h` score `2.2167` n `117` status `ready` deltaP `12.1272` edge `0.2003` maxDD `-4.047`
- `news_risk_high->equity_4h` score `2.1251` n `65` status `ready` deltaP `17.9712` edge `0.1183` maxDD `-2.881`
- `news_risk_high->index_1h` score `1.9129` n `65` status `ready` deltaP `23.8208` edge `0.0156` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.7509` n `65` status `ready` deltaP `16.6628` edge `0.0764` maxDD `-0.993`
- `market_context_high->fx_4h` score `1.5477` n `117` status `ready` deltaP `26.7359` edge `0.0264` maxDD `-0.3868`
- `market_context_high->commodity_4h` score `1.2694` n `117` status `ready` deltaP `16.8733` edge `0.0633` maxDD `-1.6002`
- `news_risk_high->crypto_alt_1h` score `1.1002` n `65` status `ready` deltaP `3.222` edge `0.1221` maxDD `-2.4854`
- `market_context_high->fx_1h` score `1.0091` n `117` status `ready` deltaP `15.8363` edge `0.0069` maxDD `-0.271`
- `market_context_high->commodity_1h` score `0.7849` n `117` status `ready` deltaP `12.6542` edge `0.0207` maxDD `-0.5059`
- `market_context_high->metal_24h` score `0.7242` n `78` status `ready` deltaP `24.5308` edge `0.0668` maxDD `-5.6663`
- `market_context_high->equity_24h` score `0.636` n `78` status `ready` deltaP `13.2435` edge `-0.0292` maxDD `-0.1536`
- `news_risk_high->commodity_24h` score `0.3472` n `65` status `ready` deltaP `25.4005` edge `0.0783` maxDD `-10.9169`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
