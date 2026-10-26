# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-26T05:52:23.841923+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `64`

- Symbol pattern count: `7254`

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

- `market_context_high->unknown_4h` score `24.2964` n `116` status `ready` deltaP `-2.8595` edge `2.0773` maxDD `-1.016`
- `market_context_high->metal_24h` score `0.5138` n `110` status `ready` deltaP `27.1654` edge `0.1518` maxDD `-7.3625`
- `market_context_high->fx_24h` score `0.1902` n `110` status `ready` deltaP `22.6231` edge `0.0308` maxDD `-1.2451`
- `market_context_high->fx_1h` score `0.0181` n `128` status `ready` deltaP `5.436` edge `0.0019` maxDD `-0.1986`
- `market_context_high->fx_4h` score `-0.106` n `116` status `ready` deltaP `6.4971` edge `0.0077` maxDD `-0.4545`
- `market_context_high->metal_1h` score `-0.3418` n `128` status `ready` deltaP `5.4547` edge `-0.001` maxDD `-1.6682`
- `market_context_high->commodity_1h` score `-0.4636` n `128` status `ready` deltaP `0.2152` edge `0.01` maxDD `-1.0053`
- `market_context_high->commodity_4h` score `-0.593` n `116` status `ready` deltaP `0.5046` edge `0.0435` maxDD `-1.165`
- `market_context_high->index_1h` score `-0.6102` n `128` status `ready` deltaP `-1.2959` edge `-0.0044` maxDD `-1.2155`
- `market_context_high->index_24h` score `-0.6549` n `110` status `ready` deltaP `11.1553` edge `-0.0301` maxDD `-4.925`
- `market_context_high->crypto_major_1h` score `-1.2912` n `128` status `ready` deltaP `2.9753` edge `-0.0273` maxDD `-9.3126`
- `market_context_high->metal_4h` score `-1.3028` n `116` status `ready` deltaP `3.3117` edge `-0.0181` maxDD `-5.3474`
- `market_context_high->index_4h` score `-2.1058` n `116` status `ready` deltaP `-6.9964` edge `-0.0359` maxDD `-4.3282`
- `market_context_high->equity_1h` score `-2.3242` n `128` status `ready` deltaP `0.5005` edge `-0.0727` maxDD `-12.2891`
- `market_context_high->crypto_alt_1h` score `-2.4171` n `128` status `ready` deltaP `-1.3099` edge `-0.0527` maxDD `-13.2099`
- `market_context_high->crypto_major_24h` score `-4.762` n `110` status `ready` deltaP `-2.5537` edge `-0.1402` maxDD `-27.5967`
- `market_context_high->commodity_24h` score `-6.1764` n `110` status `ready` deltaP `-18.0997` edge `-0.1474` maxDD `-22.2359`
- `market_context_high->crypto_major_4h` score `-6.5515` n `116` status `ready` deltaP `-12.3686` edge `-0.2535` maxDD `-32.9851`
- `market_context_high->equity_24h` score `-7.4189` n `110` status `ready` deltaP `-5.2809` edge `-0.3709` maxDD `-36.6024`
- `market_context_high->equity_4h` score `-9.1109` n `116` status `ready` deltaP `-9.12` edge `-0.3811` maxDD `-45.7601`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
