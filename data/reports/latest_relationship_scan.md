# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-21T19:22:25.633282+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `13790`

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

- `market_context_high->unknown_1h` score `1.2408` n `133` status `ready` deltaP `8.3878` edge `0.0702` maxDD `-0.4843`
- `market_context_high->fx_4h` score `0.208` n `133` status `ready` deltaP `10.0392` edge `0.01` maxDD `-0.3539`
- `market_context_high->index_1h` score `0.1818` n `133` status `ready` deltaP `10.7559` edge `0.0047` maxDD `-0.9144`
- `market_context_high->unknown_4h` score `0.007` n `133` status `ready` deltaP `21.0904` edge `-0.0961` maxDD `-0.5133`
- `market_context_high->fx_1h` score `-0.1323` n `133` status `ready` deltaP `2.1791` edge `0.0044` maxDD `-0.2043`
- `market_context_high->equity_1h` score `-0.2209` n `133` status `ready` deltaP `6.5643` edge `0.0349` maxDD `-5.2257`
- `market_context_high->metal_1h` score `-0.3519` n `133` status `ready` deltaP `0.3827` edge `-0.0058` maxDD `-0.6822`
- `market_context_high->metal_4h` score `-0.4867` n `133` status `ready` deltaP `3.27` edge `-0.0226` maxDD `-1.5942`
- `market_context_high->index_4h` score `-0.6124` n `133` status `ready` deltaP `2.3164` edge `0.0096` maxDD `-2.618`
- `market_context_high->crypto_alt_1h` score `-0.6344` n `133` status `ready` deltaP `0.5696` edge `0.0235` maxDD `-2.413`
- `market_context_high->commodity_4h` score `-0.6857` n `133` status `ready` deltaP `-1.466` edge `0.0069` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.6869` n `133` status `ready` deltaP `-4.7206` edge `0.0` maxDD `-1.1941`
- `market_context_high->commodity_24h` score `-0.8897` n `105` status `ready` deltaP `0.9425` edge `0.1029` maxDD `-4.666`
- `market_context_high->crypto_major_1h` score `-1.1781` n `133` status `ready` deltaP `-1.1008` edge `-0.0412` maxDD `-4.1996`
- `market_context_high->crypto_alt_4h` score `-1.47` n `133` status `ready` deltaP `2.9835` edge `-0.0154` maxDD `-5.4926`
- `market_context_high->equity_4h` score `-1.8769` n `133` status `ready` deltaP `-2.5823` edge `0.0571` maxDD `-16.1079`
- `market_context_high->fx_24h` score `-2.626` n `105` status `ready` deltaP `-8.4822` edge `-0.0013` maxDD `-2.2121`
- `market_context_high->crypto_major_4h` score `-4.0487` n `133` status `ready` deltaP `-0.7346` edge `-0.2304` maxDD `-3.1677`
- `market_context_high->index_24h` score `-4.2597` n `105` status `ready` deltaP `-6.4633` edge `-0.0528` maxDD `-18.6848`
- `market_context_high->metal_24h` score `-4.7685` n `105` status `ready` deltaP `-18.4574` edge `-0.1575` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
