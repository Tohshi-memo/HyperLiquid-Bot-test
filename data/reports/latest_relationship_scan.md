# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-18T03:07:27.351603+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4173`

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

- `market_context_high->unknown_24h` score `1489.6734` n `98` status `ready` deltaP `3.4722` edge `124.1163` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `15.3573` n `98` status `ready` deltaP `45.844` edge `1.9903` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `14.189` n `98` status `ready` deltaP `30.8638` edge `1.8257` maxDD `-13.3222`
- `market_context_high->metal_1h` score `-0.4049` n `98` status `ready` deltaP `0.3819` edge `0.0057` maxDD `-2.1461`
- `market_context_high->crypto_alt_4h` score `-0.7753` n `98` status `ready` deltaP `-0.3422` edge `0.1839` maxDD `-17.1476`
- `market_context_high->metal_24h` score `-0.8533` n `98` status `ready` deltaP `15.3557` edge `0.149` maxDD `-15.7982`
- `market_context_high->index_1h` score `-0.9928` n `98` status `ready` deltaP `-4.1214` edge `-0.0011` maxDD `-1.2295`
- `market_context_high->metal_4h` score `-1.0945` n `98` status `ready` deltaP `7.3513` edge `-0.0095` maxDD `-6.1238`
- `market_context_high->crypto_alt_1h` score `-1.1713` n `98` status `ready` deltaP `-1.6589` edge `0.0112` maxDD `-7.6911`
- `market_context_high->fx_1h` score `-1.2933` n `98` status `ready` deltaP `-7.8486` edge `-0.0008` maxDD `-0.3721`
- `market_context_high->crypto_major_4h` score `-1.5191` n `98` status `ready` deltaP `-3.6025` edge `0.1875` maxDD `-22.3259`
- `market_context_high->crypto_major_1h` score `-2.2734` n `98` status `ready` deltaP `-1.9858` edge `0.0105` maxDD `-10.2705`
- `market_context_high->index_4h` score `-2.799` n `98` status `ready` deltaP `-11.1312` edge `-0.0247` maxDD `-4.7471`
- `market_context_high->commodity_1h` score `-2.9786` n `98` status `ready` deltaP `-16.2715` edge `-0.035` maxDD `-3.7125`
- `market_context_high->equity_1h` score `-3.296` n `98` status `ready` deltaP `-0.1894` edge `-0.0548` maxDD `-11.1548`
- `market_context_high->fx_4h` score `-4.6096` n `98` status `ready` deltaP `-25.4542` edge `-0.0102` maxDD `-2.0058`
- `market_context_high->fx_24h` score `-6.7564` n `98` status `ready` deltaP `-18.8138` edge `-0.0067` maxDD `-5.8059`
- `market_context_high->commodity_4h` score `-7.7199` n `98` status `ready` deltaP `-26.6488` edge `-0.1196` maxDD `-14.6855`
- `market_context_high->index_24h` score `-8.4013` n `98` status `ready` deltaP `-9.4778` edge `-0.0947` maxDD `-20.7114`
- `market_context_high->equity_4h` score `-13.4499` n `98` status `ready` deltaP `-18.0874` edge `-0.3148` maxDD `-44.5018`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
