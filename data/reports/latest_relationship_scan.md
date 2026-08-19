# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-19T14:07:44.423730+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11750`

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

- `market_context_high->equity_4h` score `2.1365` n `96` status `ready` deltaP `11.4583` edge `0.1905` maxDD `-2.4411`
- `market_context_high->equity_1h` score `1.8332` n `96` status `ready` deltaP `15.0013` edge `0.0829` maxDD `-0.4112`
- `market_context_high->crypto_major_24h` score `1.5715` n `96` status `ready` deltaP `4.6875` edge `0.2205` maxDD `-4.9964`
- `market_context_high->metal_4h` score `1.062` n `96` status `ready` deltaP `17.0223` edge `0.0326` maxDD `-1.273`
- `market_context_high->index_1h` score `0.9702` n `96` status `ready` deltaP `16.361` edge `0.0105` maxDD `-0.0982`
- `market_context_high->commodity_24h` score `0.652` n `96` status `ready` deltaP `9.7222` edge `0.2021` maxDD `-4.666`
- `market_context_high->crypto_major_4h` score `0.6188` n `96` status `ready` deltaP `9.3242` edge `0.0915` maxDD `-3.1677`
- `market_context_high->unknown_24h` score `0.3384` n `96` status `ready` deltaP `18.2291` edge `-0.0427` maxDD `-1.0505`
- `market_context_high->unknown_1h` score `0.1713` n `96` status `ready` deltaP `8.009` edge `-0.0164` maxDD `-0.4843`
- `market_context_high->fx_4h` score `0.1507` n `96` status `ready` deltaP `9.4766` edge `0.0064` maxDD `-0.3539`
- `market_context_high->index_4h` score `0.1324` n `96` status `ready` deltaP `8.1046` edge `0.0225` maxDD `-0.5728`
- `market_context_high->metal_1h` score `0.0817` n `96` status `ready` deltaP `5.5202` edge `0.0087` maxDD `-0.4291`
- `market_context_high->crypto_alt_4h` score `-0.2049` n `96` status `ready` deltaP `7.622` edge `0.0591` maxDD `-5.4926`
- `market_context_high->fx_1h` score `-0.3191` n `96` status `ready` deltaP `-1.1727` edge `0.0028` maxDD `-0.2043`
- `market_context_high->crypto_major_1h` score `-0.4555` n `96` status `ready` deltaP `2.5324` edge `0.0092` maxDD `-2.7581`
- `market_context_high->crypto_alt_1h` score `-0.4977` n `96` status `ready` deltaP `1.3286` edge `0.0075` maxDD `-2.413`
- `market_context_high->commodity_4h` score `-0.6128` n `96` status `ready` deltaP `0.2795` edge `0.0046` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.8978` n `96` status `ready` deltaP `-7.7408` edge `-0.0069` maxDD `-1.1941`
- `market_context_high->metal_24h` score `-2.322` n `96` status `ready` deltaP `-4.5139` edge `0.0632` maxDD `-11.4635`
- `market_context_high->fx_24h` score `-3.797` n `96` status `ready` deltaP `-21.1805` edge `-0.0169` maxDD `-1.9981`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
