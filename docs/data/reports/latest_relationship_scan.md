# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-06T06:37:27.100478+00:00`
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

- `news_risk_high->crypto_major_4h` score `9.6768` n `65` status `ready` deltaP `33.6187` edge `0.6026` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `6.3162` n `65` status `ready` deltaP `21.1585` edge `0.5197` maxDD `-6.4195`
- `market_context_high->crypto_major_24h` score `4.7461` n `100` status `ready` deltaP `13.6151` edge `0.4318` maxDD `-6.1645`
- `news_risk_high->equity_24h` score `3.7844` n `65` status `ready` deltaP `11.0283` edge `0.2518` maxDD `-0.1298`
- `news_risk_high->index_24h` score `3.2544` n `65` status `ready` deltaP `22.6804` edge `0.12` maxDD `0.0`
- `news_risk_high->index_4h` score `2.6325` n `65` status `ready` deltaP `29.3223` edge `0.0501` maxDD `-0.4296`
- `market_context_high->crypto_major_4h` score `2.5674` n `117` status `ready` deltaP `13.1059` edge `0.223` maxDD `-4.047`
- `news_risk_high->crypto_major_1h` score `2.4881` n `65` status `ready` deltaP `9.567` edge `0.1791` maxDD `-1.5096`
- `news_risk_high->equity_4h` score `2.0745` n `65` status `ready` deltaP `17.6806` edge `0.1148` maxDD `-2.7837`
- `news_risk_high->index_1h` score `1.8925` n `65` status `ready` deltaP `23.6711` edge `0.0149` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.8888` n `65` status `ready` deltaP `18.0113` edge `0.0789` maxDD `-0.993`
- `market_context_high->fx_4h` score `1.2975` n `117` status `ready` deltaP `23.9238` edge `0.0243` maxDD `-0.3868`
- `news_risk_high->crypto_alt_1h` score `1.2548` n `65` status `ready` deltaP `4.2699` edge `0.128` maxDD `-2.4854`
- `market_context_high->commodity_4h` score `1.2077` n `117` status `ready` deltaP `16.2967` edge `0.062` maxDD `-1.6002`
- `market_context_high->fx_1h` score `0.9324` n `117` status `ready` deltaP `14.9381` edge `0.0065` maxDD `-0.271`
- `market_context_high->commodity_1h` score `0.7837` n `117` status `ready` deltaP `12.5045` edge `0.0216` maxDD `-0.5059`
- `market_context_high->metal_24h` score `0.2805` n `100` status `ready` deltaP `17.0928` edge `0.0595` maxDD `-5.6663`
- `market_context_high->crypto_alt_4h` score `0.2187` n `117` status `ready` deltaP `-0.7218` edge `0.1954` maxDD `-7.1222`
- `news_risk_high->metal_1h` score `0.1069` n `65` status `ready` deltaP `6.216` edge `0.0093` maxDD `-1.0132`
- `news_risk_high->commodity_24h` score `-0.0959` n `65` status `ready` deltaP `23.5104` edge `0.0341` maxDD `-10.9169`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
