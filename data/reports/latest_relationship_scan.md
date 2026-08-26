# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-26T12:07:25.371217+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14760`

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

- `news_risk_high->unknown_24h` score `44.7942` n `53` status `ready` deltaP `11.6319` edge `3.6553` maxDD `0.0`
- `news_risk_high->unknown_4h` score `12.018` n `53` status `ready` deltaP `24.0652` edge `0.851` maxDD `-0.1281`
- `news_risk_high->crypto_alt_24h` score `9.5629` n `53` status `ready` deltaP `30.9486` edge `0.6347` maxDD `-2.8629`
- `news_risk_high->equity_24h` score `7.0171` n `53` status `ready` deltaP `29.7661` edge `0.4794` maxDD `-4.7801`
- `news_risk_high->index_24h` score `4.0421` n `53` status `ready` deltaP `40.114` edge `0.0846` maxDD `-0.2147`
- `news_risk_high->fx_4h` score `2.8877` n `53` status `ready` deltaP `34.8108` edge `0.022` maxDD `-0.0746`
- `news_risk_high->unknown_1h` score `2.7375` n `53` status `ready` deltaP `15.2638` edge `0.1619` maxDD `-0.8426`
- `market_context_high->unknown_4h` score `2.6511` n `136` status `ready` deltaP `22.3727` edge `0.1126` maxDD `-0.5994`
- `news_risk_high->metal_24h` score `1.7828` n `53` status `ready` deltaP `29.1896` edge `-0.0418` maxDD `-0.0053`
- `news_risk_high->equity_4h` score `1.7501` n `53` status `ready` deltaP `19.889` edge `0.0903` maxDD `-2.164`
- `news_risk_high->fx_1h` score `1.0638` n `53` status `ready` deltaP `15.0209` edge `0.0055` maxDD `-0.0257`
- `market_context_high->unknown_1h` score `1.0559` n `136` status `ready` deltaP `11.3376` edge `0.0573` maxDD `-1.5916`
- `news_risk_high->equity_1h` score `0.4607` n `53` status `ready` deltaP `12.7754` edge `0.0103` maxDD `-0.9128`
- `news_risk_high->commodity_1h` score `0.4428` n `53` status `ready` deltaP `10.8265` edge `-0.004` maxDD `-0.5024`
- `news_risk_high->index_4h` score `0.1997` n `53` status `ready` deltaP `7.2711` edge `0.0079` maxDD `-0.1788`
- `news_risk_high->index_1h` score `-0.0674` n `53` status `ready` deltaP `3.8499` edge `0.001` maxDD `-0.1583`
- `news_risk_high->metal_4h` score `-0.2542` n `53` status `ready` deltaP `6.0343` edge `-0.0083` maxDD `-0.249`
- `news_risk_high->metal_1h` score `-0.3624` n `53` status `ready` deltaP `0.2853` edge `-0.0095` maxDD `-0.1413`
- `market_context_high->fx_1h` score `-0.4473` n `136` status `ready` deltaP `2.5625` edge `-0.0012` maxDD `-0.8587`
- `news_risk_high->commodity_4h` score `-0.9519` n `53` status `ready` deltaP `-0.7536` edge `0.0063` maxDD `-1.1986`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
