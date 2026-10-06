# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-06T00:07:27.387768+00:00`
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

- `market_context_high->crypto_major_24h` score `10.5173` n `78` status `ready` deltaP `27.5046` edge `0.7067` maxDD `-0.423`
- `news_risk_high->crypto_major_4h` score `9.1335` n `65` status `ready` deltaP `31.7016` edge `0.5701` maxDD `-0.6258`
- `market_context_high->crypto_alt_24h` score `5.6125` n `78` status `ready` deltaP `25.8261` edge `0.3575` maxDD `-2.9571`
- `news_risk_high->crypto_alt_4h` score `5.5857` n `65` status `ready` deltaP `19.2424` edge `0.4716` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `3.3137` n `65` status `ready` deltaP `9.6538` edge `0.2218` maxDD `-0.1344`
- `news_risk_high->index_24h` score `3.2388` n `65` status `ready` deltaP `22.6804` edge `0.1187` maxDD `0.0`
- `news_risk_high->index_4h` score `2.5938` n `65` status `ready` deltaP `28.9278` edge `0.0495` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.439` n `65` status `ready` deltaP `9.2676` edge `0.177` maxDD `-1.5096`
- `market_context_high->crypto_major_4h` score `2.0241` n `117` status `ready` deltaP `11.1888` edge `0.1905` maxDD `-4.047`
- `news_risk_high->equity_4h` score `1.9948` n `65` status `ready` deltaP `17.0163` edge `0.1138` maxDD `-2.881`
- `news_risk_high->index_1h` score `1.974` n `65` status `ready` deltaP `24.5693` edge `0.0157` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.749` n `65` status `ready` deltaP `16.655` edge `0.0763` maxDD `-0.993`
- `market_context_high->fx_4h` score `1.4857` n `117` status `ready` deltaP `26.0062` edge `0.0261` maxDD `-0.3868`
- `market_context_high->commodity_4h` score `1.2691` n `117` status `ready` deltaP `16.8843` edge `0.0632` maxDD `-1.6002`
- `news_risk_high->crypto_alt_1h` score `1.1517` n `65` status `ready` deltaP `3.5214` edge `0.1244` maxDD `-2.4854`
- `market_context_high->fx_1h` score `0.9959` n `117` status `ready` deltaP `15.6866` edge `0.0068` maxDD `-0.271`
- `market_context_high->commodity_1h` score `0.7837` n `117` status `ready` deltaP `12.6542` edge `0.0206` maxDD `-0.5059`
- `market_context_high->metal_24h` score `0.7421` n `78` status `ready` deltaP `24.5308` edge `0.0691` maxDD `-5.6663`
- `market_context_high->equity_24h` score `0.7128` n `78` status `ready` deltaP `13.2435` edge `-0.0228` maxDD `-0.1536`
- `news_risk_high->commodity_24h` score `0.2785` n `65` status `ready` deltaP `25.4005` edge `0.0695` maxDD `-10.9169`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
