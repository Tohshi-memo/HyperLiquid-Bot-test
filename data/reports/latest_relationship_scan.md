# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-18T13:07:24.813924+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11633`

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

- `market_context_high->crypto_major_24h` score `2.357` n `87` status `ready` deltaP `9.0002` edge `0.2572` maxDD `-4.9964`
- `market_context_high->commodity_24h` score `1.6335` n `87` status `ready` deltaP `17.8569` edge `0.2737` maxDD `-4.666`
- `market_context_high->equity_1h` score `1.0736` n `96` status `ready` deltaP `9.6121` edge `0.0558` maxDD `-0.4329`
- `market_context_high->metal_4h` score `0.7201` n `96` status `ready` deltaP `14.2784` edge `0.0224` maxDD `-1.273`
- `market_context_high->index_1h` score `0.6611` n `96` status `ready` deltaP `12.9179` edge `0.0077` maxDD `-0.0982`
- `market_context_high->crypto_major_4h` score `0.5944` n `96` status `ready` deltaP `9.0193` edge `0.0915` maxDD `-3.1677`
- `market_context_high->unknown_1h` score `0.5424` n `96` status `ready` deltaP `9.3563` edge `0.0055` maxDD `-0.4807`
- `market_context_high->crypto_alt_4h` score `0.3176` n `96` status `ready` deltaP `9.9085` edge `0.0874` maxDD `-5.4926`
- `market_context_high->equity_4h` score `0.0697` n `96` status `ready` deltaP `2.7693` edge `0.0778` maxDD `-2.5696`
- `market_context_high->metal_1h` score `-0.0717` n `96` status `ready` deltaP `3.7238` edge `0.0079` maxDD `-0.4291`
- `market_context_high->fx_4h` score `-0.1902` n `96` status `ready` deltaP `3.8363` edge `0.0003` maxDD `-0.3539`
- `market_context_high->unknown_24h` score `-0.2382` n `87` status `ready` deltaP `12.3309` edge `-0.0837` maxDD `-0.1352`
- `market_context_high->commodity_4h` score `-0.371` n `96` status `ready` deltaP `4.0905` edge `0.0102` maxDD `-2.4692`
- `market_context_high->crypto_alt_1h` score `-0.3885` n `96` status `ready` deltaP `1.9274` edge `0.0175` maxDD `-2.413`
- `market_context_high->fx_1h` score `-0.4545` n `96` status `ready` deltaP `-3.5679` edge `0.0014` maxDD `-0.2043`
- `market_context_high->crypto_major_1h` score `-0.478` n `96` status `ready` deltaP `1.3348` edge `0.0143` maxDD `-2.7581`
- `market_context_high->index_4h` score `-0.6079` n `96` status `ready` deltaP `0.6351` edge `0.0106` maxDD `-0.5728`
- `market_context_high->commodity_1h` score `-0.8658` n `96` status `ready` deltaP `-7.2917` edge `-0.0058` maxDD `-1.1941`
- `market_context_high->metal_24h` score `-2.1265` n `87` status `ready` deltaP `-7.5659` edge `0.0193` maxDD `-7.3195`
- `market_context_high->fx_24h` score `-4.6078` n `87` status `ready` deltaP `-30.8651` edge `-0.0301` maxDD `-1.1825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
