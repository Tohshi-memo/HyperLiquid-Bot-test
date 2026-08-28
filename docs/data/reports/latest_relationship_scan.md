# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-28T03:52:24.964847+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11831`

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

- `news_risk_high->unknown_24h` score `52.6446` n `50` status `ready` deltaP `11.6319` edge `4.3095` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `26.523` n `50` status `ready` deltaP `37.8403` edge `2.0021` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `12.6408` n `50` status `ready` deltaP `24.3354` edge `0.9011` maxDD `-0.1279`
- `news_risk_high->metal_24h` score `5.2822` n `50` status `ready` deltaP `48.3472` edge `0.1221` maxDD `-0.0053`
- `news_risk_high->equity_24h` score `5.1532` n `50` status `ready` deltaP `28.7917` edge `0.3303` maxDD `-4.7584`
- `news_risk_high->fx_4h` score `3.8543` n `50` status `ready` deltaP `45.0488` edge `0.0299` maxDD `-0.0559`
- `market_context_high->unknown_24h` score `3.2202` n `128` status `ready` deltaP `5.3819` edge `0.3057` maxDD `-3.1917`
- `news_risk_high->unknown_1h` score `2.978` n `50` status `ready` deltaP `16.0778` edge `0.1766` maxDD `-0.8495`
- `news_risk_high->index_24h` score `2.7902` n `50` status `ready` deltaP `31.2292` edge `0.0394` maxDD `-0.2064`
- `market_context_high->unknown_4h` score `2.1978` n `148` status `ready` deltaP `17.4976` edge `0.1072` maxDD `-0.5894`
- `news_risk_high->fx_1h` score `1.5647` n `50` status `ready` deltaP `20.9521` edge `0.0077` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `1.344` n `50` status `ready` deltaP `18.1617` edge `0.0188` maxDD `-0.2301`
- `news_risk_high->equity_4h` score `1.2296` n `50` status `ready` deltaP `20.8171` edge `0.04` maxDD `-2.105`
- `market_context_high->unknown_1h` score `0.8546` n `148` status `ready` deltaP `8.3751` edge `0.0604` maxDD `-1.6015`
- `news_risk_high->commodity_1h` score `0.5417` n `50` status `ready` deltaP `14.7485` edge `0.0024` maxDD `-0.5024`
- `news_risk_high->metal_4h` score `0.2384` n `50` status `ready` deltaP `10.5122` edge `0.0029` maxDD `-0.249`
- `news_risk_high->index_1h` score `0.1639` n `50` status `ready` deltaP `8.1078` edge `0.0009` maxDD `-0.0486`
- `news_risk_high->metal_1h` score `0.149` n `50` status `ready` deltaP `6.1497` edge `0.0007` maxDD `-0.1413`
- `news_risk_high->index_4h` score `-0.0747` n `50` status `ready` deltaP `5.1037` edge `-0.0006` maxDD `-0.1719`
- `market_context_high->metal_24h` score `-0.1062` n `128` status `ready` deltaP `12.8472` edge `0.0698` maxDD `-3.8102`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
