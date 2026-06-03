# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-03T04:52:24.329380+00:00`
- Price records: `672`
- Market context records: `2731`
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

- `market_context_high->crypto_alt_24h` score `11.4271` n `111` status `ready` deltaP `16.3523` edge `1.1926` maxDD `-19.9486`
- `market_context_high->unknown_24h` score `8.5998` n `111` status `ready` deltaP `17.3048` edge `0.6341` maxDD `-1.6255`
- `market_context_high->crypto_major_24h` score `1.3484` n `111` status `ready` deltaP `6.5175` edge `0.8857` maxDD `-44.169`
- `market_context_high->unknown_4h` score `1.1986` n `143` status `ready` deltaP `7.7734` edge `0.1534` maxDD `-3.7602`
- `market_context_high->index_4h` score `0.0404` n `143` status `ready` deltaP `9.4843` edge `0.0261` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `-0.1423` n `143` status `ready` deltaP `2.8988` edge `0.0419` maxDD `-3.1801`
- `market_context_high->index_1h` score `-0.1861` n `143` status `ready` deltaP `2.7512` edge `0.0072` maxDD `-1.2855`
- `market_context_high->crypto_alt_4h` score `-0.3437` n `143` status `ready` deltaP `16.8206` edge `0.2933` maxDD `-28.7261`
- `market_context_high->fx_1h` score `-0.5195` n `143` status `ready` deltaP `-0.3475` edge `0.0034` maxDD `-0.2164`
- `market_context_high->commodity_1h` score `-0.5374` n `143` status `ready` deltaP `0.9506` edge `0.0001` maxDD `-4.3601`
- `market_context_high->crypto_alt_1h` score `-0.5541` n `143` status `ready` deltaP `6.1451` edge `0.064` maxDD `-10.747`
- `market_context_high->metal_1h` score `-0.7442` n `143` status `ready` deltaP `-1.25` edge `-0.0025` maxDD `-3.0996`
- `market_context_high->crypto_major_1h` score `-0.9183` n `143` status `ready` deltaP `3.6473` edge `0.0449` maxDD `-9.622`
- `market_context_high->fx_4h` score `-1.0165` n `143` status `ready` deltaP `-2.421` edge `0.0093` maxDD `-0.5631`
- `market_context_high->fx_24h` score `-1.0861` n `111` status `ready` deltaP `1.2716` edge `-0.0118` maxDD `-0.6418`
- `market_context_high->equity_1h` score `-1.2999` n `143` status `ready` deltaP `-4.8343` edge `0.0072` maxDD `-2.6634`
- `market_context_high->commodity_4h` score `-1.3881` n `143` status `ready` deltaP `1.2089` edge `0.006` maxDD `-10.0279`
- `market_context_high->commodity_24h` score `-1.6394` n `111` status `ready` deltaP `2.5807` edge `0.082` maxDD `-12.4171`
- `market_context_high->equity_4h` score `-2.0903` n `143` status `ready` deltaP `-1.2493` edge `-0.0279` maxDD `-5.7037`
- `market_context_high->crypto_major_4h` score `-2.2374` n `143` status `ready` deltaP `6.9046` edge `0.1577` maxDD `-32.2466`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
