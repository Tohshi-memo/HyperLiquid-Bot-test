# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-18T15:52:28.979079+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11630`

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

- `market_context_high->crypto_major_24h` score `2.4371` n `91` status `ready` deltaP `9.6121` edge `0.2598` maxDD `-4.9964`
- `market_context_high->commodity_24h` score `1.7388` n `91` status `ready` deltaP `19.3727` edge `0.2771` maxDD `-4.666`
- `market_context_high->equity_1h` score `1.2172` n `96` status `ready` deltaP `10.2109` edge `0.0635` maxDD `-0.4112`
- `market_context_high->metal_4h` score `0.7211` n `96` status `ready` deltaP `14.126` edge `0.0235` maxDD `-1.273`
- `market_context_high->index_1h` score `0.6959` n `96` status `ready` deltaP `13.2173` edge `0.0086` maxDD `-0.0982`
- `market_context_high->unknown_1h` score `0.5083` n `96` status `ready` deltaP `9.3563` edge `0.0027` maxDD `-0.4843`
- `market_context_high->crypto_major_4h` score `0.3854` n `96` status `ready` deltaP `7.9522` edge `0.0812` maxDD `-3.1677`
- `market_context_high->equity_4h` score `0.236` n `96` status `ready` deltaP `3.2266` edge `0.087` maxDD `-2.4411`
- `market_context_high->metal_1h` score `-0.0046` n `96` status `ready` deltaP `4.3226` edge `0.0095` maxDD `-0.4291`
- `market_context_high->crypto_alt_4h` score `-0.0444` n `96` status `ready` deltaP `8.3841` edge `0.0674` maxDD `-5.4926`
- `market_context_high->fx_4h` score `-0.2091` n `96` status `ready` deltaP `3.5315` edge `-0.0001` maxDD `-0.3539`
- `market_context_high->unknown_24h` score `-0.3115` n `91` status `ready` deltaP `11.4785` edge `-0.0811` maxDD `-0.3771`
- `market_context_high->commodity_4h` score `-0.3719` n `96` status `ready` deltaP `3.938` edge `0.0111` maxDD `-2.4692`
- `market_context_high->fx_1h` score `-0.4717` n `96` status `ready` deltaP `-3.8673` edge `0.0012` maxDD `-0.2043`
- `market_context_high->crypto_alt_1h` score `-0.5101` n `96` status `ready` deltaP `1.0292` edge `0.0079` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-0.6026` n `96` status `ready` deltaP `0.1372` edge `0.0063` maxDD `-2.7581`
- `market_context_high->index_4h` score `-0.6311` n `96` status `ready` deltaP `0.3303` edge `0.0107` maxDD `-0.5728`
- `market_context_high->commodity_1h` score `-0.858` n `96` status `ready` deltaP `-7.142` edge `-0.0058` maxDD `-1.1941`
- `market_context_high->metal_24h` score `-2.4473` n `91` status `ready` deltaP `-8.0846` edge `0.0172` maxDD `-8.831`
- `market_context_high->fx_24h` score `-4.5602` n `91` status `ready` deltaP `-30.0703` edge `-0.0296` maxDD `-1.3293`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
