# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-23T01:37:32.765419+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9740`

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

- `market_context_high->unknown_4h` score `45.9102` n `46` status `ready` deltaP `7.0122` edge `3.7791` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `29.6883` n `46` status `ready` deltaP `13.5341` edge `2.3994` maxDD `-0.5817`
- `market_context_high->equity_24h` score `16.4545` n `46` status `ready` deltaP `12.1453` edge `1.3003` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `13.008` n `46` status `ready` deltaP `10.5903` edge `1.0134` maxDD `0.0`
- `market_context_high->index_24h` score `5.5287` n `46` status `ready` deltaP `19.6105` edge `0.3387` maxDD `-0.03`
- `news_risk_high->crypto_major_24h` score `4.9947` n `96` status `ready` deltaP `-9.2014` edge `1.1634` maxDD `-46.1999`
- `news_risk_high->commodity_24h` score `4.6028` n `96` status `ready` deltaP `35.2431` edge `0.2665` maxDD `-2.431`
- `news_risk_high->crypto_major_4h` score `2.9132` n `97` status `ready` deltaP `14.3701` edge `0.2047` maxDD `-2.619`
- `news_risk_high->crypto_alt_4h` score `2.3314` n `97` status `ready` deltaP `9.4921` edge `0.2308` maxDD `-5.9838`
- `market_context_high->index_4h` score `1.9507` n `46` status `ready` deltaP `23.1641` edge `0.0215` maxDD `-0.0692`
- `news_risk_high->crypto_alt_1h` score `1.809` n `97` status `ready` deltaP `10.4713` edge `0.1205` maxDD `-1.1645`
- `news_risk_high->fx_4h` score `1.3827` n `97` status `ready` deltaP `20.5086` edge `0.0421` maxDD `-0.421`
- `news_risk_high->crypto_major_1h` score `1.3624` n `97` status `ready` deltaP `12.7169` edge `0.0681` maxDD `-1.8141`
- `news_risk_high->fx_24h` score `0.8295` n `96` status `ready` deltaP `23.2639` edge `0.1102` maxDD `-1.7159`
- `news_risk_high->metal_1h` score `0.6588` n `97` status `ready` deltaP `15.3806` edge `0.0117` maxDD `-0.7468`
- `market_context_high->equity_1h` score `0.6579` n `46` status `ready` deltaP `5.8644` edge `0.04` maxDD `-0.2751`
- `market_context_high->index_1h` score `0.6243` n `46` status `ready` deltaP `10.056` edge `0.0103` maxDD `-0.0249`
- `market_context_high->metal_24h` score `0.5347` n `46` status `ready` deltaP `18.6217` edge `-0.0562` maxDD `-0.2042`
- `market_context_high->equity_4h` score `0.3659` n `46` status `ready` deltaP `3.4133` edge `0.0384` maxDD `-0.4529`
- `news_risk_high->fx_1h` score `0.3311` n `97` status `ready` deltaP `9.0962` edge `0.0113` maxDD `-0.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
