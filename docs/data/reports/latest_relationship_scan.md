# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-10T02:37:25.202792+00:00`
- Price records: `672`
- Market context records: `6241`
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

- `news_risk_high->crypto_alt_24h` score `14.075` n `32` status `ready` deltaP `42.2194` edge `0.9062` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.1797` n `32` status `ready` deltaP `52.7211` edge `0.1635` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.2023` n `32` status `ready` deltaP `43.9787` edge `0.0616` maxDD `-0.0345`
- `news_risk_high->crypto_major_24h` score `3.17` n `32` status `ready` deltaP `15.625` edge `0.3802` maxDD `-4.2368`
- `news_risk_high->fx_1h` score `2.338` n `32` status `ready` deltaP `28.1437` edge `0.0211` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `2.2387` n `192` status `ready` deltaP `2.2611` edge `0.2723` maxDD `-3.7317`
- `news_risk_high->commodity_24h` score `2.0236` n `32` status `ready` deltaP `24.341` edge `0.0269` maxDD `-0.3101`
- `market_context_high->unknown_4h` score `1.8796` n `192` status `ready` deltaP `0.4446` edge `0.4069` maxDD `-11.925`
- `news_risk_high->crypto_major_1h` score `1.3368` n `32` status `ready` deltaP `14.128` edge `0.1239` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.7483` n `32` status `ready` deltaP `10.4229` edge `0.0726` maxDD `-1.6923`
- `market_context_high->metal_24h` score `-0.0728` n `192` status `ready` deltaP `19.8023` edge `0.1155` maxDD `-11.8809`
- `news_risk_high->index_24h` score `-0.173` n `32` status `ready` deltaP `8.801` edge `0.0063` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.2972` n `192` status `ready` deltaP `1.0604` edge `-0.0006` maxDD `-0.5659`
- `market_context_high->metal_4h` score `-0.5109` n `192` status `ready` deltaP `4.281` edge `0.0247` maxDD `-3.4996`
- `market_context_high->equity_4h` score `-0.6724` n `192` status `ready` deltaP `2.6677` edge `0.0179` maxDD `-2.671`
- `market_context_high->commodity_1h` score `-0.6841` n `192` status `ready` deltaP `-2.0958` edge `0.0016` maxDD `-0.5708`
- `news_risk_high->metal_1h` score `-0.7893` n `32` status `ready` deltaP `-3.5928` edge `-0.0275` maxDD `-1.6464`
- `market_context_high->metal_1h` score `-0.8736` n `192` status `ready` deltaP `1.6155` edge `-0.0037` maxDD `-2.0564`
- `market_context_high->crypto_alt_1h` score `-0.9154` n `192` status `ready` deltaP `4.6937` edge `0.0266` maxDD `-9.3536`
- `market_context_high->crypto_major_1h` score `-0.9628` n `192` status `ready` deltaP `4.2322` edge `0.0251` maxDD `-9.807`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
