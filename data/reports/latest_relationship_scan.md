# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-20T08:22:33.357903+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10800`

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

- `market_context_high->equity_4h` score `1.7814` n `96` status `ready` deltaP `9.629` edge `0.1731` maxDD `-2.4411`
- `market_context_high->equity_1h` score `1.2093` n `100` status `ready` deltaP `11.6108` edge `0.0634` maxDD `-1.2022`
- `market_context_high->index_1h` score `0.5974` n `100` status `ready` deltaP `12.3054` edge `0.0077` maxDD `-0.1961`
- `market_context_high->metal_4h` score `0.3638` n `96` status `ready` deltaP `12.4492` edge `0.0049` maxDD `-1.273`
- `market_context_high->index_4h` score `0.0537` n `96` status `ready` deltaP `7.4949` edge `0.02` maxDD `-0.5728`
- `market_context_high->commodity_24h` score `0.0212` n `96` status `ready` deltaP `5.5556` edge `0.149` maxDD `-4.666`
- `market_context_high->fx_4h` score `-0.0067` n `96` status `ready` deltaP `6.8851` edge `0.0035` maxDD `-0.3539`
- `market_context_high->unknown_1h` score `-0.2051` n `100` status `ready` deltaP `6.6647` edge `-0.0388` maxDD `-0.4843`
- `market_context_high->metal_1h` score `-0.2351` n `100` status `ready` deltaP `2.5509` edge `0.0021` maxDD `-0.4291`
- `market_context_high->fx_1h` score `-0.2422` n `100` status `ready` deltaP `0.2455` edge `0.0032` maxDD `-0.2043`
- `market_context_high->unknown_24h` score `-0.6249` n `96` status `ready` deltaP `17.7083` edge `-0.1195` maxDD `-1.0505`
- `market_context_high->crypto_alt_1h` score `-0.7102` n `100` status `ready` deltaP `0.2575` edge `-0.0126` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-0.7961` n `100` status `ready` deltaP `2.2515` edge `-0.0326` maxDD `-2.7581`
- `market_context_high->commodity_4h` score `-0.8674` n `96` status `ready` deltaP `-3.8363` edge `-0.0006` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.9061` n `100` status `ready` deltaP `-8.0958` edge `-0.0056` maxDD `-1.1941`
- `market_context_high->crypto_alt_4h` score `-2.0972` n `96` status `ready` deltaP `3.9634` edge `-0.0742` maxDD `-5.4926`
- `market_context_high->crypto_major_4h` score `-2.3143` n `96` status `ready` deltaP `6.2754` edge `-0.1326` maxDD `-3.1677`
- `market_context_high->fx_24h` score `-3.3227` n `96` status `ready` deltaP `-17.1875` edge `-0.004` maxDD `-1.9981`
- `market_context_high->index_24h` score `-3.8052` n `96` status `ready` deltaP `-0.8681` edge `-0.0653` maxDD `-18.3411`
- `market_context_high->metal_24h` score `-4.4739` n `96` status `ready` deltaP `-17.1875` edge `-0.1282` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
