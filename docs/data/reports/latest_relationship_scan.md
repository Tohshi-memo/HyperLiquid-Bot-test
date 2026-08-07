# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-07T18:37:29.788216+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11773`

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

- `market_context_high->metal_24h` score `3.2295` n `95` status `ready` deltaP `14.6434` edge `0.2291` maxDD `-2.2743`
- `market_context_high->equity_24h` score `2.2065` n `95` status `ready` deltaP `-3.4507` edge `0.5337` maxDD `-21.1456`
- `market_context_high->fx_24h` score `1.5787` n `95` status `ready` deltaP `26.1847` edge `0.0573` maxDD `-2.6912`
- `market_context_high->commodity_4h` score `1.4639` n `109` status `ready` deltaP `14.8327` edge `0.0904` maxDD `-2.7169`
- `market_context_high->index_24h` score `0.7234` n `95` status `ready` deltaP `8.324` edge `0.1561` maxDD `-5.7715`
- `market_context_high->commodity_1h` score `0.4205` n `118` status `ready` deltaP `10.0705` edge `0.0261` maxDD `-1.1463`
- `market_context_high->fx_4h` score `0.1322` n `109` status `ready` deltaP `9.3113` edge `0.0076` maxDD `-1.6928`
- `market_context_high->fx_1h` score `-0.2131` n `118` status `ready` deltaP `5.3841` edge `-0.0041` maxDD `-0.9639`
- `market_context_high->index_4h` score `-0.5175` n `109` status `ready` deltaP `-0.1399` edge `-0.0049` maxDD `-1.1743`
- `market_context_high->index_1h` score `-0.7873` n `118` status `ready` deltaP `-1.9486` edge `-0.0109` maxDD `-1.3375`
- `market_context_high->metal_1h` score `-0.9302` n `118` status `ready` deltaP `-3.3949` edge `-0.0053` maxDD `-0.9664`
- `market_context_high->metal_4h` score `-0.9364` n `109` status `ready` deltaP `2.9397` edge `0.003` maxDD `-2.7169`
- `market_context_high->equity_1h` score `-1.1279` n `118` status `ready` deltaP `3.5827` edge `-0.0297` maxDD `-9.1031`
- `market_context_high->crypto_alt_1h` score `-1.5357` n `118` status `ready` deltaP `-6.3838` edge `-0.0225` maxDD `-2.3669`
- `market_context_high->crypto_alt_4h` score `-1.6133` n `109` status `ready` deltaP `-1.6727` edge `-0.0442` maxDD `-5.7857`
- `market_context_high->equity_4h` score `-1.6163` n `109` status `ready` deltaP `7.0556` edge `-0.048` maxDD `-7.6983`
- `market_context_high->crypto_major_24h` score `-3.1093` n `95` status `ready` deltaP `1.155` edge `-0.1569` maxDD `-14.2873`
- `market_context_high->crypto_major_1h` score `-3.1865` n `118` status `ready` deltaP `-8.0255` edge `-0.0665` maxDD `-8.3095`
- `market_context_high->crypto_alt_24h` score `-4.4781` n `95` status `ready` deltaP `-15.6548` edge `-0.1245` maxDD `-4.5445`
- `market_context_high->crypto_major_4h` score `-6.7336` n `109` status `ready` deltaP `-7.6485` edge `-0.1905` maxDD `-19.2378`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
