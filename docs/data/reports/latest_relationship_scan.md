# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-08T00:22:25.815591+00:00`
- Price records: `672`
- Market context records: `3231`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9724`

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

- `market_context_high->crypto_alt_24h` score `14.6874` n `103` status `ready` deltaP `20.213` edge `2.7324` maxDD `-70.3986`
- `market_context_high->commodity_24h` score `13.867` n `103` status `ready` deltaP `50.2512` edge `0.8634` maxDD `-2.0927`
- `market_context_high->index_24h` score `9.9313` n `103` status `ready` deltaP `33.3991` edge `0.8604` maxDD `-16.1026`
- `market_context_high->equity_24h` score `6.9654` n `103` status `ready` deltaP `20.9581` edge `1.5949` maxDD `-53.663`
- `market_context_high->crypto_major_24h` score `3.2937` n `103` status `ready` deltaP `24.2836` edge `2.3303` maxDD `-152.2601`
- `market_context_high->commodity_4h` score `2.494` n `129` status `ready` deltaP `18.7133` edge `0.1497` maxDD `-2.663`
- `market_context_high->commodity_1h` score `-0.234` n `141` status `ready` deltaP `4.0504` edge `0.0187` maxDD `-2.216`
- `market_context_high->index_1h` score `-0.5412` n `141` status `ready` deltaP `3.7191` edge `0.0121` maxDD `-4.5023`
- `market_context_high->unknown_4h` score `-0.7568` n `129` status `ready` deltaP `9.6155` edge `0.0994` maxDD `-15.1257`
- `market_context_high->crypto_major_1h` score `-0.8004` n `141` status `ready` deltaP `3.6554` edge `0.0993` maxDD `-15.1032`
- `market_context_high->crypto_alt_1h` score `-0.8705` n `141` status `ready` deltaP `3.459` edge `0.0908` maxDD `-14.7034`
- `market_context_high->equity_1h` score `-0.9545` n `141` status `ready` deltaP `3.3805` edge `0.012` maxDD `-8.8863`
- `market_context_high->metal_1h` score `-1.3852` n `141` status `ready` deltaP `-3.1915` edge `-0.0096` maxDD `-8.0708`
- `market_context_high->index_4h` score `-1.4123` n `129` status `ready` deltaP `9.9818` edge `0.0433` maxDD `-17.6057`
- `market_context_high->fx_24h` score `-1.487` n `103` status `ready` deltaP `-5.4376` edge `-0.0205` maxDD `-2.0446`
- `market_context_high->fx_1h` score `-1.9537` n `141` status `ready` deltaP `-13.0027` edge `-0.0065` maxDD `-0.9034`
- `market_context_high->fx_4h` score `-2.3621` n `129` status `ready` deltaP `-13.6179` edge `-0.014` maxDD `-1.6975`
- `market_context_high->unknown_1h` score `-2.8421` n `141` status `ready` deltaP `1.6871` edge `-0.1319` maxDD `-17.8311`
- `market_context_high->equity_4h` score `-3.3071` n `129` status `ready` deltaP `11.2013` edge `0.0319` maxDD `-36.7784`
- `market_context_high->metal_4h` score `-3.8965` n `129` status `ready` deltaP `-10.3032` edge `-0.0214` maxDD `-24.4238`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
