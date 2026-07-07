# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-07T20:37:30.319475+00:00`
- Price records: `672`
- Market context records: `6016`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11126`

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

- `news_risk_high->fx_24h` score `7.6494` n `30` status `ready` deltaP `69.0972` edge `0.1768` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.2029` n `30` status `ready` deltaP `43.5061` edge `0.0648` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `3.4835` n `30` status `ready` deltaP `29.375` edge `0.115` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.243` n `30` status `ready` deltaP `26.9261` edge `0.0213` maxDD `-0.1113`
- `market_context_high->equity_24h` score `1.3676` n `186` status `ready` deltaP `27.285` edge `0.4772` maxDD `-31.6107`
- `market_context_high->equity_4h` score `1.14` n `212` status `ready` deltaP `7.5616` edge `0.1536` maxDD `-4.0541`
- `news_risk_high->crypto_major_1h` score `0.8107` n `30` status `ready` deltaP `10.1896` edge `0.0827` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.1881` n `30` status `ready` deltaP `5.1697` edge `0.0358` maxDD `-1.6923`
- `news_risk_high->index_24h` score `0.1343` n `30` status `ready` deltaP `9.2361` edge `0.0428` maxDD `-2.3058`
- `market_context_high->metal_1h` score `-0.3671` n `212` status `ready` deltaP `4.0363` edge `0.0059` maxDD `-2.0564`
- `news_risk_high->metal_1h` score `-0.4234` n `30` status `ready` deltaP `1.2375` edge `-0.0259` maxDD `-1.2643`
- `market_context_high->equity_1h` score `-0.6131` n `212` status `ready` deltaP `1.2061` edge `0.0262` maxDD `-4.3608`
- `market_context_high->commodity_1h` score `-0.6706` n `212` status `ready` deltaP `-1.3925` edge `-0.0002` maxDD `-0.7117`
- `market_context_high->fx_1h` score `-0.6714` n `212` status `ready` deltaP `-0.6525` edge `-0.0014` maxDD `-0.6829`
- `market_context_high->index_24h` score `-0.9449` n `186` status `ready` deltaP `3.7523` edge `0.0617` maxDD `-8.6284`
- `market_context_high->crypto_alt_1h` score `-1.0509` n `212` status `ready` deltaP `2.7483` edge `0.0222` maxDD `-9.3536`
- `news_risk_high->index_1h` score `-1.0524` n `30` status `ready` deltaP `-9.7006` edge `-0.0188` maxDD `-1.1161`
- `market_context_high->commodity_4h` score `-1.0599` n `212` status `ready` deltaP `-2.1399` edge `-0.0094` maxDD `-2.9773`
- `market_context_high->crypto_major_1h` score `-1.0626` n `212` status `ready` deltaP `2.9884` edge `0.0206` maxDD `-9.807`
- `market_context_high->index_4h` score `-1.09` n `212` status `ready` deltaP `1.3202` edge `0.0157` maxDD `-2.8063`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
