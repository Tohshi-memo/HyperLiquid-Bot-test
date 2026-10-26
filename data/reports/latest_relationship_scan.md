# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-26T11:07:25.420394+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8298`

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

- `market_context_high->unknown_4h` score `18.9688` n `135` status `ready` deltaP `-1.2048` edge `1.6223` maxDD `-1.016`
- `market_context_high->metal_24h` score `0.5928` n `113` status `ready` deltaP `28.4445` edge `0.1534` maxDD `-7.3625`
- `market_context_high->fx_1h` score `0.122` n `147` status `ready` deltaP `6.6123` edge `0.0019` maxDD `-0.1986`
- `market_context_high->fx_24h` score `0.0412` n `113` status `ready` deltaP `19.9668` edge `0.0294` maxDD `-1.2451`
- `market_context_high->fx_4h` score `0.0371` n `135` status `ready` deltaP `8.2565` edge `0.0079` maxDD `-0.4545`
- `market_context_high->metal_1h` score `-0.2977` n `147` status `ready` deltaP `6.1235` edge `0.0002` maxDD `-1.6682`
- `market_context_high->commodity_1h` score `-0.3466` n `147` status `ready` deltaP `1.4828` edge `0.0113` maxDD `-1.0053`
- `market_context_high->index_24h` score `-0.485` n `113` status `ready` deltaP `11.3032` edge `-0.0093` maxDD `-4.925`
- `market_context_high->commodity_4h` score `-0.5573` n `135` status `ready` deltaP `4.598` edge `0.0458` maxDD `-1.165`
- `market_context_high->index_1h` score `-0.6394` n `147` status `ready` deltaP `-1.9319` edge `-0.0039` maxDD `-1.2155`
- `market_context_high->metal_4h` score `-1.1709` n `135` status `ready` deltaP `4.7245` edge `-0.0106` maxDD `-5.3474`
- `market_context_high->crypto_major_1h` score `-1.3263` n `147` status `ready` deltaP `1.551` edge `-0.0223` maxDD `-9.3126`
- `market_context_high->index_4h` score `-2.1636` n `135` status `ready` deltaP `-8.9329` edge `-0.0304` maxDD `-4.3282`
- `market_context_high->equity_1h` score `-2.3862` n `147` status `ready` deltaP `-1.8769` edge `-0.0648` maxDD `-12.2891`
- `market_context_high->crypto_alt_1h` score `-2.495` n `147` status `ready` deltaP `-3.3321` edge `-0.0492` maxDD `-13.2099`
- `market_context_high->crypto_major_24h` score `-4.6311` n `113` status `ready` deltaP `-2.0726` edge `-0.0942` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-5.648` n `135` status `ready` deltaP `-5.839` edge `-0.1812` maxDD `-32.9851`
- `market_context_high->commodity_24h` score `-6.4825` n `113` status `ready` deltaP `-18.8191` edge `-0.1467` maxDD `-24.0477`
- `market_context_high->equity_24h` score `-6.4981` n `113` status `ready` deltaP `-3.3386` edge `-0.2533` maxDD `-36.6024`
- `market_context_high->equity_4h` score `-8.5624` n `135` status `ready` deltaP `-7.9754` edge `-0.3184` maxDD `-45.7601`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
