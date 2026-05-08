# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-08T19:07:25.775176+00:00`
- Price records: `672`
- Market context records: `785`
- Flow alert records: `2212`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `1170`

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

- `market_context_high->crypto_major_24h` score `13.1765` n `149` status `ready` deltaP `31.2058` edge `0.9234` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.3529` n `149` status `ready` deltaP `7.1414` edge `0.4866` maxDD `-0.0508`
- `risk_on_high->equity_4h` score `3.8223` n `33` status `ready` deltaP `10.5364` edge `0.2848` maxDD `-0.9217`
- `risk_on_and_context->equity_4h` score `3.8223` n `33` status `ready` deltaP `10.5364` edge `0.2848` maxDD `-0.9217`
- `risk_on_high->crypto_major_4h` score `3.1254` n `33` status `ready` deltaP `21.3369` edge `0.1554` maxDD `-0.9758`
- `risk_on_and_context->crypto_major_4h` score `3.1254` n `33` status `ready` deltaP `21.3369` edge `0.1554` maxDD `-0.9758`
- `risk_on_high->index_4h` score `3.0494` n `33` status `ready` deltaP `19.2043` edge `0.1349` maxDD `-0.038`
- `risk_on_and_context->index_4h` score `3.0494` n `33` status `ready` deltaP `19.2043` edge `0.1349` maxDD `-0.038`
- `risk_on_high->crypto_alt_4h` score `3.0287` n `33` status `ready` deltaP `21.5493` edge `0.1292` maxDD `-0.6377`
- `risk_on_and_context->crypto_alt_4h` score `3.0287` n `33` status `ready` deltaP `21.5493` edge `0.1292` maxDD `-0.6377`
- `risk_on_high->metal_1h` score `1.0188` n `33` status `ready` deltaP `12.6611` edge `0.0235` maxDD `-0.5074`
- `risk_on_and_context->metal_1h` score `1.0188` n `33` status `ready` deltaP `12.6611` edge `0.0235` maxDD `-0.5074`
- `risk_on_high->commodity_4h` score `0.5955` n `33` status `ready` deltaP `3.43` edge `0.1366` maxDD `-1.3162`
- `risk_on_and_context->commodity_4h` score `0.5955` n `33` status `ready` deltaP `3.43` edge `0.1366` maxDD `-1.3162`
- `market_context_high->index_24h` score `0.4341` n `149` status `ready` deltaP `2.728` edge `0.2175` maxDD `-5.9609`
- `risk_on_high->commodity_1h` score `0.2824` n `33` status `ready` deltaP `8.0094` edge `0.0204` maxDD `-0.6739`
- `risk_on_and_context->commodity_1h` score `0.2824` n `33` status `ready` deltaP `8.0094` edge `0.0204` maxDD `-0.6739`
- `risk_on_high->fx_1h` score `0.2672` n `33` status `ready` deltaP `8.3653` edge `0.002` maxDD `-0.2147`
- `risk_on_and_context->fx_1h` score `0.2672` n `33` status `ready` deltaP `8.3653` edge `0.002` maxDD `-0.2147`
- `risk_on_high->crypto_major_1h` score `-0.1393` n `33` status `ready` deltaP `4.2824` edge `-0.016` maxDD `-1.0995`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
