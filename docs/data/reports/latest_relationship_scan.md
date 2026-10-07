# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-07T17:52:34.397151+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8742`

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

- `market_context_high->unknown_4h` score `37.9414` n `90` status `ready` deltaP `-5.5994` edge `3.253` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `10.8805` n `62` status `ready` deltaP `37.9841` edge `0.6738` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `7.4277` n `62` status `ready` deltaP `23.7132` edge `0.5953` maxDD `-6.4195`
- `news_risk_high->index_24h` score `4.1272` n `62` status `ready` deltaP `29.5848` edge `0.1467` maxDD `0.0`
- `news_risk_high->equity_24h` score `4.1028` n `62` status `ready` deltaP `9.6384` edge `0.2876` maxDD `-0.1298`
- `news_risk_high->index_4h` score `3.0033` n `62` status `ready` deltaP `33.0866` edge `0.0559` maxDD `-0.4296`
- `market_context_high->crypto_major_24h` score `2.7776` n `90` status `ready` deltaP `8.143` edge `0.5992` maxDD `-16.7906`
- `news_risk_high->crypto_major_1h` score `2.4875` n `62` status `ready` deltaP `10.1748` edge `0.175` maxDD `-1.5096`
- `market_context_high->crypto_major_4h` score `2.3756` n `90` status `ready` deltaP `16.0486` edge `0.1874` maxDD `-4.047`
- `news_risk_high->equity_4h` score `2.2477` n `62` status `ready` deltaP `19.0362` edge `0.1202` maxDD `-2.7837`
- `news_risk_high->index_1h` score `2.0295` n `62` status `ready` deltaP `25.4733` edge `0.0143` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.4251` n `62` status `ready` deltaP `20.1735` edge `0.0898` maxDD `-0.993`
- `news_risk_high->crypto_alt_1h` score `1.3313` n `62` status `ready` deltaP `4.2061` edge `0.1348` maxDD `-2.4854`
- `market_context_high->fx_4h` score `0.856` n `90` status `ready` deltaP `19.517` edge `0.0159` maxDD `-0.3077`
- `market_context_high->metal_24h` score `0.8256` n `90` status `ready` deltaP `19.0426` edge `0.1274` maxDD `-3.5466`
- `market_context_high->fx_1h` score `0.7765` n `90` status `ready` deltaP `12.8443` edge `0.0033` maxDD `-0.271`
- `news_risk_high->unknown_4h` score `0.721` n `62` status `ready` deltaP `-8.5744` edge `0.2418` maxDD `-5.6309`
- `market_context_high->crypto_major_1h` score `0.1518` n `90` status `ready` deltaP `10.1031` edge `0.041` maxDD `-3.7778`
- `news_risk_high->metal_1h` score `0.0922` n `62` status `ready` deltaP `6.3019` edge `0.0075` maxDD `-1.0132`
- `market_context_high->commodity_1h` score `0.0228` n `90` status `ready` deltaP `4.6806` edge `0.0083` maxDD `-0.3417`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
