# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-06T01:07:32.720299+00:00`
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

- `market_context_high->crypto_major_24h` score `10.4952` n `78` status `ready` deltaP `27.3328` edge `0.706` maxDD `-0.423`
- `news_risk_high->crypto_major_4h` score `9.0295` n `65` status `ready` deltaP `31.3321` edge `0.5639` maxDD `-0.6258`
- `market_context_high->crypto_alt_24h` score `5.7144` n `78` status `ready` deltaP `26.1697` edge `0.3637` maxDD `-2.9571`
- `news_risk_high->crypto_alt_4h` score `5.4228` n `65` status `ready` deltaP `18.872` edge `0.4605` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `3.3677` n `65` status `ready` deltaP `9.6538` edge `0.2263` maxDD `-0.1344`
- `news_risk_high->index_24h` score `3.2376` n `65` status `ready` deltaP `22.6804` edge `0.1186` maxDD `0.0`
- `news_risk_high->index_4h` score `2.5572` n `65` status `ready` deltaP `28.5601` edge `0.0489` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.4294` n `65` status `ready` deltaP `9.1179` edge `0.1772` maxDD `-1.5096`
- `news_risk_high->index_1h` score `1.9848` n `65` status `ready` deltaP `24.719` edge `0.0156` maxDD `-0.1997`
- `news_risk_high->equity_4h` score `1.9229` n `65` status `ready` deltaP `16.6135` edge `0.1105` maxDD `-2.881`
- `market_context_high->crypto_major_4h` score `1.9201` n `117` status `ready` deltaP `10.8193` edge `0.1843` maxDD `-4.047`
- `news_risk_high->metal_4h` score `1.7222` n `65` status `ready` deltaP `16.3345` edge `0.0762` maxDD `-0.993`
- `market_context_high->fx_4h` score `1.4642` n `117` status `ready` deltaP `25.7531` edge `0.026` maxDD `-0.3868`
- `market_context_high->commodity_4h` score `1.3025` n `117` status `ready` deltaP `17.2113` edge `0.0638` maxDD `-1.6002`
- `news_risk_high->crypto_alt_1h` score `1.2273` n `65` status `ready` deltaP `3.8208` edge `0.1287` maxDD `-2.4854`
- `market_context_high->fx_1h` score `1.0079` n `117` status `ready` deltaP `15.8363` edge `0.0068` maxDD `-0.271`
- `market_context_high->equity_24h` score `0.7668` n `78` status `ready` deltaP `13.2435` edge `-0.0183` maxDD `-0.1536`
- `market_context_high->metal_24h` score `0.7635` n `78` status `ready` deltaP `24.7026` edge `0.0707` maxDD `-5.6663`
- `market_context_high->commodity_1h` score `0.7441` n `117` status `ready` deltaP `12.2051` edge `0.0203` maxDD `-0.5059`
- `news_risk_high->commodity_24h` score `0.2434` n `65` status `ready` deltaP `25.4005` edge `0.065` maxDD `-10.9169`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
