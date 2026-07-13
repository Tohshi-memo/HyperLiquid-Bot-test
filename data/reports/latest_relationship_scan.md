# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-13T08:22:30.297903+00:00`
- Price records: `672`
- Market context records: `6585`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9808`

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

- `market_context_high->unknown_24h` score `4.9633` n `153` status `ready` deltaP `7.3555` edge `0.6946` maxDD `-15.0689`
- `market_context_high->unknown_1h` score `1.9597` n `210` status `ready` deltaP `-5.7285` edge `0.2916` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `1.1917` n `153` status `ready` deltaP `12.8145` edge `0.2007` maxDD `-5.2791`
- `market_context_high->fx_1h` score `-0.3604` n `210` status `ready` deltaP `0.7086` edge `-0.0002` maxDD `-0.7249`
- `market_context_high->crypto_major_1h` score `-0.4423` n `210` status `ready` deltaP `6.7479` edge `0.0249` maxDD `-6.7936`
- `market_context_high->commodity_1h` score `-0.558` n `210` status `ready` deltaP `0.0399` edge `-0.0035` maxDD `-2.1314`
- `market_context_high->index_1h` score `-0.5631` n `210` status `ready` deltaP `-0.5304` edge `0.0033` maxDD `-0.7564`
- `market_context_high->crypto_alt_1h` score `-0.6162` n `210` status `ready` deltaP `4.8432` edge `0.02` maxDD `-5.8368`
- `market_context_high->index_4h` score `-0.9105` n `210` status `ready` deltaP `9.142` edge `0.0103` maxDD `-5.7046`
- `market_context_high->equity_1h` score `-1.1633` n `210` status `ready` deltaP `2.0816` edge `0.0002` maxDD `-4.2147`
- `market_context_high->commodity_4h` score `-1.2955` n `210` status `ready` deltaP `-1.1266` edge `-0.0091` maxDD `-5.6246`
- `market_context_high->metal_1h` score `-1.3818` n `210` status `ready` deltaP `-4.625` edge `-0.0036` maxDD `-2.1239`
- `market_context_high->unknown_4h` score `-1.6559` n `210` status `ready` deltaP `-16.6086` edge `0.2133` maxDD `-10.5788`
- `market_context_high->fx_4h` score `-1.7195` n `210` status `ready` deltaP `0.5342` edge `-0.0028` maxDD `-3.3635`
- `market_context_high->crypto_major_4h` score `-1.7998` n `210` status `ready` deltaP `7.2765` edge `0.0522` maxDD `-16.8495`
- `market_context_high->crypto_alt_4h` score `-2.1027` n `210` status `ready` deltaP `4.171` edge `0.0428` maxDD `-19.2145`
- `market_context_high->metal_4h` score `-2.1579` n `210` status `ready` deltaP `-1.5012` edge `0.0194` maxDD `-5.2172`
- `market_context_high->metal_24h` score `-3.1025` n `153` status `ready` deltaP `3.5999` edge `0.0748` maxDD `-7.9205`
- `market_context_high->fx_24h` score `-3.7483` n `153` status `ready` deltaP `-3.7895` edge `-0.0018` maxDD `-9.2795`
- `market_context_high->equity_4h` score `-4.7387` n `210` status `ready` deltaP `7.3534` edge `-0.017` maxDD `-27.1529`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
