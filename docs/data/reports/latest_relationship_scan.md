# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-10T14:22:32.871660+00:00`
- Price records: `672`
- Market context records: `6291`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11116`

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

- `news_risk_high->crypto_alt_24h` score `15.2046` n `32` status `ready` deltaP `43.2292` edge `0.9936` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `5.9653` n `32` status `ready` deltaP `50.5208` edge `0.1603` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.1889` n `32` status `ready` deltaP `43.8262` edge `0.0615` maxDD `-0.0345`
- `news_risk_high->crypto_major_24h` score `4.1149` n `32` status `ready` deltaP `16.6667` edge `0.4944` maxDD `-4.2368`
- `news_risk_high->commodity_24h` score `2.8819` n `32` status `ready` deltaP `26.9097` edge `0.0813` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.3991` n `32` status `ready` deltaP `28.8922` edge `0.0212` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.4101` n `32` status `ready` deltaP `14.2777` edge `0.1323` maxDD `-2.0691`
- `market_context_high->unknown_1h` score `1.3117` n `206` status `ready` deltaP `-0.7616` edge `0.2152` maxDD `-3.7317`
- `news_risk_high->crypto_alt_1h` score `0.8924` n `32` status `ready` deltaP `11.6205` edge `0.0831` maxDD `-1.6923`
- `market_context_high->equity_4h` score `0.3835` n `194` status `ready` deltaP `7.5874` edge `0.0731` maxDD `-2.671`
- `market_context_high->unknown_4h` score `0.1145` n `194` status `ready` deltaP `-4.174` edge `0.2906` maxDD `-11.925`
- `market_context_high->metal_4h` score `-0.1448` n `194` status `ready` deltaP `7.4931` edge `0.0343` maxDD `-2.7056`
- `market_context_high->metal_24h` score `-0.1853` n `178` status `ready` deltaP `19.9789` edge `0.0999` maxDD `-11.8809`
- `news_risk_high->index_24h` score `-0.3195` n `32` status `ready` deltaP `6.9444` edge `-0.0001` maxDD `-2.3058`
- `market_context_high->metal_1h` score `-0.4201` n `206` status `ready` deltaP `3.4664` edge `0.0008` maxDD `-1.8877`
- `market_context_high->commodity_1h` score `-0.444` n `206` status `ready` deltaP `0.0727` edge `0.0002` maxDD `-1.6086`
- `market_context_high->fx_1h` score `-0.6583` n `206` status `ready` deltaP `-0.9622` edge `-0.0019` maxDD `-0.7232`
- `news_risk_high->metal_1h` score `-0.7255` n `32` status `ready` deltaP `-2.8443` edge `-0.0243` maxDD `-1.6464`
- `market_context_high->commodity_4h` score `-0.8304` n `194` status `ready` deltaP `-3.2232` edge `0.0051` maxDD `-1.2054`
- `market_context_high->index_1h` score `-0.8769` n `206` status `ready` deltaP `-3.9605` edge `0.0009` maxDD `-0.9531`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
