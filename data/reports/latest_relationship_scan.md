# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-28T08:52:24.078388+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11608`

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

- `news_risk_high->unknown_24h` score `53.1781` n `50` status `ready` deltaP `11.6118` edge `4.3541` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `29.7622` n `50` status `ready` deltaP `38.461` edge `2.2679` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `12.7874` n `50` status `ready` deltaP `25.5068` edge `0.9055` maxDD `-0.1279`
- `news_risk_high->equity_24h` score `5.3995` n `50` status `ready` deltaP `30.1005` edge `0.3421` maxDD `-4.7584`
- `news_risk_high->metal_24h` score `5.2195` n `50` status `ready` deltaP `48.4333` edge `0.1163` maxDD `-0.0053`
- `news_risk_high->fx_4h` score `3.9255` n `50` status `ready` deltaP `45.7291` edge `0.0313` maxDD `-0.0559`
- `market_context_high->unknown_24h` score `2.9386` n `133` status `ready` deltaP `5.5968` edge `0.2808` maxDD `-3.1917`
- `news_risk_high->unknown_1h` score `2.666` n `52` status `ready` deltaP `15.2234` edge `0.1563` maxDD `-0.8495`
- `news_risk_high->index_24h` score `2.5739` n `50` status `ready` deltaP `28.9012` edge `0.0369` maxDD `-0.2064`
- `market_context_high->unknown_4h` score `2.3443` n `148` status `ready` deltaP `18.669` edge `0.1116` maxDD `-0.5894`
- `news_risk_high->crypto_major_24h` score `1.8794` n `50` status `ready` deltaP `18.1421` edge `0.085` maxDD `-2.6128`
- `news_risk_high->equity_4h` score `1.7687` n `50` status `ready` deltaP `23.6408` edge `0.0661` maxDD `-2.105`
- `news_risk_high->fx_1h` score `1.5569` n `52` status `ready` deltaP `20.8544` edge `0.0077` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `1.2548` n `52` status `ready` deltaP `16.6628` edge `0.0217` maxDD `-0.2574`
- `market_context_high->unknown_1h` score `0.8269` n `148` status `ready` deltaP `8.6745` edge `0.0561` maxDD `-1.6015`
- `news_risk_high->commodity_1h` score `0.5365` n `52` status `ready` deltaP `14.6591` edge `0.0028` maxDD `-0.5397`
- `news_risk_high->metal_4h` score `0.3035` n `50` status `ready` deltaP `11.2055` edge `0.0037` maxDD `-0.249`
- `market_context_high->metal_24h` score `0.1719` n `133` status `ready` deltaP `14.3431` edge `0.083` maxDD `-3.8102`
- `news_risk_high->index_4h` score `0.114` n `50` status `ready` deltaP `7.1629` edge `0.0014` maxDD `-0.1719`
- `news_risk_high->index_1h` score `0.0788` n `52` status `ready` deltaP `6.4717` edge `0.0009` maxDD `-0.0486`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
