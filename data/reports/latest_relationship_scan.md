# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-04T03:07:27.505855+00:00`
- Price records: `672`
- Market context records: `5621`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8743`

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

- `market_context_high->equity_24h` score `3.0751` n `174` status `ready` deltaP `15.0084` edge `0.6641` maxDD `-31.6316`
- `market_context_high->fx_24h` score `1.3292` n `174` status `ready` deltaP `22.1325` edge `0.0606` maxDD `-1.457`
- `market_context_high->crypto_major_4h` score `0.9971` n `233` status `ready` deltaP `11.8706` edge `0.2332` maxDD `-14.0065`
- `market_context_high->equity_4h` score `0.4199` n `233` status `ready` deltaP `6.744` edge `0.1539` maxDD `-7.4425`
- `market_context_high->crypto_alt_4h` score `0.2276` n `233` status `ready` deltaP `6.6478` edge `0.1429` maxDD `-9.46`
- `market_context_high->fx_1h` score `-0.2797` n `237` status `ready` deltaP `1.5993` edge `0.0011` maxDD `-0.4764`
- `market_context_high->equity_1h` score `-0.3523` n `237` status `ready` deltaP `5.6154` edge `0.0339` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.5083` n `237` status `ready` deltaP `0.2924` edge `0.0004` maxDD `-2.0682`
- `market_context_high->crypto_major_1h` score `-0.5246` n `237` status `ready` deltaP `4.8795` edge `0.0483` maxDD `-6.9639`
- `market_context_high->crypto_alt_1h` score `-0.6153` n `237` status `ready` deltaP `1.137` edge `0.0373` maxDD `-5.0257`
- `market_context_high->index_1h` score `-0.9178` n `237` status `ready` deltaP `0.7283` edge `0.0055` maxDD `-0.9472`
- `market_context_high->commodity_1h` score `-1.0704` n `237` status `ready` deltaP `-1.0277` edge `-0.0058` maxDD `-3.7906`
- `market_context_high->fx_4h` score `-1.3277` n `233` status `ready` deltaP `0.9323` edge `0.0065` maxDD `-1.3012`
- `market_context_high->index_4h` score `-1.8331` n `233` status `ready` deltaP `-0.0504` edge `0.0097` maxDD `-2.9695`
- `market_context_high->index_24h` score `-2.3824` n `174` status `ready` deltaP `10.0874` edge `0.026` maxDD `-16.8946`
- `market_context_high->crypto_major_24h` score `-2.7024` n `174` status `ready` deltaP `7.5491` edge `0.1785` maxDD `-29.6555`
- `market_context_high->metal_4h` score `-2.8608` n `233` status `ready` deltaP `-11.1765` edge `-0.0539` maxDD `-11.7351`
- `market_context_high->commodity_4h` score `-4.1043` n `233` status `ready` deltaP `-5.2758` edge `-0.0393` maxDD `-14.071`
- `market_context_high->metal_24h` score `-8.2717` n `174` status `ready` deltaP `-10.9315` edge `-0.2515` maxDD `-32.8874`
- `market_context_high->crypto_alt_24h` score `-12.5049` n `174` status `ready` deltaP `-2.664` edge `-0.1546` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
