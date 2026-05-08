# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-08T18:22:11.532857+00:00`
- Price records: `669`
- Market context records: `782`
- Flow alert records: `2202`
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

- `market_context_high->crypto_major_24h` score `13.2641` n `149` status `ready` deltaP `31.4148` edge `0.9293` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.4666` n `149` status `ready` deltaP `7.1823` edge `0.4958` maxDD `-0.0508`
- `risk_on_high->equity_4h` score `3.5962` n `32` status `ready` deltaP `10.0202` edge `0.2694` maxDD `-0.9217`
- `risk_on_and_context->equity_4h` score `3.5962` n `32` status `ready` deltaP `10.0202` edge `0.2694` maxDD `-0.9217`
- `risk_on_high->index_4h` score `2.9499` n `32` status `ready` deltaP `18.8896` edge `0.1287` maxDD `-0.038`
- `risk_on_and_context->index_4h` score `2.9499` n `32` status `ready` deltaP `18.8896` edge `0.1287` maxDD `-0.038`
- `risk_on_high->crypto_major_4h` score `2.7119` n `32` status `ready` deltaP `20.7887` edge `0.1246` maxDD `-0.9758`
- `risk_on_and_context->crypto_major_4h` score `2.7119` n `32` status `ready` deltaP `20.7887` edge `0.1246` maxDD `-0.9758`
- `risk_on_high->crypto_alt_4h` score `2.5324` n `32` status `ready` deltaP `21.406` edge `0.0888` maxDD `-0.6377`
- `risk_on_and_context->crypto_alt_4h` score `2.5324` n `32` status `ready` deltaP `21.406` edge `0.0888` maxDD `-0.6377`
- `risk_on_high->metal_1h` score `1.0235` n `33` status `ready` deltaP `12.7045` edge `0.0236` maxDD `-0.5074`
- `risk_on_and_context->metal_1h` score `1.0235` n `33` status `ready` deltaP `12.7045` edge `0.0236` maxDD `-0.5074`
- `risk_on_high->commodity_4h` score `0.749` n `32` status `ready` deltaP `4.6562` edge `0.1481` maxDD `-1.3162`
- `risk_on_and_context->commodity_4h` score `0.749` n `32` status `ready` deltaP `4.6562` edge `0.1481` maxDD `-1.3162`
- `market_context_high->index_24h` score `0.5129` n `149` status `ready` deltaP `2.8874` edge `0.223` maxDD `-5.9609`
- `risk_on_high->fx_1h` score `0.2785` n `33` status `ready` deltaP `8.5683` edge `0.0021` maxDD `-0.2147`
- `risk_on_and_context->fx_1h` score `0.2785` n `33` status `ready` deltaP `8.5683` edge `0.0021` maxDD `-0.2147`
- `risk_on_high->commodity_1h` score `0.2746` n `33` status `ready` deltaP `7.9494` edge `0.0198` maxDD `-0.6739`
- `risk_on_and_context->commodity_1h` score `0.2746` n `33` status `ready` deltaP `7.9494` edge `0.0198` maxDD `-0.6739`
- `market_context_high->equity_24h` score `-0.1103` n `149` status `ready` deltaP `1.498` edge `0.2413` maxDD `-10.5047`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
