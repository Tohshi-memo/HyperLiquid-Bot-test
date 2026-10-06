# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-06T04:23:03.027781+00:00`
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

- `news_risk_high->crypto_major_4h` score `9.2635` n `65` status `ready` deltaP `32.2467` edge `0.5773` maxDD `-0.6258`
- `market_context_high->crypto_major_24h` score `5.9957` n `91` status `ready` deltaP `15.5432` edge `0.5116` maxDD `-5.2462`
- `news_risk_high->crypto_alt_4h` score `5.7636` n `65` status `ready` deltaP `19.7866` edge `0.4828` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `3.6308` n `65` status `ready` deltaP `11.0283` edge `0.239` maxDD `-0.1298`
- `news_risk_high->index_24h` score `3.2508` n `65` status `ready` deltaP `22.6804` edge `0.1197` maxDD `0.0`
- `news_risk_high->index_4h` score `2.5646` n `65` status `ready` deltaP `28.7125` edge `0.0485` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.4365` n `65` status `ready` deltaP `9.4173` edge `0.1758` maxDD `-1.5096`
- `market_context_high->crypto_major_4h` score `2.1541` n `117` status `ready` deltaP `11.7339` edge `0.1977` maxDD `-4.047`
- `news_risk_high->index_1h` score `1.9704` n `65` status `ready` deltaP `24.5693` edge `0.0154` maxDD `-0.1997`
- `news_risk_high->equity_4h` score `1.9021` n `65` status `ready` deltaP `17.0708` edge `0.1045` maxDD `-2.7837`
- `news_risk_high->metal_4h` score `1.7648` n `65` status `ready` deltaP `16.7918` edge `0.0767` maxDD `-0.993`
- `market_context_high->fx_4h` score `1.3535` n `117` status `ready` deltaP `24.5336` edge `0.0249` maxDD `-0.3868`
- `market_context_high->commodity_4h` score `1.3097` n `117` status `ready` deltaP `17.2113` edge `0.0644` maxDD `-1.6002`
- `news_risk_high->crypto_alt_1h` score `1.1996` n `65` status `ready` deltaP `4.1202` edge `0.1244` maxDD `-2.4854`
- `market_context_high->fx_1h` score `0.9575` n `117` status `ready` deltaP `15.2375` edge `0.0066` maxDD `-0.271`
- `market_context_high->commodity_1h` score `0.7369` n `117` status `ready` deltaP `12.0554` edge `0.0207` maxDD `-0.5059`
- `market_context_high->metal_24h` score `0.5215` n `91` status `ready` deltaP `20.949` edge `0.0647` maxDD `-5.6663`
- `market_context_high->crypto_alt_24h` score `0.4542` n `91` status `ready` deltaP `14.7238` edge `0.1545` maxDD `-12.8513`
- `news_risk_high->metal_1h` score `0.1081` n `65` status `ready` deltaP `6.216` edge `0.0094` maxDD `-1.0132`
- `news_risk_high->commodity_24h` score `0.0494` n `65` status `ready` deltaP `24.3696` edge `0.047` maxDD `-10.9169`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
