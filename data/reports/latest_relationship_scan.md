# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-28T08:22:25.244525+00:00`
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

- `news_risk_high->unknown_24h` score `53.1193` n `50` status `ready` deltaP `11.6118` edge `4.3492` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `29.4573` n `50` status `ready` deltaP `38.1144` edge `2.2448` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `12.773` n `50` status `ready` deltaP `25.5068` edge `0.9043` maxDD `-0.1279`
- `news_risk_high->equity_24h` score `5.3767` n `50` status `ready` deltaP `30.1005` edge `0.3402` maxDD `-4.7584`
- `news_risk_high->metal_24h` score `5.2573` n `50` status `ready` deltaP `48.6066` edge `0.1183` maxDD `-0.0053`
- `news_risk_high->fx_4h` score `3.9231` n `50` status `ready` deltaP `45.7291` edge `0.0311` maxDD `-0.0559`
- `market_context_high->unknown_24h` score `3.0429` n `132` status `ready` deltaP `5.5512` edge `0.2898` maxDD `-3.1917`
- `news_risk_high->unknown_1h` score `2.9288` n `50` status `ready` deltaP `16.2275` edge `0.1715` maxDD `-0.8495`
- `news_risk_high->index_24h` score `2.5763` n `50` status `ready` deltaP `28.9012` edge `0.0371` maxDD `-0.2064`
- `market_context_high->unknown_4h` score `2.3299` n `148` status `ready` deltaP `18.669` edge `0.1104` maxDD `-0.5894`
- `news_risk_high->equity_4h` score `1.7252` n `50` status `ready` deltaP `23.3364` edge `0.0645` maxDD `-2.105`
- `news_risk_high->fx_1h` score `1.639` n `50` status `ready` deltaP `21.8503` edge `0.0079` maxDD `-0.0257`
- `news_risk_high->crypto_major_24h` score `1.5824` n `50` status `ready` deltaP `17.9688` edge `0.0614` maxDD `-2.6128`
- `news_risk_high->equity_1h` score `1.507` n `50` status `ready` deltaP `19.3593` edge `0.0244` maxDD `-0.2301`
- `market_context_high->unknown_1h` score `0.8054` n `148` status `ready` deltaP `8.5248` edge `0.0553` maxDD `-1.6015`
- `news_risk_high->commodity_1h` score `0.5814` n `50` status `ready` deltaP `15.3473` edge `0.0035` maxDD `-0.5024`
- `news_risk_high->metal_4h` score `0.3107` n `50` status `ready` deltaP `11.2055` edge `0.0043` maxDD `-0.249`
- `news_risk_high->index_1h` score `0.2067` n `50` status `ready` deltaP `8.8563` edge `0.0014` maxDD `-0.0486`
- `news_risk_high->metal_1h` score `0.1637` n `50` status `ready` deltaP `6.5988` edge `-0.0004` maxDD `-0.1413`
- `market_context_high->metal_24h` score `0.1423` n `132` status `ready` deltaP `14.243` edge `0.0812` maxDD `-3.8102`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
