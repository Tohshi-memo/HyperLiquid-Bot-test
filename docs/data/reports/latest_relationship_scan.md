# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-09T21:37:29.286736+00:00`
- Price records: `672`
- Market context records: `6220`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11110`

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

- `news_risk_high->crypto_alt_24h` score `13.2038` n `32` status `ready` deltaP `42.2194` edge `0.8336` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.485` n `32` status `ready` deltaP `55.9524` edge `0.1674` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.1379` n `32` status `ready` deltaP `43.3689` edge `0.0603` maxDD `-0.0345`
- `news_risk_high->crypto_major_24h` score `2.5039` n `32` status `ready` deltaP `15.625` edge `0.2948` maxDD `-4.2368`
- `news_risk_high->fx_1h` score `2.32` n `32` status `ready` deltaP `27.994` edge `0.0206` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `1.9736` n `192` status `ready` deltaP `1.9617` edge `0.2522` maxDD `-3.7317`
- `news_risk_high->crypto_major_1h` score `1.3821` n `32` status `ready` deltaP `14.128` edge `0.1297` maxDD `-2.0691`
- `news_risk_high->commodity_24h` score `1.2511` n `32` status `ready` deltaP `20.9396` edge `-0.0148` maxDD `-0.3101`
- `news_risk_high->crypto_alt_1h` score `0.7405` n `32` status `ready` deltaP `9.8241` edge `0.0756` maxDD `-1.6923`
- `market_context_high->unknown_4h` score `0.5901` n `192` status `ready` deltaP `-1.9944` edge `0.3157` maxDD `-11.925`
- `market_context_high->metal_24h` score `-0.047` n `192` status `ready` deltaP `19.8023` edge `0.1188` maxDD `-11.8809`
- `news_risk_high->index_24h` score `-0.2261` n `32` status `ready` deltaP `8.801` edge `-0.0005` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.3089` n `192` status `ready` deltaP `0.9107` edge `-0.0011` maxDD `-0.5659`
- `market_context_high->commodity_1h` score `-0.5967` n `192` status `ready` deltaP `-1.0479` edge `0.0019` maxDD `-0.5708`
- `market_context_high->metal_4h` score `-0.6607` n `192` status `ready` deltaP `3.3664` edge `0.0116` maxDD `-3.4996`
- `news_risk_high->metal_1h` score `-0.8096` n `32` status `ready` deltaP `-3.8922` edge `-0.0281` maxDD `-1.6464`
- `market_context_high->metal_1h` score `-0.9048` n `192` status `ready` deltaP `1.3161` edge `-0.0043` maxDD `-2.0564`
- `market_context_high->crypto_major_1h` score `-0.9176` n `192` status `ready` deltaP `4.2322` edge `0.0309` maxDD `-9.807`
- `market_context_high->crypto_alt_1h` score `-0.9232` n `192` status `ready` deltaP `4.0949` edge `0.0296` maxDD `-9.3536`
- `market_context_high->equity_4h` score `-1.0756` n `192` status `ready` deltaP `0.8384` edge `-0.0035` maxDD `-2.671`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
