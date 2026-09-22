# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-22T13:07:30.284049+00:00`
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

- `market_context_high->unknown_4h` score `46.9054` n `46` status `ready` deltaP `7.3171` edge `3.86` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `31.4059` n `46` status `ready` deltaP `16.6591` edge `2.5217` maxDD `-0.5817`
- `market_context_high->crypto_alt_24h` score `16.5663` n `46` status `ready` deltaP `15.7986` edge `1.2752` maxDD `0.0`
- `market_context_high->equity_24h` score `16.3431` n `46` status `ready` deltaP `12.4925` edge `1.2887` maxDD `-0.1382`
- `market_context_high->index_24h` score `5.5536` n `46` status `ready` deltaP `20.1314` edge `0.3373` maxDD `-0.03`
- `news_risk_high->crypto_major_24h` score `3.6887` n `101` status `ready` deltaP `-8.6961` edge `1.0512` maxDD `-46.1999`
- `news_risk_high->commodity_24h` score `3.2455` n `101` status `ready` deltaP `38.9954` edge `0.2867` maxDD `-3.4467`
- `news_risk_high->crypto_alt_4h` score `2.3323` n `101` status `ready` deltaP `12.0593` edge `0.2349` maxDD `-7.675`
- `news_risk_high->crypto_alt_1h` score `2.1527` n `101` status `ready` deltaP `13.3871` edge `0.1367` maxDD `-2.058`
- `market_context_high->index_4h` score `1.9991` n `46` status `ready` deltaP `23.4689` edge `0.0235` maxDD `-0.0692`
- `news_risk_high->crypto_major_4h` score `1.6813` n `101` status `ready` deltaP `14.8032` edge `0.1672` maxDD `-8.0625`
- `news_risk_high->crypto_major_1h` score `1.4837` n `101` status `ready` deltaP `15.0338` edge `0.0757` maxDD `-2.8494`
- `market_context_high->equity_4h` score `1.14` n `46` status `ready` deltaP `8.1389` edge `0.0714` maxDD `-0.4529`
- `news_risk_high->fx_4h` score `1.0538` n `101` status `ready` deltaP `17.1773` edge `0.0369` maxDD `-0.421`
- `market_context_high->equity_1h` score `0.978` n `46` status `ready` deltaP `7.8105` edge `0.0537` maxDD `-0.2751`
- `market_context_high->metal_24h` score `0.8834` n `46` status `ready` deltaP `21.2259` edge `-0.0445` maxDD `-0.2042`
- `market_context_high->crypto_alt_4h` score `0.7767` n `46` status `ready` deltaP `7.7545` edge `0.0725` maxDD `-2.7574`
- `market_context_high->index_1h` score `0.7214` n `46` status `ready` deltaP `11.1039` edge `0.0114` maxDD `-0.0249`
- `news_risk_high->metal_1h` score `0.6053` n `101` status `ready` deltaP `14.598` edge `0.0133` maxDD `-0.8144`
- `market_context_high->crypto_major_1h` score `0.3958` n `46` status `ready` deltaP `0.4622` edge `0.0822` maxDD `-2.1836`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
