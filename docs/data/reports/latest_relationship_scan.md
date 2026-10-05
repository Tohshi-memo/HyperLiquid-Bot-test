# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-05T11:07:34.964471+00:00`
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

- `market_context_high->unknown_1h` score `78.6726` n `124` status `ready` deltaP `-0.6422` edge `6.6018` maxDD `-0.9839`
- `market_context_high->crypto_major_24h` score `10.8116` n `81` status `ready` deltaP `29.8032` edge `0.7159` maxDD `-0.423`
- `news_risk_high->crypto_major_4h` score `9.3657` n `65` status `ready` deltaP `32.3992` edge `0.5848` maxDD `-0.6258`
- `market_context_high->crypto_alt_24h` score `6.4902` n `81` status `ready` deltaP `25.3666` edge `0.4337` maxDD `-2.9571`
- `news_risk_high->crypto_alt_4h` score `5.851` n `65` status `ready` deltaP `19.6341` edge `0.4911` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `3.4189` n `112` status `ready` deltaP `15.9844` edge `0.2581` maxDD `-4.047`
- `news_risk_high->index_24h` score `3.3958` n `65` status `ready` deltaP `24.1319` edge `0.1221` maxDD `0.0`
- `news_risk_high->equity_24h` score `3.1192` n `65` status `ready` deltaP `10.6865` edge `0.1987` maxDD `-0.1344`
- `news_risk_high->index_4h` score `2.968` n `65` status `ready` deltaP `32.6759` edge `0.0557` maxDD `-0.4296`
- `news_risk_high->equity_4h` score `2.546` n `65` status `ready` deltaP `20.5769` edge `0.136` maxDD `-2.881`
- `news_risk_high->crypto_major_1h` score `2.4749` n `65` status `ready` deltaP `9.8664` edge `0.176` maxDD `-1.5096`
- `news_risk_high->index_1h` score `2.0866` n `65` status `ready` deltaP `25.7669` edge `0.0171` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.8168` n `65` status `ready` deltaP `17.0967` edge `0.079` maxDD `-0.993`
- `market_context_high->fx_4h` score `1.6305` n `112` status `ready` deltaP `27.5915` edge `0.0276` maxDD `-0.3868`
- `news_risk_high->crypto_alt_1h` score `1.1313` n `65` status `ready` deltaP `3.5214` edge `0.1227` maxDD `-2.4854`
- `market_context_high->fx_1h` score `0.9184` n `124` status `ready` deltaP `14.8831` edge `0.0057` maxDD `-0.271`
- `market_context_high->commodity_4h` score `0.6873` n `112` status `ready` deltaP `12.2604` edge `0.0516` maxDD `-2.0852`
- `market_context_high->equity_24h` score `0.587` n `81` status `ready` deltaP `9.4329` edge `-0.0001` maxDD `-0.4427`
- `market_context_high->crypto_alt_4h` score `0.5822` n `112` status `ready` deltaP `3.027` edge `0.2007` maxDD `-7.1222`
- `market_context_high->crypto_major_1h` score `0.5261` n `124` status `ready` deltaP `9.0352` edge `0.0725` maxDD `-3.7778`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
