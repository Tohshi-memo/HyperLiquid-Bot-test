# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-27T14:22:40.501176+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14764`

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

- `news_risk_high->unknown_24h` score `51.6173` n `50` status `ready` deltaP `11.5717` edge `4.2243` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `19.9404` n `50` status `ready` deltaP `37.6235` edge `1.455` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `12.7276` n `50` status `ready` deltaP `26.4695` edge `0.8941` maxDD `-0.1279`
- `news_risk_high->equity_24h` score `4.6021` n `50` status `ready` deltaP `25.6235` edge `0.3055` maxDD `-4.7584`
- `news_risk_high->metal_24h` score `4.5537` n `50` status `ready` deltaP `45.4957` edge `0.0804` maxDD `-0.0053`
- `news_risk_high->fx_4h` score `4.0211` n `50` status `ready` deltaP `46.878` edge `0.0316` maxDD `-0.0559`
- `market_context_high->unknown_4h` score `3.1223` n `138` status `ready` deltaP `23.7738` edge `0.1424` maxDD `-0.5894`
- `news_risk_high->unknown_1h` score `2.9946` n `50` status `ready` deltaP `17.2754` edge `0.17` maxDD `-0.8495`
- `news_risk_high->index_24h` score `2.6702` n `50` status `ready` deltaP `29.9689` edge `0.0378` maxDD `-0.2064`
- `market_context_high->unknown_24h` score `2.193` n `128` status `ready` deltaP `5.3217` edge `0.2205` maxDD `-3.1917`
- `news_risk_high->fx_1h` score `1.5539` n `50` status `ready` deltaP `20.8024` edge `0.0078` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `1.2181` n `50` status `ready` deltaP `17.4132` edge `0.0133` maxDD `-0.2301`
- `market_context_high->unknown_1h` score `0.8712` n `148` status `ready` deltaP `9.5727` edge `0.0538` maxDD `-1.6015`
- `news_risk_high->equity_4h` score `0.6245` n `50` status `ready` deltaP `17.7683` edge `0.0099` maxDD `-2.105`
- `news_risk_high->commodity_1h` score `0.537` n `50` status `ready` deltaP `14.7485` edge `0.0018` maxDD `-0.5024`
- `news_risk_high->index_1h` score `0.1802` n `50` status `ready` deltaP `8.4072` edge `0.001` maxDD `-0.0486`
- `news_risk_high->metal_1h` score `0.1201` n `50` status `ready` deltaP `5.8503` edge `-0.001` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `-0.0193` n `50` status `ready` deltaP `7.9207` edge `-0.0013` maxDD `-0.249`
- `news_risk_high->index_4h` score `-0.0855` n `50` status `ready` deltaP `5.1037` edge `-0.0015` maxDD `-0.1719`
- `market_context_high->fx_1h` score `-0.4937` n `148` status `ready` deltaP `1.5051` edge `-0.0001` maxDD `-0.8587`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
