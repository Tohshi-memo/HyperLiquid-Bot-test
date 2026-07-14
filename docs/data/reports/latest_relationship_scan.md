# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-14T05:52:28.559183+00:00`
- Price records: `672`
- Market context records: `6680`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11784`

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

- `market_context_high->unknown_1h` score `2.4844` n `201` status `ready` deltaP `-4.4798` edge `0.327` maxDD `-3.2083`
- `market_context_high->unknown_4h` score `1.3793` n `201` status `ready` deltaP `-13.1689` edge `0.4433` maxDD `-10.5788`
- `market_context_high->commodity_24h` score `1.1425` n `201` status `ready` deltaP `12.1399` edge `0.2011` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `0.0182` n `201` status `ready` deltaP `7.4076` edge `0.0431` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `-0.1636` n `201` status `ready` deltaP `4.9684` edge `0.038` maxDD `-3.7803`
- `market_context_high->unknown_24h` score `-0.1719` n `201` status `ready` deltaP `-3.7081` edge `0.3779` maxDD `-12.3511`
- `market_context_high->fx_1h` score `-0.2659` n `201` status `ready` deltaP `2.3051` edge `0.0009` maxDD `-0.6953`
- `market_context_high->index_1h` score `-0.5425` n `201` status `ready` deltaP `-0.0946` edge `0.0025` maxDD `-0.7136`
- `market_context_high->commodity_1h` score `-0.6178` n `201` status `ready` deltaP `-0.359` edge `-0.0085` maxDD `-2.1314`
- `market_context_high->index_4h` score `-0.888` n `201` status `ready` deltaP `10.2794` edge `0.0056` maxDD `-5.7046`
- `market_context_high->equity_1h` score `-0.9902` n `201` status `ready` deltaP `2.9828` edge `0.0003` maxDD `-3.8827`
- `market_context_high->metal_1h` score `-1.2171` n `201` status `ready` deltaP `-4.6206` edge `-0.0014` maxDD `-1.5374`
- `market_context_high->fx_4h` score `-1.4058` n `201` status `ready` deltaP `6.1772` edge `-0.0002` maxDD `-3.3635`
- `market_context_high->crypto_major_4h` score `-1.4309` n `201` status `ready` deltaP `8.9712` edge `0.0882` maxDD `-16.8495`
- `market_context_high->commodity_4h` score `-1.4821` n `201` status `ready` deltaP `-1.5957` edge `-0.0299` maxDD `-5.6246`
- `market_context_high->crypto_alt_4h` score `-1.6991` n `201` status `ready` deltaP `6.4115` edge `0.0796` maxDD `-19.2145`
- `market_context_high->metal_4h` score `-2.1603` n `201` status `ready` deltaP `-1.6222` edge `0.0199` maxDD `-5.2172`
- `market_context_high->equity_4h` score `-4.8701` n `201` status `ready` deltaP `7.5105` edge `-0.029` maxDD `-27.1529`
- `market_context_high->fx_24h` score `-6.3201` n `201` status `ready` deltaP `-12.1864` edge `-0.0124` maxDD `-10.6427`
- `market_context_high->metal_24h` score `-6.9947` n `201` status `ready` deltaP `-6.2604` edge `-0.0065` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
