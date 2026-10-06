# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-06T14:07:42.117082+00:00`
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

- `market_context_high->unknown_24h` score `738.9226` n `117` status `ready` deltaP `11.0847` edge `61.541` maxDD `-1.3748`
- `news_risk_high->crypto_major_4h` score `9.3496` n `62` status `ready` deltaP `33.3989` edge `0.5768` maxDD `-0.6258`
- `market_context_high->unknown_4h` score `6.9627` n `117` status `ready` deltaP `-0.3583` edge `0.6365` maxDD `-2.3109`
- `news_risk_high->crypto_alt_4h` score `5.4914` n `62` status `ready` deltaP `19.4286` edge `0.4625` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `3.1861` n `62` status `ready` deltaP `9.6996` edge `0.2108` maxDD `-0.1298`
- `news_risk_high->index_24h` score `3.0808` n `62` status `ready` deltaP `21.6495` edge `0.1124` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `2.6048` n `117` status `ready` deltaP `13.2583` edge `0.2251` maxDD `-4.047`
- `news_risk_high->index_4h` score `2.4589` n `62` status `ready` deltaP `27.8865` edge `0.0452` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.0631` n `62` status `ready` deltaP `8.079` edge `0.1536` maxDD `-1.5096`
- `news_risk_high->index_1h` score `1.8187` n `62` status `ready` deltaP `23.2278` edge `0.0117` maxDD `-0.1997`
- `news_risk_high->equity_4h` score `1.646` n `62` status `ready` deltaP `16.4044` edge `0.0876` maxDD `-2.7837`
- `news_risk_high->metal_4h` score `1.1545` n `62` status `ready` deltaP `16.9797` edge `0.0764` maxDD `-0.993`
- `market_context_high->commodity_4h` score `1.1385` n `117` status `ready` deltaP `15.6869` edge `0.0603` maxDD `-1.6002`
- `market_context_high->fx_4h` score `0.9774` n `117` status `ready` deltaP `20.4177` edge `0.021` maxDD `-0.3868`
- `news_risk_high->crypto_alt_1h` score `0.8394` n `62` status `ready` deltaP `3.1582` edge `0.1008` maxDD `-2.4854`
- `news_risk_high->commodity_24h` score `0.7905` n `62` status `ready` deltaP `27.0092` edge `0.0779` maxDD `-8.196`
- `market_context_high->fx_1h` score `0.7527` n `117` status `ready` deltaP `12.8423` edge `0.0055` maxDD `-0.271`
- `market_context_high->commodity_1h` score `0.6327` n `117` status `ready` deltaP `11.0075` edge `0.019` maxDD `-0.5059`
- `market_context_high->crypto_alt_4h` score `0.3665` n `117` status `ready` deltaP `-1.484` edge `0.2128` maxDD `-7.1222`
- `market_context_high->crypto_major_1h` score `-0.0526` n `117` status `ready` deltaP `7.6655` edge `0.0334` maxDD `-3.7778`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
