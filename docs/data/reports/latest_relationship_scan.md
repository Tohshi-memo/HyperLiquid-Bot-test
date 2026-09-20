# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-20T22:52:27.667706+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9028`

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

- `news_risk_high->crypto_major_24h` score `24.6197` n `98` status `ready` deltaP `12.7906` edge `2.6522` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `20.2791` n `98` status `ready` deltaP `15.0935` edge `2.0774` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `4.586` n `101` status `ready` deltaP `20.5958` edge `0.3658` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `3.7429` n `101` status `ready` deltaP `20.4434` edge `0.3014` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `2.7018` n `101` status `ready` deltaP `16.2314` edge `0.1635` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.0568` n `101` status `ready` deltaP `18.1775` edge `0.1025` maxDD `-2.8494`
- `market_context_high->commodity_4h` score `1.6867` n `43` status `ready` deltaP `31.5477` edge `0.0362` maxDD `-0.7557`
- `market_context_high->fx_1h` score `1.3579` n `51` status `ready` deltaP `18.058` edge `0.0107` maxDD `-0.1012`
- `news_risk_high->commodity_24h` score `0.985` n `98` status `ready` deltaP `22.2541` edge `0.1085` maxDD `-3.4467`
- `news_risk_high->metal_4h` score `0.624` n `101` status `ready` deltaP `17.2512` edge `0.0424` maxDD `-2.0994`
- `news_risk_high->metal_1h` score `0.6197` n `101` status `ready` deltaP `14.598` edge `0.0145` maxDD `-0.8144`
- `market_context_high->metal_1h` score `0.4466` n `51` status `ready` deltaP `8.075` edge `0.0157` maxDD `-0.2519`
- `market_context_high->fx_4h` score `0.3798` n `43` status `ready` deltaP `10.848` edge `0.0046` maxDD `-0.2586`
- `news_risk_high->equity_24h` score `0.3295` n `98` status `ready` deltaP `15.7029` edge `0.0637` maxDD `-4.941`
- `news_risk_high->fx_4h` score `0.2395` n `101` status `ready` deltaP `9.098` edge `0.0229` maxDD `-0.421`
- `news_risk_high->equity_1h` score `0.1034` n `101` status `ready` deltaP `4.4658` edge `0.0194` maxDD `-0.9112`
- `news_risk_high->metal_24h` score `0.0362` n `98` status `ready` deltaP `14.2893` edge `-0.0062` maxDD `-2.4203`
- `market_context_high->commodity_1h` score `-0.1126` n `51` status `ready` deltaP `4.3032` edge `-0.0013` maxDD `-1.013`
- `market_context_high->index_1h` score `-0.128` n `51` status `ready` deltaP `1.4442` edge `0.0038` maxDD `-0.3875`
- `market_context_high->equity_1h` score `-0.2258` n `51` status `ready` deltaP `-0.0381` edge `0.0058` maxDD `-1.0927`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
