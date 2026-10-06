# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-06T05:52:27.876870+00:00`
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

- `news_risk_high->crypto_major_4h` score `9.5478` n `65` status `ready` deltaP `33.1614` edge `0.5949` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `6.1524` n `65` status `ready` deltaP `20.7012` edge `0.5091` maxDD `-6.4195`
- `market_context_high->crypto_major_24h` score `5.5231` n `97` status `ready` deltaP `15.6358` edge `0.4716` maxDD `-5.2462`
- `news_risk_high->equity_24h` score `3.7268` n `65` status `ready` deltaP `11.0283` edge `0.247` maxDD `-0.1298`
- `news_risk_high->index_24h` score `3.252` n `65` status `ready` deltaP `22.6804` edge `0.1198` maxDD `0.0`
- `news_risk_high->index_4h` score `2.6265` n `65` status `ready` deltaP `29.3223` edge `0.0496` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.4533` n `65` status `ready` deltaP `9.4173` edge `0.1772` maxDD `-1.5096`
- `market_context_high->crypto_major_4h` score `2.4384` n `117` status `ready` deltaP `12.6486` edge `0.2153` maxDD `-4.047`
- `news_risk_high->equity_4h` score `2.0289` n `65` status `ready` deltaP `17.6806` edge `0.111` maxDD `-2.7837`
- `news_risk_high->index_1h` score `1.9309` n `65` status `ready` deltaP `24.1202` edge `0.0151` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.845` n `65` status `ready` deltaP `17.554` edge `0.0783` maxDD `-0.993`
- `market_context_high->fx_4h` score `1.3121` n `117` status `ready` deltaP `24.0763` edge `0.0245` maxDD `-0.3868`
- `news_risk_high->crypto_alt_1h` score `1.226` n `65` status `ready` deltaP `4.1202` edge `0.1266` maxDD `-2.4854`
- `market_context_high->commodity_4h` score `1.2173` n `117` status `ready` deltaP `16.2967` edge `0.0628` maxDD `-1.6002`
- `market_context_high->fx_1h` score `0.9444` n `117` status `ready` deltaP `15.0878` edge `0.0065` maxDD `-0.271`
- `market_context_high->commodity_1h` score `0.7489` n `117` status `ready` deltaP `12.2051` edge `0.0207` maxDD `-0.5059`
- `market_context_high->metal_24h` score `0.3839` n `97` status `ready` deltaP `18.5567` edge `0.063` maxDD `-5.6663`
- `news_risk_high->metal_1h` score `0.1057` n `65` status `ready` deltaP `6.216` edge `0.0092` maxDD `-1.0132`
- `market_context_high->crypto_alt_4h` score `0.0549` n `117` status `ready` deltaP `-1.1791` edge `0.1848` maxDD `-7.1222`
- `news_risk_high->commodity_24h` score `-0.0565` n `65` status `ready` deltaP `23.6823` edge `0.038` maxDD `-10.9169`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
