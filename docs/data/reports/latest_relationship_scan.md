# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-05T16:22:31.946632+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8110`

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

- `market_context_high->crypto_major_24h` score `11.1318` n `78` status `ready` deltaP `30.5956` edge `0.7373` maxDD `-0.423`
- `news_risk_high->crypto_major_4h` score `9.6492` n `65` status `ready` deltaP `33.6187` edge `0.6003` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `6.0806` n `65` status `ready` deltaP `20.8537` edge `0.5021` maxDD `-6.4195`
- `market_context_high->crypto_alt_24h` score `5.4859` n `78` status `ready` deltaP `26.0283` edge `0.3456` maxDD `-2.9571`
- `news_risk_high->index_24h` score `3.4494` n `65` status `ready` deltaP `24.6528` edge `0.1231` maxDD `0.0`
- `news_risk_high->equity_24h` score `3.2033` n `65` status `ready` deltaP `9.8184` edge `0.2115` maxDD `-0.1344`
- `news_risk_high->index_4h` score `2.8771` n `65` status `ready` deltaP `31.9137` edge `0.0532` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.6068` n `65` status `ready` deltaP `10.3155` edge `0.184` maxDD `-1.5096`
- `market_context_high->crypto_major_4h` score `2.5398` n `117` status `ready` deltaP `13.1059` edge `0.2207` maxDD `-4.047`
- `news_risk_high->equity_4h` score `2.4448` n `65` status `ready` deltaP `20.272` edge `0.1296` maxDD `-2.881`
- `news_risk_high->index_1h` score `2.0015` n `65` status `ready` deltaP `24.8687` edge `0.016` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.9093` n `65` status `ready` deltaP `18.1637` edge `0.0796` maxDD `-0.993`
- `market_context_high->fx_4h` score `1.6202` n `117` status `ready` deltaP `27.5824` edge `0.0268` maxDD `-0.3868`
- `news_risk_high->crypto_alt_1h` score `1.2572` n `65` status `ready` deltaP `3.9705` edge `0.1302` maxDD `-2.4854`
- `market_context_high->fx_1h` score `1.0582` n `117` status `ready` deltaP `16.4351` edge `0.007` maxDD `-0.271`
- `market_context_high->commodity_4h` score `0.9786` n `117` status `ready` deltaP `14.4674` edge `0.0551` maxDD `-1.6002`
- `market_context_high->metal_24h` score `0.8911` n `78` status `ready` deltaP `26.6159` edge `0.0743` maxDD `-5.6663`
- `market_context_high->commodity_1h` score `0.6531` n `117` status `ready` deltaP `11.3069` edge `0.0187` maxDD `-0.5059`
- `market_context_high->equity_24h` score `0.6024` n `78` status `ready` deltaP `13.4081` edge `-0.0331` maxDD `-0.1536`
- `news_risk_high->commodity_24h` score `0.3647` n `65` status `ready` deltaP `24.9119` edge `0.0838` maxDD `-10.9169`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
