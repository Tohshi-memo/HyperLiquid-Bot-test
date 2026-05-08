# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-08T20:52:21.649111+00:00`
- Price records: `672`
- Market context records: `794`
- Flow alert records: `2234`
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

- `market_context_high->crypto_major_24h` score `12.8676` n `149` status `ready` deltaP `30.1641` edge `0.9046` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `5.9701` n `149` status `ready` deltaP `7.1414` edge `0.4547` maxDD `-0.0508`
- `risk_on_high->equity_4h` score `3.7024` n `33` status `ready` deltaP `10.3428` edge `0.2761` maxDD `-0.9217`
- `risk_on_and_context->equity_4h` score `3.7024` n `33` status `ready` deltaP `10.3428` edge `0.2761` maxDD `-0.9217`
- `risk_on_high->index_4h` score `2.9833` n `33` status `ready` deltaP `18.8424` edge `0.1318` maxDD `-0.038`
- `risk_on_and_context->index_4h` score `2.9833` n `33` status `ready` deltaP `18.8424` edge `0.1318` maxDD `-0.038`
- `risk_on_high->crypto_major_4h` score `2.8734` n `33` status `ready` deltaP `20.4222` edge `0.1405` maxDD `-0.9758`
- `risk_on_and_context->crypto_major_4h` score `2.8734` n `33` status `ready` deltaP `20.4222` edge `0.1405` maxDD `-0.9758`
- `risk_on_high->crypto_alt_4h` score `2.8507` n `33` status `ready` deltaP `21.2445` edge `0.1164` maxDD `-0.6377`
- `risk_on_and_context->crypto_alt_4h` score `2.8507` n `33` status `ready` deltaP `21.2445` edge `0.1164` maxDD `-0.6377`
- `risk_on_high->metal_1h` score `1.1015` n `33` status `ready` deltaP `12.9605` edge `0.0284` maxDD `-0.5074`
- `risk_on_and_context->metal_1h` score `1.1015` n `33` status `ready` deltaP `12.9605` edge `0.0284` maxDD `-0.5074`
- `risk_on_high->commodity_4h` score `0.695` n `33` status `ready` deltaP `4.1435` edge `0.1446` maxDD `-1.3162`
- `risk_on_and_context->commodity_4h` score `0.695` n `33` status `ready` deltaP `4.1435` edge `0.1446` maxDD `-1.3162`
- `risk_on_high->commodity_1h` score `0.3195` n `33` status `ready` deltaP `8.4377` edge `0.0223` maxDD `-0.6739`
- `risk_on_and_context->commodity_1h` score `0.3195` n `33` status `ready` deltaP `8.4377` edge `0.0223` maxDD `-0.6739`
- `risk_on_high->fx_1h` score `0.261` n `33` status `ready` deltaP `8.2472` edge `0.002` maxDD `-0.2147`
- `risk_on_and_context->fx_1h` score `0.261` n `33` status `ready` deltaP `8.2472` edge `0.002` maxDD `-0.2147`
- `market_context_high->index_24h` score `0.2198` n `149` status `ready` deltaP `2.3443` edge `0.2022` maxDD `-5.9609`
- `risk_on_high->crypto_major_1h` score `-0.1144` n `33` status `ready` deltaP `4.5818` edge `-0.0148` maxDD `-1.0995`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
