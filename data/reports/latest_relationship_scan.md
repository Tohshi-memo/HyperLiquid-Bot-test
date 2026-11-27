# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-27T01:52:26.877963+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3540`

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

- `news_risk_high->unknown_1h` score `3210.8268` n `31` status `ready` deltaP `1.7819` edge `267.5746` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3175.1178` n `31` status `ready` deltaP `4.3962` edge `264.5695` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `26.0969` n `31` status `ready` deltaP `34.8958` edge `1.9421` maxDD `0.0`
- `news_risk_high->equity_24h` score `23.2472` n `31` status `ready` deltaP `34.375` edge `1.7081` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `20.0082` n `31` status `ready` deltaP `34.0278` edge `1.4405` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `9.483` n `31` status `ready` deltaP `23.7116` edge `0.7192` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `8.176` n `31` status `ready` deltaP `34.6332` edge `0.4985` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `6.2364` n `31` status `ready` deltaP `16.9305` edge `0.8284` maxDD `-7.6714`
- `news_risk_high->metal_24h` score `6.1607` n `31` status `ready` deltaP `21.791` edge `0.3956` maxDD `-0.1986`
- `news_risk_high->fx_24h` score `4.9592` n `31` status `ready` deltaP `42.0587` edge `0.1457` maxDD `-0.0262`
- `news_risk_high->index_24h` score `4.1182` n `31` status `ready` deltaP `35.9375` edge `0.1036` maxDD `0.0`
- `news_risk_high->equity_1h` score `2.9687` n `31` status `ready` deltaP `17.5922` edge `0.1488` maxDD `-0.1621`
- `news_risk_high->index_4h` score `2.8867` n `31` status `ready` deltaP `32.6515` edge `0.0489` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.5236` n `31` status `ready` deltaP `30.3458` edge `0.0165` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.1782` n `31` status `ready` deltaP `7.316` edge `0.2766` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.9424` n `31` status `ready` deltaP `10.31` edge `0.216` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.2766` n `31` status `ready` deltaP `26.5887` edge `0.0143` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `0.5707` n `31` status `ready` deltaP `12.5098` edge `0.0455` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.1736` n `31` status `ready` deltaP `8.6743` edge `0.0042` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.5377` n `31` status `ready` deltaP `-3.7087` edge `0.0061` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
