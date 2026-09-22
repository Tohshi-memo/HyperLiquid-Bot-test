# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-22T06:37:32.286754+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9954`

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

- `market_context_high->unknown_4h` score `48.3562` n `46` status `ready` deltaP `7.3171` edge `3.9809` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `34.4238` n `46` status `ready` deltaP `21.173` edge `2.7431` maxDD `-0.5817`
- `market_context_high->crypto_alt_24h` score `19.1136` n `46` status `ready` deltaP `19.9653` edge `1.4597` maxDD `0.0`
- `market_context_high->equity_24h` score `16.9854` n `46` status `ready` deltaP `14.4022` edge `1.3295` maxDD `-0.1382`
- `news_risk_high->crypto_major_24h` score `6.7066` n `101` status `ready` deltaP `-4.1822` edge `1.2726` maxDD `-46.1999`
- `market_context_high->index_24h` score `5.6256` n `46` status `ready` deltaP `20.1314` edge `0.3433` maxDD `-0.03`
- `news_risk_high->commodity_24h` score `2.8695` n `101` status `ready` deltaP `35.3496` edge `0.2628` maxDD `-3.4467`
- `news_risk_high->crypto_alt_4h` score `2.6517` n `101` status `ready` deltaP `13.1263` edge `0.2544` maxDD `-7.675`
- `news_risk_high->crypto_alt_24h` score `2.6326` n `101` status `ready` deltaP `-3.7971` edge `0.7328` maxDD `-32.7147`
- `news_risk_high->crypto_alt_1h` score `2.2402` n `101` status `ready` deltaP `13.6865` edge `0.142` maxDD `-2.058`
- `news_risk_high->crypto_major_4h` score `2.1318` n `101` status `ready` deltaP `16.1751` edge `0.1956` maxDD `-8.0625`
- `market_context_high->index_4h` score `1.9931` n `46` status `ready` deltaP `23.4689` edge `0.023` maxDD `-0.0692`
- `news_risk_high->crypto_major_1h` score `1.564` n `101` status `ready` deltaP `15.3332` edge `0.0804` maxDD `-2.8494`
- `market_context_high->equity_4h` score `1.1848` n `46` status `ready` deltaP `8.4438` edge `0.0731` maxDD `-0.4529`
- `market_context_high->crypto_alt_4h` score `1.0961` n `46` status `ready` deltaP `8.8215` edge `0.092` maxDD `-2.7574`
- `market_context_high->equity_1h` score `0.9552` n `46` status `ready` deltaP `7.5111` edge `0.0538` maxDD `-0.2751`
- `news_risk_high->fx_4h` score `0.8849` n `101` status `ready` deltaP `15.5004` edge `0.034` maxDD `-0.421`
- `market_context_high->index_1h` score `0.6579` n `46` status `ready` deltaP `10.3554` edge `0.0111` maxDD `-0.0249`
- `news_risk_high->metal_1h` score `0.5478` n `101` status `ready` deltaP `13.8495` edge `0.0135` maxDD `-0.8144`
- `market_context_high->crypto_major_1h` score `0.4762` n `46` status `ready` deltaP `0.7616` edge `0.0869` maxDD `-2.1836`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
