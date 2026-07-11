# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-11T15:52:28.950037+00:00`
- Price records: `672`
- Market context records: `6406`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11093`

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

- `news_risk_high->crypto_alt_24h` score `13.3329` n `32` status `ready` deltaP `34.5486` edge `0.8955` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.6871` n `32` status `ready` deltaP `56.4236` edge `0.1811` maxDD `0.0`
- `news_risk_high->commodity_24h` score `4.2639` n `32` status `ready` deltaP `36.8056` edge `0.1305` maxDD `-0.3101`
- `news_risk_high->fx_4h` score `4.1266` n `32` status `ready` deltaP `42.9116` edge `0.0624` maxDD `-0.0345`
- `news_risk_high->crypto_major_24h` score `4.0332` n `32` status `ready` deltaP `16.1458` edge `0.4874` maxDD `-4.2368`
- `market_context_high->unknown_24h` score `3.0946` n `146` status `ready` deltaP `10.0813` edge `0.5207` maxDD `-15.0689`
- `news_risk_high->fx_1h` score `2.4458` n `32` status `ready` deltaP `29.491` edge `0.0211` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.4414` n `32` status `ready` deltaP `13.8286` edge `0.1393` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.8263` n `32` status `ready` deltaP `10.1235` edge `0.0846` maxDD `-1.6923`
- `market_context_high->unknown_1h` score `0.5239` n `212` status `ready` deltaP `-5.8242` edge `0.1833` maxDD `-3.7317`
- `market_context_high->metal_4h` score `0.3853` n `212` status `ready` deltaP `11.2689` edge `0.0408` maxDD `-2.7056`
- `market_context_high->index_4h` score `0.0221` n `212` status `ready` deltaP `7.1962` edge `0.0215` maxDD `-0.4108`
- `news_risk_high->unknown_1h` score `-0.268` n `32` status `ready` deltaP `6.381` edge `-0.0304` maxDD `-0.7581`
- `market_context_high->metal_24h` score `-0.3377` n `146` status `ready` deltaP `19.6205` edge `0.0979` maxDD `-11.8809`
- `market_context_high->metal_1h` score `-0.478` n `212` status `ready` deltaP `2.0817` edge `0.0026` maxDD `-1.8877`
- `news_risk_high->metal_1h` score `-0.6204` n `32` status `ready` deltaP `-0.7485` edge `-0.0248` maxDD `-1.6464`
- `market_context_high->fx_1h` score `-0.6791` n `212` status `ready` deltaP `-0.226` edge `-0.0017` maxDD `-0.9376`
- `market_context_high->commodity_1h` score `-0.7166` n `212` status `ready` deltaP `-3.1296` edge `-0.0027` maxDD `-2.1314`
- `market_context_high->index_1h` score `-0.7251` n `212` status `ready` deltaP `-3.5561` edge `0.0027` maxDD `-0.7564`
- `news_risk_high->index_24h` score `-0.7557` n `32` status `ready` deltaP `0.5208` edge `-0.0132` maxDD `-2.3058`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
