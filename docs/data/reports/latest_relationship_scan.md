# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-02T22:22:20.106177+00:00`
- Price records: `672`
- Market context records: `2705`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9250`

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

- `market_context_high->crypto_alt_24h` score `10.4623` n `111` status `ready` deltaP `16.3523` edge `1.1122` maxDD `-19.9486`
- `market_context_high->unknown_24h` score `8.5894` n `111` status `ready` deltaP `17.1312` edge `0.6344` maxDD `-1.626`
- `market_context_high->unknown_4h` score `0.8274` n `143` status `ready` deltaP `5.9441` edge `0.1343` maxDD `-3.7312`
- `market_context_high->index_4h` score `0.2563` n `143` status `ready` deltaP `12.0758` edge `0.0365` maxDD `-2.3986`
- `market_context_high->crypto_major_24h` score `-0.0884` n `111` status `ready` deltaP `6.5175` edge `0.7015` maxDD `-44.169`
- `market_context_high->index_1h` score `-0.1612` n `143` status `ready` deltaP `3.0506` edge `0.0084` maxDD `-1.2855`
- `market_context_high->unknown_1h` score `-0.2926` n `143` status `ready` deltaP `2.4497` edge `0.0321` maxDD `-3.1587`
- `market_context_high->fx_1h` score `-0.4165` n `143` status `ready` deltaP `0.8501` edge `0.004` maxDD `-0.2164`
- `market_context_high->commodity_1h` score `-0.4455` n `143` status `ready` deltaP `1.9985` edge `0.0049` maxDD `-4.3601`
- `market_context_high->crypto_alt_4h` score `-0.5135` n `143` status `ready` deltaP `16.3633` edge `0.2822` maxDD `-28.7261`
- `market_context_high->crypto_alt_1h` score `-0.5767` n `143` status `ready` deltaP `5.9954` edge `0.0621` maxDD `-10.747`
- `market_context_high->fx_24h` score `-0.6554` n `111` status `ready` deltaP `5.7855` edge `-0.006` maxDD `-0.6418`
- `market_context_high->metal_1h` score `-0.7536` n `143` status `ready` deltaP `-1.3997` edge `-0.0027` maxDD `-3.0996`
- `market_context_high->fx_4h` score `-0.8936` n `143` status `ready` deltaP `-1.049` edge `0.0104` maxDD `-0.5631`
- `market_context_high->crypto_major_1h` score `-1.0157` n `143` status `ready` deltaP `3.0485` edge `0.0364` maxDD `-9.622`
- `market_context_high->commodity_24h` score `-1.0361` n `111` status `ready` deltaP `6.053` edge `0.1362` maxDD `-12.4171`
- `market_context_high->commodity_4h` score `-1.0643` n `143` status `ready` deltaP `4.1052` edge `0.0282` maxDD `-10.0279`
- `market_context_high->index_24h` score `-1.2544` n `111` status `ready` deltaP `2.1068` edge `-0.0205` maxDD `-2.5127`
- `market_context_high->equity_1h` score `-1.2643` n `143` status `ready` deltaP `-4.6354` edge `0.0094` maxDD `-2.7085`
- `market_context_high->equity_4h` score `-1.9901` n `143` status `ready` deltaP `-1.034` edge `-0.0185` maxDD `-5.9024`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
