# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-19T18:52:27.122049+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9828`

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

- `market_context_high->equity_4h` score `2.3049` n `96` status `ready` deltaP `11.7632` edge `0.2025` maxDD `-2.4411`
- `market_context_high->equity_1h` score `1.9639` n `96` status `ready` deltaP `15.8995` edge `0.0878` maxDD `-0.4112`
- `market_context_high->index_1h` score `1.0013` n `96` status `ready` deltaP `16.6604` edge `0.0111` maxDD `-0.0982`
- `market_context_high->metal_4h` score `0.6155` n `96` status `ready` deltaP `14.126` edge `0.0147` maxDD `-1.273`
- `market_context_high->commodity_24h` score `0.3062` n `96` status `ready` deltaP `6.5972` edge `0.1786` maxDD `-4.666`
- `market_context_high->unknown_24h` score `0.2657` n `96` status `ready` deltaP `18.0555` edge `-0.0476` maxDD `-1.0505`
- `market_context_high->index_4h` score `0.2212` n `96` status `ready` deltaP `9.0193` edge `0.0238` maxDD `-0.5728`
- `market_context_high->unknown_1h` score `0.0646` n `96` status `ready` deltaP `7.2605` edge `-0.0203` maxDD `-0.4843`
- `market_context_high->fx_4h` score `0.0454` n `96` status `ready` deltaP `7.6473` edge `0.0051` maxDD `-0.3539`
- `market_context_high->metal_1h` score `-0.0202` n `96` status `ready` deltaP `4.622` edge `0.0062` maxDD `-0.4291`
- `market_context_high->crypto_major_24h` score `-0.0811` n `96` status `ready` deltaP `3.125` edge `0.0932` maxDD `-4.9964`
- `market_context_high->fx_1h` score `-0.3276` n `96` status `ready` deltaP `-1.3224` edge `0.0027` maxDD `-0.2043`
- `market_context_high->crypto_major_1h` score `-0.6629` n `96` status `ready` deltaP `2.0833` edge `-0.0144` maxDD `-2.7581`
- `market_context_high->crypto_alt_1h` score `-0.6637` n `96` status `ready` deltaP `0.4304` edge `-0.0078` maxDD `-2.413`
- `market_context_high->commodity_4h` score `-0.6926` n `96` status `ready` deltaP `-0.94` edge `0.0025` maxDD `-2.4692`
- `market_context_high->crypto_major_4h` score `-0.8324` n `96` status `ready` deltaP `7.19` edge `-0.0152` maxDD `-3.1677`
- `market_context_high->commodity_1h` score `-0.8658` n `96` status `ready` deltaP `-7.2917` edge `-0.0058` maxDD `-1.1941`
- `market_context_high->crypto_alt_4h` score `-1.2583` n `96` status `ready` deltaP `5.0305` edge `-0.0114` maxDD `-5.4926`
- `market_context_high->metal_24h` score `-2.8109` n `96` status `ready` deltaP `-7.8125` edge `0.0225` maxDD `-11.4635`
- `market_context_high->fx_24h` score `-3.5813` n `96` status `ready` deltaP `-19.4444` edge `-0.0105` maxDD `-1.9981`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
