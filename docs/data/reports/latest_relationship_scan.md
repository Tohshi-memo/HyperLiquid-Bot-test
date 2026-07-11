# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-11T17:07:26.148555+00:00`
- Price records: `672`
- Market context records: `6412`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5849`

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

- `news_risk_high->crypto_alt_24h` score `13.0859` n `32` status `ready` deltaP `33.6806` edge `0.8807` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.6895` n `32` status `ready` deltaP `56.4236` edge `0.1813` maxDD `0.0`
- `market_context_high->unknown_24h` score `4.4067` n `146` status `ready` deltaP `12.6379` edge `0.613` maxDD `-15.0689`
- `news_risk_high->commodity_24h` score `4.2103` n `32` status `ready` deltaP `36.2847` edge `0.1295` maxDD `-0.3101`
- `news_risk_high->fx_4h` score `4.1923` n `32` status `ready` deltaP `43.6738` edge `0.0628` maxDD `-0.0345`
- `news_risk_high->crypto_major_24h` score `3.9327` n `32` status `ready` deltaP `15.2778` edge `0.4803` maxDD `-4.2368`
- `news_risk_high->fx_1h` score `2.4841` n `32` status `ready` deltaP `29.9401` edge `0.0213` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.4967` n `32` status `ready` deltaP `14.4274` edge `0.1424` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.845` n `32` status `ready` deltaP `10.2732` edge `0.086` maxDD `-1.6923`
- `market_context_high->unknown_1h` score `0.706` n `207` status `ready` deltaP `-5.3176` edge `0.1951` maxDD `-3.7317`
- `market_context_high->metal_4h` score `0.3815` n `207` status `ready` deltaP `11.1766` edge `0.0411` maxDD `-2.7056`
- `market_context_high->index_4h` score `0.0959` n `207` status `ready` deltaP `8.0292` edge `0.0221` maxDD `-0.4108`
- `news_risk_high->unknown_1h` score `-0.286` n `32` status `ready` deltaP `6.2313` edge `-0.0309` maxDD `-0.7581`
- `market_context_high->metal_24h` score `-0.4375` n `146` status `ready` deltaP `18.5978` edge `0.0964` maxDD `-11.8809`
- `market_context_high->metal_1h` score `-0.4713` n `207` status `ready` deltaP `2.2419` edge `0.0024` maxDD `-1.8877`
- `news_risk_high->metal_1h` score `-0.629` n `32` status `ready` deltaP `-0.8982` edge `-0.0249` maxDD `-1.6464`
- `market_context_high->commodity_1h` score `-0.699` n `207` status `ready` deltaP `-2.8067` edge `-0.0026` maxDD `-2.1314`
- `market_context_high->fx_1h` score `-0.7127` n `207` status `ready` deltaP `-0.6155` edge `-0.0019` maxDD `-0.9376`
- `news_risk_high->index_24h` score `-0.7557` n `32` status `ready` deltaP `0.5208` edge `-0.0132` maxDD `-2.3058`
- `market_context_high->index_1h` score `-0.7587` n `207` status `ready` deltaP `-4.188` edge `0.0026` maxDD `-0.7564`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
