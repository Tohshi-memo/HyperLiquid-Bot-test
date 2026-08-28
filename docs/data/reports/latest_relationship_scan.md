# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-28T06:22:27.547008+00:00`
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

- `news_risk_high->unknown_24h` score `52.9309` n `50` status `ready` deltaP `11.6118` edge `4.3335` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `28.4084` n `50` status `ready` deltaP `37.7678` edge `2.1597` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `12.6535` n `50` status `ready` deltaP `24.898` edge `0.8984` maxDD `-0.1279`
- `news_risk_high->metal_24h` score `5.3872` n `50` status `ready` deltaP `49.2998` edge `0.1245` maxDD `-0.0053`
- `news_risk_high->equity_24h` score `5.3227` n `50` status `ready` deltaP `30.1005` edge `0.3357` maxDD `-4.7584`
- `news_risk_high->fx_4h` score `3.8904` n `50` status `ready` deltaP `45.4247` edge `0.0304` maxDD `-0.0559`
- `market_context_high->unknown_24h` score `3.5066` n `128` status `ready` deltaP `5.3618` edge `0.3297` maxDD `-3.1917`
- `news_risk_high->unknown_1h` score `2.9312` n `50` status `ready` deltaP `16.2275` edge `0.1717` maxDD `-0.8495`
- `news_risk_high->index_24h` score `2.6727` n `50` status `ready` deltaP `29.9411` edge `0.0382` maxDD `-0.2064`
- `market_context_high->unknown_4h` score `2.2104` n `148` status `ready` deltaP `18.0602` edge `0.1045` maxDD `-0.5894`
- `news_risk_high->fx_1h` score `1.615` n `50` status `ready` deltaP `21.5509` edge `0.0079` maxDD `-0.0257`
- `news_risk_high->equity_4h` score `1.4873` n `50` status `ready` deltaP `22.1187` edge `0.0528` maxDD `-2.105`
- `news_risk_high->equity_1h` score `1.4255` n `50` status `ready` deltaP `18.7605` edge `0.0216` maxDD `-0.2301`
- `market_context_high->unknown_1h` score `0.8078` n `148` status `ready` deltaP `8.5248` edge `0.0555` maxDD `-1.6015`
- `news_risk_high->crypto_major_24h` score `0.698` n `50` status `ready` deltaP `17.9688` edge `-0.0123` maxDD `-2.6128`
- `news_risk_high->commodity_1h` score `0.5253` n `50` status `ready` deltaP `14.4491` edge `0.0023` maxDD `-0.5024`
- `news_risk_high->metal_4h` score `0.3359` n `50` status `ready` deltaP `11.2055` edge `0.0064` maxDD `-0.249`
- `news_risk_high->index_1h` score `0.1896` n `50` status `ready` deltaP `8.5569` edge `0.0012` maxDD `-0.0486`
- `news_risk_high->metal_1h` score `0.1739` n `50` status `ready` deltaP `6.5988` edge `0.0009` maxDD `-0.1413`
- `news_risk_high->index_4h` score `0.018` n `50` status `ready` deltaP `6.0974` edge `0.0005` maxDD `-0.1719`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
