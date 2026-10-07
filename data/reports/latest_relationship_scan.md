# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-07T05:07:38.026468+00:00`
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

- `market_context_high->unknown_24h` score `1165.8924` n `113` status `ready` deltaP `10.7731` edge `97.1239` maxDD `-1.3748`
- `market_context_high->unknown_4h` score `30.4981` n `113` status `ready` deltaP `-0.8714` edge `2.6012` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `9.8676` n `62` status `ready` deltaP `34.9233` edge `0.6098` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `6.3363` n `62` status `ready` deltaP `21.4103` edge `0.5197` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `3.6081` n `113` status `ready` deltaP `17.3241` edge `0.2816` maxDD `-4.047`
- `news_risk_high->index_24h` score `3.1621` n `62` status `ready` deltaP `22.3958` edge `0.1142` maxDD `0.0`
- `news_risk_high->index_4h` score `2.7446` n `62` status `ready` deltaP `30.7829` edge `0.0497` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.1159` n `62` status `ready` deltaP `7.7796` edge `0.16` maxDD `-1.5096`
- `news_risk_high->equity_24h` score `1.9355` n `62` status `ready` deltaP `3.097` edge `0.1506` maxDD `-0.1298`
- `news_risk_high->index_1h` score `1.9265` n `62` status `ready` deltaP `24.4254` edge `0.0127` maxDD `-0.1997`
- `news_risk_high->equity_4h` score `1.7458` n `62` status `ready` deltaP `16.5569` edge `0.0949` maxDD `-2.7837`
- `market_context_high->crypto_alt_4h` score `1.5213` n `113` status `ready` deltaP `1.67` edge `0.288` maxDD `-7.1222`
- `market_context_high->crypto_major_24h` score `1.4215` n `113` status `ready` deltaP `7.2209` edge `0.3677` maxDD `-16.7906`
- `news_risk_high->metal_4h` score `1.2869` n `62` status `ready` deltaP `18.5041` edge `0.0832` maxDD `-0.993`
- `news_risk_high->crypto_alt_1h` score `0.9919` n `62` status `ready` deltaP `2.7091` edge `0.1165` maxDD `-2.4854`
- `news_risk_high->commodity_24h` score `0.849` n `62` status `ready` deltaP `28.5843` edge `0.0749` maxDD `-8.196`
- `market_context_high->fx_4h` score `0.8432` n `113` status `ready` deltaP `19.1156` edge `0.0185` maxDD `-0.3868`
- `market_context_high->fx_1h` score `0.7458` n `113` status `ready` deltaP `12.8451` edge `0.0049` maxDD `-0.271`
- `market_context_high->commodity_4h` score `0.4476` n `113` status `ready` deltaP `11.4599` edge `0.0309` maxDD `-1.6002`
- `market_context_high->crypto_major_1h` score `0.2873` n `113` status `ready` deltaP `9.6352` edge `0.0486` maxDD `-3.7778`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
