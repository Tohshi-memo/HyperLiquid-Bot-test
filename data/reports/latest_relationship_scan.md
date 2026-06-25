# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-25T20:34:40.877337+00:00`
- Price records: `672`
- Market context records: `4757`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7476`

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

- `market_context_high->unknown_1h` score `7.0693` n `135` status `ready` deltaP `12.79` edge `0.5456` maxDD `-1.674`
- `market_context_high->unknown_4h` score `6.3673` n `132` status `ready` deltaP `14.5279` edge `0.5548` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `3.0341` n `120` status `ready` deltaP `14.8611` edge `0.2461` maxDD `-4.7201`
- `market_context_high->index_4h` score `-0.3741` n `132` status `ready` deltaP `7.7282` edge `0.0074` maxDD `-5.5505`
- `market_context_high->equity_4h` score `-0.4607` n `132` status `ready` deltaP `7.1138` edge `0.0621` maxDD `-8.8203`
- `market_context_high->commodity_1h` score `-0.577` n `135` status `ready` deltaP `1.6068` edge `0.0208` maxDD `-2.0345`
- `market_context_high->fx_4h` score `-0.7016` n `132` status `ready` deltaP `-0.4481` edge `-0.001` maxDD `-1.5439`
- `market_context_high->equity_1h` score `-0.9095` n `135` status `ready` deltaP `-1.2686` edge `-0.0175` maxDD `-5.2521`
- `market_context_high->commodity_4h` score `-1.0471` n `132` status `ready` deltaP `8.2363` edge `0.0257` maxDD `-8.0963`
- `market_context_high->fx_1h` score `-1.1179` n `135` status `ready` deltaP `-3.6017` edge `-0.0042` maxDD `-0.8626`
- `market_context_high->index_1h` score `-1.5582` n `135` status `ready` deltaP `-3.2147` edge `-0.008` maxDD `-2.6999`
- `market_context_high->metal_1h` score `-2.5095` n `135` status `ready` deltaP `-2.9951` edge `-0.0699` maxDD `-15.2153`
- `market_context_high->commodity_24h` score `-2.5127` n `120` status `ready` deltaP `17.4653` edge `0.0723` maxDD `-27.5371`
- `market_context_high->crypto_alt_1h` score `-2.8518` n `135` status `ready` deltaP `-1.1034` edge `-0.0604` maxDD `-19.8288`
- `market_context_high->crypto_major_1h` score `-3.3143` n `135` status `ready` deltaP `-0.4968` edge `-0.0785` maxDD `-24.7815`
- `market_context_high->fx_24h` score `-4.1126` n `120` status `ready` deltaP `-15.3473` edge `-0.021` maxDD `-4.2191`
- `market_context_high->crypto_alt_4h` score `-5.3963` n `132` status `ready` deltaP `2.282` edge `-0.039` maxDD `-48.1101`
- `market_context_high->index_24h` score `-6.9154` n `120` status `ready` deltaP `-11.0764` edge `-0.1145` maxDD `-22.3683`
- `market_context_high->crypto_major_4h` score `-8.1471` n `132` status `ready` deltaP `3.0442` edge `-0.1417` maxDD `-68.5143`
- `market_context_high->metal_4h` score `-8.309` n `132` status `ready` deltaP `4.878` edge `-0.2737` maxDD `-61.2596`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
