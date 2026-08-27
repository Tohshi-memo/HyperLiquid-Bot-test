# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-27T18:07:43.417239+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14777`

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

- `news_risk_high->unknown_24h` score `52.1406` n `50` status `ready` deltaP `11.6319` edge `4.2675` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `21.3174` n `50` status `ready` deltaP `37.8403` edge `1.5683` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `13.061` n `50` status `ready` deltaP `27.2317` edge `0.9168` maxDD `-0.1279`
- `news_risk_high->metal_24h` score `4.7728` n `50` status `ready` deltaP `46.0903` edge `0.0947` maxDD `-0.0053`
- `news_risk_high->equity_24h` score `4.5235` n `50` status `ready` deltaP `25.8403` edge `0.2975` maxDD `-4.7584`
- `news_risk_high->fx_4h` score `4.0369` n `50` status `ready` deltaP `47.0305` edge `0.0319` maxDD `-0.0559`
- `news_risk_high->unknown_1h` score `3.0918` n `50` status `ready` deltaP `17.2754` edge `0.1781` maxDD `-0.8495`
- `market_context_high->unknown_24h` score `2.7162` n `128` status `ready` deltaP `5.3819` edge `0.2637` maxDD `-3.1917`
- `news_risk_high->index_24h` score `2.6287` n `50` status `ready` deltaP `29.8403` edge `0.0352` maxDD `-0.2064`
- `market_context_high->unknown_4h` score `2.6179` n `148` status `ready` deltaP `20.3939` edge `0.1229` maxDD `-0.5894`
- `news_risk_high->fx_1h` score `1.5815` n `50` status `ready` deltaP `21.1018` edge `0.0081` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `1.1223` n `50` status `ready` deltaP `16.515` edge `0.0113` maxDD `-0.2301`
- `market_context_high->unknown_1h` score `0.9684` n `148` status `ready` deltaP `9.5727` edge `0.0619` maxDD `-1.6015`
- `news_risk_high->equity_4h` score `0.7625` n `50` status `ready` deltaP `18.6829` edge `0.0153` maxDD `-2.105`
- `news_risk_high->commodity_1h` score `0.5245` n `50` status `ready` deltaP `14.5988` edge `0.0012` maxDD `-0.5024`
- `news_risk_high->index_1h` score `0.1288` n `50` status `ready` deltaP `7.509` edge `0.0004` maxDD `-0.0486`
- `news_risk_high->metal_1h` score `0.0532` n `50` status `ready` deltaP `4.6527` edge `-0.0016` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `-0.0931` n `50` status `ready` deltaP `7.4634` edge `-0.0044` maxDD `-0.249`
- `news_risk_high->index_4h` score `-0.1719` n `50` status `ready` deltaP `4.189` edge `-0.0026` maxDD `-0.1719`
- `market_context_high->metal_4h` score `-0.4417` n `148` status `ready` deltaP `6.3283` edge `-0.0071` maxDD `-3.3377`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
