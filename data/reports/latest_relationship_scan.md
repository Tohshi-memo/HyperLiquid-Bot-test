# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-19T08:52:28.203578+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11762`

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

- `market_context_high->crypto_major_24h` score `2.2289` n `96` status `ready` deltaP `7.6389` edge `0.2556` maxDD `-4.9964`
- `market_context_high->equity_4h` score `1.7677` n `96` status `ready` deltaP `10.2388` edge `0.1679` maxDD `-2.4411`
- `market_context_high->equity_1h` score `1.6018` n `96` status `ready` deltaP `13.8037` edge `0.0716` maxDD `-0.4112`
- `market_context_high->metal_4h` score `1.3844` n `96` status `ready` deltaP `19.4613` edge `0.0432` maxDD `-1.273`
- `market_context_high->crypto_major_4h` score `1.1345` n `96` status `ready` deltaP `11.9156` edge `0.1172` maxDD `-3.1677`
- `market_context_high->commodity_24h` score `1.06` n `96` status `ready` deltaP `13.3681` edge `0.2301` maxDD `-4.666`
- `market_context_high->index_1h` score `0.8863` n `96` status `ready` deltaP `15.4628` edge `0.0095` maxDD `-0.0982`
- `market_context_high->unknown_1h` score `0.2061` n `96` status `ready` deltaP `8.1587` edge `-0.0145` maxDD `-0.4843`
- `market_context_high->crypto_alt_4h` score `0.1832` n `96` status `ready` deltaP `9.9085` edge `0.0762` maxDD `-5.4926`
- `market_context_high->metal_1h` score `0.156` n `96` status `ready` deltaP `5.9693` edge `0.0119` maxDD `-0.4291`
- `market_context_high->index_4h` score `0.0935` n `96` status `ready` deltaP `7.6473` edge `0.0223` maxDD `-0.5728`
- `market_context_high->fx_4h` score `0.0684` n `96` status `ready` deltaP `8.1046` edge `0.005` maxDD `-0.3539`
- `market_context_high->unknown_24h` score `-0.1083` n `96` status `ready` deltaP `15.4514` edge `-0.0614` maxDD `-1.0505`
- `market_context_high->fx_1h` score `-0.3276` n `96` status `ready` deltaP `-1.3224` edge `0.0027` maxDD `-0.2043`
- `market_context_high->crypto_major_1h` score `-0.4032` n `96` status `ready` deltaP `2.6821` edge `0.0149` maxDD `-2.7581`
- `market_context_high->crypto_alt_1h` score `-0.4836` n `96` status `ready` deltaP `1.3286` edge `0.0093` maxDD `-2.413`
- `market_context_high->commodity_4h` score `-0.5181` n `96` status `ready` deltaP `1.6515` edge `0.0076` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.8798` n `96` status `ready` deltaP `-7.5911` edge `-0.0056` maxDD `-1.1941`
- `market_context_high->metal_24h` score `-2.1988` n `96` status `ready` deltaP `-3.6458` edge `0.0732` maxDD `-11.4635`
- `market_context_high->fx_24h` score `-4.1779` n `96` status `ready` deltaP `-24.6527` edge `-0.0255` maxDD `-1.9981`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
