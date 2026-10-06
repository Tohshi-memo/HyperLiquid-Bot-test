# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-06T13:07:35.713324+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8732`

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

- `market_context_high->unknown_24h` score `506.1274` n `117` status `ready` deltaP `11.0847` edge `42.1414` maxDD `-1.3748`
- `news_risk_high->crypto_major_4h` score `9.5038` n `62` status `ready` deltaP `33.8562` edge `0.5866` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `5.6505` n `62` status `ready` deltaP `20.0384` edge `0.4717` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `3.3515` n `62` status `ready` deltaP `10.3869` edge `0.22` maxDD `-0.1298`
- `news_risk_high->index_24h` score `3.1609` n `62` status `ready` deltaP `22.3368` edge `0.1145` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `2.759` n `117` status `ready` deltaP `13.7156` edge `0.2349` maxDD `-4.047`
- `news_risk_high->index_4h` score `2.5209` n `62` status `ready` deltaP `28.4963` edge `0.0463` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.0199` n `62` status `ready` deltaP `7.9293` edge `0.151` maxDD `-1.5096`
- `news_risk_high->index_1h` score `1.8306` n `62` status `ready` deltaP `23.3775` edge `0.0117` maxDD `-0.1997`
- `news_risk_high->equity_4h` score `1.715` n `62` status `ready` deltaP `16.8618` edge `0.0903` maxDD `-2.7837`
- `market_context_high->commodity_4h` score `1.2029` n `117` status `ready` deltaP `16.2967` edge `0.0616` maxDD `-1.6002`
- `news_risk_high->metal_4h` score `1.1608` n `62` status `ready` deltaP `16.9797` edge `0.0772` maxDD `-0.993`
- `market_context_high->fx_4h` score `1.031` n `117` status `ready` deltaP `21.0275` edge `0.0214` maxDD `-0.3868`
- `news_risk_high->crypto_alt_1h` score `0.8083` n `62` status `ready` deltaP `2.8588` edge `0.1002` maxDD `-2.4854`
- `news_risk_high->commodity_24h` score `0.778` n `62` status `ready` deltaP `27.0092` edge `0.0763` maxDD `-8.196`
- `market_context_high->fx_1h` score `0.7276` n `117` status `ready` deltaP `12.5429` edge `0.0054` maxDD `-0.271`
- `market_context_high->commodity_1h` score `0.7058` n `117` status `ready` deltaP `11.6063` edge `0.0211` maxDD `-0.5059`
- `market_context_high->crypto_alt_4h` score `0.5257` n `117` status `ready` deltaP `-0.8742` edge `0.222` maxDD `-7.1222`
- `news_risk_high->metal_1h` score `-0.0564` n `62` status `ready` deltaP `4.8049` edge `0.0051` maxDD `-1.0132`
- `market_context_high->crypto_major_1h` score `-0.0958` n `117` status `ready` deltaP `7.5158` edge `0.0308` maxDD `-3.7778`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
