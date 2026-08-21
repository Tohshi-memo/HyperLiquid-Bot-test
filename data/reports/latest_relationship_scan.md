# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-21T10:52:27.630813+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `13758`

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

- `market_context_high->equity_1h` score `0.5727` n `112` status `ready` deltaP `10.6822` edge `0.058` maxDD `-3.1861`
- `market_context_high->index_1h` score `0.4197` n `112` status `ready` deltaP `11.6018` edge `0.0064` maxDD `-0.5685`
- `market_context_high->fx_4h` score `0.1151` n `105` status `ready` deltaP `8.5525` edge `0.008` maxDD `-0.3539`
- `market_context_high->equity_4h` score `-0.0009` n `105` status `ready` deltaP `4.4353` edge `0.1333` maxDD `-8.3685`
- `market_context_high->fx_1h` score `-0.0451` n `112` status `ready` deltaP `3.7211` edge `0.0053` maxDD `-0.2043`
- `market_context_high->metal_4h` score `-0.2554` n `105` status `ready` deltaP `6.5302` edge `-0.0187` maxDD `-1.273`
- `market_context_high->index_4h` score `-0.3019` n `105` status `ready` deltaP `5.4283` edge `0.0175` maxDD `-1.7252`
- `market_context_high->metal_1h` score `-0.3659` n `112` status `ready` deltaP `-0.0107` edge `-0.0069` maxDD `-0.5281`
- `market_context_high->commodity_24h` score `-0.4396` n `105` status `ready` deltaP `4.5883` edge `0.1161` maxDD `-4.666`
- `market_context_high->unknown_1h` score `-0.4639` n `112` status `ready` deltaP `9.0248` edge `-0.0761` maxDD `-0.4843`
- `market_context_high->commodity_1h` score `-0.6591` n `112` status `ready` deltaP `-4.4857` edge `0.002` maxDD `-1.1941`
- `market_context_high->commodity_4h` score `-0.7908` n `105` status `ready` deltaP `-3.2622` edge `0.0054` maxDD `-2.4692`
- `market_context_high->crypto_major_1h` score `-1.1392` n `112` status `ready` deltaP `-2.5609` edge `-0.0445` maxDD `-2.7581`
- `market_context_high->crypto_alt_1h` score `-1.3618` n `112` status `ready` deltaP `-2.4326` edge `-0.0171` maxDD `-2.413`
- `market_context_high->fx_24h` score `-3.217` n `105` status `ready` deltaP `-14.3849` edge `-0.0112` maxDD `-2.2121`
- `market_context_high->crypto_alt_4h` score `-3.5154` n `105` status `ready` deltaP `-1.3589` edge `-0.1569` maxDD `-5.4926`
- `market_context_high->crypto_major_4h` score `-3.8511` n `105` status `ready` deltaP `0.2802` edge `-0.2207` maxDD `-3.1677`
- `market_context_high->index_24h` score `-4.0404` n `105` status `ready` deltaP `-3.6855` edge `-0.0432` maxDD `-18.6848`
- `market_context_high->unknown_24h` score `-4.2805` n `105` status `ready` deltaP `10.2034` edge `-0.3741` maxDD `-1.0505`
- `market_context_high->metal_24h` score `-4.3584` n `105` status `ready` deltaP `-16.7212` edge `-0.1165` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
