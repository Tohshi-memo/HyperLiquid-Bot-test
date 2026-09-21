# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-21T08:37:27.825009+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9168`

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

- `market_context_high->unknown_4h` score `33.2809` n `58` status `ready` deltaP `1.23` edge `2.7802` maxDD `-0.5326`
- `news_risk_high->crypto_major_24h` score `22.993` n `101` status `ready` deltaP `10.922` edge `2.5291` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `17.7094` n `101` status `ready` deltaP `11.307` edge `1.8885` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `4.1921` n `101` status `ready` deltaP `18.4617` edge `0.3472` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `3.8707` n `101` status `ready` deltaP `20.9007` edge `0.309` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `2.6407` n `101` status `ready` deltaP `15.7823` edge `0.1614` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.0305` n `101` status `ready` deltaP `17.7284` edge `0.1033` maxDD `-2.8494`
- `news_risk_high->commodity_24h` score `1.1256` n `101` status `ready` deltaP `23.0232` edge `0.1214` maxDD `-3.4467`
- `market_context_high->equity_1h` score `0.8546` n `58` status `ready` deltaP `6.4578` edge `0.0535` maxDD `-0.36`
- `market_context_high->index_1h` score `0.7064` n `58` status `ready` deltaP `10.5771` edge `0.0139` maxDD `-0.0435`
- `news_risk_high->metal_1h` score `0.537` n `101` status `ready` deltaP `13.8495` edge `0.0126` maxDD `-0.8144`
- `market_context_high->fx_1h` score `0.3462` n `58` status `ready` deltaP `8.7756` edge `0.006` maxDD `-0.1854`
- `news_risk_high->metal_4h` score `0.3443` n `101` status `ready` deltaP `15.2695` edge `0.0323` maxDD `-2.0994`
- `market_context_high->index_4h` score `0.3137` n `58` status `ready` deltaP `14.4764` edge `0.0074` maxDD `-1.0949`
- `market_context_high->metal_1h` score `0.2591` n `58` status `ready` deltaP `5.3996` edge `0.0164` maxDD `-0.1314`
- `news_risk_high->fx_4h` score `0.2491` n `101` status `ready` deltaP `9.098` edge `0.0237` maxDD `-0.421`
- `news_risk_high->fx_1h` score `-0.2028` n `101` status `ready` deltaP `3.1422` edge `0.0065` maxDD `-0.2147`
- `news_risk_high->equity_1h` score `-0.2202` n `101` status `ready` deltaP `2.0706` edge `0.0084` maxDD `-0.9112`
- `market_context_high->crypto_major_1h` score `-0.2545` n `58` status `ready` deltaP `-2.0906` edge `0.0646` maxDD `-2.7494`
- `news_risk_high->metal_24h` score `-0.4361` n `101` status `ready` deltaP `9.2564` edge `-0.0332` maxDD `-2.4203`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
