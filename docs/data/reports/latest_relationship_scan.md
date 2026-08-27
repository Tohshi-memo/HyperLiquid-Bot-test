# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-27T15:07:29.246180+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14761`

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

- `news_risk_high->unknown_24h` score `51.7605` n `50` status `ready` deltaP `11.5917` edge `4.2361` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `20.2978` n `50` status `ready` deltaP `37.6955` edge `1.4843` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `12.8494` n `50` status `ready` deltaP `26.9268` edge `0.9012` maxDD `-0.1279`
- `news_risk_high->metal_24h` score `4.6491` n `50` status `ready` deltaP `45.9239` edge `0.0855` maxDD `-0.0053`
- `news_risk_high->equity_24h` score `4.6055` n `50` status `ready` deltaP `25.6955` edge `0.3053` maxDD `-4.7584`
- `news_risk_high->fx_4h` score `4.0211` n `50` status `ready` deltaP `46.878` edge `0.0316` maxDD `-0.0559`
- `news_risk_high->unknown_1h` score `2.9898` n `50` status `ready` deltaP `17.1257` edge `0.1706` maxDD `-0.8495`
- `market_context_high->unknown_4h` score `2.9111` n `141` status `ready` deltaP `22.2885` edge `0.1347` maxDD `-0.5894`
- `news_risk_high->index_24h` score `2.6561` n `50` status `ready` deltaP `29.8685` edge `0.0373` maxDD `-0.2064`
- `market_context_high->unknown_24h` score `2.3362` n `128` status `ready` deltaP `5.3417` edge `0.2323` maxDD `-3.1917`
- `news_risk_high->fx_1h` score `1.5551` n `50` status `ready` deltaP `20.8024` edge `0.0079` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `1.2265` n `50` status `ready` deltaP `17.4132` edge `0.014` maxDD `-0.2301`
- `market_context_high->unknown_1h` score `0.8664` n `148` status `ready` deltaP `9.423` edge `0.0544` maxDD `-1.6015`
- `news_risk_high->equity_4h` score `0.6487` n `50` status `ready` deltaP `17.9207` edge `0.0109` maxDD `-2.105`
- `news_risk_high->commodity_1h` score `0.5378` n `50` status `ready` deltaP `14.7485` edge `0.0019` maxDD `-0.5024`
- `news_risk_high->index_1h` score `0.1725` n `50` status `ready` deltaP `8.2575` edge `0.001` maxDD `-0.0486`
- `news_risk_high->metal_1h` score `0.1248` n `50` status `ready` deltaP `5.8503` edge `-0.0004` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `-0.0097` n `50` status `ready` deltaP `7.9207` edge `-0.0005` maxDD `-0.249`
- `news_risk_high->index_4h` score `-0.0745` n `50` status `ready` deltaP `5.2561` edge `-0.0016` maxDD `-0.1719`
- `market_context_high->fx_1h` score `-0.493` n `148` status `ready` deltaP `1.5051` edge `0.0` maxDD `-0.8587`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
