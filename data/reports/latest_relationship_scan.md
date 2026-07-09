# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-09T22:37:38.997203+00:00`
- Price records: `672`
- Market context records: `6224`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11110`

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

- `news_risk_high->crypto_alt_24h` score `13.3406` n `32` status `ready` deltaP `42.2194` edge `0.845` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.4246` n `32` status `ready` deltaP `55.2721` edge `0.1669` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.1635` n `32` status `ready` deltaP `43.6738` edge `0.0604` maxDD `-0.0345`
- `news_risk_high->crypto_major_24h` score `2.6045` n `32` status `ready` deltaP `15.625` edge `0.3077` maxDD `-4.2368`
- `news_risk_high->fx_1h` score `2.3452` n `32` status `ready` deltaP `28.2934` edge `0.0207` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `2.1127` n `192` status `ready` deltaP `2.5605` edge `0.2598` maxDD `-3.7317`
- `news_risk_high->commodity_24h` score `1.4159` n `32` status `ready` deltaP `21.6199` edge `-0.0056` maxDD `-0.3101`
- `news_risk_high->crypto_major_1h` score `1.3766` n `32` status `ready` deltaP `14.128` edge `0.129` maxDD `-2.0691`
- `market_context_high->unknown_4h` score `0.8537` n `192` status `ready` deltaP `-1.3847` edge `0.3336` maxDD `-11.925`
- `news_risk_high->crypto_alt_1h` score `0.7686` n `32` status `ready` deltaP `10.2732` edge `0.0762` maxDD `-1.6923`
- `market_context_high->metal_24h` score `-0.047` n `192` status `ready` deltaP `19.8023` edge `0.1188` maxDD `-11.8809`
- `news_risk_high->index_24h` score `-0.2112` n `32` status `ready` deltaP `8.801` edge `0.0014` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.2926` n `192` status `ready` deltaP `1.2101` edge `-0.001` maxDD `-0.5659`
- `market_context_high->commodity_1h` score `-0.5571` n `192` status `ready` deltaP `-0.5988` edge `0.0022` maxDD `-0.5708`
- `market_context_high->metal_4h` score `-0.6126` n `192` status `ready` deltaP `3.9762` edge `0.0137` maxDD `-3.4996`
- `news_risk_high->metal_1h` score `-0.8135` n `32` status `ready` deltaP `-4.0419` edge `-0.0276` maxDD `-1.6464`
- `market_context_high->crypto_alt_1h` score `-0.8951` n `192` status `ready` deltaP `4.544` edge `0.0302` maxDD `-9.3536`
- `market_context_high->metal_1h` score `-0.9107` n `192` status `ready` deltaP `1.1664` edge `-0.0038` maxDD `-2.0564`
- `market_context_high->crypto_major_1h` score `-0.923` n `192` status `ready` deltaP `4.2322` edge `0.0302` maxDD `-9.807`
- `market_context_high->equity_4h` score `-0.9692` n `192` status `ready` deltaP `1.4482` edge `0.0013` maxDD `-2.671`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
