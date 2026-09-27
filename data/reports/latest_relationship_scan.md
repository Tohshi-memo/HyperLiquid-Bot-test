# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-27T01:22:29.334374+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11444`

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

- `news_risk_high->unknown_24h` score `3229.5504` n `97` status `ready` deltaP `1.2153` edge `269.1211` maxDD `0.0`
- `market_context_high->unknown_1h` score `74.8923` n `44` status `ready` deltaP `10.1524` edge `6.178` maxDD `-0.0395`
- `market_context_high->crypto_major_24h` score `51.2202` n `44` status `ready` deltaP `27.4148` edge `4.1207` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `27.7878` n `44` status `ready` deltaP `14.9148` edge `2.2542` maxDD `-2.7051`
- `market_context_high->equity_24h` score `27.7024` n `44` status `ready` deltaP `36.0954` edge `2.0993` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.6721` n `44` status `ready` deltaP `31.5815` edge `0.4376` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.6657` n `44` status `ready` deltaP `31.7866` edge `0.1174` maxDD `-0.2401`
- `market_context_high->index_4h` score `3.4139` n `44` status `ready` deltaP `38.2899` edge `0.0363` maxDD `-0.2323`
- `market_context_high->equity_4h` score `3.0704` n `44` status `ready` deltaP `18.7361` edge `0.1686` maxDD `-1.3444`
- `market_context_high->crypto_alt_4h` score `1.4473` n `44` status `ready` deltaP `9.6175` edge `0.1191` maxDD `-3.3417`
- `news_risk_high->index_24h` score `1.3129` n `97` status `ready` deltaP `18.3903` edge `0.048` maxDD `-2.2287`
- `market_context_high->crypto_major_1h` score `1.1839` n `44` status `ready` deltaP `9.2678` edge `0.1103` maxDD `-4.5405`
- `market_context_high->equity_1h` score `1.1282` n `44` status `ready` deltaP `12.466` edge `0.0512` maxDD `-1.5564`
- `news_risk_high->metal_24h` score `1.0999` n `97` status `ready` deltaP `25.6479` edge `0.1348` maxDD `-6.8481`
- `market_context_high->crypto_major_4h` score `1.0732` n `44` status `ready` deltaP `7.6774` edge `0.1287` maxDD `-5.2359`
- `market_context_high->index_1h` score `0.8152` n `44` status `ready` deltaP `12.3163` edge `0.0095` maxDD `-0.2275`
- `market_context_high->metal_1h` score `0.2719` n `44` status `ready` deltaP `6.4643` edge `0.0112` maxDD `-0.1976`
- `market_context_high->crypto_alt_1h` score `0.1674` n `44` status `ready` deltaP `4.4502` edge `0.0732` maxDD `-5.7799`
- `market_context_high->fx_1h` score `0.1391` n `44` status `ready` deltaP `7.0631` edge `0.0064` maxDD `-0.1854`
- `news_risk_high->index_1h` score `-0.1058` n `139` status `ready` deltaP `2.5223` edge `0.0035` maxDD `-0.3305`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
