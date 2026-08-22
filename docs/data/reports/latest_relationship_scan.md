# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-22T16:36:35.159762+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14818`

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

- `market_context_high->unknown_1h` score `1.5479` n `149` status `ready` deltaP `6.8571` edge `0.106` maxDD `-0.4843`
- `market_context_high->unknown_4h` score `0.9037` n `147` status `ready` deltaP `18.5592` edge `-0.0045` maxDD `-0.5133`
- `market_context_high->fx_4h` score `0.0891` n `147` status `ready` deltaP `7.8117` edge `0.0096` maxDD `-0.3539`
- `market_context_high->index_1h` score `-0.0523` n `149` status `ready` deltaP `6.2985` edge `0.0044` maxDD `-0.9144`
- `market_context_high->fx_1h` score `-0.1114` n `149` status `ready` deltaP `2.566` edge `0.0045` maxDD `-0.2043`
- `market_context_high->metal_4h` score `-0.3174` n `147` status `ready` deltaP `7.8366` edge `-0.0171` maxDD `-1.5942`
- `market_context_high->equity_1h` score `-0.3291` n `149` status `ready` deltaP `4.8738` edge `0.0323` maxDD `-5.2257`
- `market_context_high->metal_1h` score `-0.3717` n `149` status `ready` deltaP `-0.1185` edge `-0.005` maxDD `-0.6822`
- `market_context_high->index_4h` score `-0.4664` n `147` status `ready` deltaP `4.8086` edge `0.0117` maxDD `-2.618`
- `market_context_high->commodity_4h` score `-0.8328` n `147` status `ready` deltaP `-3.3049` edge `0.0003` maxDD `-2.4692`
- `market_context_high->fx_24h` score `-1.0497` n `133` status `ready` deltaP `2.176` edge `0.0119` maxDD `-2.2121`
- `market_context_high->commodity_1h` score `-1.1399` n `149` status `ready` deltaP `-8.6213` edge `-0.0029` maxDD `-1.1941`
- `market_context_high->equity_4h` score `-1.6846` n `147` status `ready` deltaP `-0.7383` edge `0.0696` maxDD `-16.1188`
- `market_context_high->commodity_24h` score `-2.2883` n `133` status `ready` deltaP `-6.1155` edge `0.0334` maxDD `-4.666`
- `market_context_high->crypto_alt_4h` score `-2.3452` n `147` status `ready` deltaP `3.6274` edge `-0.0728` maxDD `-7.0785`
- `market_context_high->crypto_alt_1h` score `-2.4345` n `149` status `ready` deltaP `-2.0847` edge `-0.0395` maxDD `-7.9582`
- `market_context_high->crypto_major_1h` score `-3.4985` n `149` status `ready` deltaP `-4.7592` edge `-0.1121` maxDD `-7.8171`
- `market_context_high->index_24h` score `-4.4576` n `133` status `ready` deltaP `-8.1245` edge `-0.0366` maxDD `-21.1244`
- `market_context_high->metal_24h` score `-5.5121` n `133` status `ready` deltaP `-25.1985` edge `-0.2079` maxDD `-11.4635`
- `market_context_high->crypto_major_4h` score `-5.5593` n `147` status `ready` deltaP `-0.3723` edge `-0.3278` maxDD `-5.6395`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
