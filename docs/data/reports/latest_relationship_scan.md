# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-06T19:07:32.385288+00:00`
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

- `market_context_high->unknown_24h` score `1523.4766` n `117` status `ready` deltaP `11.0847` edge `126.9205` maxDD `-1.3748`
- `market_context_high->unknown_4h` score `28.7463` n `117` status `ready` deltaP `-0.3583` edge `2.4518` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `9.1127` n `62` status `ready` deltaP `32.9416` edge `0.5601` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `5.2366` n `62` status `ready` deltaP `19.1238` edge `0.4433` maxDD `-6.4195`
- `news_risk_high->index_24h` score `3.0964` n `62` status `ready` deltaP `21.6495` edge `0.1137` maxDD `0.0`
- `news_risk_high->equity_24h` score `2.6695` n `62` status `ready` deltaP `7.6377` edge `0.1815` maxDD `-0.1298`
- `news_risk_high->index_4h` score `2.5221` n `62` status `ready` deltaP `28.4963` edge `0.0464` maxDD `-0.4296`
- `market_context_high->crypto_major_4h` score `2.3678` n `117` status `ready` deltaP `12.801` edge `0.2084` maxDD `-4.047`
- `news_risk_high->crypto_major_1h` score `1.8784` n `62` status `ready` deltaP `7.1808` edge `0.1442` maxDD `-1.5096`
- `news_risk_high->index_1h` score `1.8318` n `62` status `ready` deltaP `23.3775` edge `0.0118` maxDD `-0.1997`
- `news_risk_high->equity_4h` score `1.451` n `62` status `ready` deltaP `15.0325` edge `0.0805` maxDD `-2.7837`
- `news_risk_high->metal_4h` score `1.197` n `62` status `ready` deltaP `17.437` edge `0.0788` maxDD `-0.993`
- `news_risk_high->commodity_24h` score `0.9695` n `62` status `ready` deltaP `29.0711` edge `0.0871` maxDD `-8.196`
- `market_context_high->fx_4h` score `0.8556` n `117` status `ready` deltaP `19.0458` edge `0.02` maxDD `-0.3868`
- `market_context_high->commodity_4h` score `0.7406` n `117` status `ready` deltaP `13.2479` edge `0.0434` maxDD `-1.6002`
- `market_context_high->fx_1h` score `0.7024` n `117` status `ready` deltaP `12.2435` edge `0.0053` maxDD `-0.271`
- `news_risk_high->crypto_alt_1h` score `0.6763` n `62` status `ready` deltaP `2.5594` edge `0.0912` maxDD `-2.4854`
- `market_context_high->commodity_1h` score `0.4937` n `117` status `ready` deltaP `9.8099` edge `0.0154` maxDD `-0.5059`
- `market_context_high->crypto_alt_4h` score `0.1118` n `117` status `ready` deltaP `-1.7888` edge `0.1936` maxDD `-7.1222`
- `news_risk_high->metal_1h` score `-0.1067` n `62` status `ready` deltaP `4.3558` edge `0.0039` maxDD `-1.0132`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
