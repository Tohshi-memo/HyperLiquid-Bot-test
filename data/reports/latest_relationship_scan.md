# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-05T13:37:28.956507+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8444`

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

- `market_context_high->crypto_major_24h` score `10.9592` n `82` status `ready` deltaP `29.8484` edge `0.7279` maxDD `-0.423`
- `news_risk_high->crypto_major_4h` score `9.3998` n `65` status `ready` deltaP `32.8565` edge `0.5846` maxDD `-0.6258`
- `market_context_high->crypto_alt_24h` score `6.1758` n `82` status `ready` deltaP `25.487` edge `0.4067` maxDD `-2.9571`
- `news_risk_high->crypto_alt_4h` score `5.7202` n `65` status `ready` deltaP `19.6341` edge `0.4802` maxDD `-6.4195`
- `news_risk_high->index_24h` score `3.4585` n `65` status `ready` deltaP `24.8264` edge `0.1227` maxDD `0.0`
- `news_risk_high->equity_24h` score `3.0034` n `65` status `ready` deltaP `9.6448` edge `0.196` maxDD `-0.1344`
- `news_risk_high->index_4h` score `2.8965` n `65` status `ready` deltaP `32.0662` edge `0.0538` maxDD `-0.4296`
- `market_context_high->crypto_major_4h` score `2.79` n `116` status `ready` deltaP `12.9626` edge `0.2425` maxDD `-4.047`
- `news_risk_high->crypto_major_1h` score `2.5241` n `65` status `ready` deltaP `9.8664` edge `0.1801` maxDD `-1.5096`
- `news_risk_high->equity_4h` score `2.4248` n `65` status `ready` deltaP `20.5769` edge `0.1259` maxDD `-2.881`
- `news_risk_high->index_1h` score `2.059` n `65` status `ready` deltaP `25.4675` edge `0.0168` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.7818` n `65` status `ready` deltaP `16.9442` edge `0.0771` maxDD `-0.993`
- `market_context_high->fx_4h` score `1.5996` n `116` status `ready` deltaP `27.2497` edge `0.0273` maxDD `-0.3868`
- `news_risk_high->crypto_alt_1h` score `1.1937` n `65` status `ready` deltaP `3.6711` edge `0.1269` maxDD `-2.4854`
- `market_context_high->equity_24h` score `1.0365` n `82` status `ready` deltaP `13.3596` edge `0.0034` maxDD `-0.1536`
- `market_context_high->metal_24h` score `0.9129` n `82` status `ready` deltaP `26.9901` edge `0.0762` maxDD `-5.7943`
- `market_context_high->fx_1h` score `0.9113` n `121` status `ready` deltaP `14.7498` edge `0.006` maxDD `-0.271`
- `market_context_high->commodity_4h` score `0.9044` n `116` status `ready` deltaP `13.7458` edge `0.0508` maxDD `-1.3656`
- `market_context_high->crypto_alt_4h` score `0.5513` n `116` status `ready` deltaP `0.841` edge `0.2127` maxDD `-7.1222`
- `news_risk_high->commodity_24h` score `0.4427` n `65` status `ready` deltaP `24.9119` edge `0.0938` maxDD `-10.9169`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
