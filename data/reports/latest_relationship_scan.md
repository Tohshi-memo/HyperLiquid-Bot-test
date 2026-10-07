# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-07T20:07:34.592293+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8598`

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

- `market_context_high->unknown_4h` score `38.1551` n `90` status `ready` deltaP `-5.4185` edge `3.2696` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `10.8065` n `62` status `ready` deltaP `37.7498` edge `0.6692` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `7.0658` n `62` status `ready` deltaP `22.5635` edge `0.5728` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `4.5194` n `62` status `ready` deltaP `10.6764` edge `0.3154` maxDD `-0.1298`
- `news_risk_high->index_24h` score `4.2071` n `62` status `ready` deltaP `30.1038` edge `0.1499` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `3.1458` n `90` status `ready` deltaP `8.489` edge `0.6441` maxDD `-16.7906`
- `news_risk_high->index_4h` score `2.8691` n `62` status `ready` deltaP `31.7843` edge `0.0534` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.4324` n `62` status `ready` deltaP `9.8754` edge `0.1724` maxDD `-1.5096`
- `market_context_high->crypto_major_4h` score `2.3017` n `90` status `ready` deltaP `15.8143` edge `0.1828` maxDD `-4.047`
- `news_risk_high->equity_4h` score `2.0936` n `62` status `ready` deltaP `17.8745` edge `0.1151` maxDD `-2.7837`
- `news_risk_high->index_1h` score `1.9756` n `62` status `ready` deltaP `24.8745` edge `0.0138` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.4585` n `62` status `ready` deltaP `20.7099` edge `0.0905` maxDD `-0.993`
- `news_risk_high->crypto_alt_1h` score `1.173` n `62` status `ready` deltaP `3.4576` edge `0.1266` maxDD `-2.4854`
- `news_risk_high->unknown_4h` score `0.9347` n `62` status `ready` deltaP `-8.3935` edge `0.2584` maxDD `-5.6309`
- `market_context_high->metal_24h` score `0.9322` n `90` status `ready` deltaP `19.5617` edge `0.1376` maxDD `-3.5466`
- `market_context_high->fx_4h` score `0.9141` n `90` status `ready` deltaP `20.2131` edge `0.0161` maxDD `-0.3077`
- `market_context_high->fx_1h` score `0.6903` n `90` status `ready` deltaP `11.7964` edge `0.0031` maxDD `-0.271`
- `news_risk_high->metal_1h` score `0.1245` n `62` status `ready` deltaP `6.6013` edge `0.0082` maxDD `-1.0132`
- `market_context_high->crypto_major_1h` score `0.116` n `90` status `ready` deltaP `9.8037` edge `0.0384` maxDD `-3.7778`
- `market_context_high->equity_24h` score `0.0149` n `90` status `ready` deltaP `8.2391` edge `-0.0108` maxDD `-1.0977`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
