# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-10T20:37:29.572783+00:00`
- Price records: `672`
- Market context records: `6319`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11134`

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

- `news_risk_high->crypto_alt_24h` score `15.405` n `32` status `ready` deltaP `43.2292` edge `1.0103` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.0277` n `32` status `ready` deltaP `50.5208` edge `0.1655` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `4.3434` n `32` status `ready` deltaP `16.6667` edge `0.5237` maxDD `-4.2368`
- `news_risk_high->fx_4h` score `4.2033` n `32` status `ready` deltaP `43.8262` edge `0.0627` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `3.3503` n `32` status `ready` deltaP `30.0347` edge `0.0995` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.4254` n `32` status `ready` deltaP `29.1916` edge `0.0214` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.4858` n `32` status `ready` deltaP `14.7268` edge `0.139` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.9369` n `32` status `ready` deltaP `11.7702` edge `0.0878` maxDD `-1.6923`
- `market_context_high->unknown_1h` score `0.2524` n `208` status `ready` deltaP `-5.9333` edge `0.1614` maxDD `-3.7317`
- `market_context_high->metal_4h` score `-0.0202` n `196` status `ready` deltaP `8.6455` edge `0.037` maxDD `-2.7056`
- `market_context_high->metal_24h` score `-0.1982` n `155` status `ready` deltaP `20.196` edge `0.0968` maxDD `-11.8809`
- `market_context_high->metal_1h` score `-0.4255` n `208` status `ready` deltaP `3.256` edge `0.0015` maxDD `-1.8877`
- `news_risk_high->index_24h` score `-0.5227` n `32` status `ready` deltaP `3.4722` edge `-0.003` maxDD `-2.3058`
- `market_context_high->commodity_1h` score `-0.5921` n `208` status `ready` deltaP `-1.0796` edge `-0.0004` maxDD `-2.1314`
- `market_context_high->index_4h` score `-0.6316` n `196` status `ready` deltaP `3.5497` edge `0.019` maxDD `-1.2241`
- `news_risk_high->metal_1h` score `-0.7379` n `32` status `ready` deltaP `-2.994` edge `-0.0249` maxDD `-1.6464`
- `market_context_high->fx_1h` score `-0.782` n `208` status `ready` deltaP `-1.5776` edge `-0.0021` maxDD `-0.8706`
- `market_context_high->index_1h` score `-0.8248` n `208` status `ready` deltaP `-3.7828` edge `0.002` maxDD `-0.9358`
- `news_risk_high->unknown_1h` score `-0.875` n `32` status `ready` deltaP `4.884` edge `-0.071` maxDD `-0.7581`
- `market_context_high->crypto_alt_1h` score `-1.0035` n `208` status `ready` deltaP `4.799` edge `0.0146` maxDD `-9.3536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
