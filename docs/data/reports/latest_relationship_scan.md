# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-29T23:37:28.545006+00:00`
- Price records: `672`
- Market context records: `5194`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5644`

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

- `market_context_high->unknown_24h` score `19.5633` n `89` status `ready` deltaP `33.3528` edge `1.4269` maxDD `-0.8515`
- `market_context_high->crypto_major_24h` score `14.0842` n `89` status `ready` deltaP `28.1172` edge `1.3524` maxDD `-22.6266`
- `market_context_high->crypto_alt_24h` score `10.7652` n `89` status `ready` deltaP `28.7102` edge `1.0444` maxDD `-23.4292`
- `market_context_high->unknown_4h` score `5.4731` n `155` status `ready` deltaP `19.7266` edge `0.4268` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `4.4535` n `155` status `ready` deltaP `13.2367` edge `0.4428` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `4.3476` n `155` status `ready` deltaP `13.6123` edge `0.5008` maxDD `-14.0065`
- `market_context_high->unknown_1h` score `2.594` n `155` status `ready` deltaP `9.2872` edge `0.2184` maxDD `-2.7986`
- `market_context_high->equity_4h` score `0.9872` n `155` status `ready` deltaP `8.4647` edge `0.1897` maxDD `-7.4425`
- `market_context_high->crypto_alt_1h` score `0.5432` n `155` status `ready` deltaP `4.5036` edge `0.1114` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `0.5165` n `155` status `ready` deltaP `6.4033` edge `0.1249` maxDD `-6.9639`
- `market_context_high->fx_24h` score `0.3368` n `89` status `ready` deltaP `12.2698` edge `0.0358` maxDD `-0.8294`
- `market_context_high->equity_1h` score `0.1866` n `155` status `ready` deltaP `7.1663` edge `0.0643` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.0337` n `155` status `ready` deltaP `5.1845` edge `0.013` maxDD `-1.0296`
- `market_context_high->metal_1h` score `-0.0927` n `155` status `ready` deltaP `4.5605` edge `0.0169` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.2487` n `155` status `ready` deltaP `1.9587` edge `0.0003` maxDD `-0.6194`
- `market_context_high->index_4h` score `-0.5014` n `155` status `ready` deltaP `5.7533` edge `0.0316` maxDD `-2.9391`
- `market_context_high->fx_4h` score `-0.5092` n `155` status `ready` deltaP `4.7108` edge `0.0067` maxDD `-1.6047`
- `market_context_high->commodity_1h` score `-0.5876` n `155` status `ready` deltaP `0.875` edge `-0.0003` maxDD `-2.4692`
- `market_context_high->index_24h` score `-0.9355` n `89` status `ready` deltaP `9.0395` edge `-0.0167` maxDD `-7.413`
- `market_context_high->metal_4h` score `-1.3175` n `155` status `ready` deltaP `0.0501` edge `0.0311` maxDD `-9.3609`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
