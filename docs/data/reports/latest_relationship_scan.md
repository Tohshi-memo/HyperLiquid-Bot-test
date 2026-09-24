# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-24T04:37:29.732078+00:00`
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

- `market_context_high->unknown_1h` score `72.2022` n `47` status `ready` deltaP `10.8645` edge `5.9515` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `38.0199` n `46` status `ready` deltaP `25.3397` edge `3.015` maxDD `-0.5817`
- `market_context_high->crypto_alt_24h` score `22.7006` n `46` status `ready` deltaP `20.3125` edge `1.7563` maxDD `0.0`
- `market_context_high->equity_24h` score `21.9745` n `46` status `ready` deltaP `22.7355` edge `1.6897` maxDD `-0.1382`
- `market_context_high->index_24h` score `7.3506` n `46` status `ready` deltaP `31.7633` edge `0.4095` maxDD `-0.03`
- `news_risk_high->crypto_alt_4h` score `5.0019` n `103` status `ready` deltaP `14.6889` edge `0.4187` maxDD `-5.9838`
- `news_risk_high->crypto_major_4h` score `4.7953` n `103` status `ready` deltaP `18.6523` edge `0.333` maxDD `-2.619`
- `news_risk_high->crypto_major_24h` score `4.2788` n `103` status `ready` deltaP `-2.3513` edge `1.2765` maxDD `-63.6743`
- `news_risk_high->crypto_alt_1h` score `2.6348` n `103` status `ready` deltaP `14.0559` edge `0.1749` maxDD `-1.5895`
- `market_context_high->index_4h` score `2.5854` n `47` status `ready` deltaP `30.3678` edge `0.0284` maxDD `-0.2323`
- `market_context_high->metal_24h` score `2.4518` n `46` status `ready` deltaP `25.7398` edge `0.0561` maxDD `-0.2042`
- `news_risk_high->commodity_24h` score `2.2791` n `103` status `ready` deltaP `22.5323` edge `0.1576` maxDD `-2.431`
- `news_risk_high->crypto_major_1h` score `2.1463` n `103` status `ready` deltaP `16.6008` edge `0.1117` maxDD `-1.8141`
- `market_context_high->equity_4h` score `1.6856` n `47` status `ready` deltaP `13.1811` edge `0.0944` maxDD `-1.3444`
- `news_risk_high->fx_4h` score `1.5734` n `103` status `ready` deltaP `23.0716` edge `0.0409` maxDD `-0.421`
- `news_risk_high->fx_24h` score `1.2242` n `103` status `ready` deltaP `29.6639` edge `0.1223` maxDD `-1.7159`
- `market_context_high->index_1h` score `0.8565` n `47` status `ready` deltaP `13.5622` edge `0.0088` maxDD `-0.2275`
- `market_context_high->equity_1h` score `0.6933` n `47` status `ready` deltaP `9.67` edge `0.0336` maxDD `-1.5564`
- `news_risk_high->metal_1h` score `0.6793` n `103` status `ready` deltaP `15.6517` edge `0.0116` maxDD `-0.7468`
- `news_risk_high->crypto_alt_24h` score `0.4385` n `103` status `ready` deltaP `-4.9302` edge `0.7707` maxDD `-49.7699`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
