# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-23T23:07:24.174552+00:00`
- Price records: `672`
- Market context records: `7717`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14676`

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

- `market_context_high->equity_24h` score `3.5751` n `132` status `ready` deltaP `19.396` edge `0.3028` maxDD `-6.0681`
- `market_context_high->crypto_major_1h` score `1.0801` n `133` status `ready` deltaP `13.3076` edge `0.0454` maxDD `-1.5286`
- `market_context_high->crypto_major_4h` score `1.0522` n `133` status `ready` deltaP `14.8037` edge `0.1608` maxDD `-6.7444`
- `market_context_high->crypto_alt_4h` score `0.6671` n `133` status `ready` deltaP `8.6569` edge `0.1096` maxDD `-3.9374`
- `market_context_high->equity_1h` score `0.6651` n `133` status `ready` deltaP `8.9469` edge `0.0817` maxDD `-4.2072`
- `market_context_high->equity_4h` score `0.6112` n `133` status `ready` deltaP `2.1223` edge `0.2555` maxDD `-6.9701`
- `market_context_high->index_1h` score `0.4239` n `133` status `ready` deltaP `9.3952` edge `0.0157` maxDD `-0.7743`
- `market_context_high->crypto_alt_1h` score `0.1653` n `133` status `ready` deltaP `3.9789` edge `0.0305` maxDD `-1.4603`
- `market_context_high->fx_24h` score `0.0623` n `132` status `ready` deltaP `13.6865` edge `0.0255` maxDD `-3.0343`
- `market_context_high->commodity_4h` score `-0.1531` n `133` status `ready` deltaP `4.6343` edge `0.0157` maxDD `-1.0817`
- `market_context_high->commodity_1h` score `-0.164` n `133` status `ready` deltaP `3.8452` edge `0.0066` maxDD `-0.6722`
- `market_context_high->index_4h` score `-0.2213` n `133` status `ready` deltaP `11.0172` edge `0.044` maxDD `-1.3325`
- `market_context_high->metal_24h` score `-0.4215` n `133` status `ready` deltaP `3.202` edge `0.1526` maxDD `-2.3927`
- `market_context_high->fx_1h` score `-0.5552` n `133` status `ready` deltaP `-0.9776` edge `-0.001` maxDD `-0.4331`
- `market_context_high->metal_1h` score `-0.8662` n `133` status `ready` deltaP `1.2674` edge `0.0197` maxDD `-0.6936`
- `market_context_high->metal_4h` score `-1.4697` n `133` status `ready` deltaP `1.1381` edge `0.0754` maxDD `-1.4368`
- `market_context_high->fx_4h` score `-1.5862` n `133` status `ready` deltaP `-5.5379` edge `-0.0036` maxDD `-1.6936`
- `market_context_high->commodity_24h` score `-1.7501` n `132` status `ready` deltaP `5.6858` edge `-0.0254` maxDD `-7.0012`
- `market_context_high->unknown_1h` score `-2.1385` n `133` status `ready` deltaP `-0.825` edge `-0.1137` maxDD `-1.054`
- `market_context_high->index_24h` score `-2.5957` n `132` status `ready` deltaP `-18.4537` edge `0.0005` maxDD `-2.1544`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
