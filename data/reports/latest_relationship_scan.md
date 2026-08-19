# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-19T16:07:30.473206+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8829`

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

- `market_context_high->equity_4h` score `2.3235` n `96` status `ready` deltaP `12.2205` edge `0.201` maxDD `-2.4411`
- `market_context_high->equity_1h` score `1.856` n `96` status `ready` deltaP `15.3007` edge `0.0828` maxDD `-0.4112`
- `market_context_high->crypto_major_24h` score `1.1671` n `96` status `ready` deltaP `4.6875` edge `0.1868` maxDD `-4.9964`
- `market_context_high->index_1h` score `0.9079` n `96` status `ready` deltaP `15.6125` edge `0.0103` maxDD `-0.0982`
- `market_context_high->metal_4h` score `0.8313` n `96` status `ready` deltaP `15.8028` edge `0.0215` maxDD `-1.273`
- `market_context_high->commodity_24h` score `0.4877` n `96` status `ready` deltaP `8.3333` edge `0.1903` maxDD `-4.666`
- `market_context_high->unknown_24h` score `0.3564` n `96` status `ready` deltaP `18.2291` edge `-0.0412` maxDD `-1.0505`
- `market_context_high->crypto_major_4h` score `0.1622` n `96` status `ready` deltaP `8.8668` edge `0.0565` maxDD `-3.1677`
- `market_context_high->index_4h` score `0.1312` n `96` status `ready` deltaP `8.1046` edge `0.0224` maxDD `-0.5728`
- `market_context_high->fx_4h` score `0.0992` n `96` status `ready` deltaP `8.562` edge `0.0059` maxDD `-0.3539`
- `market_context_high->unknown_1h` score `0.0862` n `96` status `ready` deltaP `7.2605` edge `-0.0185` maxDD `-0.4843`
- `market_context_high->metal_1h` score `-0.0394` n `96` status `ready` deltaP `4.3226` edge `0.0066` maxDD `-0.4291`
- `market_context_high->fx_1h` score `-0.344` n `96` status `ready` deltaP `-1.6218` edge `0.0026` maxDD `-0.2043`
- `market_context_high->crypto_alt_4h` score `-0.5517` n `96` status `ready` deltaP `6.7073` edge `0.0363` maxDD `-5.4926`
- `market_context_high->commodity_4h` score `-0.6341` n `96` status `ready` deltaP `-0.0254` edge `0.0039` maxDD `-2.4692`
- `market_context_high->crypto_major_1h` score `-0.6356` n `96` status `ready` deltaP `2.233` edge `-0.0119` maxDD `-2.7581`
- `market_context_high->crypto_alt_1h` score `-0.6388` n `96` status `ready` deltaP `0.7298` edge `-0.0066` maxDD `-2.413`
- `market_context_high->commodity_1h` score `-0.9009` n `96` status `ready` deltaP `-7.7408` edge `-0.0073` maxDD `-1.1941`
- `market_context_high->metal_24h` score `-2.5244` n `96` status `ready` deltaP `-5.9028` edge `0.0465` maxDD `-11.4635`
- `market_context_high->fx_24h` score `-3.7078` n `96` status `ready` deltaP `-20.4861` edge `-0.0141` maxDD `-1.9981`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
