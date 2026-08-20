# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-20T00:52:35.626475+00:00`
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

- `market_context_high->equity_4h` score `2.1403` n `96` status `ready` deltaP `11.6107` edge `0.1898` maxDD `-2.4411`
- `market_context_high->equity_1h` score `1.729` n `96` status `ready` deltaP `14.1031` edge `0.0802` maxDD `-0.4112`
- `market_context_high->index_1h` score `0.9354` n `96` status `ready` deltaP `15.9119` edge `0.0106` maxDD `-0.0982`
- `market_context_high->metal_4h` score `0.3608` n `96` status `ready` deltaP `11.9918` edge `0.0077` maxDD `-1.273`
- `market_context_high->index_4h` score `0.2676` n `96` status `ready` deltaP `9.629` edge `0.0236` maxDD `-0.5728`
- `market_context_high->commodity_24h` score `0.1677` n `96` status `ready` deltaP `6.4236` edge `0.162` maxDD `-4.666`
- `market_context_high->fx_4h` score `0.009` n `96` status `ready` deltaP `7.0376` edge `0.0045` maxDD `-0.3539`
- `market_context_high->metal_1h` score `-0.0801` n `96` status `ready` deltaP `4.0232` edge `0.0052` maxDD `-0.4291`
- `market_context_high->unknown_1h` score `-0.204` n `96` status `ready` deltaP `5.7635` edge `-0.0327` maxDD `-0.4843`
- `market_context_high->unknown_24h` score `-0.3129` n `96` status `ready` deltaP `17.7083` edge `-0.0935` maxDD `-1.0505`
- `market_context_high->fx_1h` score `-0.3549` n `96` status `ready` deltaP `-1.7715` edge `0.0022` maxDD `-0.2043`
- `market_context_high->commodity_4h` score `-0.7176` n `96` status `ready` deltaP `-1.8546` edge `0.0054` maxDD `-2.4692`
- `market_context_high->crypto_alt_1h` score `-0.8446` n `96` status `ready` deltaP `-0.3181` edge `-0.026` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-0.9428` n `96` status `ready` deltaP `1.1851` edge `-0.0443` maxDD `-2.7581`
- `market_context_high->commodity_1h` score `-0.9507` n `96` status `ready` deltaP `-8.7887` edge `-0.0067` maxDD `-1.1941`
- `market_context_high->crypto_alt_4h` score `-2.157` n `96` status `ready` deltaP `3.2012` edge `-0.0741` maxDD `-5.4926`
- `market_context_high->crypto_major_4h` score `-2.4799` n `96` status `ready` deltaP `5.3607` edge `-0.1403` maxDD `-3.1677`
- `market_context_high->fx_24h` score `-3.1387` n `96` status `ready` deltaP `-15.2777` edge `-0.0014` maxDD `-1.9981`
- `market_context_high->metal_24h` score `-3.5752` n `96` status `ready` deltaP `-11.9792` edge `-0.0477` maxDD `-11.4635`
- `market_context_high->index_24h` score `-3.7896` n `96` status `ready` deltaP `-0.8681` edge `-0.0633` maxDD `-18.3411`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
