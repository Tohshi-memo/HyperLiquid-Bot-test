# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-22T02:37:27.512921+00:00`
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

- `market_context_high->unknown_4h` score `48.7426` n `46` status `ready` deltaP `7.3171` edge `4.0131` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `37.1012` n `46` status `ready` deltaP `23.9508` edge `2.9477` maxDD `-0.5817`
- `market_context_high->crypto_alt_24h` score `21.4022` n `46` status `ready` deltaP `22.7431` edge `1.6319` maxDD `0.0`
- `market_context_high->equity_24h` score `18.0201` n `46` status `ready` deltaP `17.18` edge `1.3972` maxDD `-0.1382`
- `news_risk_high->crypto_major_24h` score `9.3841` n `101` status `ready` deltaP `-1.4044` edge `1.4772` maxDD `-46.1999`
- `market_context_high->index_24h` score `5.8433` n `46` status `ready` deltaP `21.173` edge `0.3545` maxDD `-0.03`
- `news_risk_high->crypto_alt_24h` score `4.9213` n `101` status `ready` deltaP `-1.0193` edge `0.905` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `2.806` n `101` status `ready` deltaP `13.7361` edge `0.2632` maxDD `-7.675`
- `news_risk_high->commodity_24h` score `2.6572` n `101` status `ready` deltaP `32.5718` edge `0.2541` maxDD `-3.4467`
- `news_risk_high->crypto_alt_1h` score `2.2894` n `101` status `ready` deltaP `13.8362` edge `0.1451` maxDD `-2.058`
- `news_risk_high->crypto_major_4h` score `2.1512` n `101` status `ready` deltaP `16.3276` edge `0.1962` maxDD `-8.0625`
- `market_context_high->index_4h` score `2.0125` n `46` status `ready` deltaP `23.6214` edge `0.0236` maxDD `-0.0692`
- `news_risk_high->crypto_major_1h` score `1.6624` n `101` status `ready` deltaP `15.932` edge `0.0846` maxDD `-2.8494`
- `market_context_high->crypto_alt_4h` score `1.2505` n `46` status `ready` deltaP `9.4313` edge `0.1008` maxDD `-2.7574`
- `market_context_high->equity_4h` score `1.178` n `46` status `ready` deltaP `8.7487` edge `0.0705` maxDD `-0.4529`
- `market_context_high->equity_1h` score `0.9396` n `46` status `ready` deltaP `7.5111` edge `0.0525` maxDD `-0.2751`
- `news_risk_high->fx_4h` score `0.6576` n `101` status `ready` deltaP `13.2139` edge `0.0303` maxDD `-0.421`
- `market_context_high->index_1h` score `0.6256` n `46` status `ready` deltaP `9.9063` edge `0.0114` maxDD `-0.0249`
- `market_context_high->crypto_major_1h` score `0.5745` n `46` status `ready` deltaP `1.3604` edge `0.0911` maxDD `-2.1836`
- `news_risk_high->metal_1h` score `0.5574` n `101` status `ready` deltaP `13.9992` edge `0.0133` maxDD `-0.8144`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
