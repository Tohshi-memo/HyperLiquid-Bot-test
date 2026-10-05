# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-05T21:25:28.838799+00:00`
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

- `market_context_high->crypto_major_24h` score `10.6292` n `78` status `ready` deltaP `28.3637` edge `0.7103` maxDD `-0.423`
- `news_risk_high->crypto_major_4h` score `9.391` n `65` status `ready` deltaP `32.7911` edge `0.5843` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `5.8323` n `65` status `ready` deltaP `20.0302` edge `0.4869` maxDD `-6.4195`
- `market_context_high->crypto_alt_24h` score `5.4853` n `78` status `ready` deltaP `25.8261` edge `0.3469` maxDD `-2.9571`
- `news_risk_high->index_24h` score `3.2472` n `65` status `ready` deltaP `22.6804` edge `0.1194` maxDD `0.0`
- `news_risk_high->equity_24h` score `3.2069` n `65` status `ready` deltaP `9.6538` edge `0.2129` maxDD `-0.1344`
- `news_risk_high->index_4h` score `2.6784` n `65` status `ready` deltaP `29.8652` edge `0.0503` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.4391` n `65` status `ready` deltaP `9.2238` edge `0.1773` maxDD `-1.5096`
- `market_context_high->crypto_major_4h` score `2.2816` n `117` status `ready` deltaP `12.2783` edge `0.2047` maxDD `-4.047`
- `news_risk_high->equity_4h` score `2.1263` n `65` status `ready` deltaP `17.9712` edge `0.1184` maxDD `-2.881`
- `news_risk_high->index_1h` score `1.9074` n `65` status `ready` deltaP `23.767` edge `0.0155` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.7798` n `65` status `ready` deltaP `16.9649` edge `0.0768` maxDD `-0.993`
- `market_context_high->fx_4h` score `1.573` n `117` status `ready` deltaP `27.038` edge `0.0265` maxDD `-0.3868`
- `market_context_high->commodity_4h` score `1.226` n `117` status `ready` deltaP `16.4201` edge `0.0627` maxDD `-1.6002`
- `news_risk_high->crypto_alt_1h` score `1.1152` n `65` status `ready` deltaP `3.3199` edge `0.1227` maxDD `-2.4854`
- `market_context_high->fx_1h` score `1.0138` n `117` status `ready` deltaP `15.8954` edge `0.0069` maxDD `-0.271`
- `market_context_high->commodity_1h` score `0.759` n `117` status `ready` deltaP `12.4066` edge `0.0202` maxDD `-0.5059`
- `market_context_high->metal_24h` score `0.7218` n `78` status `ready` deltaP `24.5308` edge `0.0665` maxDD `-5.6663`
- `market_context_high->equity_24h` score `0.606` n `78` status `ready` deltaP `13.2435` edge `-0.0317` maxDD `-0.1536`
- `news_risk_high->commodity_24h` score `0.3745` n `65` status `ready` deltaP `25.4005` edge `0.0818` maxDD `-10.9169`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
