# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-20T02:37:25.093250+00:00`
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

- `market_context_high->equity_4h` score `2.1077` n `96` status `ready` deltaP `11.4583` edge `0.1881` maxDD `-2.4411`
- `market_context_high->equity_1h` score `1.7829` n `96` status `ready` deltaP `14.7019` edge `0.0807` maxDD `-0.4112`
- `market_context_high->index_1h` score `0.9294` n `96` status `ready` deltaP `15.9119` edge `0.0101` maxDD `-0.0982`
- `market_context_high->metal_4h` score `0.3584` n `96` status `ready` deltaP `11.9918` edge `0.0075` maxDD `-1.273`
- `market_context_high->index_4h` score `0.2422` n `96` status `ready` deltaP `9.4766` edge `0.0225` maxDD `-0.5728`
- `market_context_high->commodity_24h` score `0.1466` n `96` status `ready` deltaP `6.4236` edge `0.1593` maxDD `-4.666`
- `market_context_high->fx_4h` score `0.0012` n `96` status `ready` deltaP `7.0376` edge `0.0035` maxDD `-0.3539`
- `market_context_high->metal_1h` score `-0.1077` n `96` status `ready` deltaP `3.7238` edge `0.0049` maxDD `-0.4291`
- `market_context_high->unknown_1h` score `-0.2123` n `96` status `ready` deltaP `5.6138` edge `-0.0324` maxDD `-0.4843`
- `market_context_high->unknown_24h` score `-0.2313` n `96` status `ready` deltaP `17.7083` edge `-0.0867` maxDD `-1.0505`
- `market_context_high->fx_1h` score `-0.3494` n `96` status `ready` deltaP `-1.6218` edge `0.0019` maxDD `-0.2043`
- `market_context_high->commodity_4h` score `-0.7105` n `96` status `ready` deltaP `-1.8546` edge `0.0063` maxDD `-2.4692`
- `market_context_high->crypto_alt_1h` score `-0.8547` n `96` status `ready` deltaP `-0.4678` edge `-0.0263` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-0.9265` n `96` status `ready` deltaP `1.3348` edge `-0.0432` maxDD `-2.7581`
- `market_context_high->commodity_1h` score `-0.9756` n `96` status `ready` deltaP `-9.2378` edge `-0.0069` maxDD `-1.1941`
- `market_context_high->crypto_alt_4h` score `-2.047` n `96` status `ready` deltaP `3.811` edge `-0.069` maxDD `-5.4926`
- `market_context_high->crypto_major_4h` score `-2.2025` n `96` status `ready` deltaP `6.4278` edge `-0.1243` maxDD `-3.1677`
- `market_context_high->fx_24h` score `-3.0597` n `96` status `ready` deltaP `-14.4097` edge `-0.0006` maxDD `-1.9981`
- `market_context_high->index_24h` score `-3.7896` n `96` status `ready` deltaP `-0.8681` edge `-0.0633` maxDD `-18.3411`
- `market_context_high->metal_24h` score `-3.8045` n `96` status `ready` deltaP `-13.1944` edge `-0.069` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
