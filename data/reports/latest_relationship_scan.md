# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-08T18:01:26.802884+00:00`
- Price records: `668`
- Market context records: `780`
- Flow alert records: `2198`
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

- `market_context_high->crypto_major_24h` score `13.2902` n `148` status `ready` deltaP `31.426` edge `0.9314` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.4121` n `148` status `ready` deltaP `7.1914` edge `0.4912` maxDD `-0.0508`
- `risk_on_high->equity_4h` score `3.6085` n `32` status `ready` deltaP `10.0694` edge `0.2701` maxDD `-0.9217`
- `risk_on_and_context->equity_4h` score `3.6085` n `32` status `ready` deltaP `10.0694` edge `0.2701` maxDD `-0.9217`
- `risk_on_high->index_4h` score `2.9601` n `32` status `ready` deltaP `18.9429` edge `0.1292` maxDD `-0.038`
- `risk_on_and_context->index_4h` score `2.9601` n `32` status `ready` deltaP `18.9429` edge `0.1292` maxDD `-0.038`
- `risk_on_high->crypto_major_4h` score `2.7379` n `32` status `ready` deltaP `20.8589` edge `0.1263` maxDD `-0.9758`
- `risk_on_and_context->crypto_major_4h` score `2.7379` n `32` status `ready` deltaP `20.8589` edge `0.1263` maxDD `-0.9758`
- `risk_on_high->crypto_alt_4h` score `2.5638` n `32` status `ready` deltaP `21.4532` edge `0.0911` maxDD `-0.6377`
- `risk_on_and_context->crypto_alt_4h` score `2.5638` n `32` status `ready` deltaP `21.4532` edge `0.0911` maxDD `-0.6377`
- `risk_on_high->metal_1h` score `1.0334` n `33` status `ready` deltaP `12.7693` edge `0.024` maxDD `-0.5074`
- `risk_on_and_context->metal_1h` score `1.0334` n `33` status `ready` deltaP `12.7693` edge `0.024` maxDD `-0.5074`
- `risk_on_high->commodity_4h` score `0.7432` n `32` status `ready` deltaP `4.591` edge `0.1478` maxDD `-1.3162`
- `risk_on_and_context->commodity_4h` score `0.7432` n `32` status `ready` deltaP `4.591` edge `0.1478` maxDD `-1.3162`
- `market_context_high->index_24h` score `0.4627` n `148` status `ready` deltaP `2.755` edge `0.2197` maxDD `-5.9609`
- `risk_on_high->fx_1h` score `0.282` n `33` status `ready` deltaP `8.6364` edge `0.0021` maxDD `-0.2147`
- `risk_on_and_context->fx_1h` score `0.282` n `33` status `ready` deltaP `8.6364` edge `0.0021` maxDD `-0.2147`
- `risk_on_high->commodity_1h` score `0.2678` n `33` status `ready` deltaP `7.8788` edge `0.0194` maxDD `-0.6739`
- `risk_on_and_context->commodity_1h` score `0.2678` n `33` status `ready` deltaP `7.8788` edge `0.0194` maxDD `-0.6739`
- `risk_on_high->crypto_major_1h` score `-0.0989` n `33` status `ready` deltaP `4.5638` edge `-0.0127` maxDD `-1.0995`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
