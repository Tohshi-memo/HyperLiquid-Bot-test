# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-19T15:52:22.754120+00:00`
- Price records: `672`
- Market context records: `1234`
- Flow alert records: `5458`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8788`

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

- `market_context_high->crypto_major_24h` score `18.806` n `128` status `ready` deltaP `44.184` edge `1.3858` maxDD `-8.0553`
- `market_context_high->unknown_4h` score `7.9155` n `128` status `ready` deltaP `4.0015` edge `0.7546` maxDD `-6.7322`
- `market_context_high->crypto_alt_24h` score `7.7077` n `128` status `ready` deltaP `22.6562` edge `0.6929` maxDD `-15.1306`
- `market_context_high->metal_24h` score `6.5084` n `128` status `ready` deltaP `-0.3472` edge `0.7114` maxDD `-6.3373`
- `market_context_high->commodity_24h` score `4.4806` n `128` status `ready` deltaP `-5.9028` edge `0.5609` maxDD `-6.8535`
- `market_context_high->equity_4h` score `3.4976` n `128` status `ready` deltaP `17.5495` edge `0.2408` maxDD `-3.6396`
- `market_context_high->index_24h` score `3.4824` n `128` status `ready` deltaP `21.875` edge `0.253` maxDD `-5.3574`
- `market_context_high->equity_24h` score `3.0842` n `128` status `ready` deltaP `22.0486` edge `0.4811` maxDD `-14.2815`
- `market_context_high->index_4h` score `1.5669` n `128` status `ready` deltaP `13.5861` edge `0.1083` maxDD `-2.1308`
- `market_context_high->unknown_24h` score `1.2711` n `128` status `ready` deltaP `0.8681` edge `0.3731` maxDD `-10.1706`
- `market_context_high->index_1h` score `0.7308` n `128` status `ready` deltaP `10.1984` edge `0.0246` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.6602` n `128` status `ready` deltaP `5.609` edge `0.0545` maxDD `-1.2834`
- `market_context_high->fx_24h` score `0.5006` n `128` status `ready` deltaP `7.0313` edge `0.0413` maxDD `-0.3831`
- `market_context_high->metal_1h` score `0.1514` n `128` status `ready` deltaP `10.2685` edge `0.0052` maxDD `-2.2164`
- `market_context_high->fx_1h` score `-0.0629` n `128` status `ready` deltaP `6.0489` edge `0.0` maxDD `-0.3124`
- `market_context_high->crypto_major_4h` score `-0.0935` n `128` status `ready` deltaP `6.1548` edge `0.1391` maxDD `-8.3693`
- `market_context_high->metal_4h` score `-0.1041` n `128` status `ready` deltaP `14.5389` edge `0.0375` maxDD `-6.4478`
- `market_context_high->crypto_alt_1h` score `-0.3313` n `128` status `ready` deltaP `0.4959` edge `0.0385` maxDD `-3.4088`
- `market_context_high->crypto_major_1h` score `-0.4409` n `128` status `ready` deltaP `2.0771` edge `0.0062` maxDD `-4.1256`
- `market_context_high->crypto_alt_4h` score `-0.8002` n `128` status `ready` deltaP `7.3361` edge `0.145` maxDD `-16.7194`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
