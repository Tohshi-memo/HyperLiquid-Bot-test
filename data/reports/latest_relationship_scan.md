# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-11T15:22:25.015109+00:00`
- Price records: `672`
- Market context records: `6403`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11091`

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

- `news_risk_high->crypto_alt_24h` score `13.4375` n `32` status `ready` deltaP `34.8958` edge `0.9019` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.6859` n `32` status `ready` deltaP `56.4236` edge `0.181` maxDD `0.0`
- `news_risk_high->commodity_24h` score `4.3061` n `32` status `ready` deltaP `37.1528` edge `0.1317` maxDD `-0.3101`
- `news_risk_high->fx_4h` score `4.101` n `32` status `ready` deltaP `42.6067` edge `0.0623` maxDD `-0.0345`
- `news_risk_high->crypto_major_24h` score `4.0755` n `32` status `ready` deltaP `16.4931` edge `0.4905` maxDD `-4.2368`
- `news_risk_high->fx_1h` score `2.4458` n `32` status `ready` deltaP `29.491` edge `0.0211` maxDD `-0.1113`
- `market_context_high->unknown_24h` score `2.4428` n `146` status `ready` deltaP `9.0587` edge `0.4781` maxDD `-15.4609`
- `news_risk_high->crypto_major_1h` score `1.4281` n `32` status `ready` deltaP `13.6789` edge `0.1386` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.8216` n `32` status `ready` deltaP `10.1235` edge `0.084` maxDD `-1.6923`
- `market_context_high->unknown_1h` score `0.4936` n `214` status `ready` deltaP `-5.648` edge `0.1796` maxDD `-3.7317`
- `market_context_high->metal_4h` score `0.3861` n `214` status `ready` deltaP `11.2948` edge `0.0407` maxDD `-2.7056`
- `market_context_high->index_4h` score `0.0187` n `214` status `ready` deltaP `7.1989` edge `0.0212` maxDD `-0.4108`
- `news_risk_high->unknown_1h` score `-0.2465` n `32` status `ready` deltaP `6.5307` edge `-0.0296` maxDD `-0.7581`
- `market_context_high->metal_24h` score `-0.3293` n `146` status `ready` deltaP `19.6205` edge `0.0986` maxDD `-11.8809`
- `market_context_high->metal_1h` score `-0.4714` n `214` status `ready` deltaP `2.2231` edge `0.0025` maxDD `-1.8877`
- `market_context_high->equity_4h` score `-0.5181` n `214` status `ready` deltaP `8.0336` edge `0.0499` maxDD `-8.2573`
- `news_risk_high->metal_1h` score `-0.6375` n `32` status `ready` deltaP `-1.0479` edge `-0.025` maxDD `-1.6464`
- `market_context_high->fx_1h` score `-0.713` n `214` status `ready` deltaP `-0.6492` edge `-0.0017` maxDD `-0.9376`
- `market_context_high->index_1h` score `-0.717` n `214` status `ready` deltaP `-3.3843` edge `0.0026` maxDD `-0.7564`
- `market_context_high->commodity_1h` score `-0.7349` n `214` status `ready` deltaP `-3.4207` edge `-0.0031` maxDD `-2.1314`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
