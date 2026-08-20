# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-20T08:52:27.789864+00:00`
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

- `market_context_high->equity_4h` score `1.8212` n `96` status `ready` deltaP `9.7815` edge `0.1754` maxDD `-2.4411`
- `market_context_high->equity_1h` score `0.7446` n `102` status `ready` deltaP `10.2971` edge `0.0524` maxDD `-2.3866`
- `market_context_high->index_1h` score `0.4383` n `102` status `ready` deltaP `11.0309` edge `0.0057` maxDD `-0.4174`
- `market_context_high->metal_4h` score `0.3978` n `96` status `ready` deltaP `12.754` edge `0.0057` maxDD `-1.273`
- `market_context_high->index_4h` score `0.0829` n `96` status `ready` deltaP `7.7998` edge `0.0204` maxDD `-0.5728`
- `market_context_high->commodity_24h` score `0.0149` n `96` status `ready` deltaP `5.5556` edge `0.1482` maxDD `-4.666`
- `market_context_high->fx_4h` score `-0.0233` n `96` status `ready` deltaP `6.5803` edge `0.0034` maxDD `-0.3539`
- `market_context_high->metal_1h` score `-0.1542` n `102` status `ready` deltaP `3.4725` edge `0.0027` maxDD `-0.4291`
- `market_context_high->fx_1h` score `-0.2008` n `102` status `ready` deltaP `0.9657` edge `0.0037` maxDD `-0.2043`
- `market_context_high->unknown_1h` score `-0.2206` n `102` status `ready` deltaP `7.3706` edge `-0.0448` maxDD `-0.4843`
- `market_context_high->crypto_alt_1h` score `-0.5096` n `102` status `ready` deltaP `1.0098` edge `0.0081` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-0.5578` n `102` status `ready` deltaP `2.8737` edge `-0.0062` maxDD `-2.7581`
- `market_context_high->unknown_24h` score `-0.6681` n `96` status `ready` deltaP `17.7083` edge `-0.1231` maxDD `-1.0505`
- `market_context_high->commodity_1h` score `-0.849` n `102` status `ready` deltaP `-7.2972` edge `-0.0036` maxDD `-1.1941`
- `market_context_high->commodity_4h` score `-0.8934` n `96` status `ready` deltaP `-4.1412` edge `-0.0019` maxDD `-2.4692`
- `market_context_high->crypto_alt_4h` score `-2.1754` n `96` status `ready` deltaP `3.811` edge `-0.0797` maxDD `-5.4926`
- `market_context_high->crypto_major_4h` score `-2.4455` n `96` status `ready` deltaP `5.9705` edge `-0.1415` maxDD `-3.1677`
- `market_context_high->fx_24h` score `-3.3589` n `96` status `ready` deltaP `-17.5347` edge `-0.0047` maxDD `-1.9981`
- `market_context_high->index_24h` score `-3.7778` n `96` status `ready` deltaP `-0.5209` edge `-0.0641` maxDD `-18.3411`
- `market_context_high->metal_24h` score `-4.5193` n `96` status `ready` deltaP `-17.5347` edge `-0.1317` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
