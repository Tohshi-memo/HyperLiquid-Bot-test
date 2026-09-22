# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-22T12:52:49.707993+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9954`

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

- `market_context_high->unknown_4h` score `46.9294` n `46` status `ready` deltaP `7.3171` edge `3.862` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `31.5254` n `46` status `ready` deltaP `16.8328` edge `2.5305` maxDD `-0.5817`
- `market_context_high->crypto_alt_24h` score `16.6702` n `46` status `ready` deltaP `15.9722` edge `1.2827` maxDD `0.0`
- `market_context_high->equity_24h` score `16.3798` n `46` status `ready` deltaP `12.6661` edge `1.2906` maxDD `-0.1382`
- `market_context_high->index_24h` score `5.5584` n `46` status `ready` deltaP `20.1314` edge `0.3377` maxDD `-0.03`
- `news_risk_high->crypto_major_24h` score `3.8082` n `101` status `ready` deltaP `-8.5224` edge `1.06` maxDD `-46.1999`
- `news_risk_high->commodity_24h` score `3.2263` n `101` status `ready` deltaP `38.8218` edge `0.2854` maxDD `-3.4467`
- `news_risk_high->crypto_alt_4h` score `2.3901` n `101` status `ready` deltaP `12.2117` edge `0.2387` maxDD `-7.675`
- `news_risk_high->crypto_alt_1h` score `2.203` n `101` status `ready` deltaP `13.5368` edge `0.1399` maxDD `-2.058`
- `market_context_high->index_4h` score `2.0161` n `46` status `ready` deltaP `23.6214` edge `0.0239` maxDD `-0.0692`
- `news_risk_high->crypto_major_4h` score `1.7463` n `101` status `ready` deltaP `14.9556` edge `0.1716` maxDD `-8.0625`
- `news_risk_high->crypto_major_1h` score `1.5245` n `101` status `ready` deltaP `15.1835` edge `0.0781` maxDD `-2.8494`
- `market_context_high->equity_4h` score `1.1738` n `46` status `ready` deltaP `8.2914` edge `0.0732` maxDD `-0.4529`
- `news_risk_high->fx_4h` score `1.0526` n `101` status `ready` deltaP `17.1773` edge `0.0368` maxDD `-0.421`
- `market_context_high->equity_1h` score `0.9972` n `46` status `ready` deltaP `7.9602` edge `0.0543` maxDD `-0.2751`
- `market_context_high->metal_24h` score `0.86` n `46` status `ready` deltaP `21.0523` edge `-0.0453` maxDD `-0.2042`
- `market_context_high->crypto_alt_4h` score `0.8345` n `46` status `ready` deltaP `7.9069` edge `0.0763` maxDD `-2.7574`
- `market_context_high->index_1h` score `0.7358` n `46` status `ready` deltaP `11.2536` edge `0.0116` maxDD `-0.0249`
- `news_risk_high->metal_1h` score `0.6077` n `101` status `ready` deltaP `14.598` edge `0.0135` maxDD `-0.8144`
- `market_context_high->crypto_major_1h` score `0.4366` n `46` status `ready` deltaP `0.6119` edge `0.0846` maxDD `-2.1836`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
