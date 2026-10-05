# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-05T09:22:35.237243+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8300`

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

- `market_context_high->unknown_1h` score `72.6222` n `124` status `ready` deltaP `-0.6422` edge `6.0976` maxDD `-0.9839`
- `market_context_high->unknown_4h` score `57.5598` n `112` status `ready` deltaP `-0.6315` edge `4.8465` maxDD `-1.6513`
- `market_context_high->crypto_major_24h` score `10.9292` n `81` status `ready` deltaP `29.8032` edge `0.7257` maxDD `-0.423`
- `news_risk_high->crypto_major_4h` score `9.3371` n `65` status `ready` deltaP `32.5516` edge `0.5814` maxDD `-0.6258`
- `market_context_high->crypto_alt_24h` score `7.1394` n `81` status `ready` deltaP `25.3666` edge `0.4878` maxDD `-2.9571`
- `news_risk_high->crypto_alt_4h` score `5.8248` n `65` status `ready` deltaP `19.7866` edge `0.4879` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `3.5565` n `112` status `ready` deltaP `15.2439` edge `0.2745` maxDD `-4.047`
- `news_risk_high->index_24h` score `3.3584` n `65` status `ready` deltaP `23.7847` edge `0.1213` maxDD `0.0`
- `news_risk_high->equity_24h` score `3.1927` n `65` status `ready` deltaP `11.3809` edge `0.2002` maxDD `-0.1344`
- `news_risk_high->index_4h` score `2.9157` n `65` status `ready` deltaP `32.0662` edge `0.0554` maxDD `-0.4296`
- `news_risk_high->equity_4h` score `2.5228` n `65` status `ready` deltaP `20.272` edge `0.1361` maxDD `-2.881`
- `news_risk_high->crypto_major_1h` score `2.4017` n `65` status `ready` deltaP `9.567` edge `0.1719` maxDD `-1.5096`
- `news_risk_high->index_1h` score `2.0471` n `65` status `ready` deltaP `25.3178` edge `0.0168` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.903` n `65` status `ready` deltaP `17.8588` edge `0.0811` maxDD `-0.993`
- `market_context_high->fx_4h` score `1.3648` n `112` status `ready` deltaP `24.6298` edge `0.0252` maxDD `-0.3868`
- `news_risk_high->crypto_alt_1h` score `1.051` n `65` status `ready` deltaP `3.0723` edge `0.119` maxDD `-2.4854`
- `market_context_high->fx_1h` score `0.8671` n `124` status `ready` deltaP `14.2264` edge `0.0058` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.8496` n `124` status `ready` deltaP `10.3487` edge `0.0907` maxDD `-3.7778`
- `market_context_high->crypto_alt_4h` score `0.628` n `112` status `ready` deltaP `2.2866` edge `0.216` maxDD `-7.6465`
- `news_risk_high->commodity_24h` score `0.548` n `65` status `ready` deltaP `24.9119` edge `0.1073` maxDD `-10.9169`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
