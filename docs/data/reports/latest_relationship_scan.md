# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-27T06:37:27.876483+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9656`

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

- `market_context_high->unknown_4h` score `74.3373` n `141` status `ready` deltaP `3.0348` edge `6.2081` maxDD `-1.0178`
- `market_context_high->unknown_1h` score `22.1535` n `141` status `ready` deltaP `0.6827` edge `1.8905` maxDD `-1.5807`
- `market_context_high->index_24h` score `0.553` n `120` status `ready` deltaP `21.7938` edge `0.0264` maxDD `-2.7307`
- `market_context_high->fx_4h` score `0.4618` n `141` status `ready` deltaP `13.2795` edge `0.0098` maxDD `-0.4545`
- `market_context_high->fx_1h` score `0.4388` n `141` status `ready` deltaP `10.3622` edge `0.0033` maxDD `-0.1986`
- `market_context_high->metal_1h` score `0.0726` n `141` status `ready` deltaP `11.0077` edge `0.0106` maxDD `-1.3073`
- `market_context_high->metal_24h` score `-0.0329` n `120` status `ready` deltaP `19.3241` edge `0.1195` maxDD `-6.204`
- `market_context_high->commodity_1h` score `-0.0954` n `141` status `ready` deltaP `3.9326` edge `0.0159` maxDD `-1.0053`
- `market_context_high->fx_24h` score `-0.3422` n `120` status `ready` deltaP `13.5529` edge `0.023` maxDD `-1.2451`
- `market_context_high->crypto_major_1h` score `-0.5513` n `141` status `ready` deltaP `5.4763` edge `0.0252` maxDD `-7.2574`
- `market_context_high->commodity_4h` score `-0.5788` n `141` status `ready` deltaP `5.2597` edge `0.0396` maxDD `-1.165`
- `market_context_high->index_1h` score `-0.6701` n `141` status `ready` deltaP `-1.2454` edge `-0.0039` maxDD `-1.8961`
- `market_context_high->metal_4h` score `-0.7996` n `141` status `ready` deltaP `9.1496` edge `0.0007` maxDD `-4.8031`
- `market_context_high->equity_1h` score `-1.7954` n `141` status `ready` deltaP `1.1891` edge `-0.0105` maxDD `-12.2088`
- `market_context_high->crypto_alt_1h` score `-2.0028` n `141` status `ready` deltaP `-0.86` edge `-0.0066` maxDD `-12.8878`
- `market_context_high->equity_24h` score `-2.9754` n `120` status `ready` deltaP `0.374` edge `-0.0433` maxDD `-19.2526`
- `market_context_high->index_4h` score `-3.0536` n `141` status `ready` deltaP `-5.0078` edge `-0.0259` maxDD `-6.2809`
- `market_context_high->crypto_major_4h` score `-3.8789` n `141` status `ready` deltaP `2.2833` edge `-0.0662` maxDD `-28.3718`
- `market_context_high->crypto_major_24h` score `-4.405` n `120` status `ready` deltaP `0.8203` edge `-0.0845` maxDD `-29.1905`
- `market_context_high->equity_4h` score `-5.6828` n `141` status `ready` deltaP `1.839` edge `-0.1364` maxDD `-39.6876`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
