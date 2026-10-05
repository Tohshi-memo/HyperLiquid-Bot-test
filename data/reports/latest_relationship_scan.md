# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-05T17:52:32.175580+00:00`
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

- `market_context_high->crypto_major_24h` score `10.9334` n `78` status `ready` deltaP `29.9012` edge `0.7254` maxDD `-0.423`
- `news_risk_high->crypto_major_4h` score `9.648` n `65` status `ready` deltaP `33.6187` edge `0.6002` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `6.1528` n `65` status `ready` deltaP `21.0061` edge `0.5071` maxDD `-6.4195`
- `market_context_high->crypto_alt_24h` score `5.554` n `78` status `ready` deltaP `26.5492` edge `0.3478` maxDD `-2.9571`
- `news_risk_high->index_24h` score `3.3457` n `65` status `ready` deltaP `23.6111` edge `0.1214` maxDD `0.0`
- `news_risk_high->equity_24h` score `3.2129` n `65` status `ready` deltaP `9.8184` edge `0.2123` maxDD `-0.1344`
- `news_risk_high->index_4h` score `2.7981` n `65` status `ready` deltaP `31.1515` edge `0.0517` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.5996` n `65` status `ready` deltaP `10.1658` edge `0.1844` maxDD `-1.5096`
- `market_context_high->crypto_major_4h` score `2.5386` n `117` status `ready` deltaP `13.1059` edge `0.2206` maxDD `-4.047`
- `news_risk_high->equity_4h` score `2.3164` n `65` status `ready` deltaP `19.3574` edge `0.125` maxDD `-2.881`
- `news_risk_high->index_1h` score `1.9764` n `65` status `ready` deltaP `24.5693` edge `0.0159` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.9045` n `65` status `ready` deltaP `18.1637` edge `0.0792` maxDD `-0.993`
- `market_context_high->fx_4h` score `1.6482` n `117` status `ready` deltaP `27.8873` edge `0.0271` maxDD `-0.3868`
- `news_risk_high->crypto_alt_1h` score `1.316` n `65` status `ready` deltaP `4.2699` edge `0.1331` maxDD `-2.4854`
- `market_context_high->fx_1h` score `1.0713` n `117` status `ready` deltaP `16.5848` edge `0.0071` maxDD `-0.271`
- `market_context_high->commodity_4h` score `1.0501` n `117` status `ready` deltaP `15.0772` edge `0.057` maxDD `-1.6002`
- `market_context_high->metal_24h` score `0.812` n `78` status `ready` deltaP `25.5743` edge `0.0711` maxDD `-5.6663`
- `market_context_high->commodity_1h` score `0.6638` n `117` status `ready` deltaP `11.4566` edge `0.0186` maxDD `-0.5059`
- `market_context_high->equity_24h` score `0.612` n `78` status `ready` deltaP `13.4081` edge `-0.0323` maxDD `-0.1536`
- `news_risk_high->commodity_24h` score `0.3491` n `65` status `ready` deltaP `24.9119` edge `0.0818` maxDD `-10.9169`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
