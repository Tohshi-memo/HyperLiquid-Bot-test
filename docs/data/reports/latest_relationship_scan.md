# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-06T02:37:29.241919+00:00`
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

- `news_risk_high->crypto_major_4h` score `9.0187` n `65` status `ready` deltaP `31.3321` edge `0.563` maxDD `-0.6258`
- `market_context_high->crypto_major_24h` score `8.0952` n `84` status `ready` deltaP `20.3731` edge `0.5978` maxDD `-2.7214`
- `news_risk_high->crypto_alt_4h` score `5.3976` n `65` status `ready` deltaP `18.872` edge `0.4584` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `3.4701` n `65` status `ready` deltaP `10.6847` edge `0.2279` maxDD `-0.1298`
- `market_context_high->crypto_alt_24h` score `3.4696` n `84` status `ready` deltaP `19.9312` edge `0.2487` maxDD `-5.3954`
- `news_risk_high->index_24h` score `3.2484` n `65` status `ready` deltaP `22.6804` edge `0.1195` maxDD `0.0`
- `news_risk_high->index_4h` score `2.5524` n `65` status `ready` deltaP `28.5601` edge `0.0485` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.4102` n `65` status `ready` deltaP `9.2676` edge `0.1746` maxDD `-1.5096`
- `news_risk_high->index_1h` score `1.9979` n `65` status `ready` deltaP `24.8687` edge `0.0157` maxDD `-0.1997`
- `market_context_high->crypto_major_4h` score `1.9093` n `117` status `ready` deltaP `10.8193` edge `0.1834` maxDD `-4.047`
- `news_risk_high->equity_4h` score `1.8559` n `65` status `ready` deltaP `16.6135` edge `0.1037` maxDD `-2.7837`
- `news_risk_high->metal_4h` score `1.7234` n `65` status `ready` deltaP `16.3345` edge `0.0763` maxDD `-0.993`
- `market_context_high->fx_4h` score `1.4095` n `117` status `ready` deltaP `25.1434` edge `0.0255` maxDD `-0.3868`
- `market_context_high->commodity_4h` score `1.3109` n `117` status `ready` deltaP `17.2113` edge `0.0645` maxDD `-1.6002`
- `news_risk_high->crypto_alt_1h` score `1.1984` n `65` status `ready` deltaP `3.9705` edge `0.1253` maxDD `-2.4854`
- `market_context_high->fx_1h` score `0.9947` n `117` status `ready` deltaP `15.6866` edge `0.0067` maxDD `-0.271`
- `market_context_high->commodity_1h` score `0.7333` n `117` status `ready` deltaP `12.0554` edge `0.0204` maxDD `-0.5059`
- `market_context_high->metal_24h` score `0.4934` n `84` status `ready` deltaP `20.4222` edge `0.0646` maxDD `-5.6663`
- `news_risk_high->commodity_24h` score `0.1729` n `65` status `ready` deltaP `25.2287` edge `0.0571` maxDD `-10.9169`
- `news_risk_high->metal_1h` score `0.0686` n `65` status `ready` deltaP `5.7669` edge `0.0091` maxDD `-1.0132`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
