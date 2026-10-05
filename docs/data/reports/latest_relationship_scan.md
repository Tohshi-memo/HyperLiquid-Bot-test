# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-05T13:52:32.047869+00:00`
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

- `market_context_high->crypto_major_24h` score `10.9508` n `82` status `ready` deltaP `29.8484` edge `0.7272` maxDD `-0.423`
- `news_risk_high->crypto_major_4h` score `9.384` n `65` status `ready` deltaP `32.704` edge `0.5843` maxDD `-0.6258`
- `market_context_high->crypto_alt_24h` score `6.1806` n `82` status `ready` deltaP `25.487` edge `0.4071` maxDD `-2.9571`
- `news_risk_high->crypto_alt_4h` score `5.713` n `65` status `ready` deltaP `19.6341` edge `0.4796` maxDD `-6.4195`
- `news_risk_high->index_24h` score `3.4585` n `65` status `ready` deltaP `24.8264` edge `0.1227` maxDD `0.0`
- `news_risk_high->equity_24h` score `3.0034` n `65` status `ready` deltaP `9.6448` edge `0.196` maxDD `-0.1344`
- `news_risk_high->index_4h` score `2.8831` n `65` status `ready` deltaP `31.9137` edge `0.0537` maxDD `-0.4296`
- `market_context_high->crypto_major_4h` score `2.7762` n `117` status `ready` deltaP `13.0459` edge `0.2408` maxDD `-4.047`
- `news_risk_high->crypto_major_1h` score `2.4905` n `65` status `ready` deltaP `9.7167` edge `0.1783` maxDD `-1.5096`
- `news_risk_high->equity_4h` score `2.42` n `65` status `ready` deltaP `20.5769` edge `0.1255` maxDD `-2.881`
- `news_risk_high->index_1h` score `2.0447` n `65` status `ready` deltaP `25.3178` edge `0.0166` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.7964` n `65` status `ready` deltaP `17.0967` edge `0.0773` maxDD `-0.993`
- `market_context_high->fx_4h` score `1.5616` n `117` status `ready` deltaP `26.8202` edge `0.027` maxDD `-0.3868`
- `news_risk_high->crypto_alt_1h` score `1.1577` n `65` status `ready` deltaP `3.5214` edge `0.1249` maxDD `-2.4854`
- `market_context_high->equity_24h` score `1.0365` n `82` status `ready` deltaP `13.3596` edge `0.0034` maxDD `-0.1536`
- `market_context_high->fx_1h` score `0.9245` n `121` status `ready` deltaP `14.8995` edge `0.0061` maxDD `-0.271`
- `market_context_high->metal_24h` score `0.8992` n `82` status `ready` deltaP `26.8165` edge `0.0756` maxDD `-5.7943`
- `market_context_high->commodity_4h` score `0.838` n `117` status `ready` deltaP `13.2153` edge `0.0488` maxDD `-1.3656`
- `market_context_high->crypto_alt_4h` score `0.4543` n `117` status `ready` deltaP `0.3179` edge `0.2081` maxDD `-7.1222`
- `news_risk_high->commodity_24h` score `0.4372` n `65` status `ready` deltaP `24.9119` edge `0.0931` maxDD `-10.9169`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
