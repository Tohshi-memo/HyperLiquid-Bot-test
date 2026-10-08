# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-08T00:37:24.245593+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8574`

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

- `market_context_high->unknown_4h` score `38.5368` n `90` status `ready` deltaP `-4.3224` edge `3.2941` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `10.9197` n `62` status `ready` deltaP `38.4294` edge `0.6741` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `6.9867` n `62` status `ready` deltaP `22.325` edge `0.5678` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `5.641` n `62` status `ready` deltaP `13.7906` edge `0.3881` maxDD `-0.1298`
- `news_risk_high->index_24h` score `4.6038` n `62` status `ready` deltaP `33.218` edge `0.1622` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `4.0575` n `90` status `ready` deltaP `10.0461` edge `0.7506` maxDD `-16.7906`
- `news_risk_high->index_4h` score `2.8486` n `62` status `ready` deltaP `31.3926` edge `0.0543` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.4815` n `62` status `ready` deltaP `10.3245` edge `0.1735` maxDD `-1.5096`
- `market_context_high->crypto_major_4h` score `2.4149` n `90` status `ready` deltaP `16.4939` edge `0.1877` maxDD `-4.047`
- `news_risk_high->equity_4h` score `2.0418` n `62` status `ready` deltaP `17.1666` edge `0.1155` maxDD `-2.7837`
- `news_risk_high->index_1h` score `1.9265` n `62` status `ready` deltaP `24.2757` edge `0.0137` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.4904` n `62` status `ready` deltaP `21.248` edge `0.091` maxDD `-0.993`
- `news_risk_high->unknown_4h` score `1.3164` n `62` status `ready` deltaP `-7.2974` edge `0.2829` maxDD `-5.6309`
- `market_context_high->equity_24h` score `1.1364` n `90` status `ready` deltaP `11.3533` edge `0.0619` maxDD `-1.0977`
- `market_context_high->metal_24h` score `1.123` n `90` status `ready` deltaP `20.0807` edge `0.1586` maxDD `-3.5466`
- `news_risk_high->crypto_alt_1h` score `1.0639` n `62` status `ready` deltaP `2.7091` edge `0.1225` maxDD `-2.4854`
- `market_context_high->fx_4h` score `0.9745` n `90` status `ready` deltaP `20.7588` edge `0.0175` maxDD `-0.3077`
- `market_context_high->fx_1h` score `0.6819` n `90` status `ready` deltaP `11.6467` edge `0.0034` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.1479` n `90` status `ready` deltaP `10.2528` edge `0.0395` maxDD `-3.7778`
- `news_risk_high->metal_1h` score `0.103` n `62` status `ready` deltaP `6.3019` edge `0.0084` maxDD `-1.0132`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
