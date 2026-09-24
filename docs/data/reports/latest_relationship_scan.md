# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-24T03:37:28.135968+00:00`
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

- `market_context_high->unknown_1h` score `72.003` n `47` status `ready` deltaP `10.5651` edge `5.9369` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `37.2672` n `46` status `ready` deltaP `24.6453` edge `2.9569` maxDD `-0.5817`
- `market_context_high->crypto_alt_24h` score `21.7822` n `46` status `ready` deltaP `19.6181` edge `1.6844` maxDD `0.0`
- `market_context_high->equity_24h` score `21.595` n `46` status `ready` deltaP `22.0411` edge `1.6627` maxDD `-0.1382`
- `market_context_high->index_24h` score `7.2422` n `46` status `ready` deltaP `31.0689` edge `0.4051` maxDD `-0.03`
- `news_risk_high->crypto_alt_4h` score `4.9731` n `103` status `ready` deltaP `14.6889` edge `0.4163` maxDD `-5.9838`
- `news_risk_high->crypto_major_4h` score `4.6782` n `103` status `ready` deltaP `18.0426` edge `0.3273` maxDD `-2.619`
- `news_risk_high->crypto_major_24h` score `3.526` n `103` status `ready` deltaP `-3.0457` edge `1.2184` maxDD `-63.6743`
- `news_risk_high->crypto_alt_1h` score `2.5533` n `103` status `ready` deltaP `13.6068` edge `0.1711` maxDD `-1.5895`
- `market_context_high->index_4h` score `2.544` n `47` status `ready` deltaP `29.9105` edge `0.028` maxDD `-0.2323`
- `news_risk_high->commodity_24h` score `2.4067` n `103` status `ready` deltaP `23.2268` edge `0.1636` maxDD `-2.431`
- `market_context_high->metal_24h` score `2.3014` n `46` status `ready` deltaP `25.0453` edge `0.0482` maxDD `-0.2042`
- `news_risk_high->crypto_major_1h` score `2.066` n `103` status `ready` deltaP `16.002` edge `0.109` maxDD `-1.8141`
- `market_context_high->equity_4h` score `1.5792` n `47` status `ready` deltaP `12.5713` edge `0.0896` maxDD `-1.3444`
- `news_risk_high->fx_4h` score `1.5722` n `103` status `ready` deltaP `23.0716` edge `0.0408` maxDD `-0.421`
- `news_risk_high->fx_24h` score `1.2195` n `103` status `ready` deltaP `29.6639` edge `0.1217` maxDD `-1.7159`
- `market_context_high->index_1h` score `0.8445` n `47` status `ready` deltaP `13.4125` edge `0.0088` maxDD `-0.2275`
- `news_risk_high->metal_1h` score `0.6805` n `103` status `ready` deltaP `15.6517` edge `0.0117` maxDD `-0.7468`
- `market_context_high->equity_1h` score `0.6658` n `47` status `ready` deltaP `9.5203` edge `0.0323` maxDD `-1.5564`
- `news_risk_high->metal_4h` score `0.3826` n `103` status `ready` deltaP `15.0322` edge `0.0446` maxDD `-1.9941`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
