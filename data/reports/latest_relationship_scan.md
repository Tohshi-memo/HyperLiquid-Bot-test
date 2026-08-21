# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-21T01:52:36.033890+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `13819`

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

- `market_context_high->equity_1h` score `0.3964` n `105` status `ready` deltaP `9.0191` edge `0.0544` maxDD `-3.1861`
- `market_context_high->index_1h` score `0.3622` n `105` status `ready` deltaP `10.8569` edge `0.0065` maxDD `-0.5622`
- `market_context_high->equity_4h` score `0.3067` n `105` status `ready` deltaP `5.6548` edge `0.1508` maxDD `-8.3685`
- `market_context_high->fx_4h` score `0.0036` n `105` status `ready` deltaP `6.7232` edge `0.0059` maxDD `-0.3539`
- `market_context_high->commodity_24h` score `-0.1386` n `96` status `ready` deltaP `4.6875` edge `0.1343` maxDD `-4.666`
- `market_context_high->unknown_1h` score `-0.1676` n `105` status `ready` deltaP `8.9778` edge `-0.0511` maxDD `-0.4843`
- `market_context_high->fx_1h` score `-0.192` n `105` status `ready` deltaP `1.075` edge `0.0041` maxDD `-0.2043`
- `market_context_high->metal_4h` score `-0.2336` n `105` status `ready` deltaP `6.5302` edge `-0.0159` maxDD `-1.273`
- `market_context_high->metal_1h` score `-0.276` n `105` status `ready` deltaP `2.639` edge `-0.0019` maxDD `-0.4291`
- `market_context_high->index_4h` score `-0.2823` n `105` status `ready` deltaP `5.5807` edge `0.019` maxDD `-1.7252`
- `market_context_high->crypto_alt_1h` score `-0.5766` n `105` status `ready` deltaP `0.8013` edge `0.0009` maxDD `-2.413`
- `market_context_high->commodity_4h` score `-0.7354` n `105` status `ready` deltaP `-2.3476` edge `0.0064` maxDD `-2.4692`
- `market_context_high->crypto_major_1h` score `-0.7794` n `105` status `ready` deltaP `0.9381` edge `-0.0217` maxDD `-2.7581`
- `market_context_high->commodity_1h` score `-0.8304` n `105` status `ready` deltaP `-7.0758` edge `-0.0027` maxDD `-1.1941`
- `market_context_high->crypto_alt_4h` score `-1.8676` n `105` status `ready` deltaP `3.5192` edge `-0.0521` maxDD `-5.4926`
- `market_context_high->crypto_major_4h` score `-2.2327` n `105` status `ready` deltaP `5.6156` edge `-0.1214` maxDD `-3.1677`
- `market_context_high->index_24h` score `-3.5983` n `96` status `ready` deltaP `1.0416` edge `-0.0515` maxDD `-18.3411`
- `market_context_high->fx_24h` score `-3.8376` n `96` status `ready` deltaP `-20.8333` edge `-0.0226` maxDD `-1.9981`
- `market_context_high->unknown_24h` score `-4.4329` n `96` status `ready` deltaP `13.368` edge `-0.4079` maxDD `-1.0505`
- `market_context_high->metal_24h` score `-4.9416` n `96` status `ready` deltaP `-21.0069` edge `-0.1627` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
