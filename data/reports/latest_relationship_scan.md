# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-19T21:46:17.325339+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10828`

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

- `market_context_high->equity_4h` score `2.2543` n `96` status `ready` deltaP `11.6107` edge `0.1993` maxDD `-2.4411`
- `market_context_high->equity_1h` score `1.7613` n `96` status `ready` deltaP `14.5522` edge `0.0799` maxDD `-0.4112`
- `market_context_high->index_1h` score `0.9726` n `96` status `ready` deltaP `16.361` edge `0.0107` maxDD `-0.0982`
- `market_context_high->metal_4h` score `0.498` n `96` status `ready` deltaP `13.2113` edge `0.011` maxDD `-1.273`
- `market_context_high->index_4h` score `0.2942` n `96` status `ready` deltaP `9.7815` edge `0.0248` maxDD `-0.5728`
- `market_context_high->commodity_24h` score `0.2223` n `96` status `ready` deltaP `6.4236` edge `0.169` maxDD `-4.666`
- `market_context_high->fx_4h` score `0.0359` n `96` status `ready` deltaP `7.4949` edge `0.0049` maxDD `-0.3539`
- `market_context_high->unknown_24h` score `-0.0093` n `96` status `ready` deltaP `17.7083` edge `-0.0682` maxDD `-1.0505`
- `market_context_high->unknown_1h` score `-0.1812` n `96` status `ready` deltaP `5.9132` edge `-0.0318` maxDD `-0.4843`
- `market_context_high->metal_1h` score `-0.1927` n `96` status `ready` deltaP `2.8256` edge `0.0038` maxDD `-0.4291`
- `market_context_high->fx_1h` score `-0.3198` n `96` status `ready` deltaP `-1.1727` edge `0.0027` maxDD `-0.2043`
- `market_context_high->commodity_4h` score `-0.6591` n `96` status `ready` deltaP `-0.94` edge `0.0068` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.9063` n `96` status `ready` deltaP `-8.0402` edge `-0.006` maxDD `-1.1941`
- `market_context_high->crypto_alt_1h` score `-0.9116` n `96` status `ready` deltaP `-0.9169` edge `-0.0306` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-1.0021` n `96` status `ready` deltaP `0.8857` edge `-0.0499` maxDD `-2.7581`
- `market_context_high->crypto_major_4h` score `-1.8115` n `96` status `ready` deltaP `5.3607` edge `-0.0846` maxDD `-3.1677`
- `market_context_high->crypto_alt_4h` score `-1.863` n `96` status `ready` deltaP `3.2012` edge `-0.0496` maxDD `-5.4926`
- `market_context_high->crypto_major_24h` score `-2.0725` n `96` status `ready` deltaP `2.9514` edge `-0.0716` maxDD `-4.9964`
- `market_context_high->metal_24h` score `-3.1876` n `96` status `ready` deltaP `-9.8958` edge `-0.0119` maxDD `-11.4635`
- `market_context_high->fx_24h` score `-3.3594` n `96` status `ready` deltaP `-17.3611` edge `-0.0059` maxDD `-1.9981`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
