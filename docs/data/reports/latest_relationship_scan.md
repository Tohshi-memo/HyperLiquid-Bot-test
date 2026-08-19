# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-19T19:08:56.873825+00:00`
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

- `market_context_high->equity_4h` score `2.3013` n `96` status `ready` deltaP `11.7632` edge `0.2022` maxDD `-2.4411`
- `market_context_high->equity_1h` score `1.9483` n `96` status `ready` deltaP `15.7498` edge `0.0875` maxDD `-0.4112`
- `market_context_high->index_1h` score `0.9893` n `96` status `ready` deltaP `16.5107` edge `0.0111` maxDD `-0.0982`
- `market_context_high->metal_4h` score `0.5961` n `96` status `ready` deltaP `13.9735` edge `0.0141` maxDD `-1.273`
- `market_context_high->commodity_24h` score `0.2894` n `96` status `ready` deltaP `6.4236` edge `0.1776` maxDD `-4.666`
- `market_context_high->unknown_24h` score `0.2422` n `96` status `ready` deltaP `17.8819` edge `-0.0484` maxDD `-1.0505`
- `market_context_high->index_4h` score `0.2224` n `96` status `ready` deltaP `9.0193` edge `0.0239` maxDD `-0.5728`
- `market_context_high->fx_4h` score `0.0375` n `96` status `ready` deltaP `7.4949` edge `0.0051` maxDD `-0.3539`
- `market_context_high->unknown_1h` score `0.031` n `96` status `ready` deltaP `7.1108` edge `-0.0221` maxDD `-0.4843`
- `market_context_high->metal_1h` score `-0.0358` n `96` status `ready` deltaP `4.4723` edge `0.0059` maxDD `-0.4291`
- `market_context_high->crypto_major_24h` score `-0.2029` n `96` status `ready` deltaP `2.9514` edge `0.0842` maxDD `-4.9964`
- `market_context_high->fx_1h` score `-0.3362` n `96` status `ready` deltaP `-1.4721` edge `0.0026` maxDD `-0.2043`
- `market_context_high->crypto_alt_1h` score `-0.6793` n `96` status `ready` deltaP `0.2807` edge `-0.0088` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-0.6793` n `96` status `ready` deltaP `1.9336` edge `-0.0155` maxDD `-2.7581`
- `market_context_high->commodity_4h` score `-0.6911` n `96` status `ready` deltaP `-0.94` edge `0.0027` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.8643` n `96` status `ready` deltaP `-7.2917` edge `-0.0056` maxDD `-1.1941`
- `market_context_high->crypto_major_4h` score `-0.8925` n `96` status `ready` deltaP `7.0376` edge `-0.0192` maxDD `-3.1677`
- `market_context_high->crypto_alt_4h` score `-1.3053` n `96` status `ready` deltaP `4.878` edge `-0.0143` maxDD `-5.4926`
- `market_context_high->metal_24h` score `-2.8395` n `96` status `ready` deltaP `-7.9861` edge `0.02` maxDD `-11.4635`
- `market_context_high->fx_24h` score `-3.5626` n `96` status `ready` deltaP `-19.2708` edge `-0.0101` maxDD `-1.9981`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
