# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-17T17:52:29.827994+00:00`
- Price records: `672`
- Market context records: `7053`
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

- `market_context_high->fx_4h` score `0.492` n `195` status `ready` deltaP `15.0305` edge `0.0108` maxDD `-0.9333`
- `market_context_high->fx_1h` score `-0.3005` n `195` status `ready` deltaP `2.7568` edge `0.0017` maxDD `-0.276`
- `market_context_high->crypto_alt_1h` score `-0.6193` n `195` status `ready` deltaP `0.8744` edge `0.029` maxDD `-4.5815`
- `market_context_high->metal_1h` score `-0.8076` n `195` status `ready` deltaP `-3.7126` edge `-0.002` maxDD `-2.1427`
- `market_context_high->commodity_1h` score `-0.8123` n `195` status `ready` deltaP `-3.827` edge `-0.017` maxDD `-1.9306`
- `market_context_high->index_1h` score `-0.8217` n `195` status `ready` deltaP `-1.5339` edge `-0.004` maxDD `-2.2895`
- `market_context_high->unknown_1h` score `-0.8661` n `195` status `ready` deltaP `-2.4129` edge `0.0163` maxDD `-2.1244`
- `market_context_high->crypto_major_1h` score `-0.9701` n `195` status `ready` deltaP `3.5245` edge `0.0309` maxDD `-7.1523`
- `market_context_high->unknown_4h` score `-1.2278` n `195` status `ready` deltaP `-5.6355` edge `0.1042` maxDD `-5.1827`
- `market_context_high->equity_1h` score `-1.9984` n `195` status `ready` deltaP `2.8458` edge `-0.0329` maxDD `-14.716`
- `market_context_high->metal_4h` score `-2.146` n `195` status `ready` deltaP `3.1786` edge `0.002` maxDD `-5.5324`
- `market_context_high->index_4h` score `-2.2301` n `195` status `ready` deltaP `2.0989` edge `-0.03` maxDD `-12.2591`
- `market_context_high->commodity_24h` score `-2.2809` n `195` status `ready` deltaP `-1.0497` edge `-0.0522` maxDD `-4.4704`
- `market_context_high->commodity_4h` score `-2.3556` n `195` status `ready` deltaP `-5.9795` edge `-0.0404` maxDD `-2.9494`
- `market_context_high->crypto_alt_4h` score `-2.6419` n `195` status `ready` deltaP `2.7509` edge `0.0215` maxDD `-22.2831`
- `market_context_high->crypto_major_4h` score `-2.8434` n `195` status `ready` deltaP `4.456` edge `0.0342` maxDD `-24.6094`
- `market_context_high->unknown_24h` score `-3.2381` n `195` status `ready` deltaP `-12.7752` edge `0.1847` maxDD `-23.5076`
- `market_context_high->fx_24h` score `-3.5042` n `195` status `ready` deltaP `0.0748` edge `-0.0098` maxDD `-3.9503`
- `market_context_high->equity_4h` score `-7.8123` n `195` status `ready` deltaP `3.4295` edge `-0.1374` maxDD `-63.963`
- `market_context_high->metal_24h` score `-15.0844` n `195` status `ready` deltaP `-17.3959` edge `-0.0817` maxDD `-44.4154`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
