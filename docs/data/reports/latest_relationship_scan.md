# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-22T02:52:28.645580+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9972`

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

- `market_context_high->unknown_4h` score `48.7894` n `46` status `ready` deltaP `7.3171` edge `4.017` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `36.9205` n `46` status `ready` deltaP `23.7772` edge `2.9338` maxDD `-0.5817`
- `market_context_high->crypto_alt_24h` score `21.2264` n `46` status `ready` deltaP `22.5694` edge `1.6184` maxDD `0.0`
- `market_context_high->equity_24h` score `17.927` n `46` status `ready` deltaP `17.0064` edge `1.3906` maxDD `-0.1382`
- `news_risk_high->crypto_major_24h` score `9.2034` n `101` status `ready` deltaP `-1.578` edge `1.4633` maxDD `-46.1999`
- `market_context_high->index_24h` score `5.8175` n `46` status `ready` deltaP `20.9994` edge `0.3535` maxDD `-0.03`
- `news_risk_high->crypto_alt_24h` score `4.7454` n `101` status `ready` deltaP `-1.193` edge `0.8915` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `2.7758` n `101` status `ready` deltaP `13.5837` edge `0.2617` maxDD `-7.675`
- `news_risk_high->commodity_24h` score `2.6716` n `101` status `ready` deltaP `32.7454` edge `0.2548` maxDD `-3.4467`
- `news_risk_high->crypto_alt_1h` score `2.2846` n `101` status `ready` deltaP `13.8362` edge `0.1447` maxDD `-2.058`
- `news_risk_high->crypto_major_4h` score `2.15` n `101` status `ready` deltaP `16.3276` edge `0.1961` maxDD `-8.0625`
- `market_context_high->index_4h` score `1.9967` n `46` status `ready` deltaP `23.4689` edge `0.0233` maxDD `-0.0692`
- `news_risk_high->crypto_major_1h` score `1.66` n `101` status `ready` deltaP `15.932` edge `0.0844` maxDD `-2.8494`
- `market_context_high->crypto_alt_4h` score `1.2203` n `46` status `ready` deltaP `9.2789` edge `0.0993` maxDD `-2.7574`
- `market_context_high->equity_4h` score `1.1478` n `46` status `ready` deltaP `8.5963` edge `0.069` maxDD `-0.4529`
- `market_context_high->equity_1h` score `0.9216` n `46` status `ready` deltaP `7.3614` edge `0.052` maxDD `-0.2751`
- `news_risk_high->fx_4h` score `0.6734` n `101` status `ready` deltaP `13.3663` edge `0.0306` maxDD `-0.421`
- `market_context_high->index_1h` score `0.6244` n `46` status `ready` deltaP `9.9063` edge `0.0113` maxDD `-0.0249`
- `market_context_high->crypto_major_1h` score `0.5721` n `46` status `ready` deltaP `1.3604` edge `0.0909` maxDD `-2.1836`
- `news_risk_high->metal_1h` score `0.5574` n `101` status `ready` deltaP `13.9992` edge `0.0133` maxDD `-0.8144`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
