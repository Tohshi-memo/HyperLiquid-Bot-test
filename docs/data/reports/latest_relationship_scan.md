# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-06T06:07:36.832845+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9400`

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

- `news_risk_high->crypto_major_4h` score `9.596` n `65` status `ready` deltaP `33.3138` edge `0.5979` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `6.2126` n `65` status `ready` deltaP `20.8537` edge `0.5131` maxDD `-6.4195`
- `market_context_high->crypto_major_24h` score `5.2987` n `98` status `ready` deltaP `14.945` edge `0.4575` maxDD `-5.2462`
- `news_risk_high->equity_24h` score `3.7448` n `65` status `ready` deltaP `11.0283` edge `0.2485` maxDD `-0.1298`
- `news_risk_high->index_24h` score `3.252` n `65` status `ready` deltaP `22.6804` edge `0.1198` maxDD `0.0`
- `news_risk_high->index_4h` score `2.6289` n `65` status `ready` deltaP `29.3223` edge `0.0498` maxDD `-0.4296`
- `market_context_high->crypto_major_4h` score `2.4866` n `117` status `ready` deltaP `12.801` edge `0.2183` maxDD `-4.047`
- `news_risk_high->crypto_major_1h` score `2.4641` n `65` status `ready` deltaP `9.4173` edge `0.1781` maxDD `-1.5096`
- `news_risk_high->equity_4h` score `2.0457` n `65` status `ready` deltaP `17.6806` edge `0.1124` maxDD `-2.7837`
- `news_risk_high->index_1h` score `1.9189` n `65` status `ready` deltaP `23.9705` edge `0.0151` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.8608` n `65` status `ready` deltaP `17.7064` edge `0.0786` maxDD `-0.993`
- `market_context_high->fx_4h` score `1.3121` n `117` status `ready` deltaP `24.0763` edge `0.0245` maxDD `-0.3868`
- `news_risk_high->crypto_alt_1h` score `1.2344` n `65` status `ready` deltaP `4.1202` edge `0.1273` maxDD `-2.4854`
- `market_context_high->commodity_4h` score `1.2113` n `117` status `ready` deltaP `16.2967` edge `0.0623` maxDD `-1.6002`
- `market_context_high->fx_1h` score `0.9456` n `117` status `ready` deltaP `15.0878` edge `0.0066` maxDD `-0.271`
- `market_context_high->commodity_1h` score `0.7621` n `117` status `ready` deltaP `12.3548` edge `0.0208` maxDD `-0.5059`
- `market_context_high->metal_24h` score `0.3453` n `98` status `ready` deltaP `18.0552` edge `0.0614` maxDD `-5.6663`
- `news_risk_high->metal_1h` score `0.1201` n `65` status `ready` deltaP `6.3657` edge `0.0094` maxDD `-1.0132`
- `market_context_high->crypto_alt_4h` score `0.1151` n `117` status `ready` deltaP `-1.0266` edge `0.1888` maxDD `-7.1222`
- `news_risk_high->commodity_24h` score `-0.0779` n `65` status `ready` deltaP `23.5104` edge `0.0364` maxDD `-10.9169`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
