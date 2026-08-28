# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-28T06:37:24.604214+00:00`
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

- `news_risk_high->unknown_24h` score `52.9621` n `50` status `ready` deltaP `11.6118` edge `4.3361` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `28.5272` n `50` status `ready` deltaP `37.7678` edge `2.1696` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `12.6728` n `50` status `ready` deltaP `25.0502` edge `0.899` maxDD `-0.1279`
- `news_risk_high->metal_24h` score `5.3848` n `50` status `ready` deltaP `49.2998` edge `0.1243` maxDD `-0.0053`
- `news_risk_high->equity_24h` score `5.3215` n `50` status `ready` deltaP `30.1005` edge `0.3356` maxDD `-4.7584`
- `news_risk_high->fx_4h` score `3.905` n `50` status `ready` deltaP `45.5769` edge `0.0306` maxDD `-0.0559`
- `market_context_high->unknown_24h` score `3.5378` n `128` status `ready` deltaP `5.3618` edge `0.3323` maxDD `-3.1917`
- `news_risk_high->unknown_1h` score `2.93` n `50` status `ready` deltaP `16.2275` edge `0.1716` maxDD `-0.8495`
- `news_risk_high->index_24h` score `2.6577` n `50` status `ready` deltaP `29.7678` edge `0.0381` maxDD `-0.2064`
- `market_context_high->unknown_4h` score `2.2298` n `148` status `ready` deltaP `18.2124` edge `0.1051` maxDD `-0.5894`
- `news_risk_high->fx_1h` score `1.6282` n `50` status `ready` deltaP `21.7006` edge `0.008` maxDD `-0.0257`
- `news_risk_high->equity_4h` score `1.5175` n `50` status `ready` deltaP `22.2709` edge `0.0543` maxDD `-2.105`
- `news_risk_high->equity_1h` score `1.4267` n `50` status `ready` deltaP `18.7605` edge `0.0217` maxDD `-0.2301`
- `market_context_high->unknown_1h` score `0.8066` n `148` status `ready` deltaP `8.5248` edge `0.0554` maxDD `-1.6015`
- `news_risk_high->crypto_major_24h` score `0.7904` n `50` status `ready` deltaP `17.9688` edge `-0.0046` maxDD `-2.6128`
- `news_risk_high->commodity_1h` score `0.5253` n `50` status `ready` deltaP `14.4491` edge `0.0023` maxDD `-0.5024`
- `news_risk_high->metal_4h` score `0.3383` n `50` status `ready` deltaP `11.2055` edge `0.0066` maxDD `-0.249`
- `news_risk_high->index_1h` score `0.1981` n `50` status `ready` deltaP `8.7066` edge `0.0013` maxDD `-0.0486`
- `news_risk_high->metal_1h` score `0.1731` n `50` status `ready` deltaP `6.5988` edge `0.0008` maxDD `-0.1413`
- `news_risk_high->index_4h` score `0.0314` n `50` status `ready` deltaP `6.2496` edge `0.0006` maxDD `-0.1719`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
