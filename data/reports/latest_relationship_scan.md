# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-08T17:37:12.191747+00:00`
- Price records: `666`
- Market context records: `778`
- Flow alert records: `2192`
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

- `market_context_high->crypto_major_24h` score `13.3651` n `147` status `ready` deltaP `31.5074` edge `0.9371` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.4139` n `147` status `ready` deltaP `7.2144` edge `0.4912` maxDD `-0.0508`
- `risk_on_high->equity_4h` score `3.6332` n `32` status `ready` deltaP `10.1683` edge `0.2715` maxDD `-0.9217`
- `risk_on_and_context->equity_4h` score `3.6332` n `32` status `ready` deltaP `10.1683` edge `0.2715` maxDD `-0.9217`
- `risk_on_high->index_4h` score `2.9759` n `32` status `ready` deltaP `19.0499` edge `0.1298` maxDD `-0.038`
- `risk_on_and_context->index_4h` score `2.9759` n `32` status `ready` deltaP `19.0499` edge `0.1298` maxDD `-0.038`
- `risk_on_high->crypto_major_4h` score `2.7984` n `32` status `ready` deltaP `21.0` edge `0.1304` maxDD `-0.9758`
- `risk_on_and_context->crypto_major_4h` score `2.7984` n `32` status `ready` deltaP `21.0` edge `0.1304` maxDD `-0.9758`
- `risk_on_high->crypto_alt_4h` score `2.6386` n `32` status `ready` deltaP `21.5481` edge `0.0967` maxDD `-0.6377`
- `risk_on_and_context->crypto_alt_4h` score `2.6386` n `32` status `ready` deltaP `21.5481` edge `0.0967` maxDD `-0.6377`
- `risk_on_high->metal_1h` score `1.0522` n `33` status `ready` deltaP `12.8994` edge `0.0247` maxDD `-0.5074`
- `risk_on_and_context->metal_1h` score `1.0522` n `33` status `ready` deltaP `12.8994` edge `0.0247` maxDD `-0.5074`
- `risk_on_high->commodity_4h` score `0.7492` n `32` status `ready` deltaP `4.6149` edge `0.1484` maxDD `-1.3162`
- `risk_on_and_context->commodity_4h` score `0.7492` n `32` status `ready` deltaP `4.6149` edge `0.1484` maxDD `-1.3162`
- `market_context_high->index_24h` score `0.4454` n `147` status `ready` deltaP `2.6742` edge `0.2188` maxDD `-5.9609`
- `risk_on_high->fx_1h` score `0.2899` n `33` status `ready` deltaP `8.7732` edge `0.0022` maxDD `-0.2147`
- `risk_on_and_context->fx_1h` score `0.2899` n `33` status `ready` deltaP `8.7732` edge `0.0022` maxDD `-0.2147`
- `risk_on_high->commodity_1h` score `0.255` n `33` status `ready` deltaP `7.737` edge `0.0187` maxDD `-0.6739`
- `risk_on_and_context->commodity_1h` score `0.255` n `33` status `ready` deltaP `7.737` edge `0.0187` maxDD `-0.6739`
- `risk_on_high->crypto_major_1h` score `-0.0728` n `33` status `ready` deltaP `4.7057` edge `-0.0103` maxDD `-1.0995`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
