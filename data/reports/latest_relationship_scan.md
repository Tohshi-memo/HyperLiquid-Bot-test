# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-22T07:52:30.319386+00:00`
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

- `market_context_high->unknown_4h` score `47.983` n `46` status `ready` deltaP `7.3171` edge `3.9498` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `33.6763` n `46` status `ready` deltaP `20.305` edge `2.6866` maxDD `-0.5817`
- `market_context_high->crypto_alt_24h` score `18.4598` n `46` status `ready` deltaP `19.0972` edge `1.411` maxDD `0.0`
- `market_context_high->equity_24h` score `16.8468` n `46` status `ready` deltaP `14.2286` edge `1.3191` maxDD `-0.1382`
- `news_risk_high->crypto_major_24h` score `5.9592` n `101` status `ready` deltaP `-5.0502` edge `1.2161` maxDD `-46.1999`
- `market_context_high->index_24h` score `5.6088` n `46` status `ready` deltaP `20.1314` edge `0.3419` maxDD `-0.03`
- `news_risk_high->commodity_24h` score `2.8961` n `101` status `ready` deltaP `35.6968` edge `0.2639` maxDD `-3.4467`
- `news_risk_high->crypto_alt_4h` score `2.5597` n `101` status `ready` deltaP `12.5166` edge `0.2508` maxDD `-7.675`
- `news_risk_high->crypto_alt_1h` score `2.1863` n `101` status `ready` deltaP `13.3871` edge `0.1395` maxDD `-2.058`
- `news_risk_high->crypto_major_4h` score `2.127` n `101` status `ready` deltaP `16.1751` edge `0.1952` maxDD `-8.0625`
- `market_context_high->index_4h` score `2.0745` n `46` status `ready` deltaP `24.2311` edge `0.0247` maxDD `-0.0692`
- `news_risk_high->crypto_alt_24h` score `1.9788` n `101` status `ready` deltaP `-4.6652` edge `0.6841` maxDD `-32.7147`
- `news_risk_high->crypto_major_1h` score `1.5269` n `101` status `ready` deltaP `15.0338` edge `0.0793` maxDD `-2.8494`
- `market_context_high->equity_4h` score `1.3669` n `46` status `ready` deltaP `9.206` edge `0.0832` maxDD `-0.4529`
- `market_context_high->crypto_alt_4h` score `1.0041` n `46` status `ready` deltaP `8.2118` edge `0.0884` maxDD `-2.7574`
- `market_context_high->equity_1h` score `0.93` n `46` status `ready` deltaP `7.3614` edge `0.0527` maxDD `-0.2751`
- `news_risk_high->fx_4h` score `0.8971` n `101` status `ready` deltaP `15.6529` edge `0.034` maxDD `-0.421`
- `market_context_high->index_1h` score `0.6567` n `46` status `ready` deltaP `10.3554` edge `0.011` maxDD `-0.0249`
- `news_risk_high->metal_1h` score `0.5274` n `101` status `ready` deltaP `13.6998` edge `0.0128` maxDD `-0.8144`
- `market_context_high->crypto_major_1h` score `0.439` n `46` status `ready` deltaP `0.4622` edge `0.0858` maxDD `-2.1836`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
