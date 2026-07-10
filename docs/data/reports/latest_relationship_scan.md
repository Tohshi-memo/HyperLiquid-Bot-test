# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-10T09:07:27.045115+00:00`
- Price records: `672`
- Market context records: `6269`
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

- `news_risk_high->crypto_alt_24h` score `15.0093` n `32` status `ready` deltaP `42.8879` edge `0.9796` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `5.941` n `32` status `ready` deltaP `50.5172` edge `0.1583` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.1781` n `32` status `ready` deltaP `43.8262` edge `0.0606` maxDD `-0.0345`
- `news_risk_high->crypto_major_24h` score `3.9039` n `32` status `ready` deltaP `16.3147` edge `0.4697` maxDD `-4.2368`
- `news_risk_high->commodity_24h` score `2.4786` n `32` status `ready` deltaP `25.7543` edge `0.0554` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.3104` n `32` status `ready` deltaP `27.8443` edge `0.0208` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `2.0163` n `199` status `ready` deltaP `2.5705` edge `0.2517` maxDD `-3.7317`
- `news_risk_high->crypto_major_1h` score `1.3283` n `32` status `ready` deltaP `13.6789` edge `0.1258` maxDD `-2.0691`
- `market_context_high->unknown_4h` score `1.2977` n `192` status `ready` deltaP `-1.3847` edge `0.3706` maxDD `-11.925`
- `news_risk_high->crypto_alt_1h` score `0.7904` n `32` status `ready` deltaP `10.5726` edge `0.077` maxDD `-1.6923`
- `market_context_high->equity_4h` score `-0.0609` n `192` status `ready` deltaP `5.1067` edge `0.0526` maxDD `-2.671`
- `news_risk_high->index_24h` score `-0.1552` n `32` status `ready` deltaP `9.3534` edge `0.0049` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.2975` n `199` status `ready` deltaP `1.0855` edge `-0.0008` maxDD `-0.5659`
- `market_context_high->metal_24h` score `-0.3494` n `192` status `ready` deltaP `17.1516` edge `0.0977` maxDD `-11.8809`
- `market_context_high->metal_4h` score `-0.4701` n `192` status `ready` deltaP `4.5859` edge `0.0279` maxDD `-3.4996`
- `market_context_high->commodity_1h` score `-0.5496` n `199` status `ready` deltaP `-0.401` edge `0.0029` maxDD `-0.682`
- `news_risk_high->metal_1h` score `-0.6819` n `32` status `ready` deltaP `-2.0958` edge `-0.0237` maxDD `-1.6464`
- `market_context_high->crypto_alt_1h` score `-0.7417` n `199` status `ready` deltaP `6.474` edge `0.037` maxDD `-9.3536`
- `market_context_high->crypto_major_1h` score `-0.8795` n `199` status `ready` deltaP `4.3353` edge `0.0351` maxDD `-9.807`
- `market_context_high->metal_1h` score `-0.8972` n `199` status `ready` deltaP `1.1705` edge `-0.0027` maxDD `-2.0564`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
