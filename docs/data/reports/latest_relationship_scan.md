# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-28T03:07:24.475418+00:00`
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

- `news_risk_high->unknown_24h` score `52.593` n `50` status `ready` deltaP `11.6319` edge `4.3052` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `25.8798` n `50` status `ready` deltaP `37.8403` edge `1.9485` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `12.687` n `50` status `ready` deltaP `24.7927` edge `0.9019` maxDD `-0.1279`
- `news_risk_high->metal_24h` score `5.2201` n `50` status `ready` deltaP `47.8264` edge `0.1204` maxDD `-0.0053`
- `news_risk_high->equity_24h` score `5.0983` n `50` status `ready` deltaP `28.2708` edge `0.3292` maxDD `-4.7584`
- `news_risk_high->fx_4h` score `3.8117` n `50` status `ready` deltaP `44.5915` edge `0.0294` maxDD `-0.0559`
- `market_context_high->unknown_24h` score `3.1686` n `128` status `ready` deltaP `5.3819` edge `0.3014` maxDD `-3.1917`
- `news_risk_high->unknown_1h` score `2.9216` n `50` status `ready` deltaP `15.7784` edge `0.1739` maxDD `-0.8495`
- `news_risk_high->index_24h` score `2.8342` n `50` status `ready` deltaP `31.75` edge `0.0396` maxDD `-0.2064`
- `market_context_high->unknown_4h` score `2.244` n `148` status `ready` deltaP `17.9549` edge `0.108` maxDD `-0.5894`
- `news_risk_high->fx_1h` score `1.5264` n `50` status `ready` deltaP `20.503` edge `0.0075` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `1.3524` n `50` status `ready` deltaP `18.1617` edge `0.0195` maxDD `-0.2301`
- `news_risk_high->equity_4h` score `1.2442` n `50` status `ready` deltaP `20.9695` edge `0.0402` maxDD `-2.105`
- `market_context_high->unknown_1h` score `0.7982` n `148` status `ready` deltaP `8.0757` edge `0.0577` maxDD `-1.6015`
- `news_risk_high->commodity_1h` score `0.551` n `50` status `ready` deltaP `14.8982` edge `0.0026` maxDD `-0.5024`
- `news_risk_high->metal_4h` score `0.191` n `50` status `ready` deltaP `10.0549` edge `0.002` maxDD `-0.249`
- `news_risk_high->index_1h` score `0.1639` n `50` status `ready` deltaP `8.1078` edge `0.0009` maxDD `-0.0486`
- `news_risk_high->metal_1h` score `0.1505` n `50` status `ready` deltaP `6.1497` edge `0.0009` maxDD `-0.1413`
- `news_risk_high->index_4h` score `-0.0723` n `50` status `ready` deltaP `5.1037` edge `-0.0004` maxDD `-0.1719`
- `market_context_high->metal_24h` score `-0.1682` n `128` status `ready` deltaP `12.3264` edge `0.0681` maxDD `-3.8102`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
