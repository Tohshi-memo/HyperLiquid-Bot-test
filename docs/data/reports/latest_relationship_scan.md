# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-22T13:22:21.059442+00:00`
- Price records: `672`
- Market context records: `1530`
- Flow alert records: `6316`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8792`

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

- `market_context_high->metal_24h` score `13.4013` n `170` status `ready` deltaP `23.5539` edge `1.0598` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `11.7692` n `170` status `ready` deltaP `28.9645` edge `0.9893` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `10.4279` n `170` status `ready` deltaP `28.3477` edge `0.7932` maxDD `-8.0553`
- `market_context_high->index_24h` score `3.8949` n `170` status `ready` deltaP `20.2369` edge `0.2983` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.6742` n `170` status `ready` deltaP `13.5049` edge `0.3655` maxDD `-14.2815`
- `market_context_high->fx_24h` score `0.8832` n `170` status `ready` deltaP `18.2414` edge `0.0569` maxDD `-1.3925`
- `market_context_high->equity_4h` score `0.1444` n `195` status `ready` deltaP `3.8071` edge `0.0961` maxDD `-5.0894`
- `market_context_high->fx_1h` score `-0.5829` n `199` status `ready` deltaP `-1.2457` edge `-0.0032` maxDD `-0.3914`
- `market_context_high->crypto_alt_1h` score `-0.6216` n `199` status `ready` deltaP `-0.5296` edge `0.0262` maxDD `-4.1892`
- `market_context_high->crypto_alt_4h` score `-0.6374` n `195` status `ready` deltaP `10.5965` edge `0.1796` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `-0.6975` n `195` status `ready` deltaP `6.189` edge `0.1402` maxDD `-13.3376`
- `market_context_high->commodity_1h` score `-0.7289` n `199` status `ready` deltaP `-0.3475` edge `0.001` maxDD `-4.7041`
- `market_context_high->metal_1h` score `-0.7563` n `199` status `ready` deltaP `4.9981` edge `0.0033` maxDD `-6.3532`
- `market_context_high->index_1h` score `-0.7572` n `199` status `ready` deltaP `-0.1241` edge `0.0009` maxDD `-1.7205`
- `market_context_high->equity_1h` score `-0.9075` n `199` status `ready` deltaP `-1.7813` edge `0.0171` maxDD `-2.8014`
- `market_context_high->crypto_major_1h` score `-1.1265` n `199` status `ready` deltaP `-2.0905` edge `0.0052` maxDD `-6.1883`
- `market_context_high->metal_4h` score `-1.364` n `195` status `ready` deltaP `9.903` edge `0.0895` maxDD `-12.5349`
- `market_context_high->index_4h` score `-1.4865` n `195` status `ready` deltaP `-5.3963` edge `0.021` maxDD `-3.7119`
- `market_context_high->fx_4h` score `-1.9248` n `195` status `ready` deltaP `-8.2809` edge `-0.0123` maxDD `-1.4313`
- `market_context_high->unknown_24h` score `-4.8653` n `170` status `ready` deltaP `-0.4759` edge `-0.1293` maxDD `-10.1706`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
