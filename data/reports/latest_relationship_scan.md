# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-05T12:22:40.004824+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8402`

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

- `market_context_high->crypto_major_24h` score `10.9508` n `81` status `ready` deltaP `29.8032` edge `0.7275` maxDD `-0.423`
- `news_risk_high->crypto_major_4h` score `9.3465` n `65` status `ready` deltaP `32.3992` edge `0.5832` maxDD `-0.6258`
- `market_context_high->crypto_alt_24h` score `6.1554` n `81` status `ready` deltaP `25.3666` edge `0.4058` maxDD `-2.9571`
- `news_risk_high->crypto_alt_4h` score `5.7814` n `65` status `ready` deltaP `19.6341` edge `0.4853` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `3.5137` n `112` status `ready` deltaP `15.9844` edge `0.266` maxDD `-4.047`
- `news_risk_high->index_24h` score `3.4573` n `65` status `ready` deltaP `24.8264` edge `0.1226` maxDD `0.0`
- `news_risk_high->equity_24h` score `3.0643` n `65` status `ready` deltaP `10.1656` edge `0.1976` maxDD `-0.1344`
- `news_risk_high->index_4h` score `2.9426` n `65` status `ready` deltaP `32.5235` edge `0.0546` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.5241` n `65` status `ready` deltaP `9.8664` edge `0.1801` maxDD `-1.5096`
- `news_risk_high->equity_4h` score `2.468` n `65` status `ready` deltaP `20.5769` edge `0.1295` maxDD `-2.881`
- `news_risk_high->index_1h` score `2.0746` n `65` status `ready` deltaP `25.6172` edge `0.0171` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.7696` n `65` status `ready` deltaP `16.7918` edge `0.0771` maxDD `-0.993`
- `market_context_high->fx_4h` score `1.6341` n `112` status `ready` deltaP `27.5915` edge `0.0279` maxDD `-0.3868`
- `news_risk_high->crypto_alt_1h` score `1.2141` n `65` status `ready` deltaP `3.6711` edge `0.1286` maxDD `-2.4854`
- `market_context_high->commodity_4h` score `1.1254` n `112` status `ready` deltaP `15.9625` edge `0.0583` maxDD `-1.6746`
- `market_context_high->equity_24h` score `1.0194` n `81` status `ready` deltaP `12.6157` edge `0.0071` maxDD `-0.1671`
- `market_context_high->fx_1h` score `0.9248` n `122` status `ready` deltaP `14.9185` edge `0.006` maxDD `-0.271`
- `market_context_high->crypto_alt_4h` score `0.9206` n `112` status `ready` deltaP `3.027` edge `0.2289` maxDD `-7.1222`
- `market_context_high->metal_24h` score `0.8261` n `81` status `ready` deltaP `26.2924` edge `0.0708` maxDD `-5.8803`
- `news_risk_high->commodity_24h` score `0.4661` n `65` status `ready` deltaP `24.9119` edge `0.0968` maxDD `-10.9169`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
