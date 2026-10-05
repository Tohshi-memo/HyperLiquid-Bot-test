# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-05T18:07:45.992007+00:00`
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

- `market_context_high->crypto_major_24h` score `10.88` n `78` status `ready` deltaP `29.7276` edge `0.7221` maxDD `-0.423`
- `news_risk_high->crypto_major_4h` score `9.6432` n `65` status `ready` deltaP `33.6187` edge `0.5998` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `6.1456` n `65` status `ready` deltaP `21.0061` edge `0.5065` maxDD `-6.4195`
- `market_context_high->crypto_alt_24h` score `5.5161` n `78` status `ready` deltaP `26.3755` edge `0.3458` maxDD `-2.9571`
- `news_risk_high->index_24h` score `3.3282` n `65` status `ready` deltaP `23.4375` edge `0.1211` maxDD `0.0`
- `news_risk_high->equity_24h` score `3.2069` n `65` status `ready` deltaP `9.8184` edge `0.2118` maxDD `-0.1344`
- `news_risk_high->index_4h` score `2.7823` n `65` status `ready` deltaP `30.9991` edge `0.0514` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.5972` n `65` status `ready` deltaP `10.1658` edge `0.1842` maxDD `-1.5096`
- `market_context_high->crypto_major_4h` score `2.5338` n `117` status `ready` deltaP `13.1059` edge `0.2202` maxDD `-4.047`
- `news_risk_high->equity_4h` score `2.291` n `65` status `ready` deltaP `19.2049` edge `0.1239` maxDD `-2.881`
- `news_risk_high->index_1h` score `1.9644` n `65` status `ready` deltaP `24.4196` edge `0.0159` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.8876` n `65` status `ready` deltaP `18.0113` edge `0.0788` maxDD `-0.993`
- `market_context_high->fx_4h` score `1.636` n `117` status `ready` deltaP `27.7348` edge `0.0271` maxDD `-0.3868`
- `news_risk_high->crypto_alt_1h` score `1.31` n `65` status `ready` deltaP `4.2699` edge `0.1326` maxDD `-2.4854`
- `market_context_high->commodity_4h` score `1.0695` n `117` status `ready` deltaP `15.2296` edge `0.0576` maxDD `-1.6002`
- `market_context_high->fx_1h` score `1.0582` n `117` status `ready` deltaP `16.4351` edge `0.007` maxDD `-0.271`
- `market_context_high->metal_24h` score `0.7967` n `78` status `ready` deltaP `25.4007` edge `0.0703` maxDD `-5.6663`
- `market_context_high->commodity_1h` score `0.677` n `117` status `ready` deltaP `11.6063` edge `0.0187` maxDD `-0.5059`
- `market_context_high->equity_24h` score `0.606` n `78` status `ready` deltaP `13.4081` edge `-0.0328` maxDD `-0.1536`
- `news_risk_high->commodity_24h` score `0.3475` n `65` status `ready` deltaP `24.9119` edge `0.0816` maxDD `-10.9169`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
