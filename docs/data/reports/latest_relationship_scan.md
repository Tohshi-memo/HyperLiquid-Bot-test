# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-19T09:22:28.049668+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11762`

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

- `market_context_high->crypto_major_24h` score `2.2229` n `96` status `ready` deltaP `7.6389` edge `0.2551` maxDD `-4.9964`
- `market_context_high->equity_4h` score `1.7605` n `96` status `ready` deltaP `10.2388` edge `0.1673` maxDD `-2.4411`
- `market_context_high->equity_1h` score `1.6402` n `96` status `ready` deltaP `14.1031` edge `0.0728` maxDD `-0.4112`
- `market_context_high->metal_4h` score `1.388` n `96` status `ready` deltaP `19.4613` edge `0.0435` maxDD `-1.273`
- `market_context_high->crypto_major_4h` score `1.1453` n `96` status `ready` deltaP `11.9156` edge `0.1181` maxDD `-3.1677`
- `market_context_high->commodity_24h` score `1.0216` n `96` status `ready` deltaP `13.0208` edge `0.2275` maxDD `-4.666`
- `market_context_high->index_1h` score `0.9126` n `96` status `ready` deltaP `15.7622` edge `0.0097` maxDD `-0.0982`
- `market_context_high->unknown_1h` score `0.218` n `96` status `ready` deltaP `8.3084` edge `-0.0145` maxDD `-0.4843`
- `market_context_high->crypto_alt_4h` score `0.1964` n `96` status `ready` deltaP `9.9085` edge `0.0773` maxDD `-5.4926`
- `market_context_high->metal_1h` score `0.1859` n `96` status `ready` deltaP `6.2687` edge `0.0124` maxDD `-0.4291`
- `market_context_high->index_4h` score `0.0887` n `96` status `ready` deltaP `7.6473` edge `0.0219` maxDD `-0.5728`
- `market_context_high->fx_4h` score `0.0771` n `96` status `ready` deltaP `8.2571` edge `0.0051` maxDD `-0.3539`
- `market_context_high->unknown_24h` score `-0.0517` n `96` status `ready` deltaP `15.7986` edge `-0.059` maxDD `-1.0505`
- `market_context_high->fx_1h` score `-0.344` n `96` status `ready` deltaP `-1.6218` edge `0.0026` maxDD `-0.2043`
- `market_context_high->crypto_major_1h` score `-0.397` n `96` status `ready` deltaP `2.6821` edge `0.0157` maxDD `-2.7581`
- `market_context_high->crypto_alt_1h` score `-0.4688` n `96` status `ready` deltaP `1.4783` edge `0.0102` maxDD `-2.413`
- `market_context_high->commodity_4h` score `-0.5189` n `96` status `ready` deltaP `1.6515` edge `0.0075` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.9009` n `96` status `ready` deltaP `-7.8905` edge `-0.0063` maxDD `-1.1941`
- `market_context_high->metal_24h` score `-2.2004` n `96` status `ready` deltaP `-3.6458` edge `0.073` maxDD `-11.4635`
- `market_context_high->fx_24h` score `-4.1418` n `96` status `ready` deltaP `-24.3055` edge `-0.0248` maxDD `-1.9981`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
