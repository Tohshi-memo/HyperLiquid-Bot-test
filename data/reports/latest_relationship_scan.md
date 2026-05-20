# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-20T00:22:14.797071+00:00`
- Price records: `672`
- Market context records: `1270`
- Flow alert records: `5564`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8809`

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

- `market_context_high->crypto_major_24h` score `18.0025` n `128` status `ready` deltaP `41.5798` edge `1.3362` maxDD `-8.0553`
- `market_context_high->metal_24h` score `10.1463` n `128` status `ready` deltaP `5.5556` edge `0.9752` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `8.5819` n `128` status `ready` deltaP `24.9131` edge `0.7507` maxDD `-15.1306`
- `market_context_high->unknown_4h` score `8.3086` n `128` status `ready` deltaP `6.4405` edge `0.7711` maxDD `-6.7322`
- `market_context_high->index_24h` score `5.0226` n `128` status `ready` deltaP `26.5625` edge `0.3501` maxDD `-5.3574`
- `market_context_high->equity_4h` score `3.8422` n `128` status `ready` deltaP `19.5312` edge `0.2563` maxDD `-3.6396`
- `market_context_high->equity_24h` score `3.7944` n `128` status `ready` deltaP `24.6528` edge `0.5548` maxDD `-14.2815`
- `market_context_high->unknown_24h` score `2.3274` n `128` status `ready` deltaP `1.5625` edge `0.4565` maxDD `-10.1706`
- `market_context_high->commodity_24h` score `2.0067` n `128` status `ready` deltaP `-11.8056` edge `0.3941` maxDD `-6.8535`
- `market_context_high->index_4h` score `1.9618` n `128` status `ready` deltaP `15.5678` edge `0.128` maxDD `-2.1308`
- `market_context_high->metal_4h` score `0.8616` n `128` status `ready` deltaP `18.045` edge `0.0946` maxDD `-6.4478`
- `market_context_high->index_1h` score `0.6634` n `140` status `ready` deltaP `9.3713` edge `0.0245` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.618` n `140` status `ready` deltaP `6.1463` edge `0.0474` maxDD `-1.2834`
- `market_context_high->metal_1h` score `0.4721` n `140` status `ready` deltaP `12.0873` edge `0.0198` maxDD `-2.2164`
- `market_context_high->crypto_major_4h` score `0.4175` n `128` status `ready` deltaP `9.0511` edge `0.1853` maxDD `-8.3693`
- `market_context_high->fx_24h` score `0.0547` n `128` status `ready` deltaP `3.2119` edge `0.0296` maxDD `-0.3831`
- `market_context_high->crypto_alt_4h` score `-0.1855` n `128` status `ready` deltaP `10.2324` edge `0.2045` maxDD `-16.7194`
- `market_context_high->crypto_alt_1h` score `-0.3131` n `140` status `ready` deltaP `1.4414` edge `0.0373` maxDD `-3.6309`
- `market_context_high->fx_1h` score `-0.39` n `140` status `ready` deltaP `2.3054` edge `-0.0023` maxDD `-0.3124`
- `market_context_high->crypto_major_1h` score `-0.6078` n `140` status `ready` deltaP `1.0137` edge `0.0063` maxDD `-4.9451`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
