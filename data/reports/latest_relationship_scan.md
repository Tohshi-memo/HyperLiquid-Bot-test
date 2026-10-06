# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-06T13:37:35.609702+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8732`

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

- `market_context_high->unknown_24h` score `622.5346` n `117` status `ready` deltaP `11.0847` edge `51.842` maxDD `-1.3748`
- `news_risk_high->crypto_major_4h` score `9.4328` n `62` status `ready` deltaP `33.7038` edge `0.5817` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `5.5674` n `62` status `ready` deltaP `19.7335` edge `0.4668` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `3.2796` n `62` status `ready` deltaP `10.0432` edge `0.2163` maxDD `-0.1298`
- `news_risk_high->index_24h` score `3.1214` n `62` status `ready` deltaP `21.9931` edge `0.1135` maxDD `0.0`
- `market_context_high->unknown_4h` score `2.8251` n `117` status `ready` deltaP `-0.3583` edge `0.2917` maxDD `-2.3109`
- `market_context_high->crypto_major_4h` score `2.688` n `117` status `ready` deltaP `13.5632` edge `0.23` maxDD `-4.047`
- `news_risk_high->index_4h` score `2.4905` n `62` status `ready` deltaP `28.1914` edge `0.0458` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.0499` n `62` status `ready` deltaP `8.079` edge `0.1525` maxDD `-1.5096`
- `news_risk_high->index_1h` score `1.8318` n `62` status `ready` deltaP `23.3775` edge `0.0118` maxDD `-0.1997`
- `news_risk_high->equity_4h` score `1.692` n `62` status `ready` deltaP `16.7093` edge `0.0894` maxDD `-2.7837`
- `market_context_high->commodity_4h` score `1.1725` n `117` status `ready` deltaP `15.9918` edge `0.0611` maxDD `-1.6002`
- `news_risk_high->metal_4h` score `1.1577` n `62` status `ready` deltaP `16.9797` edge `0.0768` maxDD `-0.993`
- `market_context_high->fx_4h` score `1.0042` n `117` status `ready` deltaP `20.7226` edge `0.0212` maxDD `-0.3868`
- `news_risk_high->crypto_alt_1h` score `0.8071` n `62` status `ready` deltaP `2.8588` edge `0.1001` maxDD `-2.4854`
- `news_risk_high->commodity_24h` score `0.7842` n `62` status `ready` deltaP `27.0092` edge `0.0771` maxDD `-8.196`
- `market_context_high->fx_1h` score `0.7288` n `117` status `ready` deltaP `12.5429` edge `0.0055` maxDD `-0.271`
- `market_context_high->commodity_1h` score `0.6699` n `117` status `ready` deltaP `11.3069` edge `0.0201` maxDD `-0.5059`
- `market_context_high->crypto_alt_4h` score `0.4425` n `117` status `ready` deltaP `-1.1791` edge `0.2171` maxDD `-7.1222`
- `news_risk_high->metal_1h` score `-0.0588` n `62` status `ready` deltaP `4.8049` edge `0.0049` maxDD `-1.0132`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
