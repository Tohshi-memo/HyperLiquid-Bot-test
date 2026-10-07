# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-07T00:23:06.819785+00:00`
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

- `market_context_high->unknown_24h` score `1407.6532` n `117` status `ready` deltaP `11.3782` edge `117.2666` maxDD `-1.3748`
- `market_context_high->unknown_4h` score `28.8901` n `117` status `ready` deltaP `-0.5107` edge `2.4648` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `9.3374` n `62` status `ready` deltaP `34.1611` edge `0.5707` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `5.4585` n `62` status `ready` deltaP `20.0384` edge `0.4557` maxDD `-6.4195`
- `news_risk_high->index_24h` score `3.1151` n `62` status `ready` deltaP `22.0486` edge `0.1126` maxDD `0.0`
- `news_risk_high->index_4h` score `2.6838` n `62` status `ready` deltaP `30.1731` edge `0.0487` maxDD `-0.4296`
- `market_context_high->crypto_major_4h` score `2.5926` n `117` status `ready` deltaP `14.0205` edge `0.219` maxDD `-4.047`
- `news_risk_high->equity_24h` score `2.1107` n `62` status `ready` deltaP `4.3123` edge `0.1571` maxDD `-0.1298`
- `news_risk_high->crypto_major_1h` score `1.9827` n `62` status `ready` deltaP `7.7796` edge `0.1489` maxDD `-1.5096`
- `news_risk_high->index_1h` score `1.9121` n `62` status `ready` deltaP `24.2757` edge `0.0125` maxDD `-0.1997`
- `news_risk_high->equity_4h` score `1.6546` n `62` status `ready` deltaP `16.5569` edge `0.0873` maxDD `-2.7837`
- `news_risk_high->metal_4h` score `1.1977` n `62` status `ready` deltaP `17.2846` edge `0.0799` maxDD `-0.993`
- `news_risk_high->commodity_24h` score `1.0092` n `62` status `ready` deltaP `29.6259` edge `0.0885` maxDD `-8.196`
- `market_context_high->fx_4h` score `0.9044` n `117` status `ready` deltaP `19.6555` edge `0.02` maxDD `-0.3868`
- `news_risk_high->crypto_alt_1h` score `0.7364` n `62` status `ready` deltaP `2.4097` edge `0.0972` maxDD `-2.4854`
- `market_context_high->fx_1h` score `0.7252` n `117` status `ready` deltaP `12.5429` edge `0.0052` maxDD `-0.271`
- `market_context_high->commodity_4h` score `0.5764` n `117` status `ready` deltaP `12.4857` edge `0.0348` maxDD `-1.6002`
- `market_context_high->commodity_1h` score `0.3583` n `117` status `ready` deltaP `8.4626` edge `0.0131` maxDD `-0.5059`
- `market_context_high->crypto_alt_4h` score `0.3337` n `117` status `ready` deltaP `-0.8742` edge `0.206` maxDD `-7.1222`
- `market_context_high->crypto_major_24h` score `0.0987` n `117` status `ready` deltaP `4.9813` edge `0.2724` maxDD `-16.7906`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
