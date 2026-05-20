# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-20T21:07:20.005618+00:00`
- Price records: `672`
- Market context records: `1357`
- Flow alert records: `5820`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8794`

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

- `market_context_high->crypto_major_24h` score `13.4529` n `131` status `ready` deltaP `33.0246` edge `1.0141` maxDD `-8.0553`
- `market_context_high->metal_24h` score `12.6901` n `131` status `ready` deltaP `12.3781` edge `1.1417` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `9.6751` n `131` status `ready` deltaP `28.4391` edge `0.8183` maxDD `-15.1306`
- `market_context_high->index_24h` score `4.1091` n `131` status `ready` deltaP `23.5144` edge `0.2943` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.8807` n `131` status `ready` deltaP `16.4321` edge `0.3632` maxDD `-14.2815`
- `market_context_high->commodity_24h` score `2.5778` n `131` status `ready` deltaP `-8.6567` edge `0.4207` maxDD `-6.8535`
- `market_context_high->equity_4h` score `2.305` n `157` status `ready` deltaP `11.8912` edge `0.1833` maxDD `-3.6396`
- `market_context_high->fx_24h` score `1.3774` n `131` status `ready` deltaP `15.1863` edge `0.06` maxDD `-0.3831`
- `market_context_high->metal_4h` score `0.1419` n `157` status `ready` deltaP `13.068` edge `0.0678` maxDD `-6.4478`
- `market_context_high->index_1h` score `0.0289` n `168` status `ready` deltaP `4.8475` edge `0.0155` maxDD `-1.6329`
- `market_context_high->index_4h` score `-0.0016` n `157` status `ready` deltaP `4.8742` edge `0.0762` maxDD `-3.7119`
- `market_context_high->equity_1h` score `-0.0172` n `168` status `ready` deltaP `2.4559` edge `0.0268` maxDD `-1.9017`
- `market_context_high->metal_1h` score `-0.1658` n `168` status `ready` deltaP `7.4102` edge `-0.0015` maxDD `-2.8658`
- `market_context_high->fx_1h` score `-0.3088` n `168` status `ready` deltaP `1.6253` edge `-0.004` maxDD `-0.3808`
- `market_context_high->unknown_24h` score `-0.4659` n `131` status `ready` deltaP `-4.5537` edge `0.2645` maxDD `-10.1706`
- `market_context_high->commodity_1h` score `-0.5548` n `168` status `ready` deltaP `0.442` edge `0.0123` maxDD `-2.252`
- `market_context_high->crypto_alt_1h` score `-0.8627` n `168` status `ready` deltaP `-0.6202` edge `0.0193` maxDD `-3.6309`
- `market_context_high->crypto_major_1h` score `-1.1918` n `168` status `ready` deltaP `-3.8815` edge `-0.0204` maxDD `-6.1883`
- `market_context_high->crypto_alt_4h` score `-1.2925` n `157` status `ready` deltaP `8.4676` edge `0.1678` maxDD `-19.5565`
- `market_context_high->unknown_4h` score `-1.3703` n `157` status `ready` deltaP `1.5817` edge `0.0409` maxDD `-11.1695`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
