# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-18T01:52:25.165433+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11835`

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

- `risk_on_high->unknown_1h` score `10.4515` n `30` status `ready` deltaP `7.4551` edge `0.8406` maxDD `-0.5477`
- `risk_on_and_context->unknown_1h` score `10.4515` n `30` status `ready` deltaP `7.4551` edge `0.8406` maxDD `-0.5477`
- `market_context_high->crypto_major_24h` score `5.06` n `73` status `ready` deltaP `18.0836` edge `0.4219` maxDD `-4.9964`
- `market_context_high->equity_24h` score `2.2936` n `73` status `ready` deltaP `16.9844` edge `0.0779` maxDD `0.0`
- `risk_on_high->fx_4h` score `1.6135` n `30` status `ready` deltaP `20.8943` edge `0.0079` maxDD `-0.0192`
- `risk_on_and_context->fx_4h` score `1.6135` n `30` status `ready` deltaP `20.8943` edge `0.0079` maxDD `-0.0192`
- `market_context_high->index_24h` score `0.9135` n `73` status `ready` deltaP `16.4977` edge `-0.0287` maxDD `-0.0795`
- `market_context_high->commodity_4h` score `0.5472` n `112` status `ready` deltaP `11.8249` edge `0.0518` maxDD `-2.4692`
- `risk_on_high->commodity_4h` score `0.543` n `30` status `ready` deltaP `6.6463` edge `0.0882` maxDD `-1.3651`
- `risk_on_and_context->commodity_4h` score `0.543` n `30` status `ready` deltaP `6.6463` edge `0.0882` maxDD `-1.3651`
- `risk_on_high->fx_1h` score `0.4552` n `30` status `ready` deltaP `8.014` edge `0.0063` maxDD `-0.0771`
- `risk_on_and_context->fx_1h` score `0.4552` n `30` status `ready` deltaP `8.014` edge `0.0063` maxDD `-0.0771`
- `market_context_high->commodity_24h` score `0.2987` n `73` status `ready` deltaP `12.6469` edge `0.1239` maxDD `-4.666`
- `risk_on_high->index_1h` score `0.216` n `30` status `ready` deltaP `9.7805` edge `0.0` maxDD `-0.3343`
- `risk_on_and_context->index_1h` score `0.216` n `30` status `ready` deltaP `9.7805` edge `0.0` maxDD `-0.3343`
- `market_context_high->index_1h` score `0.1182` n `112` status `ready` deltaP `7.3995` edge `0.0025` maxDD `-0.3584`
- `risk_on_high->crypto_major_1h` score `0.1027` n `30` status `ready` deltaP `5.3194` edge `0.0083` maxDD `-1.1144`
- `risk_on_and_context->crypto_major_1h` score `0.1027` n `30` status `ready` deltaP `5.3194` edge `0.0083` maxDD `-1.1144`
- `market_context_high->unknown_1h` score `0.0361` n `112` status `ready` deltaP `7.2765` edge `-0.0196` maxDD `-0.7386`
- `market_context_high->metal_24h` score `0.0231` n `73` status `ready` deltaP `4.8384` edge `0.0695` maxDD `-2.5704`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
