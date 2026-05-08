# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-08T19:42:44.911197+00:00`
- Price records: `672`
- Market context records: `788`
- Flow alert records: `2219`
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

- `market_context_high->crypto_major_24h` score `13.1086` n `149` status `ready` deltaP `31.0321` edge `0.9189` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.2413` n `149` status `ready` deltaP `7.1414` edge `0.4773` maxDD `-0.0508`
- `risk_on_high->equity_4h` score `3.7977` n `33` status `ready` deltaP `10.4393` edge `0.2834` maxDD `-0.9217`
- `risk_on_and_context->equity_4h` score `3.7977` n `33` status `ready` deltaP `10.4393` edge `0.2834` maxDD `-0.9217`
- `risk_on_high->crypto_major_4h` score `3.07` n `33` status `ready` deltaP `21.1844` edge `0.1518` maxDD `-0.9758`
- `risk_on_and_context->crypto_major_4h` score `3.07` n `33` status `ready` deltaP `21.1844` edge `0.1518` maxDD `-0.9758`
- `risk_on_high->index_4h` score `3.0326` n `33` status `ready` deltaP `19.0993` edge `0.1342` maxDD `-0.038`
- `risk_on_and_context->index_4h` score `3.0326` n `33` status `ready` deltaP `19.0993` edge `0.1342` maxDD `-0.038`
- `risk_on_high->crypto_alt_4h` score `2.9783` n `33` status `ready` deltaP `21.5493` edge `0.125` maxDD `-0.6377`
- `risk_on_and_context->crypto_alt_4h` score `2.9783` n `33` status `ready` deltaP `21.5493` edge `0.125` maxDD `-0.6377`
- `risk_on_high->metal_1h` score `1.0572` n `33` status `ready` deltaP `12.8108` edge `0.0257` maxDD `-0.5074`
- `risk_on_and_context->metal_1h` score `1.0572` n `33` status `ready` deltaP `12.8108` edge `0.0257` maxDD `-0.5074`
- `risk_on_high->commodity_4h` score `0.61` n `33` status `ready` deltaP `3.5585` edge `0.1376` maxDD `-1.3162`
- `risk_on_and_context->commodity_4h` score `0.61` n `33` status `ready` deltaP `3.5585` edge `0.1376` maxDD `-1.3162`
- `market_context_high->index_24h` score `0.3837` n `149` status `ready` deltaP `2.6226` edge `0.214` maxDD `-5.9609`
- `risk_on_high->commodity_1h` score `0.2733` n `33` status `ready` deltaP `7.8488` edge `0.0203` maxDD `-0.6739`
- `risk_on_and_context->commodity_1h` score `0.2733` n `33` status `ready` deltaP `7.8488` edge `0.0203` maxDD `-0.6739`
- `risk_on_high->fx_1h` score `0.2594` n `33` status `ready` deltaP `8.231` edge `0.0019` maxDD `-0.2147`
- `risk_on_and_context->fx_1h` score `0.2594` n `33` status `ready` deltaP `8.231` edge `0.0019` maxDD `-0.2147`
- `risk_on_high->crypto_major_1h` score `-0.1175` n `33` status `ready` deltaP `4.4321` edge `-0.0142` maxDD `-1.0995`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
