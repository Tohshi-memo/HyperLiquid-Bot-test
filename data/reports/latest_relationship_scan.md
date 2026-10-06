# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-06T16:37:35.646914+00:00`
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

- `market_context_high->unknown_24h` score `1599.8326` n `117` status `ready` deltaP `11.0847` edge `133.2835` maxDD `-1.3748`
- `market_context_high->unknown_4h` score `27.9183` n `117` status `ready` deltaP `-0.3583` edge `2.3828` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `8.9441` n `62` status `ready` deltaP `32.4843` edge `0.5491` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `5.1028` n `62` status `ready` deltaP `18.6664` edge `0.4352` maxDD `-6.4195`
- `news_risk_high->index_24h` score `3.0724` n `62` status `ready` deltaP `21.6495` edge `0.1117` maxDD `0.0`
- `news_risk_high->equity_24h` score `2.9403` n `62` status `ready` deltaP `9.0123` edge `0.1949` maxDD `-0.1298`
- `news_risk_high->index_4h` score `2.3737` n `62` status `ready` deltaP `26.9719` edge `0.0442` maxDD `-0.4296`
- `market_context_high->crypto_major_4h` score `2.1992` n `117` status `ready` deltaP `12.3437` edge `0.1974` maxDD `-4.047`
- `news_risk_high->crypto_major_1h` score `1.9156` n `62` status `ready` deltaP `7.3305` edge `0.1463` maxDD `-1.5096`
- `news_risk_high->index_1h` score `1.8031` n `62` status `ready` deltaP `23.0781` edge `0.0114` maxDD `-0.1997`
- `news_risk_high->equity_4h` score `1.433` n `62` status `ready` deltaP `15.0325` edge `0.079` maxDD `-2.7837`
- `news_risk_high->metal_4h` score `1.1751` n `62` status `ready` deltaP `17.2846` edge `0.077` maxDD `-0.993`
- `market_context_high->commodity_4h` score `0.9946` n `117` status `ready` deltaP `14.7723` edge `0.0544` maxDD `-1.6002`
- `news_risk_high->commodity_24h` score `0.901` n `62` status `ready` deltaP `28.0402` edge `0.0852` maxDD `-8.196`
- `market_context_high->fx_4h` score `0.8958` n `117` status `ready` deltaP `19.5031` edge `0.0203` maxDD `-0.3868`
- `news_risk_high->crypto_alt_1h` score `0.7651` n `62` status `ready` deltaP `2.8588` edge `0.0966` maxDD `-2.4854`
- `market_context_high->fx_1h` score `0.7408` n `117` status `ready` deltaP `12.6926` edge `0.0055` maxDD `-0.271`
- `market_context_high->commodity_1h` score `0.6207` n `117` status `ready` deltaP `11.0075` edge `0.018` maxDD `-0.5059`
- `market_context_high->crypto_alt_4h` score `-0.022` n `117` status `ready` deltaP `-2.2462` edge `0.1855` maxDD `-7.1222`
- `news_risk_high->metal_1h` score `-0.0804` n `62` status `ready` deltaP `4.6552` edge `0.0041` maxDD `-1.0132`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
