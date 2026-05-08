# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-08T18:37:13.871869+00:00`
- Price records: `670`
- Market context records: `783`
- Flow alert records: `2205`
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

- `market_context_high->crypto_major_24h` score `13.2393` n `149` status `ready` deltaP `31.3449` edge `0.9277` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.4343` n `149` status `ready` deltaP `7.1686` edge `0.4932` maxDD `-0.0508`
- `risk_on_high->equity_4h` score `3.8481` n `33` status `ready` deltaP `10.6341` edge `0.2863` maxDD `-0.9217`
- `risk_on_and_context->equity_4h` score `3.8481` n `33` status `ready` deltaP `10.6341` edge `0.2863` maxDD `-0.9217`
- `risk_on_high->crypto_major_4h` score `3.1845` n `33` status `ready` deltaP `21.4763` edge `0.1594` maxDD `-0.9758`
- `risk_on_and_context->crypto_major_4h` score `3.1845` n `33` status `ready` deltaP `21.4763` edge `0.1594` maxDD `-0.9758`
- `risk_on_high->crypto_alt_4h` score `3.0902` n `33` status `ready` deltaP `21.643` edge `0.1337` maxDD `-0.6377`
- `risk_on_and_context->crypto_alt_4h` score `3.0902` n `33` status `ready` deltaP `21.643` edge `0.1337` maxDD `-0.6377`
- `risk_on_high->index_4h` score `3.0663` n `33` status `ready` deltaP `19.31` edge `0.1356` maxDD `-0.038`
- `risk_on_and_context->index_4h` score `3.0663` n `33` status `ready` deltaP `19.31` edge `0.1356` maxDD `-0.038`
- `risk_on_high->metal_1h` score `1.0159` n `33` status `ready` deltaP `12.6399` edge `0.0234` maxDD `-0.5074`
- `risk_on_and_context->metal_1h` score `1.0159` n `33` status `ready` deltaP `12.6399` edge `0.0234` maxDD `-0.5074`
- `risk_on_high->commodity_4h` score `0.5825` n `33` status `ready` deltaP `3.3007` edge `0.1358` maxDD `-1.3162`
- `risk_on_and_context->commodity_4h` score `0.5825` n `33` status `ready` deltaP `3.3007` edge `0.1358` maxDD `-1.3162`
- `market_context_high->index_24h` score `0.4882` n `149` status `ready` deltaP `2.8341` edge `0.2213` maxDD `-5.9609`
- `risk_on_high->commodity_1h` score `0.2814` n `33` status `ready` deltaP `8.0198` edge `0.0202` maxDD `-0.6739`
- `risk_on_and_context->commodity_1h` score `0.2814` n `33` status `ready` deltaP `8.0198` edge `0.0202` maxDD `-0.6739`
- `risk_on_high->fx_1h` score `0.275` n `33` status `ready` deltaP `8.5004` edge `0.0021` maxDD `-0.2147`
- `risk_on_and_context->fx_1h` score `0.275` n `33` status `ready` deltaP `8.5004` edge `0.0021` maxDD `-0.2147`
- `risk_on_high->crypto_major_1h` score `-0.1227` n `33` status `ready` deltaP `4.4226` edge `-0.0148` maxDD `-1.0995`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
