# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-20T01:07:28.922553+00:00`
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

- `market_context_high->equity_4h` score `2.1331` n `96` status `ready` deltaP `11.6107` edge `0.1892` maxDD `-2.4411`
- `market_context_high->equity_1h` score `1.7182` n `96` status `ready` deltaP `14.1031` edge `0.0793` maxDD `-0.4112`
- `market_context_high->index_1h` score `0.9318` n `96` status `ready` deltaP `15.9119` edge `0.0103` maxDD `-0.0982`
- `market_context_high->metal_4h` score `0.3584` n `96` status `ready` deltaP `11.9918` edge `0.0075` maxDD `-1.273`
- `market_context_high->index_4h` score `0.2652` n `96` status `ready` deltaP `9.629` edge `0.0234` maxDD `-0.5728`
- `market_context_high->commodity_24h` score `0.1638` n `96` status `ready` deltaP `6.4236` edge `0.1615` maxDD `-4.666`
- `market_context_high->fx_4h` score `0.0083` n `96` status `ready` deltaP `7.0376` edge `0.0044` maxDD `-0.3539`
- `market_context_high->metal_1h` score `-0.0789` n `96` status `ready` deltaP `4.0232` edge `0.0053` maxDD `-0.4291`
- `market_context_high->unknown_24h` score `-0.1821` n `96` status `ready` deltaP `17.7083` edge `-0.0826` maxDD `-1.0505`
- `market_context_high->unknown_1h` score `-0.2171` n `96` status `ready` deltaP `5.6138` edge `-0.0328` maxDD `-0.4843`
- `market_context_high->fx_1h` score `-0.3557` n `96` status `ready` deltaP `-1.7715` edge `0.0021` maxDD `-0.2043`
- `market_context_high->commodity_4h` score `-0.7168` n `96` status `ready` deltaP `-1.8546` edge `0.0055` maxDD `-2.4692`
- `market_context_high->crypto_alt_1h` score `-0.8454` n `96` status `ready` deltaP `-0.3181` edge `-0.0261` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-0.9327` n `96` status `ready` deltaP `1.3348` edge `-0.044` maxDD `-2.7581`
- `market_context_high->commodity_1h` score `-0.9593` n `96` status `ready` deltaP `-8.9384` edge `-0.0068` maxDD `-1.1941`
- `market_context_high->crypto_alt_4h` score `-2.1316` n `96` status `ready` deltaP `3.3537` edge `-0.073` maxDD `-5.4926`
- `market_context_high->crypto_major_4h` score `-2.4485` n `96` status `ready` deltaP `5.5132` edge `-0.1387` maxDD `-3.1677`
- `market_context_high->fx_24h` score `-3.1224` n `96` status `ready` deltaP `-15.1041` edge `-0.0012` maxDD `-1.9981`
- `market_context_high->metal_24h` score `-3.6084` n `96` status `ready` deltaP `-12.1528` edge `-0.0508` maxDD `-11.4635`
- `market_context_high->index_24h` score `-3.7881` n `96` status `ready` deltaP `-0.8681` edge `-0.0631` maxDD `-18.3411`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
