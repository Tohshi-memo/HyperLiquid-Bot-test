# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-29T02:22:29.631504+00:00`
- Price records: `672`
- Market context records: `5101`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10340`

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

- `market_context_high->unknown_24h` score `18.73` n `79` status `ready` deltaP `27.3734` edge `1.4126` maxDD `-1.4072`
- `market_context_high->unknown_4h` score `8.2985` n `108` status `ready` deltaP `22.4198` edge `0.6443` maxDD `-5.5109`
- `market_context_high->unknown_1h` score `7.2455` n `120` status `ready` deltaP `4.7006` edge `0.6366` maxDD `-2.7986`
- `market_context_high->crypto_alt_4h` score `2.8627` n `108` status `ready` deltaP `13.6687` edge `0.4358` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `2.1789` n `108` status `ready` deltaP `11.9693` edge `0.4288` maxDD `-14.0065`
- `market_context_high->equity_4h` score `0.9213` n `108` status `ready` deltaP `9.8691` edge `0.1738` maxDD `-6.3852`
- `market_context_high->crypto_alt_1h` score `0.523` n `120` status `ready` deltaP `7.0958` edge `0.1159` maxDD `-5.0257`
- `market_context_high->equity_1h` score `0.4698` n `120` status `ready` deltaP `8.9321` edge `0.06` maxDD `-2.745`
- `market_context_high->crypto_major_1h` score `0.413` n `120` status `ready` deltaP `7.8892` edge `0.1249` maxDD `-6.9639`
- `market_context_high->metal_1h` score `0.3021` n `120` status `ready` deltaP `8.8922` edge `0.0291` maxDD `-1.3057`
- `market_context_high->index_1h` score `-0.0416` n `120` status `ready` deltaP `5.0` edge `0.0117` maxDD `-1.0296`
- `market_context_high->index_4h` score `-0.0555` n `108` status `ready` deltaP `6.2726` edge `0.0345` maxDD `-1.6745`
- `market_context_high->metal_4h` score `-0.4271` n `108` status `ready` deltaP `3.4609` edge `0.0632` maxDD `-4.6157`
- `market_context_high->commodity_1h` score `-0.8406` n `120` status `ready` deltaP `0.8134` edge `0.0003` maxDD `-2.062`
- `market_context_high->fx_1h` score `-1.35` n `120` status `ready` deltaP `-7.006` edge `-0.0017` maxDD `-0.7944`
- `market_context_high->fx_24h` score `-1.592` n `79` status `ready` deltaP `-3.4898` edge `-0.0082` maxDD `-1.7626`
- `market_context_high->commodity_24h` score `-1.676` n `79` status `ready` deltaP `7.7004` edge `0.03` maxDD `-15.0303`
- `market_context_high->fx_4h` score `-1.9167` n `108` status `ready` deltaP `-6.9501` edge `-0.0061` maxDD `-1.9169`
- `market_context_high->commodity_4h` score `-2.1037` n `108` status `ready` deltaP `2.6761` edge `-0.0231` maxDD `-7.2707`
- `market_context_high->metal_24h` score `-4.5402` n `79` status `ready` deltaP `-6.5995` edge `0.0074` maxDD `-32.9721`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
