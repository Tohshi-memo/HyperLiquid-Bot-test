# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-19T08:52:31.394894+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8494`

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

- `news_risk_high->crypto_major_24h` score `55.3148` n `72` status `ready` deltaP `35.243` edge `4.4638` maxDD `-5.8019`
- `news_risk_high->crypto_alt_24h` score `48.3778` n `72` status `ready` deltaP `39.5834` edge `3.9055` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `36.4607` n `145` status `ready` deltaP `-2.1131` edge `3.0758` maxDD `-0.5326`
- `news_risk_high->equity_24h` score `11.4777` n `72` status `ready` deltaP `44.7917` edge `0.6621` maxDD `-0.0053`
- `risk_on_high->unknown_4h` score `8.2759` n `52` status `ready` deltaP `-9.076` edge `0.7727` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `8.2759` n `52` status `ready` deltaP `-9.076` edge `0.7727` maxDD `-0.4694`
- `risk_on_high->commodity_24h` score `8.2388` n `52` status `ready` deltaP `44.9653` edge `0.3868` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.2388` n `52` status `ready` deltaP `44.9653` edge `0.3868` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.0029` n `145` status `ready` deltaP `38.0687` edge `0.3823` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `6.7289` n `81` status `ready` deltaP `23.0974` edge `0.5277` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `4.6161` n `81` status `ready` deltaP `19.9883` edge `0.3772` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `3.3477` n `81` status `ready` deltaP `17.6` edge `0.2082` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.7168` n `81` status `ready` deltaP `20.9673` edge `0.1389` maxDD `-2.8494`
- `risk_on_high->commodity_4h` score `2.6319` n `52` status `ready` deltaP `31.3203` edge `0.0455` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.6319` n `52` status `ready` deltaP `31.3203` edge `0.0455` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.4917` n `145` status `ready` deltaP `27.2487` edge `0.0678` maxDD `-0.345`
- `news_risk_high->metal_24h` score `1.8463` n `72` status `ready` deltaP `24.1319` edge `0.0774` maxDD `-2.4203`
- `news_risk_high->fx_4h` score `1.2838` n `81` status `ready` deltaP `14.4554` edge `0.0325` maxDD `-0.084`
- `market_context_high->commodity_1h` score `1.0294` n `145` status `ready` deltaP `15.2819` edge `0.0216` maxDD `-0.3491`
- `news_risk_high->equity_1h` score `0.7988` n `81` status `ready` deltaP `9.8581` edge `0.0414` maxDD `-0.9112`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
