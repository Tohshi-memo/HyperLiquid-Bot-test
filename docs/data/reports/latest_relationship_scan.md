# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-28T08:37:28.018121+00:00`
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

- `news_risk_high->unknown_24h` score `53.1493` n `50` status `ready` deltaP `11.6118` edge `4.3517` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `29.6128` n `50` status `ready` deltaP `38.2877` edge `2.2566` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `12.7778` n `50` status `ready` deltaP `25.5068` edge `0.9047` maxDD `-0.1279`
- `news_risk_high->equity_24h` score `5.3863` n `50` status `ready` deltaP `30.1005` edge `0.341` maxDD `-4.7584`
- `news_risk_high->metal_24h` score `5.2465` n `50` status `ready` deltaP `48.6066` edge `0.1174` maxDD `-0.0053`
- `news_risk_high->fx_4h` score `3.9243` n `50` status `ready` deltaP `45.7291` edge `0.0312` maxDD `-0.0559`
- `market_context_high->unknown_24h` score `2.9098` n `133` status `ready` deltaP `5.5968` edge `0.2784` maxDD `-3.1917`
- `news_risk_high->unknown_1h` score `2.8798` n `51` status `ready` deltaP `16.6197` edge `0.1648` maxDD `-0.8495`
- `news_risk_high->index_24h` score `2.5751` n `50` status `ready` deltaP `28.9012` edge `0.037` maxDD `-0.2064`
- `market_context_high->unknown_4h` score `2.3347` n `148` status `ready` deltaP `18.669` edge `0.1108` maxDD `-0.5894`
- `news_risk_high->equity_4h` score `1.7469` n `50` status `ready` deltaP `23.4886` edge `0.0653` maxDD `-2.105`
- `news_risk_high->crypto_major_24h` score `1.7228` n `50` status `ready` deltaP `17.9688` edge `0.0731` maxDD `-2.6128`
- `news_risk_high->fx_1h` score `1.6697` n `51` status `ready` deltaP `22.2496` edge `0.0078` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `1.3729` n `51` status `ready` deltaP `17.9083` edge `0.0229` maxDD `-0.2301`
- `market_context_high->unknown_1h` score `0.8066` n `148` status `ready` deltaP `8.5248` edge `0.0554` maxDD `-1.6015`
- `news_risk_high->commodity_1h` score `0.5031` n `51` status `ready` deltaP `14.0924` edge `0.0023` maxDD `-0.5397`
- `news_risk_high->metal_4h` score `0.3083` n `50` status `ready` deltaP `11.2055` edge `0.0041` maxDD `-0.249`
- `market_context_high->metal_24h` score `0.199` n `133` status `ready` deltaP `14.5164` edge `0.0841` maxDD `-3.8102`
- `news_risk_high->index_1h` score `0.1427` n `51` status `ready` deltaP `7.6406` edge `0.0013` maxDD `-0.0486`
- `news_risk_high->metal_1h` score `0.1152` n `51` status `ready` deltaP `5.6505` edge `-0.0003` maxDD `-0.1413`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
