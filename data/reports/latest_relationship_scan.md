# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-19T06:07:37.737473+00:00`
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

- `market_context_high->crypto_major_24h` score `2.0922` n `96` status `ready` deltaP `6.7708` edge `0.25` maxDD `-4.9964`
- `market_context_high->equity_4h` score `1.7108` n `96` status `ready` deltaP `9.7815` edge `0.1662` maxDD `-2.4411`
- `market_context_high->equity_1h` score `1.6427` n `96` status `ready` deltaP `13.5043` edge `0.077` maxDD `-0.4112`
- `market_context_high->metal_4h` score `1.257` n `96` status `ready` deltaP `18.3943` edge `0.0397` maxDD `-1.273`
- `market_context_high->commodity_24h` score `1.2173` n `96` status `ready` deltaP `15.1042` edge `0.2387` maxDD `-4.666`
- `market_context_high->crypto_major_4h` score `1.0299` n `96` status `ready` deltaP `11.7632` edge `0.1095` maxDD `-3.1677`
- `market_context_high->index_1h` score `0.8995` n `96` status `ready` deltaP `15.4628` edge `0.0106` maxDD `-0.0982`
- `market_context_high->unknown_1h` score `0.2755` n `96` status `ready` deltaP `8.9072` edge `-0.0137` maxDD `-0.4843`
- `market_context_high->crypto_alt_4h` score `0.2546` n `96` status `ready` deltaP `10.3659` edge `0.0791` maxDD `-5.4926`
- `market_context_high->metal_1h` score `0.1775` n `96` status `ready` deltaP `6.2687` edge `0.0117` maxDD `-0.4291`
- `market_context_high->index_4h` score `0.0751` n `96` status `ready` deltaP `7.3424` edge `0.0228` maxDD `-0.5728`
- `market_context_high->fx_4h` score `0.0677` n `96` status `ready` deltaP `8.1046` edge `0.0049` maxDD `-0.3539`
- `market_context_high->fx_1h` score `-0.3198` n `96` status `ready` deltaP `-1.1727` edge `0.0027` maxDD `-0.2043`
- `market_context_high->unknown_24h` score `-0.3204` n `96` status `ready` deltaP `13.7152` edge `-0.0675` maxDD `-1.0505`
- `market_context_high->crypto_alt_1h` score `-0.3691` n `96` status `ready` deltaP `2.8256` edge `0.014` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-0.3939` n `96` status `ready` deltaP `2.6821` edge `0.0161` maxDD `-2.7581`
- `market_context_high->commodity_4h` score `-0.5229` n `96` status `ready` deltaP `1.499` edge `0.008` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.8806` n `96` status `ready` deltaP `-7.5911` edge `-0.0057` maxDD `-1.1941`
- `market_context_high->metal_24h` score `-2.2246` n `96` status `ready` deltaP `-3.6458` edge `0.0699` maxDD `-11.4635`
- `market_context_high->fx_24h` score `-4.2858` n `96` status `ready` deltaP `-25.5208` edge `-0.0287` maxDD `-1.9981`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
