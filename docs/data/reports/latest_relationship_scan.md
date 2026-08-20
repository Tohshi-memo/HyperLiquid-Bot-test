# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-20T04:07:26.269206+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10829`

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

- `market_context_high->equity_4h` score `1.9939` n `96` status `ready` deltaP `10.6961` edge `0.1837` maxDD `-2.4411`
- `market_context_high->equity_1h` score `1.8116` n `96` status `ready` deltaP `15.0013` edge `0.0811` maxDD `-0.4112`
- `market_context_high->index_1h` score `0.9438` n `96` status `ready` deltaP `16.0616` edge `0.0103` maxDD `-0.0982`
- `market_context_high->metal_4h` score `0.3476` n `96` status `ready` deltaP `11.9918` edge `0.0066` maxDD `-1.273`
- `market_context_high->index_4h` score `0.1546` n `96` status `ready` deltaP `8.562` edge `0.0213` maxDD `-0.5728`
- `market_context_high->commodity_24h` score `0.1287` n `96` status `ready` deltaP `6.4236` edge `0.157` maxDD `-4.666`
- `market_context_high->fx_4h` score `-0.0019` n `96` status `ready` deltaP `7.0376` edge `0.0031` maxDD `-0.3539`
- `market_context_high->unknown_1h` score `-0.138` n `96` status `ready` deltaP `5.9132` edge `-0.0282` maxDD `-0.4843`
- `market_context_high->metal_1h` score `-0.164` n `96` status `ready` deltaP `3.125` edge `0.0042` maxDD `-0.4291`
- `market_context_high->unknown_24h` score `-0.3009` n `96` status `ready` deltaP `17.7083` edge `-0.0925` maxDD `-1.0505`
- `market_context_high->fx_1h` score `-0.3494` n `96` status `ready` deltaP `-1.6218` edge `0.0019` maxDD `-0.2043`
- `market_context_high->commodity_4h` score `-0.7138` n `96` status `ready` deltaP `-2.0071` edge `0.0069` maxDD `-2.4692`
- `market_context_high->crypto_alt_1h` score `-0.7807` n `96` status `ready` deltaP `0.2807` edge `-0.0218` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-0.8548` n `96` status `ready` deltaP `1.9336` edge `-0.038` maxDD `-2.7581`
- `market_context_high->commodity_1h` score `-0.939` n `96` status `ready` deltaP `-8.639` edge `-0.0062` maxDD `-1.1941`
- `market_context_high->crypto_alt_4h` score `-1.9854` n `96` status `ready` deltaP `4.1159` edge `-0.0659` maxDD `-5.4926`
- `market_context_high->crypto_major_4h` score `-2.019` n `96` status `ready` deltaP `7.3424` edge `-0.1151` maxDD `-3.1677`
- `market_context_high->fx_24h` score `-3.1375` n `96` status `ready` deltaP `-15.2777` edge `-0.0013` maxDD `-1.9981`
- `market_context_high->index_24h` score `-3.7959` n `96` status `ready` deltaP `-0.8681` edge `-0.0641` maxDD `-18.3411`
- `market_context_high->metal_24h` score `-3.9897` n `96` status `ready` deltaP `-14.2361` edge `-0.0858` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
