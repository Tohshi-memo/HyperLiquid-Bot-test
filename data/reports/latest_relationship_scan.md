# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-18T19:36:15.036163+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11624`

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

- `market_context_high->crypto_major_24h` score `2.7213` n `91` status `ready` deltaP `10.0294` edge `0.2807` maxDD `-4.9964`
- `market_context_high->commodity_24h` score `1.6682` n `91` status `ready` deltaP `19.2899` edge `0.2686` maxDD `-4.666`
- `market_context_high->equity_1h` score `1.2532` n `96` status `ready` deltaP `10.3606` edge `0.0655` maxDD `-0.4112`
- `market_context_high->equity_4h` score `0.8581` n `96` status `ready` deltaP `5.5132` edge `0.1236` maxDD `-2.4411`
- `market_context_high->metal_4h` score `0.8407` n `96` status `ready` deltaP `14.7357` edge `0.0294` maxDD `-1.273`
- `market_context_high->index_1h` score `0.6827` n `96` status `ready` deltaP `13.0676` edge `0.0085` maxDD `-0.0982`
- `market_context_high->crypto_major_4h` score `0.5948` n `96` status `ready` deltaP `8.4095` edge `0.0956` maxDD `-3.1677`
- `market_context_high->unknown_1h` score `0.4759` n `96` status `ready` deltaP `9.3563` edge `0.0` maxDD `-0.4843`
- `market_context_high->crypto_alt_4h` score `0.0846` n `96` status `ready` deltaP `8.8415` edge `0.0751` maxDD `-5.4926`
- `market_context_high->metal_1h` score `-0.0046` n `96` status `ready` deltaP `4.3226` edge `0.0095` maxDD `-0.4291`
- `market_context_high->unknown_24h` score `-0.0221` n `91` status `ready` deltaP `13.9557` edge `-0.0735` maxDD `-0.3771`
- `market_context_high->fx_4h` score `-0.1861` n `96` status `ready` deltaP `3.9888` edge `-0.0002` maxDD `-0.3539`
- `market_context_high->fx_1h` score `-0.432` n `96` status `ready` deltaP `-3.1188` edge `0.0013` maxDD `-0.2043`
- `market_context_high->commodity_4h` score `-0.4351` n `96` status `ready` deltaP `3.0234` edge `0.0091` maxDD `-2.4692`
- `market_context_high->crypto_alt_1h` score `-0.447` n `96` status `ready` deltaP `1.7777` edge `0.011` maxDD `-2.413`
- `market_context_high->index_4h` score `-0.4648` n `96` status `ready` deltaP `1.8546` edge `0.0144` maxDD `-0.5728`
- `market_context_high->crypto_major_1h` score `-0.5644` n `96` status `ready` deltaP `0.2869` edge `0.0102` maxDD `-2.7581`
- `market_context_high->commodity_1h` score `-0.8549` n `96` status `ready` deltaP `-7.142` edge `-0.0054` maxDD `-1.1941`
- `market_context_high->metal_24h` score `-2.1434` n `91` status `ready` deltaP `-5.586` edge `0.0395` maxDD `-8.831`
- `market_context_high->fx_24h` score `-4.3354` n `91` status `ready` deltaP `-27.5603` edge `-0.0276` maxDD `-1.3293`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
