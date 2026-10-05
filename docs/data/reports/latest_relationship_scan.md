# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-05T11:22:24.783929+00:00`
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

- `market_context_high->unknown_1h` score `77.4561` n `124` status `ready` deltaP `-1.299` edge `6.5048` maxDD `-0.9839`
- `market_context_high->crypto_major_24h` score `10.8344` n `81` status `ready` deltaP `29.8032` edge `0.7178` maxDD `-0.423`
- `news_risk_high->crypto_major_4h` score `9.3561` n `65` status `ready` deltaP `32.3992` edge `0.584` maxDD `-0.6258`
- `market_context_high->crypto_alt_24h` score `6.417` n `81` status `ready` deltaP `25.3666` edge `0.4276` maxDD `-2.9571`
- `news_risk_high->crypto_alt_4h` score `5.833` n `65` status `ready` deltaP `19.6341` edge `0.4896` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `3.4657` n `112` status `ready` deltaP `15.9844` edge `0.262` maxDD `-4.047`
- `news_risk_high->index_24h` score `3.412` n `65` status `ready` deltaP `24.3056` edge `0.1223` maxDD `0.0`
- `news_risk_high->equity_24h` score `3.1192` n `65` status `ready` deltaP `10.6865` edge `0.1987` maxDD `-0.1344`
- `news_risk_high->index_4h` score `2.9656` n `65` status `ready` deltaP `32.6759` edge `0.0555` maxDD `-0.4296`
- `news_risk_high->equity_4h` score `2.5304` n `65` status `ready` deltaP `20.5769` edge `0.1347` maxDD `-2.881`
- `news_risk_high->crypto_major_1h` score `2.4881` n `65` status `ready` deltaP `9.8664` edge `0.1771` maxDD `-1.5096`
- `news_risk_high->index_1h` score `2.0866` n `65` status `ready` deltaP `25.7669` edge `0.0171` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.7998` n `65` status `ready` deltaP `16.9442` edge `0.0786` maxDD `-0.993`
- `market_context_high->fx_4h` score `1.6329` n `112` status `ready` deltaP `27.5915` edge `0.0278` maxDD `-0.3868`
- `news_risk_high->crypto_alt_1h` score `1.1613` n `65` status `ready` deltaP `3.6711` edge `0.1242` maxDD `-2.4854`
- `market_context_high->fx_1h` score `0.9745` n `124` status `ready` deltaP `15.5399` edge `0.006` maxDD `-0.271`
- `market_context_high->commodity_4h` score `0.7644` n `112` status `ready` deltaP `13.0009` edge `0.0522` maxDD `-2.0135`
- `market_context_high->crypto_alt_4h` score `0.6638` n `112` status `ready` deltaP `3.027` edge `0.2075` maxDD `-7.1222`
- `market_context_high->equity_24h` score `0.5906` n `81` status `ready` deltaP `9.4329` edge `0.0002` maxDD `-0.4427`
- `news_risk_high->commodity_24h` score `0.4926` n `65` status `ready` deltaP `24.9119` edge `0.1002` maxDD `-10.9169`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
