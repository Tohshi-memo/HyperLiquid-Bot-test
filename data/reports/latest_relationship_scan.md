# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-07T09:37:26.007438+00:00`
- Price records: `672`
- Market context records: `5968`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11242`

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

- `news_risk_high->fx_24h` score `7.123` n `30` status `ready` deltaP `65.2778` edge `0.1584` maxDD `0.0`
- `news_risk_high->commodity_24h` score `5.0978` n `30` status `ready` deltaP `37.0139` edge `0.1986` maxDD `-0.3101`
- `news_risk_high->fx_4h` score `3.8698` n `30` status `ready` deltaP `40.1524` edge `0.0594` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.1472` n `30` status `ready` deltaP `25.8782` edge `0.0203` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.525` n `235` status `ready` deltaP `9.7392` edge `0.1716` maxDD `-4.0887`
- `news_risk_high->crypto_major_1h` score `0.8497` n `30` status `ready` deltaP `10.3393` edge `0.0867` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.2239` n `30` status `ready` deltaP `5.6188` edge `0.0374` maxDD `-1.6923`
- `news_risk_high->index_24h` score `-0.0975` n `30` status `ready` deltaP `7.6736` edge `0.0235` maxDD `-2.3058`
- `news_risk_high->metal_1h` score `-0.3798` n `30` status `ready` deltaP `1.986` edge `-0.0253` maxDD `-1.2643`
- `market_context_high->equity_1h` score `-0.4286` n `245` status `ready` deltaP `3.6588` edge `0.0335` maxDD `-4.3608`
- `market_context_high->metal_1h` score `-0.4507` n `245` status `ready` deltaP `2.9384` edge `0.0025` maxDD `-2.0564`
- `market_context_high->commodity_1h` score `-0.5306` n `245` status `ready` deltaP `-1.9046` edge `0.0004` maxDD `-1.4578`
- `market_context_high->index_1h` score `-0.6689` n `245` status `ready` deltaP `0.1631` edge `0.0045` maxDD `-1.3078`
- `market_context_high->fx_1h` score `-0.6982` n `245` status `ready` deltaP `-0.9245` edge `-0.0009` maxDD `-0.756`
- `market_context_high->equity_24h` score `-0.9649` n `216` status `ready` deltaP `20.8912` edge `0.3046` maxDD `-31.2762`
- `market_context_high->index_4h` score `-1.0881` n `235` status `ready` deltaP `1.2351` edge `0.021` maxDD `-3.165`
- `news_risk_high->index_1h` score `-1.1093` n `30` status `ready` deltaP `-10.4491` edge `-0.0211` maxDD `-1.1161`
- `market_context_high->crypto_major_1h` score `-1.1123` n `245` status `ready` deltaP `2.108` edge `0.0201` maxDD `-9.807`
- `market_context_high->crypto_alt_1h` score `-1.161` n `245` status `ready` deltaP `1.6052` edge `0.0157` maxDD `-9.3536`
- `market_context_high->commodity_4h` score `-1.4118` n `235` status `ready` deltaP `-0.9555` edge `-0.0033` maxDD `-6.3734`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
