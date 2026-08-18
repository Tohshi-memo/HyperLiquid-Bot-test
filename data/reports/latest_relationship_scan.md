# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-18T16:28:28.598760+00:00`
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

- `market_context_high->crypto_major_24h` score `2.5014` n `91` status `ready` deltaP `9.7854` edge `0.264` maxDD `-4.9964`
- `market_context_high->commodity_24h` score `1.724` n `91` status `ready` deltaP `19.3727` edge `0.2752` maxDD `-4.666`
- `market_context_high->equity_1h` score `1.18` n `96` status `ready` deltaP `9.9115` edge `0.0624` maxDD `-0.4112`
- `market_context_high->metal_4h` score `0.7343` n `96` status `ready` deltaP `14.126` edge `0.0246` maxDD `-1.273`
- `market_context_high->index_1h` score `0.6839` n `96` status `ready` deltaP `13.0676` edge `0.0086` maxDD `-0.0982`
- `market_context_high->unknown_1h` score `0.4651` n `96` status `ready` deltaP `9.3563` edge `-0.0009` maxDD `-0.4843`
- `market_context_high->crypto_major_4h` score `0.4022` n `96` status `ready` deltaP `7.9522` edge `0.0826` maxDD `-3.1677`
- `market_context_high->equity_4h` score `0.3228` n `96` status `ready` deltaP `3.5315` edge `0.0922` maxDD `-2.4411`
- `market_context_high->metal_1h` score `-0.0034` n `96` status `ready` deltaP `4.3226` edge `0.0096` maxDD `-0.4291`
- `market_context_high->crypto_alt_4h` score `-0.0408` n `96` status `ready` deltaP `8.3841` edge `0.0677` maxDD `-5.4926`
- `market_context_high->fx_4h` score `-0.2091` n `96` status `ready` deltaP `3.5315` edge `-0.0001` maxDD `-0.3539`
- `market_context_high->unknown_24h` score `-0.2754` n `91` status `ready` deltaP `11.8251` edge `-0.0804` maxDD `-0.3771`
- `market_context_high->commodity_4h` score `-0.3727` n `96` status `ready` deltaP `3.938` edge `0.011` maxDD `-2.4692`
- `market_context_high->fx_1h` score `-0.4717` n `96` status `ready` deltaP `-3.8673` edge `0.0012` maxDD `-0.2043`
- `market_context_high->crypto_alt_1h` score `-0.507` n `96` status `ready` deltaP `1.0292` edge `0.0083` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-0.5871` n `96` status `ready` deltaP `0.2869` edge `0.0073` maxDD `-2.7581`
- `market_context_high->index_4h` score `-0.6239` n `96` status `ready` deltaP `0.3303` edge `0.0113` maxDD `-0.5728`
- `market_context_high->commodity_1h` score `-0.876` n `96` status `ready` deltaP `-7.4414` edge `-0.0061` maxDD `-1.1941`
- `market_context_high->metal_24h` score `-2.4027` n `91` status `ready` deltaP `-7.738` edge `0.0206` maxDD `-8.831`
- `market_context_high->fx_24h` score `-4.5301` n `91` status `ready` deltaP `-29.7237` edge `-0.0294` maxDD `-1.3293`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
