# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-31T16:37:33.720633+00:00`
- Price records: `672`
- Market context records: `8531`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5898`

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

- `news_risk_high->unknown_24h` score `6279.9394` n `52` status `ready` deltaP `43.8702` edge `523.0779` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `5.7812` n `64` status `ready` deltaP `21.2652` edge `0.3997` maxDD `-3.4427`
- `news_risk_high->index_4h` score `2.0519` n `64` status `ready` deltaP `16.8064` edge `0.078` maxDD `-0.191`
- `news_risk_high->equity_1h` score `1.8237` n `64` status `ready` deltaP `16.4016` edge `0.0903` maxDD `-2.4803`
- `news_risk_high->crypto_major_4h` score `0.967` n `64` status `ready` deltaP `6.4405` edge `0.1586` maxDD `-3.5385`
- `news_risk_high->crypto_alt_4h` score `0.8236` n `64` status `ready` deltaP `14.7866` edge `0.1462` maxDD `-5.8012`
- `news_risk_high->crypto_alt_1h` score `0.4991` n `64` status `ready` deltaP `8.7107` edge `0.0586` maxDD `-1.8813`
- `market_context_high->crypto_alt_4h` score `0.4579` n `47` status `ready` deltaP `7.6057` edge `0.1037` maxDD `-5.323`
- `news_risk_high->crypto_major_1h` score `0.3361` n `64` status `ready` deltaP `6.6149` edge `0.0502` maxDD `-2.0972`
- `news_risk_high->fx_1h` score `0.0971` n `64` status `ready` deltaP `5.436` edge `0.0043` maxDD `-0.2475`
- `news_risk_high->metal_4h` score `0.0621` n `64` status `ready` deltaP `2.9345` edge `0.036` maxDD `-0.8085`
- `news_risk_high->index_1h` score `0.048` n `64` status `ready` deltaP `4.2197` edge `0.0097` maxDD `-0.5338`
- `news_risk_high->fx_4h` score `0.035` n `64` status `ready` deltaP `11.471` edge `0.0222` maxDD `-0.6604`
- `news_risk_high->metal_1h` score `-0.0844` n `64` status `ready` deltaP `3.7051` edge `0.0086` maxDD `-0.5599`
- `market_context_high->fx_1h` score `-0.4151` n `59` status `ready` deltaP `-0.099` edge `-0.0023` maxDD `-0.6874`
- `market_context_high->commodity_1h` score `-0.4768` n `59` status `ready` deltaP `1.398` edge `-0.0079` maxDD `-2.0038`
- `market_context_high->metal_1h` score `-0.5535` n `59` status `ready` deltaP `-1.6974` edge `-0.0102` maxDD `-1.6224`
- `market_context_high->crypto_alt_1h` score `-0.7011` n `59` status `ready` deltaP `-5.034` edge `0.0064` maxDD `-3.0178`
- `market_context_high->commodity_4h` score `-0.919` n `47` status `ready` deltaP `2.7666` edge `0.0152` maxDD `-5.4508`
- `market_context_high->index_1h` score `-0.959` n `59` status `ready` deltaP `-1.0504` edge `-0.02` maxDD `-1.5667`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
