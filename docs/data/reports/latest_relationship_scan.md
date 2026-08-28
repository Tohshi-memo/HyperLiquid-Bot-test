# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-28T03:37:25.355972+00:00`
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

- `news_risk_high->unknown_24h` score `52.6254` n `50` status `ready` deltaP `11.6319` edge `4.3079` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `26.2986` n `50` status `ready` deltaP `37.8403` edge `1.9834` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `12.6554` n `50` status `ready` deltaP `24.4878` edge `0.9013` maxDD `-0.1279`
- `news_risk_high->metal_24h` score `5.2611` n `50` status `ready` deltaP `48.1736` edge `0.1215` maxDD `-0.0053`
- `news_risk_high->equity_24h` score `5.1321` n `50` status `ready` deltaP `28.6181` edge `0.3297` maxDD `-4.7584`
- `news_risk_high->fx_4h` score `3.8409` n `50` status `ready` deltaP `44.8963` edge `0.0298` maxDD `-0.0559`
- `market_context_high->unknown_24h` score `3.201` n `128` status `ready` deltaP `5.3819` edge `0.3041` maxDD `-3.1917`
- `news_risk_high->unknown_1h` score `2.9624` n `50` status `ready` deltaP `15.9281` edge `0.1763` maxDD `-0.8495`
- `news_risk_high->index_24h` score `2.8053` n `50` status `ready` deltaP `31.4028` edge `0.0395` maxDD `-0.2064`
- `market_context_high->unknown_4h` score `2.2124` n `148` status `ready` deltaP `17.65` edge `0.1074` maxDD `-0.5894`
- `news_risk_high->fx_1h` score `1.5515` n `50` status `ready` deltaP `20.8024` edge `0.0076` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `1.3452` n `50` status `ready` deltaP `18.1617` edge `0.0189` maxDD `-0.2301`
- `news_risk_high->equity_4h` score `1.226` n `50` status `ready` deltaP `20.8171` edge `0.0397` maxDD `-2.105`
- `market_context_high->unknown_1h` score `0.839` n `148` status `ready` deltaP `8.2254` edge `0.0601` maxDD `-1.6015`
- `news_risk_high->commodity_1h` score `0.5424` n `50` status `ready` deltaP `14.7485` edge `0.0025` maxDD `-0.5024`
- `news_risk_high->metal_4h` score `0.2226` n `50` status `ready` deltaP `10.3598` edge `0.0026` maxDD `-0.249`
- `news_risk_high->index_1h` score `0.1639` n `50` status `ready` deltaP `8.1078` edge `0.0009` maxDD `-0.0486`
- `news_risk_high->metal_1h` score `0.1412` n `50` status `ready` deltaP `6.0` edge `0.0007` maxDD `-0.1413`
- `news_risk_high->index_4h` score `-0.0747` n `50` status `ready` deltaP `5.1037` edge `-0.0006` maxDD `-0.1719`
- `market_context_high->metal_24h` score `-0.1272` n `128` status `ready` deltaP `12.6736` edge `0.0692` maxDD `-3.8102`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
