# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-20T01:37:26.233641+00:00`
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

- `market_context_high->equity_4h` score `2.1283` n `96` status `ready` deltaP `11.6107` edge `0.1888` maxDD `-2.4411`
- `market_context_high->equity_1h` score `1.7337` n `96` status `ready` deltaP `14.2528` edge `0.0796` maxDD `-0.4112`
- `market_context_high->index_1h` score `0.9306` n `96` status `ready` deltaP `15.9119` edge `0.0102` maxDD `-0.0982`
- `market_context_high->metal_4h` score `0.356` n `96` status `ready` deltaP `11.9918` edge `0.0073` maxDD `-1.273`
- `market_context_high->index_4h` score `0.2628` n `96` status `ready` deltaP `9.629` edge `0.0232` maxDD `-0.5728`
- `market_context_high->commodity_24h` score `0.1583` n `96` status `ready` deltaP `6.4236` edge `0.1608` maxDD `-4.666`
- `market_context_high->fx_4h` score `0.0059` n `96` status `ready` deltaP `7.0376` edge `0.0041` maxDD `-0.3539`
- `market_context_high->metal_1h` score `-0.0813` n `96` status `ready` deltaP `4.0232` edge `0.0051` maxDD `-0.4291`
- `market_context_high->unknown_24h` score `-0.1977` n `96` status `ready` deltaP `17.7083` edge `-0.0839` maxDD `-1.0505`
- `market_context_high->unknown_1h` score `-0.2088` n `96` status `ready` deltaP `5.7635` edge `-0.0331` maxDD `-0.4843`
- `market_context_high->fx_1h` score `-0.3572` n `96` status `ready` deltaP `-1.7715` edge `0.0019` maxDD `-0.2043`
- `market_context_high->commodity_4h` score `-0.7144` n `96` status `ready` deltaP `-1.8546` edge `0.0058` maxDD `-2.4692`
- `market_context_high->crypto_alt_1h` score `-0.8415` n `96` status `ready` deltaP `-0.3181` edge `-0.0256` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-0.9233` n `96` status `ready` deltaP `1.3348` edge `-0.0428` maxDD `-2.7581`
- `market_context_high->commodity_1h` score `-0.9678` n `96` status `ready` deltaP `-9.0881` edge `-0.0069` maxDD `-1.1941`
- `market_context_high->crypto_alt_4h` score `-2.0868` n `96` status `ready` deltaP `3.6585` edge `-0.0713` maxDD `-5.4926`
- `market_context_high->crypto_major_4h` score `-2.3653` n `96` status `ready` deltaP `5.8181` edge `-0.1338` maxDD `-3.1677`
- `market_context_high->fx_24h` score `-3.0899` n `96` status `ready` deltaP `-14.7569` edge `-0.0008` maxDD `-1.9981`
- `market_context_high->metal_24h` score `-3.6764` n `96` status `ready` deltaP `-12.5` edge `-0.0572` maxDD `-11.4635`
- `market_context_high->index_24h` score `-3.7865` n `96` status `ready` deltaP `-0.8681` edge `-0.0629` maxDD `-18.3411`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
