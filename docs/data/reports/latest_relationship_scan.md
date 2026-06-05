# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-05T15:37:25.588218+00:00`
- Price records: `672`
- Market context records: `2982`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6970`

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

- `market_context_high->crypto_alt_24h` score `15.6619` n `101` status `ready` deltaP `5.7498` edge `1.6585` maxDD `-22.6673`
- `market_context_high->commodity_24h` score `11.2905` n `101` status `ready` deltaP `40.24` edge `0.6907` maxDD `-0.7805`
- `market_context_high->unknown_24h` score `10.6862` n `101` status `ready` deltaP `16.7973` edge `0.825` maxDD `-1.7175`
- `market_context_high->equity_24h` score `6.7451` n `101` status `ready` deltaP `15.6095` edge `0.6584` maxDD `-12.6963`
- `market_context_high->index_24h` score `4.2175` n `101` status `ready` deltaP `15.68` edge `0.345` maxDD `-2.5127`
- `market_context_high->equity_4h` score `2.9946` n `102` status `ready` deltaP `15.0137` edge `0.1884` maxDD `-0.7819`
- `market_context_high->index_4h` score `2.1696` n `102` status `ready` deltaP `19.7602` edge `0.1279` maxDD `-1.9733`
- `market_context_high->commodity_4h` score `2.023` n `102` status `ready` deltaP `15.6892` edge `0.1287` maxDD `-2.8438`
- `market_context_high->equity_1h` score `0.8793` n `103` status `ready` deltaP `6.9734` edge `0.0618` maxDD `-1.1343`
- `market_context_high->index_1h` score `0.6318` n `103` status `ready` deltaP `8.4748` edge `0.0353` maxDD `-0.7983`
- `market_context_high->crypto_alt_4h` score `0.6113` n `102` status `ready` deltaP `22.5012` edge `0.3845` maxDD `-30.8239`
- `market_context_high->crypto_alt_1h` score `-0.1663` n `103` status `ready` deltaP `9.373` edge `0.0797` maxDD `-10.747`
- `market_context_high->commodity_1h` score `-0.1837` n `103` status `ready` deltaP `-0.1904` edge `0.0139` maxDD `-1.2282`
- `market_context_high->crypto_major_1h` score `-0.3926` n `103` status `ready` deltaP `7.812` edge `0.0512` maxDD `-9.622`
- `market_context_high->fx_1h` score `-0.4627` n `103` status `ready` deltaP `-1.4607` edge `0.0019` maxDD `-0.1244`
- `market_context_high->fx_4h` score `-1.0343` n `102` status `ready` deltaP `-8.3004` edge `0.0006` maxDD `-0.5631`
- `market_context_high->metal_1h` score `-1.2152` n `103` status `ready` deltaP `-1.8967` edge `0.0052` maxDD `-3.8394`
- `market_context_high->unknown_4h` score `-1.2693` n `102` status `ready` deltaP `-0.6964` edge `0.0042` maxDD `-3.7602`
- `market_context_high->fx_24h` score `-1.4065` n `101` status `ready` deltaP `-9.6346` edge `-0.0289` maxDD `-0.6418`
- `market_context_high->unknown_1h` score `-1.4599` n `103` status `ready` deltaP `3.0943` edge `-0.0692` maxDD `-3.1801`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
