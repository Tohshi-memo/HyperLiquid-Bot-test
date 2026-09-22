# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-22T06:46:04.663026+00:00`
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

- `market_context_high->unknown_4h` score `48.3598` n `46` status `ready` deltaP `7.3171` edge `3.9812` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `34.2671` n `46` status `ready` deltaP `20.9994` edge `2.7312` maxDD `-0.5817`
- `market_context_high->crypto_alt_24h` score `18.9821` n `46` status `ready` deltaP `19.7917` edge `1.4499` maxDD `0.0`
- `market_context_high->equity_24h` score `16.9416` n `46` status `ready` deltaP `14.2286` edge `1.327` maxDD `-0.1382`
- `news_risk_high->crypto_major_24h` score `6.55` n `101` status `ready` deltaP `-4.3558` edge `1.2607` maxDD `-46.1999`
- `market_context_high->index_24h` score `5.6208` n `46` status `ready` deltaP `20.1314` edge `0.3429` maxDD `-0.03`
- `news_risk_high->commodity_24h` score `2.8801` n `101` status `ready` deltaP `35.5232` edge `0.263` maxDD `-3.4467`
- `news_risk_high->crypto_alt_4h` score `2.6323` n `101` status `ready` deltaP `12.9739` edge `0.2538` maxDD `-7.675`
- `news_risk_high->crypto_alt_24h` score `2.5011` n `101` status `ready` deltaP `-3.9707` edge `0.723` maxDD `-32.7147`
- `news_risk_high->crypto_alt_1h` score `2.233` n `101` status `ready` deltaP `13.6865` edge `0.1414` maxDD `-2.058`
- `news_risk_high->crypto_major_4h` score `2.1318` n `101` status `ready` deltaP `16.1751` edge `0.1956` maxDD `-8.0625`
- `market_context_high->index_4h` score `2.0089` n `46` status `ready` deltaP `23.6214` edge `0.0233` maxDD `-0.0692`
- `news_risk_high->crypto_major_1h` score `1.5604` n `101` status `ready` deltaP `15.3332` edge `0.0801` maxDD `-2.8494`
- `market_context_high->equity_4h` score `1.2198` n `46` status `ready` deltaP `8.5963` edge `0.075` maxDD `-0.4529`
- `market_context_high->crypto_alt_4h` score `1.0767` n `46` status `ready` deltaP `8.6691` edge `0.0914` maxDD `-2.7574`
- `market_context_high->equity_1h` score `0.9564` n `46` status `ready` deltaP `7.5111` edge `0.0539` maxDD `-0.2751`
- `news_risk_high->fx_4h` score `0.8971` n `101` status `ready` deltaP `15.6529` edge `0.034` maxDD `-0.421`
- `market_context_high->index_1h` score `0.6579` n `46` status `ready` deltaP `10.3554` edge `0.0111` maxDD `-0.0249`
- `news_risk_high->metal_1h` score `0.5466` n `101` status `ready` deltaP `13.8495` edge `0.0134` maxDD `-0.8144`
- `market_context_high->crypto_major_1h` score `0.4726` n `46` status `ready` deltaP `0.7616` edge `0.0866` maxDD `-2.1836`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
