# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-13T08:52:27.982526+00:00`
- Price records: `672`
- Market context records: `6587`
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

- `market_context_high->unknown_24h` score `4.7376` n `155` status `ready` deltaP `7.0689` edge `0.6777` maxDD `-15.0689`
- `market_context_high->unknown_1h` score `1.9825` n `210` status `ready` deltaP `-5.7285` edge `0.2935` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `1.0793` n `155` status `ready` deltaP `12.19` edge `0.1955` maxDD `-5.2791`
- `market_context_high->fx_1h` score `-0.344` n `210` status `ready` deltaP `1.008` edge `-0.0001` maxDD `-0.7249`
- `market_context_high->crypto_major_1h` score `-0.4633` n `210` status `ready` deltaP `6.5982` edge `0.0232` maxDD `-6.7936`
- `market_context_high->commodity_1h` score `-0.5347` n `210` status `ready` deltaP `0.3393` edge `-0.0025` maxDD `-2.1314`
- `market_context_high->index_1h` score `-0.581` n `210` status `ready` deltaP `-0.8298` edge `0.003` maxDD `-0.7564`
- `market_context_high->crypto_alt_1h` score `-0.6381` n `210` status `ready` deltaP `4.6935` edge `0.0182` maxDD `-5.8368`
- `market_context_high->index_4h` score `-0.912` n `210` status `ready` deltaP `9.142` edge `0.0101` maxDD `-5.7046`
- `market_context_high->equity_1h` score `-1.2004` n `210` status `ready` deltaP `1.7822` edge `-0.0009` maxDD `-4.2147`
- `market_context_high->commodity_4h` score `-1.2718` n `210` status `ready` deltaP `-0.8217` edge `-0.0081` maxDD `-5.6246`
- `market_context_high->metal_1h` score `-1.4129` n `210` status `ready` deltaP `-4.9244` edge `-0.0042` maxDD `-2.1239`
- `market_context_high->unknown_4h` score `-1.6911` n `210` status `ready` deltaP `-16.9135` edge `0.2124` maxDD `-10.5788`
- `market_context_high->fx_4h` score `-1.7021` n `210` status `ready` deltaP `0.8391` edge `-0.0026` maxDD `-3.3635`
- `market_context_high->crypto_major_4h` score `-1.8406` n `210` status `ready` deltaP `6.9716` edge `0.049` maxDD `-16.8495`
- `market_context_high->crypto_alt_4h` score `-2.1505` n `210` status `ready` deltaP `3.8661` edge `0.0387` maxDD `-19.2145`
- `market_context_high->metal_4h` score `-2.1634` n `210` status `ready` deltaP `-1.5012` edge `0.0187` maxDD `-5.2172`
- `market_context_high->metal_24h` score `-3.311` n `155` status `ready` deltaP `3.0854` edge `0.0729` maxDD `-8.2177`
- `market_context_high->fx_24h` score `-3.7372` n `155` status `ready` deltaP `-3.6504` edge `-0.0013` maxDD `-9.2795`
- `market_context_high->equity_4h` score `-4.7483` n `210` status `ready` deltaP `7.3534` edge `-0.0178` maxDD `-27.1529`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
