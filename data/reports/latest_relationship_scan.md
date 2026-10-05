# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-05T18:37:36.701888+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8176`

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

- `market_context_high->crypto_major_24h` score `10.7898` n `78` status `ready` deltaP `29.3803` edge `0.7169` maxDD `-0.423`
- `news_risk_high->crypto_major_4h` score `9.5976` n `65` status `ready` deltaP `33.6187` edge `0.596` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `6.0758` n `65` status `ready` deltaP `20.8537` edge `0.5017` maxDD `-6.4195`
- `market_context_high->crypto_alt_24h` score `5.4631` n `78` status `ready` deltaP `26.0283` edge `0.3437` maxDD `-2.9571`
- `news_risk_high->index_24h` score `3.2932` n `65` status `ready` deltaP `23.0903` edge `0.1205` maxDD `0.0`
- `news_risk_high->equity_24h` score `3.2033` n `65` status `ready` deltaP `9.8184` edge `0.2115` maxDD `-0.1344`
- `news_risk_high->index_4h` score `2.7543` n `65` status `ready` deltaP `30.6942` edge `0.0511` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.5457` n `65` status `ready` deltaP `9.8664` edge `0.1819` maxDD `-1.5096`
- `market_context_high->crypto_major_4h` score `2.4882` n `117` status `ready` deltaP `13.1059` edge `0.2164` maxDD `-4.047`
- `news_risk_high->equity_4h` score `2.2439` n `65` status `ready` deltaP `18.9001` edge `0.122` maxDD `-2.881`
- `news_risk_high->index_1h` score `1.9393` n `65` status `ready` deltaP `24.1202` edge `0.0158` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.8706` n `65` status `ready` deltaP `17.8588` edge `0.0784` maxDD `-0.993`
- `market_context_high->fx_4h` score `1.6348` n `117` status `ready` deltaP `27.7348` edge `0.027` maxDD `-0.3868`
- `news_risk_high->crypto_alt_1h` score `1.2416` n `65` status `ready` deltaP `3.9705` edge `0.1289` maxDD `-2.4854`
- `market_context_high->commodity_4h` score `1.0925` n `117` status `ready` deltaP `15.382` edge `0.0585` maxDD `-1.6002`
- `market_context_high->fx_1h` score `1.0462` n `117` status `ready` deltaP `16.2854` edge `0.007` maxDD `-0.271`
- `market_context_high->metal_24h` score `0.7724` n `78` status `ready` deltaP `25.0534` edge `0.0695` maxDD `-5.6663`
- `market_context_high->commodity_1h` score `0.7082` n `117` status `ready` deltaP `11.9057` edge `0.0193` maxDD `-0.5059`
- `market_context_high->equity_24h` score `0.6024` n `78` status `ready` deltaP `13.4081` edge `-0.0331` maxDD `-0.1536`
- `news_risk_high->commodity_24h` score `0.3428` n `65` status `ready` deltaP `24.9119` edge `0.081` maxDD `-10.9169`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
