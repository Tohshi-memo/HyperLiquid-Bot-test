# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-07T05:52:29.053447+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8730`

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

- `market_context_high->unknown_24h` score `1160.3412` n `113` status `ready` deltaP `10.7731` edge `96.6613` maxDD `-1.3748`
- `market_context_high->unknown_4h` score `30.6157` n `113` status `ready` deltaP `-0.8714` edge `2.611` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `9.959` n `62` status `ready` deltaP `35.0757` edge `0.6164` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `6.5277` n `62` status `ready` deltaP `21.8677` edge `0.5326` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `3.6995` n `113` status `ready` deltaP `17.4765` edge `0.2882` maxDD `-4.047`
- `news_risk_high->index_24h` score `3.2169` n `62` status `ready` deltaP `22.9167` edge `0.1153` maxDD `0.0`
- `news_risk_high->index_4h` score `2.7872` n `62` status `ready` deltaP `31.2402` edge `0.0502` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.086` n `62` status `ready` deltaP `7.6299` edge `0.1585` maxDD `-1.5096`
- `news_risk_high->equity_24h` score `2.0132` n `62` status `ready` deltaP `3.6178` edge `0.1536` maxDD `-0.1298`
- `news_risk_high->index_1h` score `1.9397` n `62` status `ready` deltaP `24.5751` edge `0.0128` maxDD `-0.1997`
- `news_risk_high->equity_4h` score `1.8112` n `62` status `ready` deltaP `17.0142` edge `0.0973` maxDD `-2.7837`
- `market_context_high->crypto_alt_4h` score `1.7127` n `113` status `ready` deltaP `2.1274` edge `0.3009` maxDD `-7.1222`
- `market_context_high->crypto_major_24h` score `1.6588` n `113` status `ready` deltaP `7.7418` edge `0.384` maxDD `-16.7906`
- `news_risk_high->metal_4h` score `1.3239` n `62` status `ready` deltaP `18.9614` edge `0.0849` maxDD `-0.993`
- `news_risk_high->crypto_alt_1h` score `0.9895` n `62` status `ready` deltaP `2.7091` edge `0.1163` maxDD `-2.4854`
- `market_context_high->fx_4h` score `0.8834` n `113` status `ready` deltaP `19.5729` edge `0.0188` maxDD `-0.3868`
- `market_context_high->fx_1h` score `0.7841` n `113` status `ready` deltaP `13.2942` edge `0.0051` maxDD `-0.271`
- `news_risk_high->commodity_24h` score `0.7806` n `62` status `ready` deltaP `28.0634` edge `0.0696` maxDD `-8.196`
- `market_context_high->commodity_4h` score `0.4014` n `113` status `ready` deltaP `11.0026` edge `0.0301` maxDD `-1.6002`
- `market_context_high->crypto_major_1h` score `0.2574` n `113` status `ready` deltaP `9.4855` edge `0.0471` maxDD `-3.7778`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
