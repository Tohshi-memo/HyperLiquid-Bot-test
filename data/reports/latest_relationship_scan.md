# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-21T13:07:30.026944+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9102`

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

- `market_context_high->unknown_4h` score `31.7857` n `58` status `ready` deltaP `1.23` edge `2.6556` maxDD `-0.5326`
- `news_risk_high->crypto_major_24h` score `20.3437` n `101` status `ready` deltaP `7.9706` edge `2.328` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `14.4889` n `101` status `ready` deltaP `8.3557` edge `1.6398` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `3.3447` n `101` status `ready` deltaP `16.48` edge `0.2898` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `3.0749` n `101` status `ready` deltaP `19.8337` edge `0.2498` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `2.3709` n `101` status `ready` deltaP `14.7344` edge `0.1459` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `1.7727` n `101` status `ready` deltaP `16.5308` edge `0.0898` maxDD `-2.8494`
- `news_risk_high->commodity_24h` score `1.3236` n `101` status `ready` deltaP `23.8913` edge `0.141` maxDD `-3.4467`
- `market_context_high->equity_1h` score `0.7528` n `58` status `ready` deltaP `5.5596` edge `0.051` maxDD `-0.36`
- `market_context_high->index_1h` score `0.619` n `58` status `ready` deltaP `9.5292` edge `0.0136` maxDD `-0.0435`
- `news_risk_high->metal_1h` score `0.4711` n `101` status `ready` deltaP `13.2507` edge `0.0111` maxDD `-0.8144`
- `market_context_high->fx_1h` score `0.4097` n `58` status `ready` deltaP `9.5241` edge `0.0063` maxDD `-0.1854`
- `news_risk_high->fx_4h` score `0.3391` n `101` status `ready` deltaP `10.0126` edge `0.0251` maxDD `-0.421`
- `news_risk_high->metal_4h` score `0.2811` n `101` status `ready` deltaP `14.6598` edge `0.0311` maxDD `-2.0994`
- `market_context_high->index_4h` score `0.2521` n `58` status `ready` deltaP `13.5618` edge `0.0056` maxDD `-1.0949`
- `market_context_high->metal_1h` score `0.1932` n `58` status `ready` deltaP `4.8008` edge `0.0149` maxDD `-0.1314`
- `news_risk_high->fx_1h` score `-0.1393` n `101` status `ready` deltaP `3.8907` edge `0.0068` maxDD `-0.2147`
- `news_risk_high->equity_1h` score `-0.3221` n `101` status `ready` deltaP `1.1724` edge `0.0059` maxDD `-0.9112`
- `market_context_high->fx_4h` score `-0.4156` n `58` status `ready` deltaP `1.8187` edge `-0.003` maxDD `-0.6588`
- `news_risk_high->metal_24h` score `-0.4804` n `101` status `ready` deltaP `8.7355` edge `-0.0354` maxDD `-2.4203`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
