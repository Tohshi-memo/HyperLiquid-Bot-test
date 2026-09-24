# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-24T06:22:31.235808+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9897`

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

- `market_context_high->unknown_1h` score `66.2106` n `47` status `ready` deltaP `10.5651` edge `5.4542` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `39.2427` n `46` status `ready` deltaP `26.555` edge `3.1088` maxDD `-0.5817`
- `market_context_high->crypto_alt_24h` score `24.113` n `46` status `ready` deltaP `21.5278` edge `1.8659` maxDD `0.0`
- `market_context_high->equity_24h` score `22.6741` n `46` status `ready` deltaP `23.9508` edge `1.7399` maxDD `-0.1382`
- `market_context_high->index_24h` score `7.5534` n `46` status `ready` deltaP `32.9786` edge `0.4183` maxDD `-0.03`
- `news_risk_high->crypto_major_24h` score `5.5016` n `103` status `ready` deltaP `-1.136` edge `1.3703` maxDD `-63.6743`
- `news_risk_high->crypto_alt_4h` score `4.8855` n `103` status `ready` deltaP `14.6889` edge `0.409` maxDD `-5.9838`
- `news_risk_high->crypto_major_4h` score `4.8111` n `103` status `ready` deltaP `18.8048` edge `0.3333` maxDD `-2.619`
- `market_context_high->metal_24h` score `2.7194` n `46` status `ready` deltaP `26.9551` edge `0.0703` maxDD `-0.2042`
- `market_context_high->index_4h` score `2.6923` n `47` status `ready` deltaP `31.4349` edge `0.0302` maxDD `-0.2323`
- `news_risk_high->crypto_alt_1h` score `2.4701` n `107` status `ready` deltaP `13.4661` edge `0.1651` maxDD `-1.5895`
- `news_risk_high->commodity_24h` score `2.0547` n `103` status `ready` deltaP `21.3171` edge `0.147` maxDD `-2.431`
- `news_risk_high->crypto_major_1h` score `1.9888` n `107` status `ready` deltaP `15.5619` edge `0.1055` maxDD `-1.8141`
- `market_context_high->equity_4h` score `1.8946` n `47` status `ready` deltaP `14.2481` edge `0.1047` maxDD `-1.3444`
- `news_risk_high->crypto_alt_24h` score `1.8509` n `103` status `ready` deltaP `-3.7149` edge `0.8803` maxDD `-49.7699`
- `news_risk_high->fx_4h` score `1.6038` n `103` status `ready` deltaP `23.3765` edge `0.0414` maxDD `-0.421`
- `news_risk_high->fx_24h` score `1.2304` n `103` status `ready` deltaP `29.6639` edge `0.1231` maxDD `-1.7159`
- `market_context_high->index_1h` score `0.8732` n `47` status `ready` deltaP `13.7119` edge `0.0092` maxDD `-0.2275`
- `market_context_high->equity_1h` score `0.7041` n `47` status `ready` deltaP `9.67` edge `0.0345` maxDD `-1.5564`
- `news_risk_high->metal_1h` score `0.5821` n `107` status `ready` deltaP `14.5265` edge `0.011` maxDD `-0.7468`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
