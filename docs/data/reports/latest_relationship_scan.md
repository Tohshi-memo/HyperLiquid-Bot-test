# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-08T21:22:12.685993+00:00`
- Price records: `672`
- Market context records: `796`
- Flow alert records: `2240`
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

- `market_context_high->crypto_major_24h` score `12.8088` n `149` status `ready` deltaP `30.1641` edge `0.8997` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `5.8501` n `149` status `ready` deltaP `7.1414` edge `0.4447` maxDD `-0.0508`
- `risk_on_high->equity_4h` score `3.6712` n `33` status `ready` deltaP `10.3428` edge `0.2735` maxDD `-0.9217`
- `risk_on_and_context->equity_4h` score `3.6712` n `33` status `ready` deltaP `10.3428` edge `0.2735` maxDD `-0.9217`
- `risk_on_high->index_4h` score `2.9517` n `33` status `ready` deltaP `18.5375` edge `0.1312` maxDD `-0.038`
- `risk_on_and_context->index_4h` score `2.9517` n `33` status `ready` deltaP `18.5375` edge `0.1312` maxDD `-0.038`
- `risk_on_high->crypto_major_4h` score `2.83` n `33` status `ready` deltaP `20.2698` edge `0.1379` maxDD `-0.9758`
- `risk_on_and_context->crypto_major_4h` score `2.83` n `33` status `ready` deltaP `20.2698` edge `0.1379` maxDD `-0.9758`
- `risk_on_high->crypto_alt_4h` score `2.8231` n `33` status `ready` deltaP `21.2445` edge `0.1141` maxDD `-0.6377`
- `risk_on_and_context->crypto_alt_4h` score `2.8231` n `33` status `ready` deltaP `21.2445` edge `0.1141` maxDD `-0.6377`
- `risk_on_high->metal_1h` score `1.1063` n `33` status `ready` deltaP `12.9605` edge `0.0288` maxDD `-0.5074`
- `risk_on_and_context->metal_1h` score `1.1063` n `33` status `ready` deltaP `12.9605` edge `0.0288` maxDD `-0.5074`
- `risk_on_high->commodity_4h` score `0.7265` n `33` status `ready` deltaP `4.4484` edge `0.1466` maxDD `-1.3162`
- `risk_on_and_context->commodity_4h` score `0.7265` n `33` status `ready` deltaP `4.4484` edge `0.1466` maxDD `-1.3162`
- `risk_on_high->commodity_1h` score `0.2992` n `33` status `ready` deltaP `8.1383` edge `0.0217` maxDD `-0.6739`
- `risk_on_and_context->commodity_1h` score `0.2992` n `33` status `ready` deltaP `8.1383` edge `0.0217` maxDD `-0.6739`
- `risk_on_high->fx_1h` score `0.2532` n `33` status `ready` deltaP `8.0975` edge `0.002` maxDD `-0.2147`
- `risk_on_and_context->fx_1h` score `0.2532` n `33` status `ready` deltaP `8.0975` edge `0.002` maxDD `-0.2147`
- `market_context_high->index_24h` score `0.1248` n `149` status `ready` deltaP `1.9971` edge `0.1966` maxDD `-5.9609`
- `risk_on_high->crypto_major_1h` score `-0.0949` n `33` status `ready` deltaP `4.8812` edge `-0.0143` maxDD `-1.0995`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
