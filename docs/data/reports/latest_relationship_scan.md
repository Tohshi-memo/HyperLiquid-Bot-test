# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-20T03:07:17.992574+00:00`
- Price records: `672`
- Market context records: `1281`
- Flow alert records: `5598`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8820`

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

- `market_context_high->crypto_major_24h` score `17.7853` n `128` status `ready` deltaP `41.5798` edge `1.3181` maxDD `-8.0553`
- `market_context_high->metal_24h` score `11.169` n `128` status `ready` deltaP `7.4653` edge `1.0477` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `8.9321` n `128` status `ready` deltaP `25.7812` edge `0.7741` maxDD `-15.1306`
- `market_context_high->index_24h` score `5.455` n `128` status `ready` deltaP `28.4722` edge `0.3734` maxDD `-5.3574`
- `market_context_high->unknown_4h` score `4.0156` n `139` status `ready` deltaP `3.8844` edge `0.4523` maxDD `-7.1517`
- `market_context_high->equity_24h` score `3.898` n `128` status `ready` deltaP `25.1736` edge `0.5646` maxDD `-14.2815`
- `market_context_high->equity_4h` score `2.8152` n `139` status `ready` deltaP `13.9838` edge `0.2077` maxDD `-3.6396`
- `market_context_high->unknown_24h` score `2.3598` n `128` status `ready` deltaP `1.5625` edge `0.4592` maxDD `-10.1706`
- `market_context_high->commodity_24h` score `1.5469` n `128` status `ready` deltaP `-13.3681` edge `0.3662` maxDD `-6.8535`
- `market_context_high->index_4h` score `1.1505` n `139` status `ready` deltaP `9.3811` edge `0.1058` maxDD `-2.1308`
- `market_context_high->metal_4h` score `0.5141` n `139` status `ready` deltaP `15.711` edge `0.0812` maxDD `-6.4478`
- `market_context_high->equity_1h` score `0.4467` n `151` status `ready` deltaP `5.0611` edge `0.0462` maxDD `-1.7505`
- `market_context_high->fx_24h` score `0.2579` n `128` status `ready` deltaP `5.1216` edge `0.0338` maxDD `-0.3831`
- `market_context_high->index_1h` score `0.2331` n `151` status `ready` deltaP `7.3066` edge `0.0224` maxDD `-1.2979`
- `market_context_high->metal_1h` score `0.2304` n `151` status `ready` deltaP `10.6456` edge `0.0117` maxDD `-2.4112`
- `market_context_high->crypto_alt_1h` score `-0.2983` n `151` status `ready` deltaP `1.3969` edge `0.0395` maxDD `-3.6309`
- `market_context_high->crypto_major_4h` score `-0.4986` n `139` status `ready` deltaP `5.366` edge `0.1413` maxDD `-12.2799`
- `market_context_high->fx_1h` score `-0.5756` n `151` status `ready` deltaP `0.2855` edge `-0.0043` maxDD `-0.3124`
- `market_context_high->crypto_major_1h` score `-0.7153` n `151` status `ready` deltaP `0.3539` edge `0.008` maxDD `-5.8323`
- `market_context_high->crypto_alt_4h` score `-0.8572` n `139` status `ready` deltaP `8.3644` edge `0.1663` maxDD `-19.5565`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
