# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-27T00:37:27.359125+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7987`

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

- `market_context_high->unknown_4h` score `89.9235` n `153` status `ready` deltaP `1.0172` edge `7.5204` maxDD `-1.0178`
- `market_context_high->unknown_1h` score `20.8764` n `153` status `ready` deltaP `1.6242` edge `1.7778` maxDD `-1.5807`
- `market_context_high->fx_1h` score `0.265` n `153` status `ready` deltaP `8.2648` edge `0.0028` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.231` n `153` status `ready` deltaP `10.5442` edge `0.0088` maxDD `-0.4545`
- `market_context_high->metal_24h` score `0.2013` n `112` status `ready` deltaP `23.2421` edge `0.1335` maxDD `-7.0108`
- `market_context_high->index_24h` score `-0.0871` n `112` status `ready` deltaP `15.6119` edge `0.0086` maxDD `-4.5747`
- `market_context_high->fx_24h` score `-0.1191` n `112` status `ready` deltaP `17.3186` edge `0.0265` maxDD `-1.2451`
- `market_context_high->metal_1h` score `-0.126` n `153` status `ready` deltaP `8.4801` edge `0.0065` maxDD `-1.6682`
- `market_context_high->commodity_1h` score `-0.2115` n `153` status `ready` deltaP `2.6017` edge `0.0151` maxDD `-1.0053`
- `market_context_high->commodity_4h` score `-0.3413` n `153` status `ready` deltaP `6.6684` edge `0.05` maxDD `-1.165`
- `market_context_high->index_1h` score `-0.6203` n `153` status `ready` deltaP `-0.5861` edge `-0.0019` maxDD `-1.8971`
- `market_context_high->crypto_major_1h` score `-0.8561` n `153` status `ready` deltaP `4.8325` edge `0.0161` maxDD `-9.3126`
- `market_context_high->metal_4h` score `-0.9305` n `153` status `ready` deltaP `7.8172` edge `-0.0004` maxDD `-5.3474`
- `market_context_high->equity_1h` score `-1.8595` n `153` status `ready` deltaP `0.7064` edge `-0.0155` maxDD `-12.2088`
- `market_context_high->crypto_alt_1h` score `-1.9936` n `153` status `ready` deltaP `-0.4256` edge `-0.0043` maxDD `-13.2099`
- `market_context_high->index_4h` score `-3.3885` n `153` status `ready` deltaP `-6.0796` edge `-0.0242` maxDD `-6.7447`
- `market_context_high->crypto_major_4h` score `-4.5708` n `153` status `ready` deltaP `-0.1535` edge `-0.081` maxDD `-32.9851`
- `market_context_high->crypto_major_24h` score `-4.6624` n `112` status `ready` deltaP `-3.4847` edge `-0.0888` maxDD `-29.1905`
- `market_context_high->commodity_24h` score `-5.9264` n `112` status `ready` deltaP `-12.7444` edge `-0.1159` maxDD `-24.0477`
- `market_context_high->equity_4h` score `-6.9775` n `153` status `ready` deltaP `-0.8738` edge `-0.1663` maxDD `-45.4611`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
