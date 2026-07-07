# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-07T15:22:28.124428+00:00`
- Price records: `672`
- Market context records: `5993`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11236`

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

- `news_risk_high->fx_24h` score `7.5335` n `30` status `ready` deltaP `68.9236` edge `0.1683` maxDD `0.0`
- `news_risk_high->commodity_24h` score `4.3344` n `30` status `ready` deltaP `33.0209` edge `0.1616` maxDD `-0.3101`
- `news_risk_high->fx_4h` score `4.1409` n `30` status `ready` deltaP `42.8963` edge `0.0637` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.2298` n `30` status `ready` deltaP `26.7764` edge `0.0212` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.1152` n `228` status `ready` deltaP `7.4962` edge `0.1524` maxDD `-4.0887`
- `news_risk_high->crypto_major_1h` score `0.7764` n `30` status `ready` deltaP `9.8902` edge `0.0803` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.1896` n `30` status `ready` deltaP `5.3194` edge `0.035` maxDD `-1.6923`
- `news_risk_high->index_24h` score `0.0969` n `30` status `ready` deltaP `9.2361` edge `0.038` maxDD `-2.3058`
- `news_risk_high->metal_1h` score `-0.4024` n `30` status `ready` deltaP `1.6866` edge `-0.0262` maxDD `-1.2643`
- `market_context_high->equity_1h` score `-0.4122` n `228` status `ready` deltaP `3.7346` edge `0.0351` maxDD `-4.3608`
- `market_context_high->equity_24h` score `-0.4613` n `201` status `ready` deltaP `22.4761` edge `0.3485` maxDD `-31.2762`
- `market_context_high->metal_1h` score `-0.5041` n `228` status `ready` deltaP `2.3007` edge `-0.0001` maxDD `-2.0564`
- `market_context_high->commodity_1h` score `-0.5952` n `228` status `ready` deltaP `-0.5778` edge `0.0022` maxDD `-0.8358`
- `market_context_high->fx_1h` score `-0.782` n `228` status `ready` deltaP `-1.8201` edge `-0.0018` maxDD `-0.7655`
- `news_risk_high->index_1h` score `-1.0166` n `30` status `ready` deltaP `-9.1018` edge `-0.0182` maxDD `-1.1161`
- `market_context_high->commodity_4h` score `-1.077` n `228` status `ready` deltaP `-0.2327` edge `0.0` maxDD `-3.5888`
- `market_context_high->crypto_major_1h` score `-1.1388` n `228` status `ready` deltaP `2.2587` edge `0.0157` maxDD `-9.807`
- `market_context_high->index_1h` score `-1.1578` n `228` status `ready` deltaP `-1.2948` edge `0.0035` maxDD `-1.3078`
- `market_context_high->index_4h` score `-1.1987` n `228` status `ready` deltaP `-0.0374` edge `0.0153` maxDD `-3.165`
- `market_context_high->crypto_alt_1h` score `-1.2136` n `228` status `ready` deltaP `1.2843` edge `0.0111` maxDD `-9.3536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
