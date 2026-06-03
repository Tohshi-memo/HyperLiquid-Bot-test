# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-03T08:52:23.126207+00:00`
- Price records: `672`
- Market context records: `2748`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9237`

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

- `market_context_high->unknown_24h` score `7.3243` n `118` status `ready` deltaP `15.116` edge `0.5424` maxDD `-1.6255`
- `market_context_high->crypto_alt_24h` score `5.6763` n `118` status `ready` deltaP `12.344` edge `0.9948` maxDD `-19.9486`
- `market_context_high->unknown_4h` score `0.9521` n `143` status `ready` deltaP `6.4014` edge `0.142` maxDD `-3.7602`
- `market_context_high->index_4h` score `0.1713` n `143` status `ready` deltaP `11.1611` edge `0.0317` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `-0.1148` n `143` status `ready` deltaP `3.4976` edge `0.0402` maxDD `-3.1801`
- `market_context_high->index_1h` score `-0.155` n `143` status `ready` deltaP `3.2003` edge `0.0082` maxDD `-1.2855`
- `market_context_high->fx_1h` score `-0.5219` n `143` status `ready` deltaP `-0.3475` edge `0.0032` maxDD `-0.2164`
- `market_context_high->crypto_alt_1h` score `-0.6391` n `143` status `ready` deltaP `5.9954` edge `0.0541` maxDD `-10.747`
- `market_context_high->metal_1h` score `-0.7045` n `143` status `ready` deltaP `-0.5015` edge `-0.0024` maxDD `-3.0996`
- `market_context_high->commodity_1h` score `-0.7065` n `143` status `ready` deltaP `-0.8458` edge `-0.0096` maxDD `-4.3601`
- `market_context_high->crypto_major_1h` score `-0.9479` n `143` status `ready` deltaP `3.6473` edge `0.0411` maxDD `-9.622`
- `market_context_high->crypto_alt_4h` score `-1.0568` n `143` status `ready` deltaP `15.6011` edge `0.242` maxDD `-28.7261`
- `market_context_high->commodity_24h` score `-1.1322` n `118` status `ready` deltaP `4.8787` edge `0.1317` maxDD `-12.4171`
- `market_context_high->fx_4h` score `-1.1881` n `143` status `ready` deltaP `-4.2502` edge `0.0072` maxDD `-0.5631`
- `market_context_high->equity_1h` score `-1.2315` n `143` status `ready` deltaP `-4.3852` edge `0.0099` maxDD `-2.6634`
- `market_context_high->fx_24h` score `-1.2413` n `118` status `ready` deltaP `0.0971` edge `-0.0169` maxDD `-0.6418`
- `market_context_high->commodity_4h` score `-1.632` n `143` status `ready` deltaP `-0.4679` edge `-0.0141` maxDD `-10.0279`
- `market_context_high->equity_4h` score `-2.0027` n `143` status `ready` deltaP `-1.2493` edge `-0.0206` maxDD `-5.7037`
- `market_context_high->metal_4h` score `-2.3737` n `143` status `ready` deltaP `-2.1864` edge `-0.0347` maxDD `-11.4038`
- `market_context_high->crypto_major_4h` score `-2.4469` n `143` status `ready` deltaP `6.4473` edge `0.1339` maxDD `-32.2466`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
