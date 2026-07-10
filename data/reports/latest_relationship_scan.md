# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-10T09:22:29.950999+00:00`
- Price records: `672`
- Market context records: `6270`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11084`

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

- `news_risk_high->crypto_alt_24h` score `15.0213` n `32` status `ready` deltaP `42.8879` edge `0.9806` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `5.9422` n `32` status `ready` deltaP `50.5172` edge `0.1584` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.1793` n `32` status `ready` deltaP `43.8262` edge `0.0607` maxDD `-0.0345`
- `news_risk_high->crypto_major_24h` score `3.9117` n `32` status `ready` deltaP `16.3147` edge `0.4707` maxDD `-4.2368`
- `news_risk_high->commodity_24h` score `2.4954` n `32` status `ready` deltaP `25.7543` edge `0.0568` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.3092` n `32` status `ready` deltaP `27.8443` edge `0.0207` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `1.95` n `200` status `ready` deltaP `2.2665` edge `0.2482` maxDD `-3.7317`
- `news_risk_high->crypto_major_1h` score `1.3197` n `32` status `ready` deltaP `13.5292` edge `0.1257` maxDD `-2.0691`
- `market_context_high->unknown_4h` score `1.2761` n `192` status `ready` deltaP `-1.3847` edge `0.3688` maxDD `-11.925`
- `news_risk_high->crypto_alt_1h` score `0.7904` n `32` status `ready` deltaP `10.5726` edge `0.077` maxDD `-1.6923`
- `market_context_high->equity_4h` score `-0.0355` n `192` status `ready` deltaP `5.2591` edge `0.0537` maxDD `-2.671`
- `news_risk_high->index_24h` score `-0.1673` n `32` status `ready` deltaP `9.181` edge `0.0045` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.3108` n `200` status `ready` deltaP `0.8443` edge `-0.0009` maxDD `-0.5659`
- `market_context_high->metal_24h` score `-0.3592` n `192` status `ready` deltaP `16.9792` edge `0.0976` maxDD `-11.8809`
- `market_context_high->metal_4h` score `-0.4583` n `192` status `ready` deltaP `4.7383` edge `0.0284` maxDD `-3.4996`
- `market_context_high->commodity_1h` score `-0.5415` n `200` status `ready` deltaP `-0.2994` edge `0.0029` maxDD `-0.682`
- `news_risk_high->metal_1h` score `-0.6725` n `32` status `ready` deltaP `-1.9461` edge `-0.0235` maxDD `-1.6464`
- `market_context_high->crypto_alt_1h` score `-0.7616` n `200` status `ready` deltaP `6.1976` edge `0.0363` maxDD `-9.3536`
- `market_context_high->crypto_major_1h` score `-0.8782` n `200` status `ready` deltaP `4.4042` edge `0.0348` maxDD `-9.807`
- `market_context_high->metal_1h` score `-0.9077` n `200` status `ready` deltaP `1.0539` edge `-0.0028` maxDD `-2.0564`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
