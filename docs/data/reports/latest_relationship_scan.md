# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-19T19:22:36.169891+00:00`
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

- `market_context_high->equity_4h` score `2.2989` n `96` status `ready` deltaP `11.7632` edge `0.202` maxDD `-2.4411`
- `market_context_high->equity_1h` score `1.9291` n `96` status `ready` deltaP `15.6001` edge `0.0869` maxDD `-0.4112`
- `market_context_high->index_1h` score `0.9762` n `96` status `ready` deltaP `16.361` edge `0.011` maxDD `-0.0982`
- `market_context_high->metal_4h` score `0.5767` n `96` status `ready` deltaP `13.8211` edge `0.0135` maxDD `-1.273`
- `market_context_high->commodity_24h` score `0.2824` n `96` status `ready` deltaP `6.4236` edge `0.1767` maxDD `-4.666`
- `market_context_high->unknown_24h` score `0.229` n `96` status `ready` deltaP `17.8819` edge `-0.0495` maxDD `-1.0505`
- `market_context_high->index_4h` score `0.2236` n `96` status `ready` deltaP `9.0193` edge `0.024` maxDD `-0.5728`
- `market_context_high->fx_4h` score `0.0375` n `96` status `ready` deltaP `7.4949` edge `0.0051` maxDD `-0.3539`
- `market_context_high->unknown_1h` score `0.0082` n `96` status `ready` deltaP `6.9611` edge `-0.023` maxDD `-0.4843`
- `market_context_high->metal_1h` score `-0.0526` n `96` status `ready` deltaP `4.3226` edge `0.0055` maxDD `-0.4291`
- `market_context_high->fx_1h` score `-0.3362` n `96` status `ready` deltaP `-1.4721` edge `0.0026` maxDD `-0.2043`
- `market_context_high->crypto_major_24h` score `-0.3397` n `96` status `ready` deltaP `2.9514` edge `0.0728` maxDD `-4.9964`
- `market_context_high->commodity_4h` score `-0.6879` n `96` status `ready` deltaP `-0.94` edge `0.0031` maxDD `-2.4692`
- `market_context_high->crypto_alt_1h` score `-0.6972` n `96` status `ready` deltaP `0.131` edge `-0.0101` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-0.712` n `96` status `ready` deltaP `1.7839` edge `-0.0187` maxDD `-2.7581`
- `market_context_high->commodity_1h` score `-0.8627` n `96` status `ready` deltaP `-7.2917` edge `-0.0054` maxDD `-1.1941`
- `market_context_high->crypto_major_4h` score `-0.9791` n `96` status `ready` deltaP `6.8851` edge `-0.0254` maxDD `-3.1677`
- `market_context_high->crypto_alt_4h` score `-1.3582` n `96` status `ready` deltaP `4.7256` edge `-0.0177` maxDD `-5.4926`
- `market_context_high->metal_24h` score `-2.8688` n `96` status `ready` deltaP `-8.1597` edge `0.0174` maxDD `-11.4635`
- `market_context_high->fx_24h` score `-3.5451` n `96` status `ready` deltaP `-19.0972` edge `-0.0098` maxDD `-1.9981`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
