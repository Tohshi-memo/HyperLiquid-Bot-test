# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-01T08:22:26.960966+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6457`

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

- `market_context_high->unknown_24h` score `7032.9124` n `55` status `ready` deltaP `4.3403` edge `586.0471` maxDD `0.0`
- `market_context_high->unknown_4h` score `374.1603` n `55` status `ready` deltaP `5.3464` edge `31.1487` maxDD `-0.0124`
- `news_risk_high->unknown_1h` score `72.3948` n `113` status `ready` deltaP `-4.3757` edge `6.0907` maxDD `-0.9571`
- `market_context_high->unknown_1h` score `57.6449` n `55` status `ready` deltaP `2.4143` edge `4.7987` maxDD `-0.2178`
- `market_context_high->equity_24h` score `21.6018` n `55` status `ready` deltaP `45.5776` edge `1.5199` maxDD `-1.5546`
- `news_risk_high->crypto_alt_24h` score `12.9291` n `98` status `ready` deltaP `29.8115` edge `1.0143` maxDD `-6.8493`
- `market_context_high->index_24h` score `7.2232` n `55` status `ready` deltaP `59.375` edge `0.2061` maxDD `0.0`
- `market_context_high->commodity_24h` score `6.6719` n `55` status `ready` deltaP `46.1364` edge `0.2795` maxDD `-0.8203`
- `market_context_high->crypto_alt_4h` score `5.6711` n `55` status `ready` deltaP `22.6829` edge `0.3508` maxDD `-1.6876`
- `market_context_high->crypto_major_4h` score `5.4003` n `55` status `ready` deltaP `29.9779` edge `0.2838` maxDD `-1.6901`
- `news_risk_high->crypto_alt_4h` score `4.7561` n `108` status `ready` deltaP `17.6829` edge `0.4171` maxDD `-7.4246`
- `market_context_high->commodity_4h` score `3.3987` n `55` status `ready` deltaP `31.8293` edge `0.0961` maxDD `-0.3387`
- `market_context_high->equity_4h` score `3.3054` n `55` status `ready` deltaP `5.4379` edge `0.3094` maxDD `-2.283`
- `market_context_high->crypto_major_24h` score `2.5161` n `55` status `ready` deltaP `11.0322` edge `0.3167` maxDD `-3.0799`
- `market_context_high->crypto_alt_24h` score `1.8285` n `55` status `ready` deltaP `-4.9937` edge `0.4195` maxDD `-8.8096`
- `market_context_high->metal_4h` score `1.551` n `55` status `ready` deltaP `18.3508` edge `0.0494` maxDD `-0.7323`
- `market_context_high->equity_1h` score `1.4231` n `55` status `ready` deltaP `1.9788` edge `0.1579` maxDD `-1.5336`
- `market_context_high->crypto_major_1h` score `1.3796` n `55` status `ready` deltaP `8.0321` edge `0.1224` maxDD `-2.2118`
- `market_context_high->crypto_alt_1h` score `1.2972` n `55` status `ready` deltaP `3.6255` edge `0.151` maxDD `-2.3659`
- `market_context_high->metal_1h` score `0.8612` n `55` status `ready` deltaP `10.7267` edge `0.0251` maxDD `-0.3209`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
