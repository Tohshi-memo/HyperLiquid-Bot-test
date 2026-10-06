# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-06T15:07:35.501803+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8684`

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

- `market_context_high->unknown_24h` score `948.2218` n `117` status `ready` deltaP `11.0847` edge `78.9826` maxDD `-1.3748`
- `market_context_high->unknown_4h` score `15.4923` n `117` status `ready` deltaP `-0.3583` edge `1.3473` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `9.1269` n `62` status `ready` deltaP `32.7892` edge `0.5623` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `5.3156` n `62` status `ready` deltaP `18.9713` edge `0.4509` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `3.1333` n `62` status `ready` deltaP `9.6996` edge `0.2064` maxDD `-0.1298`
- `news_risk_high->index_24h` score `3.076` n `62` status `ready` deltaP `21.6495` edge `0.112` maxDD `0.0`
- `news_risk_high->index_4h` score `2.4005` n `62` status `ready` deltaP `27.2768` edge `0.0444` maxDD `-0.4296`
- `market_context_high->crypto_major_4h` score `2.382` n `117` status `ready` deltaP `12.6486` edge `0.2106` maxDD `-4.047`
- `news_risk_high->crypto_major_1h` score `1.9948` n `62` status `ready` deltaP `7.6299` edge `0.1509` maxDD `-1.5096`
- `news_risk_high->index_1h` score `1.8055` n `62` status `ready` deltaP `23.0781` edge `0.0116` maxDD `-0.1997`
- `news_risk_high->equity_4h` score `1.5528` n `62` status `ready` deltaP `15.7947` edge `0.0839` maxDD `-2.7837`
- `news_risk_high->metal_4h` score `1.1466` n `62` status `ready` deltaP `16.8273` edge `0.0764` maxDD `-0.993`
- `market_context_high->commodity_4h` score `1.0997` n `117` status `ready` deltaP `15.382` edge `0.0591` maxDD `-1.6002`
- `market_context_high->fx_4h` score `0.9238` n `117` status `ready` deltaP `19.808` edge `0.0206` maxDD `-0.3868`
- `news_risk_high->commodity_24h` score `0.8252` n `62` status `ready` deltaP `27.1811` edge `0.0812` maxDD `-8.196`
- `news_risk_high->crypto_alt_1h` score `0.8023` n `62` status `ready` deltaP `2.8588` edge `0.0997` maxDD `-2.4854`
- `market_context_high->fx_1h` score `0.7659` n `117` status `ready` deltaP `12.992` edge `0.0056` maxDD `-0.271`
- `market_context_high->commodity_1h` score `0.6303` n `117` status `ready` deltaP `11.0075` edge `0.0188` maxDD `-0.5059`
- `market_context_high->crypto_alt_4h` score `0.1908` n `117` status `ready` deltaP `-1.9413` edge `0.2012` maxDD `-7.1222`
- `news_risk_high->metal_1h` score `-0.042` n `62` status `ready` deltaP `4.9546` edge `0.0053` maxDD `-1.0132`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
