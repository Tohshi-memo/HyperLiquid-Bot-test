# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-17T18:22:31.031276+00:00`
- Price records: `672`
- Market context records: `7056`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11502`

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

- `market_context_high->fx_4h` score `0.5198` n `193` status `ready` deltaP `15.3474` edge `0.011` maxDD `-0.9333`
- `market_context_high->fx_1h` score `-0.2655` n `193` status `ready` deltaP `3.1491` edge `0.002` maxDD `-0.276`
- `market_context_high->crypto_alt_1h` score `-0.5551` n `193` status `ready` deltaP `1.4218` edge `0.0307` maxDD `-4.5815`
- `market_context_high->crypto_major_1h` score `-0.6092` n `193` status `ready` deltaP `3.7247` edge `0.0323` maxDD `-7.1523`
- `market_context_high->metal_1h` score `-0.7837` n `193` status `ready` deltaP `-3.2981` edge `-0.0017` maxDD `-2.1427`
- `market_context_high->unknown_1h` score `-0.8055` n `193` status `ready` deltaP `-2.0896` edge `0.0182` maxDD `-2.0452`
- `market_context_high->index_1h` score `-0.8376` n `193` status `ready` deltaP `-1.8244` edge `-0.0041` maxDD `-2.2895`
- `market_context_high->commodity_1h` score `-0.8431` n `193` status `ready` deltaP `-4.3584` edge `-0.0174` maxDD `-1.9306`
- `market_context_high->unknown_4h` score `-1.1029` n `193` status `ready` deltaP `-5.5897` edge `0.1088` maxDD `-4.742`
- `market_context_high->equity_1h` score `-2.0045` n `193` status `ready` deltaP `2.6085` edge `-0.0321` maxDD `-14.716`
- `market_context_high->metal_4h` score `-2.1896` n `193` status `ready` deltaP `2.5196` edge `0.0008` maxDD `-5.5324`
- `market_context_high->index_4h` score `-2.2685` n `193` status `ready` deltaP `1.541` edge `-0.0312` maxDD `-12.2591`
- `market_context_high->commodity_24h` score `-2.3273` n `193` status `ready` deltaP `-1.3898` edge `-0.0538` maxDD `-4.4704`
- `market_context_high->commodity_4h` score `-2.4123` n `193` status `ready` deltaP `-6.4791` edge `-0.0418` maxDD `-2.9494`
- `market_context_high->crypto_alt_4h` score `-2.6579` n `193` status `ready` deltaP `2.6065` edge `0.0204` maxDD `-22.2831`
- `market_context_high->crypto_major_4h` score `-2.8357` n `193` status `ready` deltaP `4.709` edge `0.0335` maxDD `-24.6094`
- `market_context_high->unknown_24h` score `-3.3638` n `193` status `ready` deltaP `-13.1665` edge `0.1712` maxDD `-23.5076`
- `market_context_high->fx_24h` score `-3.4935` n `193` status `ready` deltaP `0.2536` edge `-0.0101` maxDD `-3.9503`
- `market_context_high->equity_4h` score `-7.8386` n `193` status `ready` deltaP `3.6135` edge `-0.142` maxDD `-63.963`
- `market_context_high->metal_24h` score `-15.1572` n `193` status `ready` deltaP `-17.9467` edge `-0.0841` maxDD `-44.4154`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
