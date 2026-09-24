# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-24T04:22:30.860827+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9858`

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

- `market_context_high->unknown_1h` score `72.1037` n `47` status `ready` deltaP `10.8645` edge `5.9433` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `37.826` n `46` status `ready` deltaP `25.1661` edge `3.0` maxDD `-0.5817`
- `market_context_high->crypto_alt_24h` score `22.4815` n `46` status `ready` deltaP `20.1389` edge `1.7392` maxDD `0.0`
- `market_context_high->equity_24h` score `21.8778` n `46` status `ready` deltaP `22.5619` edge `1.6828` maxDD `-0.1382`
- `market_context_high->index_24h` score `7.3235` n `46` status `ready` deltaP `31.5897` edge `0.4084` maxDD `-0.03`
- `news_risk_high->crypto_alt_4h` score `4.9971` n `103` status `ready` deltaP `14.6889` edge `0.4183` maxDD `-5.9838`
- `news_risk_high->crypto_major_4h` score `4.7639` n `103` status `ready` deltaP `18.4999` edge `0.3314` maxDD `-2.619`
- `news_risk_high->crypto_major_24h` score `4.0849` n `103` status `ready` deltaP `-2.5249` edge `1.2615` maxDD `-63.6743`
- `news_risk_high->crypto_alt_1h` score `2.6336` n `103` status `ready` deltaP `14.0559` edge `0.1748` maxDD `-1.5895`
- `market_context_high->index_4h` score `2.572` n `47` status `ready` deltaP `30.2154` edge `0.0283` maxDD `-0.2323`
- `market_context_high->metal_24h` score `2.4151` n `46` status `ready` deltaP `25.5662` edge `0.0542` maxDD `-0.2042`
- `news_risk_high->commodity_24h` score `2.311` n `103` status `ready` deltaP `22.7059` edge `0.1591` maxDD `-2.431`
- `news_risk_high->crypto_major_1h` score `2.1332` n `103` status `ready` deltaP `16.4511` edge `0.1116` maxDD `-1.8141`
- `market_context_high->equity_4h` score `1.6566` n `47` status `ready` deltaP `13.0286` edge `0.093` maxDD `-1.3444`
- `news_risk_high->fx_4h` score `1.5722` n `103` status `ready` deltaP `23.0716` edge `0.0408` maxDD `-0.421`
- `news_risk_high->fx_24h` score `1.2234` n `103` status `ready` deltaP `29.6639` edge `0.1222` maxDD `-1.7159`
- `market_context_high->index_1h` score `0.8565` n `47` status `ready` deltaP `13.5622` edge `0.0088` maxDD `-0.2275`
- `market_context_high->equity_1h` score `0.6945` n `47` status `ready` deltaP `9.67` edge `0.0337` maxDD `-1.5564`
- `news_risk_high->metal_1h` score `0.6925` n `103` status `ready` deltaP `15.8014` edge `0.0117` maxDD `-0.7468`
- `news_risk_high->metal_4h` score `0.4055` n `103` status `ready` deltaP `15.3371` edge `0.0455` maxDD `-1.9941`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
