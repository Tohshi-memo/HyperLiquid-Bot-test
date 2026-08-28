# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-28T07:22:24.273819+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11607`

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

- `news_risk_high->unknown_24h` score `53.0209` n `50` status `ready` deltaP `11.6118` edge `4.341` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `28.8776` n `50` status `ready` deltaP `37.7678` edge `2.1988` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `12.7224` n `50` status `ready` deltaP `25.3546` edge `0.9011` maxDD `-0.1279`
- `news_risk_high->metal_24h` score `5.3608` n `50` status `ready` deltaP `49.2998` edge `0.1223` maxDD `-0.0053`
- `news_risk_high->equity_24h` score `5.3431` n `50` status `ready` deltaP `30.1005` edge `0.3374` maxDD `-4.7584`
- `news_risk_high->fx_4h` score `3.9195` n `50` status `ready` deltaP `45.7291` edge `0.0308` maxDD `-0.0559`
- `market_context_high->unknown_24h` score `3.5966` n `128` status `ready` deltaP `5.3618` edge `0.3372` maxDD `-3.1917`
- `news_risk_high->unknown_1h` score `2.9108` n `50` status `ready` deltaP `16.0778` edge `0.171` maxDD `-0.8495`
- `news_risk_high->index_24h` score `2.6113` n `50` status `ready` deltaP `29.2478` edge `0.0377` maxDD `-0.2064`
- `market_context_high->unknown_4h` score `2.2793` n `148` status `ready` deltaP `18.5168` edge `0.1072` maxDD `-0.5894`
- `news_risk_high->fx_1h` score `1.6533` n `50` status `ready` deltaP `22.0` edge `0.0081` maxDD `-0.0257`
- `news_risk_high->equity_4h` score `1.6189` n `50` status `ready` deltaP `22.7275` edge `0.0597` maxDD `-2.105`
- `news_risk_high->equity_1h` score `1.4591` n `50` status `ready` deltaP `18.9102` edge `0.0234` maxDD `-0.2301`
- `news_risk_high->crypto_major_24h` score `1.0784` n `50` status `ready` deltaP `17.9688` edge `0.0194` maxDD `-2.6128`
- `market_context_high->unknown_1h` score `0.7874` n `148` status `ready` deltaP `8.3751` edge `0.0548` maxDD `-1.6015`
- `news_risk_high->commodity_1h` score `0.5432` n `50` status `ready` deltaP `14.7485` edge `0.0026` maxDD `-0.5024`
- `news_risk_high->metal_4h` score `0.3287` n `50` status `ready` deltaP `11.2055` edge `0.0058` maxDD `-0.249`
- `news_risk_high->index_1h` score `0.1989` n `50` status `ready` deltaP `8.7066` edge `0.0014` maxDD `-0.0486`
- `news_risk_high->metal_1h` score `0.1653` n `50` status `ready` deltaP `6.5988` edge `-0.0002` maxDD `-0.1413`
- `news_risk_high->index_4h` score `0.0727` n `50` status `ready` deltaP `6.7062` edge `0.001` maxDD `-0.1719`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
