# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-08T04:52:24.635788+00:00`
- Price records: `672`
- Market context records: `6053`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11127`

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

- `news_risk_high->fx_24h` score `8.0355` n `30` status `ready` deltaP `72.0486` edge `0.1893` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.2381` n `30` status `ready` deltaP `43.811` edge `0.0657` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.2693` n `30` status `ready` deltaP `27.2255` edge `0.0215` maxDD `-0.1113`
- `news_risk_high->commodity_24h` score `1.9692` n `30` status `ready` deltaP `23.6459` edge `0.027` maxDD `-0.3101`
- `news_risk_high->crypto_alt_24h` score `1.8575` n `30` status `ready` deltaP `26.8402` edge `-0.0094` maxDD `-0.5131`
- `market_context_high->equity_4h` score `1.2875` n `206` status `ready` deltaP `7.727` edge `0.1475` maxDD `-2.671`
- `news_risk_high->crypto_major_1h` score `1.0313` n `30` status `ready` deltaP `11.5369` edge `0.102` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.4188` n `30` status `ready` deltaP `6.6667` edge `0.0554` maxDD `-1.6923`
- `news_risk_high->index_24h` score `0.1093` n `30` status `ready` deltaP `9.2361` edge `0.0396` maxDD `-2.3058`
- `market_context_high->metal_1h` score `-0.4695` n `206` status `ready` deltaP `2.6815` edge `0.0018` maxDD `-2.0564`
- `news_risk_high->metal_1h` score `-0.506` n `30` status `ready` deltaP `0.1896` edge `-0.0295` maxDD `-1.2643`
- `market_context_high->fx_1h` score `-0.563` n `206` status `ready` deltaP `0.0087` edge `-0.0013` maxDD `-0.6538`
- `market_context_high->commodity_1h` score `-0.6906` n `206` status `ready` deltaP `-1.8327` edge `-0.0007` maxDD `-0.5708`
- `market_context_high->crypto_major_1h` score `-0.7864` n `206` status `ready` deltaP `4.9997` edge `0.0426` maxDD `-9.807`
- `market_context_high->crypto_alt_1h` score `-0.7877` n `206` status `ready` deltaP `4.8544` edge `0.0419` maxDD `-9.3536`
- `market_context_high->equity_24h` score `-0.9148` n `192` status `ready` deltaP `25.0` edge `0.4978` maxDD `-46.5397`
- `market_context_high->index_4h` score `-1.0319` n `206` status `ready` deltaP `0.891` edge `0.0151` maxDD `-1.9335`
- `news_risk_high->index_1h` score `-1.0337` n `30` status `ready` deltaP `-9.2515` edge `-0.0194` maxDD `-1.1161`
- `market_context_high->equity_1h` score `-1.0685` n `206` status `ready` deltaP `0.6308` edge `0.0196` maxDD `-4.3608`
- `market_context_high->commodity_4h` score `-1.1535` n `206` status `ready` deltaP `-3.4262` edge `-0.0181` maxDD `-2.5555`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
