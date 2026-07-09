# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-09T02:37:27.159217+00:00`
- Price records: `672`
- Market context records: `6149`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11131`

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

- `news_risk_high->crypto_alt_24h` score `11.8616` n `30` status `ready` deltaP `41.5972` edge `0.7259` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `7.692` n `30` status `ready` deltaP `68.0556` edge `0.1873` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.3189` n `32` status `ready` deltaP `45.0457` edge `0.0642` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.4027` n `32` status `ready` deltaP `28.8922` edge `0.0215` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `1.4959` n `195` status `ready` deltaP `0.5052` edge `0.2221` maxDD `-3.7317`
- `news_risk_high->crypto_major_1h` score `1.2527` n `32` status `ready` deltaP `13.5292` edge `0.1171` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.6533` n `32` status `ready` deltaP `8.6265` edge `0.0724` maxDD `-1.6923`
- `news_risk_high->crypto_major_24h` score `0.4164` n `30` status `ready` deltaP `12.2916` edge `0.0494` maxDD `-4.2368`
- `market_context_high->equity_4h` score `0.0968` n `195` status `ready` deltaP `2.6829` edge `0.0819` maxDD `-2.671`
- `news_risk_high->index_24h` score `-0.2282` n `30` status `ready` deltaP `7.5` edge `0.0079` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.2684` n `195` status `ready` deltaP `1.5845` edge `-0.0004` maxDD `-0.5659`
- `market_context_high->unknown_4h` score `-0.3303` n `195` status `ready` deltaP `-2.4594` edge `0.2421` maxDD `-11.925`
- `market_context_high->metal_24h` score `-0.4607` n `195` status `ready` deltaP `17.7724` edge `0.0793` maxDD `-11.8809`
- `market_context_high->metal_4h` score `-0.5864` n `195` status `ready` deltaP `3.9994` edge `0.0169` maxDD `-3.4996`
- `news_risk_high->commodity_24h` score `-0.6079` n `30` status `ready` deltaP `14.0973` edge `-0.1241` maxDD `-0.3101`
- `news_risk_high->metal_1h` score `-0.7559` n `32` status `ready` deltaP `-2.8443` edge `-0.0282` maxDD `-1.6464`
- `market_context_high->commodity_1h` score `-0.7631` n `195` status `ready` deltaP `-2.1388` edge `-0.0047` maxDD `-0.5708`
- `market_context_high->metal_1h` score `-0.7972` n `195` status `ready` deltaP `2.5403` edge `-0.0035` maxDD `-2.0564`
- `market_context_high->equity_1h` score `-0.8663` n `195` status `ready` deltaP `-1.4571` edge `0.0102` maxDD `-4.2573`
- `market_context_high->crypto_alt_1h` score `-0.9226` n `195` status `ready` deltaP `3.6105` edge `0.0329` maxDD `-9.3536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
