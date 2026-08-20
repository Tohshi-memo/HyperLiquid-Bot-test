# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-20T01:22:25.191458+00:00`
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

- `market_context_high->equity_4h` score `2.1295` n `96` status `ready` deltaP `11.6107` edge `0.1889` maxDD `-2.4411`
- `market_context_high->equity_1h` score `1.717` n `96` status `ready` deltaP `14.1031` edge `0.0792` maxDD `-0.4112`
- `market_context_high->index_1h` score `0.9306` n `96` status `ready` deltaP `15.9119` edge `0.0102` maxDD `-0.0982`
- `market_context_high->metal_4h` score `0.3572` n `96` status `ready` deltaP `11.9918` edge `0.0074` maxDD `-1.273`
- `market_context_high->index_4h` score `0.264` n `96` status `ready` deltaP `9.629` edge `0.0233` maxDD `-0.5728`
- `market_context_high->commodity_24h` score `0.1607` n `96` status `ready` deltaP `6.4236` edge `0.1611` maxDD `-4.666`
- `market_context_high->fx_4h` score `0.0075` n `96` status `ready` deltaP `7.0376` edge `0.0043` maxDD `-0.3539`
- `market_context_high->metal_1h` score `-0.0801` n `96` status `ready` deltaP `4.0232` edge `0.0052` maxDD `-0.4291`
- `market_context_high->unknown_24h` score `-0.1881` n `96` status `ready` deltaP `17.7083` edge `-0.0831` maxDD `-1.0505`
- `market_context_high->unknown_1h` score `-0.204` n `96` status `ready` deltaP `5.7635` edge `-0.0327` maxDD `-0.4843`
- `market_context_high->fx_1h` score `-0.3564` n `96` status `ready` deltaP `-1.7715` edge `0.002` maxDD `-0.2043`
- `market_context_high->commodity_4h` score `-0.716` n `96` status `ready` deltaP `-1.8546` edge `0.0056` maxDD `-2.4692`
- `market_context_high->crypto_alt_1h` score `-0.8438` n `96` status `ready` deltaP `-0.3181` edge `-0.0259` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-0.9288` n `96` status `ready` deltaP `1.3348` edge `-0.0435` maxDD `-2.7581`
- `market_context_high->commodity_1h` score `-0.9678` n `96` status `ready` deltaP `-9.0881` edge `-0.0069` maxDD `-1.1941`
- `market_context_high->crypto_alt_4h` score `-2.1098` n `96` status `ready` deltaP `3.5061` edge `-0.0722` maxDD `-5.4926`
- `market_context_high->crypto_major_4h` score `-2.4099` n `96` status `ready` deltaP `5.6656` edge `-0.1365` maxDD `-3.1677`
- `market_context_high->fx_24h` score `-3.1062` n `96` status `ready` deltaP `-14.9305` edge `-0.001` maxDD `-1.9981`
- `market_context_high->metal_24h` score `-3.6431` n `96` status `ready` deltaP `-12.3264` edge `-0.0541` maxDD `-11.4635`
- `market_context_high->index_24h` score `-3.7865` n `96` status `ready` deltaP `-0.8681` edge `-0.0629` maxDD `-18.3411`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
