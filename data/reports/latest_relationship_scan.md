# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-05T19:53:18.040834+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8232`

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

- `market_context_high->crypto_major_24h` score `10.6902` n `78` status `ready` deltaP `28.7508` edge `0.7128` maxDD `-0.423`
- `news_risk_high->crypto_major_4h` score `9.5021` n `65` status `ready` deltaP `33.1892` edge `0.5909` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `5.9634` n `65` status `ready` deltaP `20.2736` edge `0.4962` maxDD `-6.4195`
- `market_context_high->crypto_alt_24h` score `5.5125` n `78` status `ready` deltaP `26.0758` edge `0.3475` maxDD `-2.9571`
- `news_risk_high->index_24h` score `3.2658` n `65` status `ready` deltaP `22.8374` edge `0.1199` maxDD `0.0`
- `news_risk_high->equity_24h` score `3.2085` n `65` status `ready` deltaP `9.7632` edge `0.2123` maxDD `-0.1344`
- `news_risk_high->index_4h` score `2.7017` n `65` status `ready` deltaP `30.1123` edge `0.0506` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.4646` n `65` status `ready` deltaP `9.4374` edge `0.178` maxDD `-1.5096`
- `market_context_high->crypto_major_4h` score `2.3927` n `117` status `ready` deltaP `12.6764` edge `0.2113` maxDD `-4.047`
- `news_risk_high->equity_4h` score `2.1783` n `65` status `ready` deltaP `18.3353` edge `0.1203` maxDD `-2.881`
- `news_risk_high->index_1h` score `1.9272` n `65` status `ready` deltaP `23.9839` edge `0.0157` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.837` n `65` status `ready` deltaP `17.5591` edge `0.0776` maxDD `-0.993`
- `market_context_high->fx_4h` score `1.6311` n `117` status `ready` deltaP `27.7038` edge `0.0269` maxDD `-0.3868`
- `market_context_high->commodity_4h` score `1.1803` n `117` status `ready` deltaP `15.9835` edge `0.0618` maxDD `-1.6002`
- `news_risk_high->crypto_alt_1h` score `1.1361` n `65` status `ready` deltaP `3.3869` edge `0.124` maxDD `-2.4854`
- `market_context_high->fx_1h` score `1.0321` n `117` status `ready` deltaP `16.1245` edge `0.0069` maxDD `-0.271`
- `market_context_high->commodity_1h` score `0.768` n `117` status `ready` deltaP `12.4889` edge `0.0204` maxDD `-0.5059`
- `market_context_high->metal_24h` score `0.7524` n `78` status `ready` deltaP `24.878` edge `0.0681` maxDD `-5.6663`
- `market_context_high->equity_24h` score `0.6076` n `78` status `ready` deltaP `13.3529` edge `-0.0323` maxDD `-0.1536`
- `news_risk_high->commodity_24h` score `0.3529` n `65` status `ready` deltaP `25.0759` edge `0.0812` maxDD `-10.9169`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
