# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-23T17:22:36.890541+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9882`

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

- `market_context_high->unknown_1h` score `82.0999` n `47` status `ready` deltaP `9.8166` edge `6.7833` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `31.7897` n `46` status `ready` deltaP `17.5272` edge `2.5479` maxDD `-0.5817`
- `market_context_high->equity_24h` score `17.9847` n `46` status `ready` deltaP `14.923` edge `1.4093` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `14.302` n `46` status `ready` deltaP `12.5` edge `1.1085` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `7.0962` n `96` status `ready` deltaP `-5.2083` edge `1.3119` maxDD `-46.1999`
- `market_context_high->index_24h` score `6.0908` n `46` status `ready` deltaP `23.9508` edge `0.3566` maxDD `-0.03`
- `news_risk_high->crypto_major_4h` score `4.1058` n `103` status `ready` deltaP `16.2133` edge `0.2918` maxDD `-2.619`
- `news_risk_high->crypto_alt_4h` score `3.5681` n `103` status `ready` deltaP `11.0304` edge `0.3236` maxDD `-5.9838`
- `news_risk_high->commodity_24h` score `3.0781` n `96` status `ready` deltaP `28.125` edge `0.1869` maxDD `-2.431`
- `news_risk_high->crypto_alt_1h` score `2.2752` n `103` status `ready` deltaP `12.1098` edge `0.1579` maxDD `-1.5895`
- `market_context_high->index_4h` score `2.2597` n `47` status `ready` deltaP `27.1666` edge `0.0226` maxDD `-0.2323`
- `news_risk_high->crypto_major_1h` score `1.9713` n `103` status `ready` deltaP `15.5529` edge `0.1041` maxDD `-1.8141`
- `news_risk_high->crypto_alt_24h` score `1.4111` n `96` status `ready` deltaP `-7.2917` edge `0.6543` maxDD `-32.7147`
- `news_risk_high->fx_4h` score `1.3091` n `103` status `ready` deltaP `20.0228` edge `0.0392` maxDD `-0.421`
- `news_risk_high->fx_24h` score `1.1786` n `96` status `ready` deltaP `28.2986` edge `0.1214` maxDD `-1.7159`
- `market_context_high->equity_4h` score `0.7862` n `47` status `ready` deltaP `7.9981` edge `0.054` maxDD `-1.3444`
- `market_context_high->index_1h` score `0.7115` n `47` status `ready` deltaP `11.7658` edge `0.0087` maxDD `-0.2275`
- `news_risk_high->metal_1h` score `0.6542` n `103` status `ready` deltaP `15.2026` edge `0.0125` maxDD `-0.7468`
- `market_context_high->metal_24h` score `0.634` n `46` status `ready` deltaP `17.9273` edge `-0.0433` maxDD `-0.2042`
- `market_context_high->equity_1h` score `0.4429` n `47` status `ready` deltaP `7.4245` edge `0.0277` maxDD `-1.5564`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
