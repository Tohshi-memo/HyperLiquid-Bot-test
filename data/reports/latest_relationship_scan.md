# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-21T16:07:31.813337+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `13774`

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

- `market_context_high->index_1h` score `0.1231` n `132` status `ready` deltaP `9.7169` edge `0.0041` maxDD `-0.9144`
- `market_context_high->fx_4h` score `0.058` n `121` status `ready` deltaP `7.2894` edge `0.0091` maxDD `-0.3539`
- `market_context_high->fx_1h` score `-0.096` n `132` status `ready` deltaP `2.8625` edge `0.0045` maxDD `-0.2043`
- `market_context_high->equity_1h` score `-0.2532` n `132` status `ready` deltaP `6.1241` edge `0.0337` maxDD `-5.2257`
- `market_context_high->metal_1h` score `-0.3405` n `132` status `ready` deltaP `0.617` edge `-0.0059` maxDD `-0.6822`
- `market_context_high->unknown_1h` score `-0.4756` n `132` status `ready` deltaP `7.8434` edge `-0.0692` maxDD `-0.4843`
- `market_context_high->crypto_alt_1h` score `-0.6015` n `132` status `ready` deltaP `0.8756` edge `0.0242` maxDD `-2.413`
- `market_context_high->metal_4h` score `-0.6148` n `121` status `ready` deltaP `1.3606` edge `-0.0263` maxDD `-1.5942`
- `market_context_high->commodity_24h` score `-0.6167` n `105` status `ready` deltaP `3.1994` edge `0.1106` maxDD `-4.666`
- `market_context_high->index_4h` score `-0.6532` n `121` status `ready` deltaP `1.0633` edge `0.0092` maxDD `-2.336`
- `market_context_high->commodity_1h` score `-0.6552` n `132` status `ready` deltaP `-4.2007` edge `0.0006` maxDD `-1.1941`
- `market_context_high->commodity_4h` score `-0.685` n `121` status `ready` deltaP `-1.6479` edge `0.0082` maxDD `-2.4692`
- `market_context_high->crypto_major_1h` score `-1.1338` n `132` status `ready` deltaP `-0.8347` edge `-0.0373` maxDD `-4.1996`
- `market_context_high->equity_4h` score `-1.2396` n `121` status `ready` deltaP `-0.9903` edge `0.0707` maxDD `-13.175`
- `market_context_high->crypto_alt_4h` score `-1.5059` n `121` status `ready` deltaP `2.565` edge `-0.0156` maxDD `-5.4926`
- `market_context_high->unknown_4h` score `-1.7923` n `121` status `ready` deltaP `20.5138` edge `-0.2422` maxDD `-0.5133`
- `market_context_high->fx_24h` score `-2.8389` n `105` status `ready` deltaP `-10.7391` edge `-0.004` maxDD `-2.2121`
- `market_context_high->crypto_major_4h` score `-3.9869` n `121` status `ready` deltaP `-0.1713` edge `-0.229` maxDD `-3.1677`
- `market_context_high->index_24h` score `-4.2464` n `105` status `ready` deltaP `-6.4633` edge `-0.0511` maxDD `-18.6848`
- `market_context_high->metal_24h` score `-4.6051` n `105` status `ready` deltaP `-17.4157` edge `-0.1435` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
