# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-05T23:52:30.962264+00:00`
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

- `market_context_high->crypto_major_24h` score `10.5089` n `78` status `ready` deltaP `27.5046` edge `0.706` maxDD `-0.423`
- `news_risk_high->crypto_major_4h` score `9.1576` n `65` status `ready` deltaP `31.8532` edge `0.5711` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `5.6254` n `65` status `ready` deltaP `19.3939` edge `0.4739` maxDD `-6.4195`
- `market_context_high->crypto_alt_24h` score `5.5897` n `78` status `ready` deltaP `25.8261` edge `0.3556` maxDD `-2.9571`
- `news_risk_high->equity_24h` score `3.2993` n `65` status `ready` deltaP `9.6538` edge `0.2206` maxDD `-0.1344`
- `news_risk_high->index_24h` score `3.2376` n `65` status `ready` deltaP `22.6804` edge `0.1186` maxDD `0.0`
- `news_risk_high->index_4h` score `2.595` n `65` status `ready` deltaP `28.9278` edge `0.0496` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.4138` n `65` status `ready` deltaP `9.1179` edge `0.1759` maxDD `-1.5096`
- `market_context_high->crypto_major_4h` score `2.0482` n `117` status `ready` deltaP `11.3404` edge `0.1915` maxDD `-4.047`
- `news_risk_high->equity_4h` score `2.0117` n `65` status `ready` deltaP `17.1678` edge `0.1142` maxDD `-2.881`
- `news_risk_high->index_1h` score `1.9608` n `65` status `ready` deltaP `24.4196` edge `0.0156` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.7502` n `65` status `ready` deltaP `16.655` edge `0.0764` maxDD `-0.993`
- `market_context_high->fx_4h` score `1.499` n `117` status `ready` deltaP `26.1578` edge `0.0262` maxDD `-0.3868`
- `market_context_high->commodity_4h` score `1.257` n `117` status `ready` deltaP `16.7327` edge `0.0632` maxDD `-1.6002`
- `news_risk_high->crypto_alt_1h` score `1.1181` n `65` status `ready` deltaP `3.3717` edge `0.1226` maxDD `-2.4854`
- `market_context_high->fx_1h` score `1.0091` n `117` status `ready` deltaP `15.8363` edge `0.0069` maxDD `-0.271`
- `market_context_high->commodity_1h` score `0.7837` n `117` status `ready` deltaP `12.6542` edge `0.0206` maxDD `-0.5059`
- `market_context_high->metal_24h` score `0.7398` n `78` status `ready` deltaP `24.5308` edge `0.0688` maxDD `-5.6663`
- `market_context_high->equity_24h` score `0.6984` n `78` status `ready` deltaP `13.2435` edge `-0.024` maxDD `-0.1536`
- `news_risk_high->commodity_24h` score `0.2894` n `65` status `ready` deltaP `25.4005` edge `0.0709` maxDD `-10.9169`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
