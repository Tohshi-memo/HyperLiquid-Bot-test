# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-07T00:37:48.376403+00:00`
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

- `market_context_high->unknown_24h` score `1405.4692` n `117` status `ready` deltaP `11.3782` edge `117.0846` maxDD `-1.3748`
- `market_context_high->unknown_4h` score `28.9119` n `117` status `ready` deltaP `-0.3583` edge `2.4656` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `9.3532` n `62` status `ready` deltaP `34.3135` edge `0.571` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `5.4791` n `62` status `ready` deltaP `20.1908` edge `0.4564` maxDD `-6.4195`
- `news_risk_high->index_24h` score `3.1` n `62` status `ready` deltaP `21.875` edge `0.1125` maxDD `0.0`
- `news_risk_high->index_4h` score `2.6692` n `62` status `ready` deltaP `30.0207` edge `0.0485` maxDD `-0.4296`
- `market_context_high->crypto_major_4h` score `2.6084` n `117` status `ready` deltaP `14.1729` edge `0.2193` maxDD `-4.047`
- `news_risk_high->equity_24h` score `2.08` n `62` status `ready` deltaP `4.1387` edge `0.1557` maxDD `-0.1298`
- `news_risk_high->crypto_major_1h` score `1.9672` n `62` status `ready` deltaP `7.6299` edge `0.1486` maxDD `-1.5096`
- `news_risk_high->index_1h` score `1.9109` n `62` status `ready` deltaP `24.2757` edge `0.0124` maxDD `-0.1997`
- `news_risk_high->equity_4h` score `1.634` n `62` status `ready` deltaP `16.4044` edge `0.0866` maxDD `-2.7837`
- `news_risk_high->metal_4h` score `1.1977` n `62` status `ready` deltaP `17.2846` edge `0.0799` maxDD `-0.993`
- `news_risk_high->commodity_24h` score `1.0053` n `62` status `ready` deltaP `29.6259` edge `0.088` maxDD `-8.196`
- `market_context_high->fx_4h` score `0.891` n `117` status `ready` deltaP `19.5031` edge `0.0199` maxDD `-0.3868`
- `news_risk_high->crypto_alt_1h` score `0.7316` n `62` status `ready` deltaP `2.4097` edge `0.0968` maxDD `-2.4854`
- `market_context_high->fx_1h` score `0.7132` n `117` status `ready` deltaP `12.3932` edge `0.0052` maxDD `-0.271`
- `market_context_high->commodity_4h` score `0.5752` n `117` status `ready` deltaP `12.4857` edge `0.0347` maxDD `-1.6002`
- `market_context_high->crypto_alt_4h` score `0.3543` n `117` status `ready` deltaP `-0.7218` edge `0.2067` maxDD `-7.1222`
- `market_context_high->commodity_1h` score `0.3451` n `117` status `ready` deltaP `8.3129` edge `0.013` maxDD `-0.5059`
- `market_context_high->crypto_major_24h` score `0.1498` n `117` status `ready` deltaP `5.1549` edge `0.2755` maxDD `-16.7906`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
