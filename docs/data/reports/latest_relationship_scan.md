# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-24T02:07:31.721207+00:00`
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

- `market_context_high->unknown_1h` score `72.1865` n `47` status `ready` deltaP `10.8645` edge `5.9502` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `36.3378` n `46` status `ready` deltaP `23.6036` edge `2.8864` maxDD `-0.5817`
- `market_context_high->equity_24h` score `21.1048` n `46` status `ready` deltaP `20.9994` edge `1.6288` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `20.5733` n `46` status `ready` deltaP `18.5764` edge `1.5906` maxDD `0.0`
- `market_context_high->index_24h` score `7.0893` n `46` status `ready` deltaP `30.0272` edge `0.3993` maxDD `-0.03`
- `news_risk_high->crypto_major_24h` score `5.5261` n `101` status `ready` deltaP `-2.7417` edge `1.2867` maxDD `-55.9664`
- `news_risk_high->crypto_alt_4h` score `4.9671` n `103` status `ready` deltaP `14.6889` edge `0.4158` maxDD `-5.9838`
- `news_risk_high->crypto_major_4h` score `4.5958` n `103` status `ready` deltaP `17.4328` edge `0.3245` maxDD `-2.619`
- `news_risk_high->crypto_alt_1h` score `2.6205` n `103` status `ready` deltaP `13.7565` edge `0.1757` maxDD `-1.5895`
- `market_context_high->index_4h` score `2.4722` n `47` status `ready` deltaP `29.1483` edge `0.0271` maxDD `-0.2323`
- `news_risk_high->commodity_24h` score `2.4687` n `101` status `ready` deltaP `23.807` edge `0.1649` maxDD `-2.431`
- `news_risk_high->crypto_major_1h` score `2.0828` n `103` status `ready` deltaP `16.002` edge `0.1104` maxDD `-1.8141`
- `market_context_high->metal_24h` score `2.0789` n `46` status `ready` deltaP `24.0037` edge `0.0366` maxDD `-0.2042`
- `news_risk_high->fx_4h` score `1.599` n `103` status `ready` deltaP `23.3765` edge `0.041` maxDD `-0.421`
- `market_context_high->equity_4h` score `1.4449` n `47` status `ready` deltaP `11.6567` edge `0.0845` maxDD `-1.3444`
- `news_risk_high->crypto_alt_24h` score `1.3155` n `101` status `ready` deltaP `-5.186` edge `0.7456` maxDD `-41.7791`
- `news_risk_high->fx_24h` score `1.1855` n `101` status `ready` deltaP `29.0102` edge `0.1217` maxDD `-1.7159`
- `market_context_high->index_1h` score `0.793` n `47` status `ready` deltaP `12.8137` edge `0.0085` maxDD `-0.2275`
- `news_risk_high->metal_1h` score `0.6494` n `103` status `ready` deltaP `15.3523` edge `0.0111` maxDD `-0.7468`
- `market_context_high->equity_1h` score `0.6011` n `47` status `ready` deltaP `8.9215` edge `0.0309` maxDD `-1.5564`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
