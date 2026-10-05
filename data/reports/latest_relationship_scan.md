# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-05T22:37:53.963833+00:00`
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

- `market_context_high->crypto_major_24h` score `10.5137` n `78` status `ready` deltaP `27.5046` edge `0.7064` maxDD `-0.423`
- `news_risk_high->crypto_major_4h` score `9.2984` n `65` status `ready` deltaP `32.489` edge `0.5786` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `5.7831` n `65` status `ready` deltaP `20.0302` edge `0.4828` maxDD `-6.4195`
- `market_context_high->crypto_alt_24h` score `5.5033` n `78` status `ready` deltaP `25.8261` edge `0.3484` maxDD `-2.9571`
- `news_risk_high->equity_24h` score `3.2477` n `65` status `ready` deltaP `9.6538` edge `0.2163` maxDD `-0.1344`
- `news_risk_high->index_24h` score `3.2424` n `65` status `ready` deltaP `22.6804` edge `0.119` maxDD `0.0`
- `news_risk_high->index_4h` score `2.6518` n `65` status `ready` deltaP `29.5631` edge `0.0501` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.3958` n `65` status `ready` deltaP `8.9682` edge `0.1754` maxDD `-1.5096`
- `market_context_high->crypto_major_4h` score `2.189` n `117` status `ready` deltaP `11.9762` edge `0.199` maxDD `-4.047`
- `news_risk_high->equity_4h` score `2.1083` n `65` status `ready` deltaP `17.8201` edge `0.1179` maxDD `-2.881`
- `news_risk_high->index_1h` score `1.9249` n `65` status `ready` deltaP `23.9705` edge `0.0156` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.7509` n `65` status `ready` deltaP `16.6628` edge `0.0764` maxDD `-0.993`
- `market_context_high->fx_4h` score `1.5477` n `117` status `ready` deltaP `26.7359` edge `0.0264` maxDD `-0.3868`
- `market_context_high->commodity_4h` score `1.2561` n `117` status `ready` deltaP `16.7222` edge `0.0632` maxDD `-1.6002`
- `news_risk_high->crypto_alt_1h` score `1.0941` n `65` status `ready` deltaP `3.222` edge `0.1216` maxDD `-2.4854`
- `market_context_high->fx_1h` score `1.0091` n `117` status `ready` deltaP `15.8363` edge `0.0069` maxDD `-0.271`
- `market_context_high->commodity_1h` score `0.7861` n `117` status `ready` deltaP `12.6542` edge `0.0208` maxDD `-0.5059`
- `market_context_high->metal_24h` score `0.7273` n `78` status `ready` deltaP `24.5308` edge `0.0672` maxDD `-5.6663`
- `market_context_high->equity_24h` score `0.6468` n `78` status `ready` deltaP `13.2435` edge `-0.0283` maxDD `-0.1536`
- `news_risk_high->commodity_24h` score `0.3378` n `65` status `ready` deltaP `25.4005` edge `0.0771` maxDD `-10.9169`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
