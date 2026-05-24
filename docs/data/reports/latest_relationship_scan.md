# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-24T00:37:21.031951+00:00`
- Price records: `672`
- Market context records: `1684`
- Flow alert records: `6754`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8854`

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

- `market_context_high->metal_24h` score `8.1159` n `151` status `ready` deltaP `26.9587` edge `0.7392` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `5.3141` n `194` status `ready` deltaP `23.1236` edge `0.5551` maxDD `-16.3135`
- `market_context_high->index_24h` score `3.8886` n `151` status `ready` deltaP `18.3975` edge `0.3392` maxDD `-5.3574`
- `market_context_high->crypto_major_4h` score `3.5849` n `194` status `ready` deltaP `20.2996` edge `0.4343` maxDD `-13.3376`
- `market_context_high->unknown_24h` score `2.9524` n `151` status `ready` deltaP `15.0267` edge `0.6779` maxDD `-35.8966`
- `market_context_high->equity_4h` score `2.8695` n `194` status `ready` deltaP `15.596` edge `0.2446` maxDD `-5.0894`
- `market_context_high->equity_24h` score `1.9018` n `151` status `ready` deltaP `17.4786` edge `0.5318` maxDD `-33.1875`
- `market_context_high->crypto_alt_1h` score `0.49` n `204` status `ready` deltaP `5.3393` edge `0.1076` maxDD `-4.1892`
- `market_context_high->crypto_alt_24h` score `0.3887` n `151` status `ready` deltaP `24.9903` edge `1.0467` maxDD `-88.8062`
- `market_context_high->index_4h` score `0.146` n `194` status `ready` deltaP `5.8602` edge `0.082` maxDD `-3.7119`
- `market_context_high->equity_1h` score `-0.0985` n `204` status `ready` deltaP `3.6809` edge `0.0481` maxDD `-2.8014`
- `market_context_high->crypto_major_24h` score `-0.1457` n `151` status `ready` deltaP `23.7013` edge `0.6819` maxDD `-62.3533`
- `market_context_high->crypto_major_1h` score `-0.3982` n `204` status `ready` deltaP `3.2553` edge `0.0725` maxDD `-5.5244`
- `market_context_high->index_1h` score `-0.5219` n `204` status `ready` deltaP `0.6722` edge `0.0152` maxDD `-1.7205`
- `market_context_high->metal_1h` score `-0.5449` n `204` status `ready` deltaP `7.0682` edge `0.0166` maxDD `-6.3532`
- `market_context_high->metal_4h` score `-0.6028` n `194` status `ready` deltaP `12.4434` edge `0.136` maxDD `-12.5349`
- `market_context_high->fx_24h` score `-0.6359` n `151` status `ready` deltaP `5.7323` edge `0.0137` maxDD `-1.3925`
- `market_context_high->fx_1h` score `-0.9411` n `204` status `ready` deltaP `-1.905` edge `-0.0025` maxDD `-0.3914`
- `market_context_high->fx_4h` score `-1.1979` n `194` status `ready` deltaP `-7.5135` edge `-0.0106` maxDD `-1.4313`
- `market_context_high->commodity_1h` score `-2.1329` n `204` status `ready` deltaP `0.4638` edge `-0.0311` maxDD `-14.9691`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
