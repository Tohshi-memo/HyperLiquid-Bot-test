# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-22T07:07:30.939282+00:00`
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

- `market_context_high->unknown_4h` score `48.379` n `46` status `ready` deltaP `7.3171` edge `3.9828` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `34.1176` n `46` status `ready` deltaP `20.8258` edge `2.7199` maxDD `-0.5817`
- `market_context_high->crypto_alt_24h` score `18.8566` n `46` status `ready` deltaP `19.6181` edge `1.4406` maxDD `0.0`
- `market_context_high->equity_24h` score `16.9176` n `46` status `ready` deltaP `14.2286` edge `1.325` maxDD `-0.1382`
- `news_risk_high->crypto_major_24h` score `6.4005` n `101` status `ready` deltaP `-4.5294` edge `1.2494` maxDD `-46.1999`
- `market_context_high->index_24h` score `5.6172` n `46` status `ready` deltaP `20.1314` edge `0.3426` maxDD `-0.03`
- `news_risk_high->commodity_24h` score `2.8816` n `101` status `ready` deltaP `35.5232` edge `0.2632` maxDD `-3.4467`
- `news_risk_high->crypto_alt_4h` score `2.6081` n `101` status `ready` deltaP `12.8215` edge `0.2528` maxDD `-7.675`
- `news_risk_high->crypto_alt_24h` score `2.3757` n `101` status `ready` deltaP `-4.1443` edge `0.7137` maxDD `-32.7147`
- `news_risk_high->crypto_alt_1h` score `2.1923` n `101` status `ready` deltaP `13.3871` edge `0.14` maxDD `-2.058`
- `news_risk_high->crypto_major_4h` score `2.1258` n `101` status `ready` deltaP `16.1751` edge `0.1951` maxDD `-8.0625`
- `market_context_high->index_4h` score `2.0247` n `46` status `ready` deltaP `23.7738` edge `0.0236` maxDD `-0.0692`
- `news_risk_high->crypto_major_1h` score `1.5221` n `101` status `ready` deltaP `15.0338` edge `0.0789` maxDD `-2.8494`
- `market_context_high->equity_4h` score `1.2548` n `46` status `ready` deltaP `8.7487` edge `0.0769` maxDD `-0.4529`
- `market_context_high->crypto_alt_4h` score `1.0525` n `46` status `ready` deltaP `8.5167` edge `0.0904` maxDD `-2.7574`
- `market_context_high->equity_1h` score `0.9528` n `46` status `ready` deltaP `7.5111` edge `0.0536` maxDD `-0.2751`
- `news_risk_high->fx_4h` score `0.9105` n `101` status `ready` deltaP `15.8053` edge `0.0341` maxDD `-0.421`
- `market_context_high->index_1h` score `0.6567` n `46` status `ready` deltaP `10.3554` edge `0.011` maxDD `-0.0249`
- `news_risk_high->metal_1h` score `0.543` n `101` status `ready` deltaP `13.8495` edge `0.0131` maxDD `-0.8144`
- `market_context_high->crypto_major_1h` score `0.4342` n `46` status `ready` deltaP `0.4622` edge `0.0854` maxDD `-2.1836`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
