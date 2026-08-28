# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-28T08:07:24.562573+00:00`
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

- `news_risk_high->unknown_24h` score `53.0893` n `50` status `ready` deltaP `11.6118` edge `4.3467` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `29.3043` n `50` status `ready` deltaP `37.9411` edge `2.2332` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `12.7658` n `50` status `ready` deltaP `25.5068` edge `0.9037` maxDD `-0.1279`
- `news_risk_high->equity_24h` score `5.3659` n `50` status `ready` deltaP `30.1005` edge `0.3393` maxDD `-4.7584`
- `news_risk_high->metal_24h` score `5.2832` n `50` status `ready` deltaP `48.7799` edge `0.1193` maxDD `-0.0053`
- `news_risk_high->fx_4h` score `3.9219` n `50` status `ready` deltaP `45.7291` edge `0.031` maxDD `-0.0559`
- `market_context_high->unknown_24h` score `3.1724` n `131` status `ready` deltaP `5.5049` edge `0.3009` maxDD `-3.1917`
- `news_risk_high->unknown_1h` score `2.9288` n `50` status `ready` deltaP `16.2275` edge `0.1715` maxDD `-0.8495`
- `news_risk_high->index_24h` score `2.5775` n `50` status `ready` deltaP `28.9012` edge `0.0372` maxDD `-0.2064`
- `market_context_high->unknown_4h` score `2.3227` n `148` status `ready` deltaP `18.669` edge `0.1098` maxDD `-0.5894`
- `news_risk_high->equity_4h` score `1.6998` n `50` status `ready` deltaP `23.1842` edge `0.0634` maxDD `-2.105`
- `news_risk_high->fx_1h` score `1.6521` n `50` status `ready` deltaP `22.0` edge `0.008` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `1.5094` n `50` status `ready` deltaP `19.3593` edge `0.0246` maxDD `-0.2301`
- `news_risk_high->crypto_major_24h` score `1.4564` n `50` status `ready` deltaP `17.9688` edge `0.0509` maxDD `-2.6128`
- `market_context_high->unknown_1h` score `0.8054` n `148` status `ready` deltaP `8.5248` edge `0.0553` maxDD `-1.6015`
- `news_risk_high->commodity_1h` score `0.5728` n `50` status `ready` deltaP `15.1976` edge `0.0034` maxDD `-0.5024`
- `news_risk_high->metal_4h` score `0.3131` n `50` status `ready` deltaP `11.2055` edge `0.0045` maxDD `-0.249`
- `news_risk_high->index_1h` score `0.2075` n `50` status `ready` deltaP `8.8563` edge `0.0015` maxDD `-0.0486`
- `news_risk_high->metal_1h` score `0.163` n `50` status `ready` deltaP `6.5988` edge `-0.0005` maxDD `-0.1413`
- `market_context_high->metal_24h` score `0.104` n `131` status `ready` deltaP `14.1387` edge `0.0787` maxDD `-3.8102`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
