# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-06T04:37:32.110955+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9496`

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

- `news_risk_high->crypto_major_4h` score `9.3153` n `65` status `ready` deltaP `32.3992` edge `0.5806` maxDD `-0.6258`
- `market_context_high->crypto_major_24h` score `5.9455` n `92` status `ready` deltaP `15.7104` edge `0.5063` maxDD `-5.2462`
- `news_risk_high->crypto_alt_4h` score `5.8394` n `65` status `ready` deltaP `19.939` edge `0.4881` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `3.6476` n `65` status `ready` deltaP `11.0283` edge `0.2404` maxDD `-0.1298`
- `news_risk_high->index_24h` score `3.2508` n `65` status `ready` deltaP `22.6804` edge `0.1197` maxDD `0.0`
- `news_risk_high->index_4h` score `2.5792` n `65` status `ready` deltaP `28.8649` edge `0.0487` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.4437` n `65` status `ready` deltaP `9.4173` edge `0.1764` maxDD `-1.5096`
- `market_context_high->crypto_major_4h` score `2.2059` n `117` status `ready` deltaP `11.8864` edge `0.201` maxDD `-4.047`
- `news_risk_high->index_1h` score `1.9704` n `65` status `ready` deltaP `24.5693` edge `0.0154` maxDD `-0.1997`
- `news_risk_high->equity_4h` score `1.9263` n `65` status `ready` deltaP `17.2232` edge `0.1055` maxDD `-2.7837`
- `news_risk_high->metal_4h` score `1.7794` n `65` status `ready` deltaP `16.9442` edge `0.0769` maxDD `-0.993`
- `market_context_high->fx_4h` score `1.3401` n `117` status `ready` deltaP `24.3812` edge `0.0248` maxDD `-0.3868`
- `market_context_high->commodity_4h` score `1.2963` n `117` status `ready` deltaP `17.0589` edge `0.0643` maxDD `-1.6002`
- `news_risk_high->crypto_alt_1h` score `1.2128` n `65` status `ready` deltaP `4.1202` edge `0.1255` maxDD `-2.4854`
- `market_context_high->fx_1h` score `0.9444` n `117` status `ready` deltaP `15.0878` edge `0.0065` maxDD `-0.271`
- `market_context_high->commodity_1h` score `0.7369` n `117` status `ready` deltaP `12.0554` edge `0.0207` maxDD `-0.5059`
- `market_context_high->metal_24h` score `0.5413` n `92` status `ready` deltaP `21.2834` edge `0.065` maxDD `-5.6663`
- `market_context_high->crypto_alt_24h` score `0.3083` n `92` status `ready` deltaP `14.0595` edge `0.1526` maxDD `-12.9847`
- `news_risk_high->metal_1h` score `0.1081` n `65` status `ready` deltaP `6.216` edge `0.0094` maxDD `-1.0132`
- `news_risk_high->commodity_24h` score `0.0377` n `65` status `ready` deltaP `24.3696` edge `0.0455` maxDD `-10.9169`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
