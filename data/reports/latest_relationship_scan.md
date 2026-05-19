# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-19T08:37:21.026336+00:00`
- Price records: `672`
- Market context records: `1203`
- Flow alert records: `5369`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8768`

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

- `market_context_high->crypto_major_24h` score `18.5489` n `134` status `ready` deltaP `44.2553` edge `1.3639` maxDD `-8.0553`
- `market_context_high->crypto_alt_24h` score `7.5418` n `134` status `ready` deltaP `22.0668` edge `0.683` maxDD `-15.1306`
- `market_context_high->unknown_4h` score `5.6405` n `134` status `ready` deltaP `3.8837` edge `0.5658` maxDD `-6.7322`
- `market_context_high->metal_24h` score `4.4657` n `134` status `ready` deltaP `-3.7417` edge `0.5638` maxDD `-6.3373`
- `market_context_high->commodity_24h` score `3.061` n `134` status `ready` deltaP `-3.8765` edge `0.5689` maxDD `-18.0378`
- `market_context_high->equity_4h` score `2.7971` n `134` status `ready` deltaP `14.5682` edge `0.2023` maxDD `-3.6396`
- `market_context_high->index_24h` score `2.2368` n `134` status `ready` deltaP `17.33` edge `0.1795` maxDD `-5.3574`
- `market_context_high->equity_24h` score `1.7704` n `134` status `ready` deltaP `17.5736` edge `0.3425` maxDD `-14.2815`
- `market_context_high->index_4h` score `0.935` n `134` status `ready` deltaP `10.4273` edge `0.0767` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.4964` n `134` status `ready` deltaP `8.4681` edge `0.0166` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.3767` n `134` status `ready` deltaP `3.9838` edge `0.0426` maxDD `-1.3546`
- `market_context_high->fx_24h` score `0.3587` n `134` status `ready` deltaP `8.3229` edge `0.0503` maxDD `-2.7379`
- `market_context_high->unknown_24h` score `-0.0861` n `134` status `ready` deltaP `1.4382` edge `0.2562` maxDD `-10.1706`
- `market_context_high->crypto_major_4h` score `-0.0862` n `134` status `ready` deltaP `6.4593` edge `0.138` maxDD `-8.3693`
- `market_context_high->fx_1h` score `-0.137` n `134` status `ready` deltaP `5.063` edge `0.0004` maxDD `-0.3124`
- `market_context_high->metal_1h` score `-0.213` n `134` status `ready` deltaP `8.3386` edge `-0.0123` maxDD `-2.2164`
- `market_context_high->crypto_major_1h` score `-0.3418` n `134` status `ready` deltaP `3.5772` edge `0.0089` maxDD `-4.1256`
- `market_context_high->crypto_alt_1h` score `-0.3613` n `134` status `ready` deltaP `0.8781` edge `0.0321` maxDD `-3.4088`
- `market_context_high->commodity_1h` score `-0.8184` n `134` status `ready` deltaP `-2.6879` edge `0.0112` maxDD `-2.252`
- `market_context_high->metal_4h` score `-0.9767` n `134` status `ready` deltaP `8.3067` edge `-0.0375` maxDD `-6.4478`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
