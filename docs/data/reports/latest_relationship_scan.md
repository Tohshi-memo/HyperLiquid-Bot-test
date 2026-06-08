# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-08T00:07:28.167025+00:00`
- Price records: `672`
- Market context records: `3230`
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

- `market_context_high->crypto_alt_24h` score `14.5273` n `102` status `ready` deltaP `19.8631` edge `2.7142` maxDD `-70.3986`
- `market_context_high->commodity_24h` score `13.9567` n `102` status `ready` deltaP `50.3676` edge `0.8701` maxDD `-2.0927`
- `market_context_high->index_24h` score `9.8941` n `102` status `ready` deltaP `33.3538` edge `0.8576` maxDD `-16.1026`
- `market_context_high->equity_24h` score `6.8449` n `102` status `ready` deltaP `20.7414` edge `1.5809` maxDD `-53.663`
- `market_context_high->crypto_major_24h` score `2.9551` n `102` status `ready` deltaP `23.8767` edge `2.2896` maxDD `-152.2601`
- `market_context_high->commodity_4h` score `2.622` n `128` status `ready` deltaP `19.1121` edge `0.1514` maxDD `-2.4918`
- `market_context_high->commodity_1h` score `-0.1602` n `140` status `ready` deltaP `4.2857` edge `0.0187` maxDD `-2.1831`
- `market_context_high->index_1h` score `-0.5833` n `140` status `ready` deltaP `3.3747` edge `0.009` maxDD `-4.5023`
- `market_context_high->unknown_4h` score `-0.7909` n `128` status `ready` deltaP `9.4893` edge `0.0974` maxDD `-15.1257`
- `market_context_high->crypto_major_1h` score `-0.8379` n `140` status `ready` deltaP `3.4303` edge `0.096` maxDD `-15.1032`
- `market_context_high->crypto_alt_1h` score `-0.8871` n `140` status `ready` deltaP `3.2592` edge `0.09` maxDD `-14.7034`
- `market_context_high->equity_1h` score `-1.0096` n `140` status `ready` deltaP `3.1908` edge `0.0062` maxDD `-8.8863`
- `market_context_high->fx_24h` score `-1.4222` n `102` status `ready` deltaP `-4.9734` edge `-0.0201` maxDD `-1.9926`
- `market_context_high->index_4h` score `-1.4594` n `128` status `ready` deltaP `9.6609` edge `0.0394` maxDD `-17.6057`
- `market_context_high->fx_1h` score `-1.9922` n `140` status `ready` deltaP `-13.4688` edge `-0.0066` maxDD `-0.9034`
- `market_context_high->metal_1h` score `-2.1868` n `140` status `ready` deltaP `-3.4217` edge `-0.0127` maxDD `-8.0708`
- `market_context_high->fx_4h` score `-2.3467` n `128` status `ready` deltaP `-13.5099` edge `-0.0139` maxDD `-1.6604`
- `market_context_high->unknown_1h` score `-2.8437` n `140` status `ready` deltaP `1.5227` edge `-0.131` maxDD `-17.8311`
- `market_context_high->equity_4h` score `-3.3995` n `128` status `ready` deltaP `10.8804` edge `0.0222` maxDD `-36.7784`
- `market_context_high->metal_4h` score `-3.954` n `128` status `ready` deltaP `-10.6897` edge `-0.0262` maxDD `-24.4238`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
