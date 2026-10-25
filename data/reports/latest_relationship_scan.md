# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-25T18:52:24.771570+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5440`

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

- `market_context_high->unknown_4h` score `30.0285` n `113` status `ready` deltaP `-0.7487` edge `2.5409` maxDD `-1.016`
- `market_context_high->fx_4h` score `-0.0305` n `113` status `ready` deltaP `7.3063` edge `0.0086` maxDD `-0.4545`
- `market_context_high->fx_1h` score `-0.0739` n `113` status `ready` deltaP `3.41` edge `0.0027` maxDD `-0.1258`
- `market_context_high->crypto_major_24h` score `-0.0839` n `70` status `ready` deltaP `0.2926` edge `0.0936` maxDD `-4.5369`
- `market_context_high->commodity_1h` score `-0.4655` n `113` status `ready` deltaP `0.2663` edge `0.0095` maxDD `-1.0053`
- `market_context_high->metal_1h` score `-0.6168` n `113` status `ready` deltaP `4.9335` edge `-0.0051` maxDD `-1.6682`
- `market_context_high->index_1h` score `-0.7017` n `113` status `ready` deltaP `-2.7847` edge `-0.0062` maxDD `-1.2155`
- `market_context_high->commodity_24h` score `-0.7828` n `70` status `ready` deltaP `1.121` edge `0.0164` maxDD `-3.6055`
- `market_context_high->commodity_4h` score `-0.8016` n `113` status `ready` deltaP `-1.7807` edge `0.032` maxDD `-1.165`
- `market_context_high->fx_24h` score `-1.0439` n `70` status `ready` deltaP `8.6161` edge `0.0128` maxDD `-1.2451`
- `market_context_high->crypto_major_1h` score `-1.3324` n `113` status `ready` deltaP `3.0973` edge `-0.0334` maxDD `-9.3126`
- `market_context_high->index_24h` score `-1.5951` n `70` status `ready` deltaP `3.2292` edge `-0.0978` maxDD `-4.925`
- `market_context_high->metal_24h` score `-1.6558` n `70` status `ready` deltaP `-0.3671` edge `0.0572` maxDD `-7.3625`
- `market_context_high->metal_4h` score `-1.9292` n `113` status `ready` deltaP `4.4612` edge `-0.0195` maxDD `-5.3474`
- `market_context_high->index_4h` score `-2.206` n `113` status `ready` deltaP `-8.6822` edge `-0.0375` maxDD `-4.3282`
- `market_context_high->crypto_alt_1h` score `-3.2026` n `113` status `ready` deltaP `-1.86` edge `-0.0671` maxDD `-11.3243`
- `market_context_high->equity_1h` score `-3.9698` n `113` status `ready` deltaP `-1.4374` edge `-0.0939` maxDD `-12.1865`
- `market_context_high->crypto_alt_24h` score `-6.4674` n `70` status `ready` deltaP `0.7342` edge `-0.1884` maxDD `-42.3182`
- `market_context_high->equity_24h` score `-9.9889` n `70` status `ready` deltaP `-10.6151` edge `-0.6815` maxDD `-36.6024`
- `market_context_high->crypto_major_4h` score `-10.2169` n `113` status `ready` deltaP `-14.1147` edge `-0.2575` maxDD `-32.9851`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
