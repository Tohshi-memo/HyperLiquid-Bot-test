# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-05T18:52:35.760166+00:00`
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

- `market_context_high->crypto_major_24h` score `10.7543` n `78` status `ready` deltaP `29.2067` edge `0.7151` maxDD `-0.423`
- `news_risk_high->crypto_major_4h` score `9.5686` n `65` status `ready` deltaP `33.4662` edge `0.5946` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `6.0384` n `65` status `ready` deltaP `20.7012` edge `0.4996` maxDD `-6.4195`
- `market_context_high->crypto_alt_24h` score `5.4655` n `78` status `ready` deltaP `26.0283` edge `0.3439` maxDD `-2.9571`
- `news_risk_high->index_24h` score `3.2769` n `65` status `ready` deltaP `22.9167` edge `0.1203` maxDD `0.0`
- `news_risk_high->equity_24h` score `3.2045` n `65` status `ready` deltaP `9.8184` edge `0.2116` maxDD `-0.1344`
- `news_risk_high->index_4h` score `2.7409` n `65` status `ready` deltaP `30.5418` edge `0.051` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.5169` n `65` status `ready` deltaP `9.7167` edge `0.1805` maxDD `-1.5096`
- `market_context_high->crypto_major_4h` score `2.4592` n `117` status `ready` deltaP `12.9534` edge `0.215` maxDD `-4.047`
- `news_risk_high->equity_4h` score `2.2257` n `65` status `ready` deltaP `18.7476` edge `0.1215` maxDD `-2.881`
- `news_risk_high->index_1h` score `1.9261` n `65` status `ready` deltaP `23.9705` edge `0.0157` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.8548` n `65` status `ready` deltaP `17.7064` edge `0.0781` maxDD `-0.993`
- `market_context_high->fx_4h` score `1.6336` n `117` status `ready` deltaP `27.7348` edge `0.0269` maxDD `-0.3868`
- `news_risk_high->crypto_alt_1h` score `1.2057` n `65` status `ready` deltaP `3.8208` edge `0.1269` maxDD `-2.4854`
- `market_context_high->commodity_4h` score `1.1143` n `117` status `ready` deltaP `15.5345` edge `0.0593` maxDD `-1.6002`
- `market_context_high->fx_1h` score `1.0342` n `117` status `ready` deltaP `16.1357` edge `0.007` maxDD `-0.271`
- `market_context_high->metal_24h` score `0.7701` n `78` status `ready` deltaP `25.0534` edge `0.0692` maxDD `-5.6663`
- `market_context_high->commodity_1h` score `0.7237` n `117` status `ready` deltaP `12.0554` edge `0.0196` maxDD `-0.5059`
- `market_context_high->equity_24h` score `0.6036` n `78` status `ready` deltaP `13.4081` edge `-0.033` maxDD `-0.1536`
- `news_risk_high->commodity_24h` score `0.3405` n `65` status `ready` deltaP `24.9119` edge `0.0807` maxDD `-10.9169`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
