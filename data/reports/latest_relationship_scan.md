# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-07T05:37:28.574901+00:00`
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

- `market_context_high->unknown_24h` score `1162.2216` n `113` status `ready` deltaP `10.7731` edge `96.818` maxDD `-1.3748`
- `market_context_high->unknown_4h` score `30.6181` n `113` status `ready` deltaP `-0.8714` edge `2.6112` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `9.941` n `62` status `ready` deltaP `35.0757` edge `0.6149` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `6.4771` n `62` status `ready` deltaP `21.7152` edge `0.5294` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `3.6815` n `113` status `ready` deltaP `17.4765` edge `0.2867` maxDD `-4.047`
- `news_risk_high->index_24h` score `3.1982` n `62` status `ready` deltaP `22.7431` edge `0.1149` maxDD `0.0`
- `news_risk_high->index_4h` score `2.7726` n `62` status `ready` deltaP `31.0877` edge `0.05` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.1075` n `62` status `ready` deltaP `7.7796` edge `0.1593` maxDD `-1.5096`
- `news_risk_high->equity_24h` score `1.9861` n `62` status `ready` deltaP `3.4442` edge `0.1525` maxDD `-0.1298`
- `news_risk_high->index_1h` score `1.9516` n `62` status `ready` deltaP `24.7248` edge `0.0128` maxDD `-0.1997`
- `news_risk_high->equity_4h` score `1.793` n `62` status `ready` deltaP `16.8618` edge `0.0968` maxDD `-2.7837`
- `market_context_high->crypto_alt_4h` score `1.6621` n `113` status `ready` deltaP `1.9749` edge `0.2977` maxDD `-7.1222`
- `market_context_high->crypto_major_24h` score `1.5849` n `113` status `ready` deltaP `7.5682` edge `0.379` maxDD `-16.7906`
- `news_risk_high->metal_4h` score `1.3121` n `62` status `ready` deltaP `18.809` edge `0.0844` maxDD `-0.993`
- `news_risk_high->crypto_alt_1h` score `0.9955` n `62` status `ready` deltaP `2.7091` edge `0.1168` maxDD `-2.4854`
- `market_context_high->fx_4h` score `0.87` n `113` status `ready` deltaP `19.4205` edge `0.0187` maxDD `-0.3868`
- `news_risk_high->commodity_24h` score `0.8036` n `62` status `ready` deltaP `28.2371` edge `0.0714` maxDD `-8.196`
- `market_context_high->fx_1h` score `0.7721` n `113` status `ready` deltaP `13.1445` edge `0.0051` maxDD `-0.271`
- `market_context_high->commodity_4h` score `0.416` n `113` status `ready` deltaP `11.1551` edge `0.0303` maxDD `-1.6002`
- `market_context_high->crypto_major_1h` score `0.2789` n `113` status `ready` deltaP `9.6352` edge `0.0479` maxDD `-3.7778`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
