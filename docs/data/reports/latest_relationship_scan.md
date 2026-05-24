# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-24T16:32:16.895733+00:00`
- Price records: `672`
- Market context records: `1755`
- Flow alert records: `6952`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8862`

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

- `market_context_high->metal_24h` score `7.1793` n `166` status `ready` deltaP `27.3113` edge `0.6588` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `5.9987` n `196` status `ready` deltaP `20.9713` edge `0.5367` maxDD `-9.1295`
- `market_context_high->crypto_major_4h` score `4.4674` n `196` status `ready` deltaP `22.5672` edge `0.4624` maxDD `-10.9117`
- `market_context_high->index_24h` score `4.1274` n `166` status `ready` deltaP `18.7333` edge `0.3419` maxDD `-4.1604`
- `market_context_high->unknown_24h` score `3.7345` n `166` status `ready` deltaP `14.872` edge `0.7441` maxDD `-35.8966`
- `news_risk_high->commodity_1h` score `3.1522` n `30` status `ready` deltaP `24.7206` edge `0.1296` maxDD `-1.2043`
- `market_context_high->equity_4h` score `3.0685` n `196` status `ready` deltaP `16.5692` edge `0.2547` maxDD `-5.0894`
- `market_context_high->unknown_4h` score `2.8947` n `196` status `ready` deltaP `12.7271` edge `0.3835` maxDD `-11.1695`
- `market_context_high->equity_24h` score `2.7793` n `166` status `ready` deltaP `17.0181` edge `0.608` maxDD `-33.1875`
- `market_context_high->index_4h` score `0.9012` n `196` status `ready` deltaP `11.8654` edge `0.1049` maxDD `-3.7119`
- `market_context_high->crypto_alt_1h` score `0.7513` n `196` status `ready` deltaP `7.2712` edge `0.1165` maxDD `-4.1892`
- `market_context_high->crypto_major_24h` score `0.5161` n `166` status `ready` deltaP `19.2436` edge `0.7733` maxDD `-62.3533`
- `market_context_high->crypto_major_1h` score `0.2041` n `196` status `ready` deltaP `4.598` edge `0.0937` maxDD `-3.9211`
- `market_context_high->equity_1h` score `0.097` n `196` status `ready` deltaP `5.2701` edge `0.0538` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.1915` n `196` status `ready` deltaP `3.9167` edge `0.0211` maxDD `-1.7205`
- `market_context_high->metal_4h` score `-0.2404` n `196` status `ready` deltaP `12.444` edge `0.1554` maxDD `-12.5349`
- `market_context_high->metal_1h` score `-0.5089` n `196` status `ready` deltaP `5.9453` edge `0.0287` maxDD `-6.3532`
- `news_risk_high->fx_1h` score `-0.5169` n `30` status `ready` deltaP `-5.8782` edge `-0.0009` maxDD `-0.0948`
- `news_risk_high->unknown_1h` score `-0.5635` n `30` status `ready` deltaP `15.9581` edge `-0.1314` maxDD `-2.1115`
- `market_context_high->fx_24h` score `-0.604` n `166` status `ready` deltaP `7.1515` edge `0.0069` maxDD `-1.3925`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
