# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-24T00:07:26.882523+00:00`
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

- `market_context_high->unknown_1h` score `72.2322` n `47` status `ready` deltaP `10.5651` edge `5.956` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `35.2571` n `46` status `ready` deltaP `22.2147` edge `2.8056` maxDD `-0.5817`
- `market_context_high->equity_24h` score `20.4729` n `46` status `ready` deltaP `19.6105` edge `1.5854` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `19.1002` n `46` status `ready` deltaP `17.1875` edge `1.4771` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `9.601` n `97` status `ready` deltaP `-1.2726` edge `1.4944` maxDD `-46.1999`
- `market_context_high->index_24h` score `6.8918` n `46` status `ready` deltaP `28.6383` edge `0.3921` maxDD `-0.03`
- `news_risk_high->crypto_alt_24h` score `5.2095` n `97` status `ready` deltaP `-3.4311` edge `0.9451` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `4.8986` n `103` status `ready` deltaP `14.5365` edge `0.4111` maxDD `-5.9838`
- `news_risk_high->crypto_major_4h` score `4.6066` n `103` status `ready` deltaP `17.4328` edge `0.3254` maxDD `-2.619`
- `news_risk_high->crypto_alt_1h` score `2.5881` n `103` status `ready` deltaP `13.6068` edge `0.174` maxDD `-1.5895`
- `news_risk_high->commodity_24h` score `2.445` n `97` status `ready` deltaP `24.216` edge `0.1602` maxDD `-2.431`
- `market_context_high->index_4h` score `2.432` n `47` status `ready` deltaP `28.691` edge `0.0268` maxDD `-0.2323`
- `news_risk_high->crypto_major_1h` score `2.0181` n `103` status `ready` deltaP `15.7026` edge `0.107` maxDD `-1.8141`
- `market_context_high->metal_24h` score `1.7602` n `46` status `ready` deltaP `22.6148` edge `0.0193` maxDD `-0.2042`
- `news_risk_high->fx_4h` score `1.5978` n `103` status `ready` deltaP `23.3765` edge `0.0409` maxDD `-0.421`
- `market_context_high->equity_4h` score `1.3393` n `47` status `ready` deltaP `10.742` edge `0.0818` maxDD `-1.3444`
- `news_risk_high->fx_24h` score `1.1086` n `97` status `ready` deltaP `27.6221` edge `0.1211` maxDD `-1.7159`
- `news_risk_high->metal_24h` score `0.8061` n `97` status `ready` deltaP `18.6927` edge `0.0705` maxDD `-3.0086`
- `market_context_high->index_1h` score `0.7678` n `47` status `ready` deltaP `12.5143` edge `0.0084` maxDD `-0.2275`
- `news_risk_high->metal_1h` score `0.6422` n `103` status `ready` deltaP `15.3523` edge `0.0105` maxDD `-0.7468`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
