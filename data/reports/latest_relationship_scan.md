# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-06T03:07:25.928863+00:00`
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

- `news_risk_high->crypto_major_4h` score `9.0585` n `65` status `ready` deltaP `31.4845` edge `0.5653` maxDD `-0.6258`
- `market_context_high->crypto_major_24h` score `7.2809` n `86` status `ready` deltaP `18.6126` edge `0.565` maxDD `-3.921`
- `news_risk_high->crypto_alt_4h` score `5.4554` n `65` status `ready` deltaP `19.0244` edge `0.4622` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `3.5307` n `65` status `ready` deltaP `10.8565` edge `0.2318` maxDD `-0.1298`
- `news_risk_high->index_24h` score `3.2508` n `65` status `ready` deltaP `22.6804` edge `0.1197` maxDD `0.0`
- `news_risk_high->index_4h` score `2.5524` n `65` status `ready` deltaP `28.5601` edge `0.0485` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.397` n `65` status `ready` deltaP `9.2676` edge `0.1735` maxDD `-1.5096`
- `market_context_high->crypto_alt_24h` score `2.3657` n `86` status `ready` deltaP `18.3369` edge `0.2103` maxDD `-8.1659`
- `news_risk_high->index_1h` score `2.0219` n `65` status `ready` deltaP `25.1681` edge `0.0157` maxDD `-0.1997`
- `market_context_high->crypto_major_4h` score `1.9491` n `117` status `ready` deltaP `10.9717` edge `0.1857` maxDD `-4.047`
- `news_risk_high->equity_4h` score `1.8571` n `65` status `ready` deltaP `16.6135` edge `0.1038` maxDD `-2.7837`
- `news_risk_high->metal_4h` score `1.7246` n `65` status `ready` deltaP `16.3345` edge `0.0764` maxDD `-0.993`
- `market_context_high->fx_4h` score `1.3961` n `117` status `ready` deltaP `24.9909` edge `0.0254` maxDD `-0.3868`
- `market_context_high->commodity_4h` score `1.3133` n `117` status `ready` deltaP `17.2113` edge `0.0647` maxDD `-1.6002`
- `news_risk_high->crypto_alt_1h` score `1.1672` n `65` status `ready` deltaP `3.9705` edge `0.1227` maxDD `-2.4854`
- `market_context_high->fx_1h` score `0.9947` n `117` status `ready` deltaP `15.6866` edge `0.0067` maxDD `-0.271`
- `market_context_high->commodity_1h` score `0.7214` n `117` status `ready` deltaP `11.9057` edge `0.0204` maxDD `-0.5059`
- `market_context_high->metal_24h` score `0.5355` n `86` status `ready` deltaP `21.142` edge `0.0652` maxDD `-5.6663`
- `news_risk_high->commodity_24h` score `0.1518` n `65` status `ready` deltaP `25.2287` edge `0.0544` maxDD `-10.9169`
- `news_risk_high->metal_1h` score `0.0686` n `65` status `ready` deltaP `5.7669` edge `0.0091` maxDD `-1.0132`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
