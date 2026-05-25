# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-25T22:22:18.341533+00:00`
- Price records: `672`
- Market context records: `1884`
- Flow alert records: `7325`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4510`

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

- `market_context_high->crypto_alt_4h` score `7.0935` n `199` status `ready` deltaP `22.8137` edge `0.5535` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `6.7867` n `199` status `ready` deltaP `27.7148` edge `0.5054` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `4.3687` n `199` status `ready` deltaP `18.2628` edge `0.4447` maxDD `-9.8581`
- `market_context_high->metal_24h` score `3.2713` n `182` status `ready` deltaP `18.5859` edge `0.3913` maxDD `-12.7414`
- `market_context_high->equity_4h` score `2.373` n `199` status `ready` deltaP `14.4296` edge `0.211` maxDD `-5.0894`
- `market_context_high->index_24h` score `1.9178` n `182` status `ready` deltaP `11.4679` edge `0.2062` maxDD `-4.1604`
- `market_context_high->unknown_24h` score `1.7241` n `182` status `ready` deltaP `12.7976` edge `0.5904` maxDD `-35.8966`
- `market_context_high->crypto_major_1h` score `0.5314` n `199` status `ready` deltaP `6.4951` edge `0.0996` maxDD `-3.2225`
- `market_context_high->index_4h` score `0.4471` n `199` status `ready` deltaP `9.7882` edge `0.0809` maxDD `-3.7119`
- `market_context_high->crypto_alt_1h` score `0.2665` n `199` status `ready` deltaP `5.7571` edge `0.0952` maxDD `-4.9097`
- `market_context_high->fx_24h` score `0.2404` n `182` status `ready` deltaP `14.7665` edge `0.0265` maxDD `-1.3925`
- `market_context_high->equity_24h` score `0.1506` n `182` status `ready` deltaP `10.3937` edge `0.4331` maxDD `-33.1875`
- `market_context_high->crypto_major_24h` score `-0.1267` n `182` status `ready` deltaP `18.4981` edge `0.7247` maxDD `-62.3533`
- `market_context_high->equity_1h` score `-0.1647` n `199` status `ready` deltaP `4.388` edge `0.0364` maxDD `-2.6836`
- `market_context_high->unknown_1h` score `-0.4857` n `199` status `ready` deltaP `3.2874` edge `0.0328` maxDD `-3.6151`
- `market_context_high->metal_1h` score `-0.5079` n `199` status `ready` deltaP `6.7305` edge `0.0236` maxDD `-6.3532`
- `market_context_high->metal_4h` score `-0.5494` n `199` status `ready` deltaP `12.3905` edge `0.1408` maxDD `-12.5349`
- `market_context_high->index_1h` score `-0.6877` n `199` status `ready` deltaP `-0.6048` edge `0.0099` maxDD `-1.7205`
- `market_context_high->fx_1h` score `-0.7017` n `199` status `ready` deltaP `-3.9509` edge `-0.0004` maxDD `-0.3914`
- `market_context_high->fx_4h` score `-0.9868` n `199` status `ready` deltaP `-5.0389` edge `-0.0041` maxDD `-1.1056`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
