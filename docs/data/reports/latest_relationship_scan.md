# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-05T10:52:31.697489+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8312`

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

- `market_context_high->unknown_1h` score `79.287` n `124` status `ready` deltaP `-0.6422` edge `6.653` maxDD `-0.9839`
- `market_context_high->crypto_major_24h` score `10.778` n `81` status `ready` deltaP `29.8032` edge `0.7131` maxDD `-0.423`
- `news_risk_high->crypto_major_4h` score `9.3789` n `65` status `ready` deltaP `32.3992` edge `0.5859` maxDD `-0.6258`
- `market_context_high->crypto_alt_24h` score `6.5514` n `81` status `ready` deltaP `25.3666` edge `0.4388` maxDD `-2.9571`
- `news_risk_high->crypto_alt_4h` score `5.869` n `65` status `ready` deltaP `19.6341` edge `0.4926` maxDD `-6.4195`
- `news_risk_high->index_24h` score `3.3946` n `65` status `ready` deltaP `24.1319` edge `0.122` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `3.3577` n `112` status `ready` deltaP `15.9844` edge `0.253` maxDD `-4.047`
- `news_risk_high->equity_24h` score `3.1342` n `65` status `ready` deltaP `10.8601` edge `0.1988` maxDD `-0.1344`
- `news_risk_high->index_4h` score `2.9704` n `65` status `ready` deltaP `32.6759` edge `0.0559` maxDD `-0.4296`
- `news_risk_high->equity_4h` score `2.5628` n `65` status `ready` deltaP `20.5769` edge `0.1374` maxDD `-2.881`
- `news_risk_high->crypto_major_1h` score `2.4737` n `65` status `ready` deltaP `9.8664` edge `0.1759` maxDD `-1.5096`
- `news_risk_high->index_1h` score `2.0854` n `65` status `ready` deltaP `25.7669` edge `0.017` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.8362` n `65` status `ready` deltaP `17.2491` edge `0.0796` maxDD `-0.993`
- `market_context_high->fx_4h` score `1.6293` n `112` status `ready` deltaP `27.5915` edge `0.0275` maxDD `-0.3868`
- `news_risk_high->crypto_alt_1h` score `1.1289` n `65` status `ready` deltaP `3.5214` edge `0.1225` maxDD `-2.4854`
- `market_context_high->fx_1h` score `0.9196` n `124` status `ready` deltaP `14.8831` edge `0.0058` maxDD `-0.271`
- `market_context_high->commodity_4h` score `0.5967` n `112` status `ready` deltaP `11.5201` edge `0.0501` maxDD `-2.174`
- `market_context_high->crypto_major_1h` score `0.5309` n `124` status `ready` deltaP `9.0352` edge `0.0729` maxDD `-3.7778`
- `news_risk_high->commodity_24h` score `0.5058` n `65` status `ready` deltaP `24.9119` edge `0.1019` maxDD `-10.9169`
- `market_context_high->equity_24h` score `0.4961` n `81` status `ready` deltaP `8.3719` edge `-0.0006` maxDD `-0.4427`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
