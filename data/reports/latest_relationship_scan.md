# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-06T05:37:27.120367+00:00`
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

- `news_risk_high->crypto_major_4h` score `9.5032` n `65` status `ready` deltaP `33.0089` edge `0.5922` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `6.0922` n `65` status `ready` deltaP `20.5488` edge `0.5051` maxDD `-6.4195`
- `market_context_high->crypto_major_24h` score `5.6818` n `96` status `ready` deltaP `16.3445` edge `0.4801` maxDD `-5.2462`
- `news_risk_high->equity_24h` score `3.7088` n `65` status `ready` deltaP `11.0283` edge `0.2455` maxDD `-0.1298`
- `news_risk_high->index_24h` score `3.2508` n `65` status `ready` deltaP `22.6804` edge `0.1197` maxDD `0.0`
- `news_risk_high->index_4h` score `2.6241` n `65` status `ready` deltaP `29.3223` edge `0.0494` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.439` n `65` status `ready` deltaP `9.2676` edge `0.177` maxDD `-1.5096`
- `market_context_high->crypto_major_4h` score `2.3938` n `117` status `ready` deltaP `12.4961` edge `0.2126` maxDD `-4.047`
- `news_risk_high->equity_4h` score `2.0157` n `65` status `ready` deltaP `17.6806` edge `0.1099` maxDD `-2.7837`
- `news_risk_high->index_1h` score `1.944` n `65` status `ready` deltaP `24.2699` edge `0.0152` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.8304` n `65` status `ready` deltaP `17.4015` edge `0.0781` maxDD `-0.993`
- `market_context_high->fx_4h` score `1.3121` n `117` status `ready` deltaP `24.0763` edge `0.0245` maxDD `-0.3868`
- `market_context_high->commodity_4h` score `1.2331` n `117` status `ready` deltaP `16.4491` edge `0.0631` maxDD `-1.6002`
- `news_risk_high->crypto_alt_1h` score `1.2188` n `65` status `ready` deltaP `4.1202` edge `0.126` maxDD `-2.4854`
- `market_context_high->fx_1h` score `0.9324` n `117` status `ready` deltaP `14.9381` edge `0.0065` maxDD `-0.271`
- `market_context_high->commodity_1h` score `0.7357` n `117` status `ready` deltaP `12.0554` edge `0.0206` maxDD `-0.5059`
- `market_context_high->metal_24h` score `0.4146` n `96` status `ready` deltaP `19.0722` edge `0.0635` maxDD `-5.6663`
- `news_risk_high->metal_1h` score `0.1057` n `65` status `ready` deltaP `6.216` edge `0.0092` maxDD `-1.0132`
- `market_context_high->crypto_alt_4h` score `-0.0053` n `117` status `ready` deltaP `-1.3315` edge `0.1808` maxDD `-7.1222`
- `news_risk_high->commodity_24h` score `-0.0359` n `65` status `ready` deltaP `23.8541` edge `0.0395` maxDD `-10.9169`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
