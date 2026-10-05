# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-05T15:52:33.873354+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8072`

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

- `market_context_high->crypto_major_24h` score `11.1589` n `78` status `ready` deltaP `30.7692` edge `0.7384` maxDD `-0.423`
- `news_risk_high->crypto_major_4h` score `9.6022` n `65` status `ready` deltaP `33.4662` edge `0.5974` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `6.001` n `65` status `ready` deltaP `20.5488` edge `0.4975` maxDD `-6.4195`
- `market_context_high->crypto_alt_24h` score `5.4096` n `78` status `ready` deltaP `25.8547` edge `0.3404` maxDD `-2.9571`
- `news_risk_high->index_24h` score `3.4494` n `65` status `ready` deltaP `24.6528` edge `0.1231` maxDD `0.0`
- `news_risk_high->equity_24h` score `3.1709` n `65` status `ready` deltaP `9.8184` edge `0.2088` maxDD `-0.1344`
- `news_risk_high->index_4h` score `2.8771` n `65` status `ready` deltaP `31.9137` edge `0.0532` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.5564` n `65` status `ready` deltaP `10.0161` edge `0.1818` maxDD `-1.5096`
- `market_context_high->crypto_major_4h` score `2.4928` n `117` status `ready` deltaP `12.9534` edge `0.2178` maxDD `-4.047`
- `news_risk_high->equity_4h` score `2.4412` n `65` status `ready` deltaP `20.272` edge `0.1293` maxDD `-2.881`
- `news_risk_high->index_1h` score `2.0003` n `65` status `ready` deltaP `24.8687` edge `0.0159` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.89` n `65` status `ready` deltaP `18.0113` edge `0.079` maxDD `-0.993`
- `market_context_high->fx_4h` score `1.6056` n `117` status `ready` deltaP `27.4299` edge `0.0266` maxDD `-0.3868`
- `news_risk_high->crypto_alt_1h` score `1.2021` n `65` status `ready` deltaP `3.6711` edge `0.1276` maxDD `-2.4854`
- `market_context_high->fx_1h` score `1.045` n `117` status `ready` deltaP `16.2854` edge `0.0069` maxDD `-0.271`
- `market_context_high->commodity_4h` score `0.9846` n `117` status `ready` deltaP `14.4674` edge `0.0556` maxDD `-1.6002`
- `market_context_high->metal_24h` score `0.9138` n `78` status `ready` deltaP `26.9632` edge `0.0749` maxDD `-5.6663`
- `market_context_high->commodity_1h` score `0.6543` n `117` status `ready` deltaP `11.3069` edge `0.0188` maxDD `-0.5059`
- `market_context_high->equity_24h` score `0.57` n `78` status `ready` deltaP `13.4081` edge `-0.0358` maxDD `-0.1536`
- `news_risk_high->commodity_24h` score `0.3779` n `65` status `ready` deltaP `24.9119` edge `0.0855` maxDD `-10.9169`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
