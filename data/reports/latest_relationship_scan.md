# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-18T16:37:31.289915+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11627`

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

- `market_context_high->crypto_major_24h` score `2.523` n `91` status `ready` deltaP `9.7854` edge `0.2658` maxDD `-4.9964`
- `market_context_high->commodity_24h` score `1.7162` n `91` status `ready` deltaP `19.3727` edge `0.2742` maxDD `-4.666`
- `market_context_high->equity_1h` score `1.1633` n `96` status `ready` deltaP `9.7618` edge `0.062` maxDD `-0.4112`
- `market_context_high->metal_4h` score `0.7403` n `96` status `ready` deltaP `14.126` edge `0.0251` maxDD `-1.273`
- `market_context_high->index_1h` score `0.6707` n `96` status `ready` deltaP `12.9179` edge `0.0085` maxDD `-0.0982`
- `market_context_high->unknown_1h` score `0.4651` n `96` status `ready` deltaP `9.3563` edge `-0.0009` maxDD `-0.4843`
- `market_context_high->crypto_major_4h` score `0.413` n `96` status `ready` deltaP `7.9522` edge `0.0835` maxDD `-3.1677`
- `market_context_high->equity_4h` score `0.3637` n `96` status `ready` deltaP `3.6839` edge `0.0946` maxDD `-2.4411`
- `market_context_high->metal_1h` score `-0.0046` n `96` status `ready` deltaP `4.3226` edge `0.0095` maxDD `-0.4291`
- `market_context_high->crypto_alt_4h` score `-0.0336` n `96` status `ready` deltaP `8.3841` edge `0.0683` maxDD `-5.4926`
- `market_context_high->fx_4h` score `-0.2099` n `96` status `ready` deltaP `3.5315` edge `-0.0002` maxDD `-0.3539`
- `market_context_high->unknown_24h` score `-0.2555` n `91` status `ready` deltaP `11.9984` edge `-0.0799` maxDD `-0.3771`
- `market_context_high->commodity_4h` score `-0.3735` n `96` status `ready` deltaP `3.938` edge `0.0109` maxDD `-2.4692`
- `market_context_high->fx_1h` score `-0.4794` n `96` status `ready` deltaP `-4.017` edge `0.0012` maxDD `-0.2043`
- `market_context_high->crypto_alt_1h` score `-0.4969` n `96` status `ready` deltaP `1.1789` edge `0.0086` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-0.5762` n `96` status `ready` deltaP `0.4366` edge `0.0077` maxDD `-2.7581`
- `market_context_high->index_4h` score `-0.6203` n `96` status `ready` deltaP `0.3303` edge `0.0116` maxDD `-0.5728`
- `market_context_high->commodity_1h` score `-0.8674` n `96` status `ready` deltaP `-7.2917` edge `-0.006` maxDD `-1.1941`
- `market_context_high->metal_24h` score `-2.3804` n `91` status `ready` deltaP `-7.5647` edge `0.0223` maxDD `-8.831`
- `market_context_high->fx_24h` score `-4.5138` n `91` status `ready` deltaP `-29.5504` edge `-0.0292` maxDD `-1.3293`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
