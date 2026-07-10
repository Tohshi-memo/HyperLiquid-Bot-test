# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-10T13:52:33.785372+00:00`
- Price records: `672`
- Market context records: `6289`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11100`

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

- `news_risk_high->crypto_alt_24h` score `15.2118` n `32` status `ready` deltaP `43.2292` edge `0.9942` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `5.9617` n `32` status `ready` deltaP `50.5208` edge `0.16` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.1877` n `32` status `ready` deltaP `43.8262` edge `0.0614` maxDD `-0.0345`
- `news_risk_high->crypto_major_24h` score `4.1172` n `32` status `ready` deltaP `16.6667` edge `0.4947` maxDD `-4.2368`
- `news_risk_high->commodity_24h` score `2.8157` n `32` status `ready` deltaP `26.5625` edge `0.0781` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.3979` n `32` status `ready` deltaP `28.8922` edge `0.0211` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.4055` n `32` status `ready` deltaP `14.2777` edge `0.1317` maxDD `-2.0691`
- `market_context_high->unknown_1h` score `1.3554` n `206` status `ready` deltaP `-0.4258` edge `0.2166` maxDD `-3.7317`
- `news_risk_high->crypto_alt_1h` score `0.8769` n `32` status `ready` deltaP `11.4708` edge `0.0821` maxDD `-1.6923`
- `market_context_high->equity_4h` score `0.4171` n `194` status `ready` deltaP `7.5874` edge `0.0759` maxDD `-2.671`
- `market_context_high->unknown_4h` score `0.2926` n `194` status `ready` deltaP `-3.4479` edge `0.3006` maxDD `-11.925`
- `market_context_high->metal_4h` score `-0.2137` n `194` status `ready` deltaP `6.767` edge `0.0334` maxDD `-2.7056`
- `market_context_high->metal_24h` score `-0.2203` n `180` status `ready` deltaP `19.4097` edge `0.0992` maxDD `-11.8809`
- `news_risk_high->index_24h` score `-0.3089` n `32` status `ready` deltaP `7.1181` edge `0.0001` maxDD `-2.3058`
- `market_context_high->metal_1h` score `-0.4445` n `206` status `ready` deltaP `3.1306` edge `-0.0001` maxDD `-1.8877`
- `market_context_high->commodity_1h` score `-0.5981` n `206` status `ready` deltaP `0.0727` edge `0.0013` maxDD `-1.1298`
- `market_context_high->fx_1h` score `-0.6432` n `206` status `ready` deltaP `-0.9622` edge `-0.0017` maxDD `-0.639`
- `news_risk_high->metal_1h` score `-0.7146` n `32` status `ready` deltaP `-2.6946` edge `-0.0239` maxDD `-1.6464`
- `market_context_high->commodity_4h` score `-0.814` n `194` status `ready` deltaP `-3.2232` edge `0.0072` maxDD `-1.2054`
- `market_context_high->crypto_alt_1h` score `-0.8699` n `206` status `ready` deltaP `5.4939` edge `0.0271` maxDD `-9.3536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
