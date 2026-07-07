# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-07T06:52:32.997827+00:00`
- Price records: `672`
- Market context records: `5956`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11184`

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

- `news_risk_high->fx_24h` score `6.9366` n `30` status `ready` deltaP `63.3681` edge `0.1556` maxDD `0.0`
- `news_risk_high->commodity_24h` score `5.4126` n `30` status `ready` deltaP `38.9236` edge `0.2121` maxDD `-0.3101`
- `news_risk_high->fx_4h` score `3.871` n `30` status `ready` deltaP `40.1524` edge `0.0595` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.0945` n `30` status `ready` deltaP `25.2794` edge `0.0199` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.4688` n `225` status `ready` deltaP `9.4268` edge `0.169` maxDD `-4.0887`
- `news_risk_high->crypto_major_1h` score `0.8707` n `30` status `ready` deltaP `10.489` edge `0.0884` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.2356` n `30` status `ready` deltaP `5.6188` edge `0.0389` maxDD `-1.6923`
- `news_risk_high->index_24h` score `-0.1827` n `30` status `ready` deltaP `6.9791` edge `0.0172` maxDD `-2.3058`
- `market_context_high->equity_1h` score `-0.3355` n `237` status `ready` deltaP `5.0298` edge `0.0363` maxDD `-4.3608`
- `news_risk_high->metal_1h` score `-0.344` n `30` status `ready` deltaP `2.5848` edge `-0.0247` maxDD `-1.2643`
- `market_context_high->metal_1h` score `-0.4779` n `237` status `ready` deltaP `2.4161` edge `0.0025` maxDD `-2.0564`
- `market_context_high->equity_24h` score `-0.5541` n `213` status `ready` deltaP `20.4421` edge `0.3003` maxDD `-31.2762`
- `market_context_high->commodity_1h` score `-0.6071` n `237` status `ready` deltaP `-3.1374` edge `-0.0012` maxDD `-1.4578`
- `market_context_high->index_1h` score `-0.6264` n `237` status `ready` deltaP `0.9052` edge `0.005` maxDD `-1.3078`
- `market_context_high->fx_1h` score `-0.6494` n `237` status `ready` deltaP `-0.3746` edge `-0.0005` maxDD `-0.756`
- `news_risk_high->index_1h` score `-1.0921` n `30` status `ready` deltaP `-10.1497` edge `-0.0209` maxDD `-1.1161`
- `market_context_high->crypto_major_1h` score `-1.1066` n `237` status `ready` deltaP `2.008` edge `0.0215` maxDD `-9.807`
- `market_context_high->crypto_alt_1h` score `-1.1095` n `237` status `ready` deltaP `2.1167` edge `0.0189` maxDD `-9.3536`
- `market_context_high->metal_4h` score `-1.5598` n `225` status `ready` deltaP `-1.8367` edge `-0.0245` maxDD `-5.725`
- `market_context_high->commodity_4h` score `-1.6339` n `225` status `ready` deltaP `-3.4709` edge `-0.015` maxDD `-6.3734`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
