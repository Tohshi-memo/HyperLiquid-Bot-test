# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-19T16:37:27.094971+00:00`
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

- `market_context_high->equity_4h` score `2.3501` n `96` status `ready` deltaP `12.3729` edge `0.2022` maxDD `-2.4411`
- `market_context_high->equity_1h` score `1.8512` n `96` status `ready` deltaP `15.3007` edge `0.0824` maxDD `-0.4112`
- `market_context_high->crypto_major_24h` score `0.9337` n `96` status `ready` deltaP `4.5139` edge `0.1685` maxDD `-4.9964`
- `market_context_high->index_1h` score `0.9222` n `96` status `ready` deltaP `15.7622` edge `0.0105` maxDD `-0.0982`
- `market_context_high->metal_4h` score `0.7769` n `96` status `ready` deltaP `15.4979` edge `0.019` maxDD `-1.273`
- `market_context_high->commodity_24h` score `0.4541` n `96` status `ready` deltaP `7.9861` edge `0.1883` maxDD `-4.666`
- `market_context_high->unknown_24h` score `0.342` n `96` status `ready` deltaP `18.2291` edge `-0.0424` maxDD `-1.0505`
- `market_context_high->index_4h` score `0.1458` n `96` status `ready` deltaP `8.2571` edge `0.0226` maxDD `-0.5728`
- `market_context_high->fx_4h` score `0.089` n `96` status `ready` deltaP `8.4095` edge `0.0056` maxDD `-0.3539`
- `market_context_high->unknown_1h` score `0.0886` n `96` status `ready` deltaP `7.2605` edge `-0.0183` maxDD `-0.4843`
- `market_context_high->crypto_major_4h` score `-0.0506` n `96` status `ready` deltaP `8.562` edge `0.0408` maxDD `-3.1677`
- `market_context_high->metal_1h` score `-0.0717` n `96` status `ready` deltaP `4.0232` edge `0.0059` maxDD `-0.4291`
- `market_context_high->fx_1h` score `-0.3525` n `96` status `ready` deltaP `-1.7715` edge `0.0025` maxDD `-0.2043`
- `market_context_high->crypto_alt_1h` score `-0.6474` n `96` status `ready` deltaP `0.7298` edge `-0.0077` maxDD `-2.413`
- `market_context_high->commodity_4h` score `-0.6547` n `96` status `ready` deltaP `-0.3303` edge `0.0033` maxDD `-2.4692`
- `market_context_high->crypto_major_1h` score `-0.6723` n `96` status `ready` deltaP `2.0833` edge `-0.0156` maxDD `-2.7581`
- `market_context_high->crypto_alt_4h` score `-0.6817` n `96` status `ready` deltaP `6.4024` edge `0.0275` maxDD `-5.4926`
- `market_context_high->commodity_1h` score `-0.9172` n `96` status `ready` deltaP `-8.0402` edge `-0.0074` maxDD `-1.1941`
- `market_context_high->metal_24h` score `-2.5792` n `96` status `ready` deltaP `-6.25` edge `0.0418` maxDD `-11.4635`
- `market_context_high->fx_24h` score `-3.6867` n `96` status `ready` deltaP `-20.3125` edge `-0.0135` maxDD `-1.9981`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
