# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-11T16:37:29.432335+00:00`
- Price records: `672`
- Market context records: `6410`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11095`

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

- `news_risk_high->crypto_alt_24h` score `13.1821` n `32` status `ready` deltaP `34.0278` edge `0.8864` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.6883` n `32` status `ready` deltaP `56.4236` edge `0.1812` maxDD `0.0`
- `news_risk_high->commodity_24h` score `4.2139` n `32` status `ready` deltaP `36.2847` edge `0.1298` maxDD `-0.3101`
- `news_risk_high->fx_4h` score `4.1655` n `32` status `ready` deltaP `43.3689` edge `0.0626` maxDD `-0.0345`
- `news_risk_high->crypto_major_24h` score `3.9687` n `32` status `ready` deltaP `15.625` edge `0.4826` maxDD `-4.2368`
- `market_context_high->unknown_24h` score `3.9037` n `146` status `ready` deltaP `11.6153` edge `0.5779` maxDD `-15.0689`
- `news_risk_high->fx_1h` score `2.4709` n `32` status `ready` deltaP `29.7904` edge `0.0212` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.4796` n `32` status `ready` deltaP `14.2777` edge `0.1412` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.8442` n `32` status `ready` deltaP `10.2732` edge `0.0859` maxDD `-1.6923`
- `market_context_high->unknown_1h` score `0.6357` n `209` status `ready` deltaP `-5.4465` edge `0.1901` maxDD `-3.7317`
- `market_context_high->metal_4h` score `0.3848` n `209` status `ready` deltaP `11.2185` edge `0.0411` maxDD `-2.7056`
- `market_context_high->index_4h` score `0.0661` n `209` status `ready` deltaP `7.6868` edge `0.0219` maxDD `-0.4108`
- `news_risk_high->unknown_1h` score `-0.3016` n `32` status `ready` deltaP `6.0816` edge `-0.0312` maxDD `-0.7581`
- `market_context_high->metal_24h` score `-0.4339` n `146` status `ready` deltaP `18.5978` edge `0.0967` maxDD `-11.8809`
- `market_context_high->metal_1h` score `-0.4549` n `209` status `ready` deltaP `2.5406` edge `0.0025` maxDD `-1.8877`
- `news_risk_high->metal_1h` score `-0.6367` n `32` status `ready` deltaP `-1.0479` edge `-0.0249` maxDD `-1.6464`
- `market_context_high->fx_1h` score `-0.6797` n `209` status `ready` deltaP `-0.2335` edge `-0.0017` maxDD `-0.9376`
- `market_context_high->commodity_1h` score `-0.6868` n `209` status `ready` deltaP `-2.6022` edge `-0.0024` maxDD `-2.1314`
- `market_context_high->index_1h` score `-0.7323` n `209` status `ready` deltaP `-3.6795` edge `0.0026` maxDD `-0.7564`
- `news_risk_high->index_24h` score `-0.7557` n `32` status `ready` deltaP `0.5208` edge `-0.0132` maxDD `-2.3058`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
