# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-07T06:07:31.419992+00:00`
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

- `market_context_high->unknown_24h` score `1158.4572` n `113` status `ready` deltaP `10.7731` edge `96.5043` maxDD `-1.3748`
- `market_context_high->unknown_4h` score `30.6205` n `113` status `ready` deltaP `-0.8714` edge `2.6114` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `9.9288` n `62` status `ready` deltaP `34.9233` edge `0.6149` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `6.5241` n `62` status `ready` deltaP `21.8677` edge `0.5323` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `3.6693` n `113` status `ready` deltaP `17.3241` edge `0.2867` maxDD `-4.047`
- `news_risk_high->index_24h` score `3.2356` n `62` status `ready` deltaP `23.0903` edge `0.1157` maxDD `0.0`
- `news_risk_high->index_4h` score `2.7994` n `62` status `ready` deltaP `31.3926` edge `0.0502` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.0656` n `62` status `ready` deltaP `7.4802` edge `0.1578` maxDD `-1.5096`
- `news_risk_high->equity_24h` score `2.0402` n `62` status `ready` deltaP `3.7915` edge `0.1547` maxDD `-0.1298`
- `news_risk_high->index_1h` score `1.9397` n `62` status `ready` deltaP `24.5751` edge `0.0128` maxDD `-0.1997`
- `news_risk_high->equity_4h` score `1.81` n `62` status `ready` deltaP `17.0142` edge `0.0972` maxDD `-2.7837`
- `market_context_high->crypto_major_24h` score `1.7242` n `113` status `ready` deltaP `7.9154` edge `0.3883` maxDD `-16.7906`
- `market_context_high->crypto_alt_4h` score `1.7091` n `113` status `ready` deltaP `2.1274` edge `0.3006` maxDD `-7.1222`
- `news_risk_high->metal_4h` score `1.3349` n `62` status `ready` deltaP `19.1139` edge `0.0853` maxDD `-0.993`
- `news_risk_high->crypto_alt_1h` score `0.9703` n `62` status `ready` deltaP `2.5594` edge `0.1157` maxDD `-2.4854`
- `market_context_high->fx_4h` score `0.8968` n `113` status `ready` deltaP `19.7254` edge `0.0189` maxDD `-0.3868`
- `market_context_high->fx_1h` score `0.7841` n `113` status `ready` deltaP `13.2942` edge `0.0051` maxDD `-0.271`
- `news_risk_high->commodity_24h` score `0.7559` n `62` status `ready` deltaP `27.8898` edge `0.0676` maxDD `-8.196`
- `market_context_high->commodity_4h` score `0.399` n `113` status `ready` deltaP `11.0026` edge `0.0299` maxDD `-1.6002`
- `market_context_high->crypto_major_1h` score `0.237` n `113` status `ready` deltaP `9.3358` edge `0.0464` maxDD `-3.7778`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
