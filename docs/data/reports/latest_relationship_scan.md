# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-06T06:22:31.260438+00:00`
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

- `news_risk_high->crypto_major_4h` score `9.6394` n `65` status `ready` deltaP `33.4662` edge `0.6005` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `6.2692` n `65` status `ready` deltaP `21.0061` edge `0.5168` maxDD `-6.4195`
- `market_context_high->crypto_major_24h` score `5.0287` n `99` status `ready` deltaP `14.2716` edge `0.444` maxDD `-5.607`
- `news_risk_high->equity_24h` score `3.7664` n `65` status `ready` deltaP `11.0283` edge `0.2503` maxDD `-0.1298`
- `news_risk_high->index_24h` score `3.2544` n `65` status `ready` deltaP `22.6804` edge `0.12` maxDD `0.0`
- `news_risk_high->index_4h` score `2.6301` n `65` status `ready` deltaP `29.3223` edge `0.0499` maxDD `-0.4296`
- `market_context_high->crypto_major_4h` score `2.53` n `117` status `ready` deltaP `12.9534` edge `0.2209` maxDD `-4.047`
- `news_risk_high->crypto_major_1h` score `2.4653` n `65` status `ready` deltaP `9.4173` edge `0.1782` maxDD `-1.5096`
- `news_risk_high->equity_4h` score `2.0613` n `65` status `ready` deltaP `17.6806` edge `0.1137` maxDD `-2.7837`
- `news_risk_high->index_1h` score `1.9057` n `65` status `ready` deltaP `23.8208` edge `0.015` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.8754` n `65` status `ready` deltaP `17.8588` edge `0.0788` maxDD `-0.993`
- `market_context_high->fx_4h` score `1.3109` n `117` status `ready` deltaP `24.0763` edge `0.0244` maxDD `-0.3868`
- `news_risk_high->crypto_alt_1h` score `1.232` n `65` status `ready` deltaP `4.1202` edge `0.1271` maxDD `-2.4854`
- `market_context_high->commodity_4h` score `1.2089` n `117` status `ready` deltaP `16.2967` edge `0.0621` maxDD `-1.6002`
- `market_context_high->fx_1h` score `0.9444` n `117` status `ready` deltaP `15.0878` edge `0.0065` maxDD `-0.271`
- `market_context_high->commodity_1h` score `0.7789` n `117` status `ready` deltaP `12.5045` edge `0.0212` maxDD `-0.5059`
- `market_context_high->metal_24h` score `0.3129` n `99` status `ready` deltaP `17.5675` edge `0.0605` maxDD `-5.6663`
- `market_context_high->crypto_alt_4h` score `0.1717` n `117` status `ready` deltaP `-0.8742` edge `0.1925` maxDD `-7.1222`
- `news_risk_high->metal_1h` score `0.1069` n `65` status `ready` deltaP `6.216` edge `0.0093` maxDD `-1.0132`
- `news_risk_high->commodity_24h` score `-0.0881` n `65` status `ready` deltaP `23.5104` edge `0.0351` maxDD `-10.9169`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
