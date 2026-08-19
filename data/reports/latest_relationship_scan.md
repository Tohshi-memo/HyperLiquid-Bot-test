# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-19T22:22:24.898898+00:00`
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

- `market_context_high->equity_4h` score `2.2243` n `96` status `ready` deltaP `11.6107` edge `0.1968` maxDD `-2.4411`
- `market_context_high->equity_1h` score `1.7301` n `96` status `ready` deltaP `14.2528` edge `0.0793` maxDD `-0.4112`
- `market_context_high->index_1h` score `0.9462` n `96` status `ready` deltaP `16.0616` edge `0.0105` maxDD `-0.0982`
- `market_context_high->metal_4h` score `0.475` n `96` status `ready` deltaP `13.0589` edge `0.0101` maxDD `-1.273`
- `market_context_high->index_4h` score `0.2906` n `96` status `ready` deltaP `9.7815` edge `0.0245` maxDD `-0.5728`
- `market_context_high->commodity_24h` score `0.2129` n `96` status `ready` deltaP `6.4236` edge `0.1678` maxDD `-4.666`
- `market_context_high->fx_4h` score `0.0352` n `96` status `ready` deltaP `7.4949` edge `0.0048` maxDD `-0.3539`
- `market_context_high->unknown_24h` score `-0.0621` n `96` status `ready` deltaP `17.7083` edge `-0.0726` maxDD `-1.0505`
- `market_context_high->metal_1h` score `-0.1951` n `96` status `ready` deltaP `2.8256` edge `0.0036` maxDD `-0.4291`
- `market_context_high->unknown_1h` score `-0.2135` n `96` status `ready` deltaP `5.6138` edge `-0.0325` maxDD `-0.4843`
- `market_context_high->fx_1h` score `-0.3198` n `96` status `ready` deltaP `-1.1727` edge `0.0027` maxDD `-0.2043`
- `market_context_high->commodity_4h` score `-0.6575` n `96` status `ready` deltaP `-0.94` edge `0.007` maxDD `-2.4692`
- `market_context_high->crypto_alt_1h` score `-0.8953` n `96` status `ready` deltaP `-0.7672` edge `-0.0295` maxDD `-2.413`
- `market_context_high->commodity_1h` score `-0.9055` n `96` status `ready` deltaP `-8.0402` edge `-0.0059` maxDD `-1.1941`
- `market_context_high->crypto_major_1h` score `-1.0223` n `96` status `ready` deltaP `0.5863` edge `-0.0505` maxDD `-2.7581`
- `market_context_high->crypto_alt_4h` score `-1.941` n `96` status `ready` deltaP `3.2012` edge `-0.0561` maxDD `-5.4926`
- `market_context_high->crypto_major_4h` score `-2.0059` n `96` status `ready` deltaP `5.3607` edge `-0.1008` maxDD `-3.1677`
- `market_context_high->crypto_major_24h` score `-2.4841` n `96` status `ready` deltaP `2.9514` edge `-0.1059` maxDD `-4.9964`
- `market_context_high->metal_24h` score `-3.2525` n `96` status `ready` deltaP `-10.2431` edge `-0.0179` maxDD `-11.4635`
- `market_context_high->fx_24h` score `-3.3208` n `96` status `ready` deltaP `-17.0139` edge `-0.005` maxDD `-1.9981`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
