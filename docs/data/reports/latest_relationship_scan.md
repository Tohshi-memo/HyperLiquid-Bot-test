# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-26T06:07:27.149459+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `64`

- Symbol pattern count: `7158`

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

- `market_context_high->unknown_4h` score `23.4242` n `117` status `ready` deltaP `-2.8572` edge `2.0046` maxDD `-1.016`
- `market_context_high->metal_24h` score `0.5465` n `111` status `ready` deltaP `27.5995` edge `0.1531` maxDD `-7.3625`
- `market_context_high->fx_24h` score `0.2018` n `111` status `ready` deltaP `22.7853` edge `0.0312` maxDD `-1.2451`
- `market_context_high->fx_1h` score `0.038` n `129` status `ready` deltaP `5.7873` edge `0.0021` maxDD `-0.1986`
- `market_context_high->fx_4h` score `-0.0742` n `117` status `ready` deltaP `6.895` edge `0.0077` maxDD `-0.4545`
- `market_context_high->metal_1h` score `-0.3665` n `129` status `ready` deltaP `5.055` edge `-0.0015` maxDD `-1.6682`
- `market_context_high->commodity_1h` score `-0.4848` n `129` status `ready` deltaP `-0.0348` edge `0.0099` maxDD `-1.0053`
- `market_context_high->commodity_4h` score `-0.6136` n `117` status `ready` deltaP `0.215` edge `0.0428` maxDD `-1.165`
- `market_context_high->index_1h` score `-0.6333` n `129` status `ready` deltaP `-1.6653` edge `-0.0049` maxDD `-1.2155`
- `market_context_high->index_24h` score `-0.6692` n `111` status `ready` deltaP `10.7311` edge `-0.0291` maxDD `-4.925`
- `market_context_high->metal_4h` score `-1.274` n `117` status `ready` deltaP `3.7758` edge `-0.0175` maxDD `-5.3474`
- `market_context_high->crypto_major_1h` score `-1.3118` n `129` status `ready` deltaP `2.5635` edge `-0.0272` maxDD `-9.3126`
- `market_context_high->index_4h` score `-2.1254` n `117` status `ready` deltaP `-7.3575` edge `-0.036` maxDD `-4.3282`
- `market_context_high->equity_1h` score `-2.3512` n `129` status `ready` deltaP `0.1311` edge `-0.0737` maxDD `-12.2891`
- `market_context_high->crypto_alt_1h` score `-2.4449` n `129` status `ready` deltaP `-1.649` edge `-0.054` maxDD `-13.2099`
- `market_context_high->crypto_major_24h` score `-4.8525` n `111` status `ready` deltaP `-2.806` edge `-0.1405` maxDD `-28.0329`
- `market_context_high->commodity_24h` score `-6.3093` n `111` status `ready` deltaP `-18.4028` edge `-0.1507` maxDD `-22.8399`
- `market_context_high->crypto_major_4h` score `-6.5151` n `117` status `ready` deltaP `-11.9685` edge `-0.2515` maxDD `-32.9851`
- `market_context_high->equity_24h` score `-7.425` n `111` status `ready` deltaP `-5.5087` edge `-0.366` maxDD `-36.6024`
- `market_context_high->equity_4h` score `-9.1079` n `117` status `ready` deltaP `-9.4369` edge `-0.3786` maxDD `-45.7601`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
