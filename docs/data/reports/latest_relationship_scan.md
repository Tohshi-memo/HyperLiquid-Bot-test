# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-06T14:22:38.525218+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8444`

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

- `market_context_high->unknown_24h` score `794.6566` n `117` status `ready` deltaP `11.0847` edge `66.1855` maxDD `-1.3748`
- `news_risk_high->crypto_major_4h` score `9.3026` n `62` status `ready` deltaP `33.2465` edge `0.5739` maxDD `-0.6258`
- `market_context_high->unknown_4h` score `6.8607` n `117` status `ready` deltaP `-0.3583` edge `0.628` maxDD `-2.3109`
- `news_risk_high->crypto_alt_4h` score `5.4722` n `62` status `ready` deltaP `19.4286` edge `0.4609` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `3.1717` n `62` status `ready` deltaP `9.6996` edge `0.2096` maxDD `-0.1298`
- `news_risk_high->index_24h` score `3.0796` n `62` status `ready` deltaP `21.6495` edge `0.1123` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `2.5578` n `117` status `ready` deltaP `13.1059` edge `0.2222` maxDD `-4.047`
- `news_risk_high->index_4h` score `2.4443` n `62` status `ready` deltaP `27.7341` edge `0.045` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.0439` n `62` status `ready` deltaP `7.9293` edge `0.153` maxDD `-1.5096`
- `news_risk_high->index_1h` score `1.8175` n `62` status `ready` deltaP `23.2278` edge `0.0116` maxDD `-0.1997`
- `news_risk_high->equity_4h` score `1.6254` n `62` status `ready` deltaP `16.252` edge `0.0869` maxDD `-2.7837`
- `news_risk_high->metal_4h` score `1.1553` n `62` status `ready` deltaP `16.9797` edge `0.0765` maxDD `-0.993`
- `market_context_high->commodity_4h` score `1.1203` n `117` status `ready` deltaP `15.5345` edge `0.0598` maxDD `-1.6002`
- `market_context_high->fx_4h` score `0.964` n `117` status `ready` deltaP `20.2653` edge `0.0209` maxDD `-0.3868`
- `news_risk_high->crypto_alt_1h` score `0.8418` n `62` status `ready` deltaP `3.1582` edge `0.101` maxDD `-2.4854`
- `news_risk_high->commodity_24h` score `0.7928` n `62` status `ready` deltaP `27.0092` edge `0.0782` maxDD `-8.196`
- `market_context_high->fx_1h` score `0.7659` n `117` status `ready` deltaP `12.992` edge `0.0056` maxDD `-0.271`
- `market_context_high->commodity_1h` score `0.6171` n `117` status `ready` deltaP `10.8578` edge `0.0187` maxDD `-0.5059`
- `market_context_high->crypto_alt_4h` score `0.3473` n `117` status `ready` deltaP `-1.484` edge `0.2112` maxDD `-7.1222`
- `news_risk_high->metal_1h` score `-0.0576` n `62` status `ready` deltaP `4.8049` edge `0.005` maxDD `-1.0132`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
