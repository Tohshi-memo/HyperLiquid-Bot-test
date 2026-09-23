# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-23T02:37:26.027431+00:00`
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

- `market_context_high->unknown_4h` score `46.0386` n `46` status `ready` deltaP `7.0122` edge `3.7898` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `29.6871` n `46` status `ready` deltaP `13.5341` edge `2.3993` maxDD `-0.5817`
- `market_context_high->equity_24h` score `16.5577` n `46` status `ready` deltaP `12.1453` edge `1.3089` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `12.9708` n `46` status `ready` deltaP `10.5903` edge `1.0103` maxDD `0.0`
- `market_context_high->index_24h` score `5.5987` n `46` status `ready` deltaP `20.305` edge `0.3399` maxDD `-0.03`
- `news_risk_high->crypto_major_24h` score `4.9935` n `96` status `ready` deltaP `-9.2014` edge `1.1633` maxDD `-46.1999`
- `news_risk_high->commodity_24h` score `4.5318` n `96` status `ready` deltaP `34.8958` edge `0.2629` maxDD `-2.431`
- `news_risk_high->crypto_major_4h` score `2.8902` n `97` status `ready` deltaP `14.2177` edge `0.2038` maxDD `-2.619`
- `news_risk_high->crypto_alt_4h` score `2.3` n `97` status `ready` deltaP `9.3396` edge `0.2292` maxDD `-5.9838`
- `market_context_high->index_4h` score `2.0151` n `46` status `ready` deltaP `23.7738` edge `0.0228` maxDD `-0.0692`
- `news_risk_high->crypto_alt_1h` score `1.6194` n `99` status `ready` deltaP `10.3022` edge `0.1153` maxDD `-1.5895`
- `news_risk_high->fx_4h` score `1.3973` n `97` status `ready` deltaP `20.661` edge `0.0423` maxDD `-0.421`
- `news_risk_high->crypto_major_1h` score `1.2761` n `99` status `ready` deltaP `12.5477` edge `0.0662` maxDD `-1.8141`
- `news_risk_high->fx_24h` score `0.8585` n `96` status `ready` deltaP `23.6111` edge `0.1116` maxDD `-1.7159`
- `market_context_high->equity_1h` score `0.7586` n `46` status `ready` deltaP `6.4632` edge `0.0444` maxDD `-0.2751`
- `market_context_high->index_1h` score `0.6794` n `46` status `ready` deltaP `10.6548` edge `0.0109` maxDD `-0.0249`
- `news_risk_high->metal_1h` score `0.5845` n `99` status `ready` deltaP `14.6465` edge `0.0104` maxDD `-0.7468`
- `market_context_high->metal_24h` score `0.4973` n `46` status `ready` deltaP `18.2745` edge `-0.057` maxDD `-0.2042`
- `market_context_high->equity_4h` score `0.4951` n `46` status `ready` deltaP `4.0231` edge `0.0451` maxDD `-0.4529`
- `news_risk_high->metal_4h` score `0.3657` n `97` status `ready` deltaP `13.2355` edge `0.038` maxDD `-1.9941`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
