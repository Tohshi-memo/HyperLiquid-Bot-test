# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-13T11:52:26.922676+00:00`
- Price records: `672`
- Market context records: `6600`
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

- `market_context_high->unknown_24h` score `3.4342` n `166` status `ready` deltaP `3.6916` edge `0.5916` maxDD `-15.0689`
- `market_context_high->unknown_1h` score `2.0352` n `210` status `ready` deltaP `-5.1297` edge `0.2939` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `0.5411` n `166` status `ready` deltaP `9.2425` edge `0.1703` maxDD `-5.2791`
- `market_context_high->fx_1h` score `-0.309` n `210` status `ready` deltaP `1.6068` edge `0.0004` maxDD `-0.7249`
- `market_context_high->crypto_major_1h` score `-0.4812` n `210` status `ready` deltaP `6.2988` edge `0.0229` maxDD `-6.7936`
- `market_context_high->commodity_1h` score `-0.558` n `210` status `ready` deltaP `0.0399` edge `-0.0035` maxDD `-2.1314`
- `market_context_high->index_1h` score `-0.5623` n `210` status `ready` deltaP `-0.5304` edge `0.0034` maxDD `-0.7564`
- `market_context_high->crypto_alt_1h` score `-0.6793` n `210` status `ready` deltaP `4.0947` edge `0.0169` maxDD `-5.8368`
- `market_context_high->index_4h` score `-0.938` n `210` status `ready` deltaP `8.8371` edge `0.0088` maxDD `-5.7046`
- `market_context_high->commodity_4h` score `-1.2105` n `210` status `ready` deltaP `-0.2119` edge `-0.0043` maxDD `-5.6246`
- `market_context_high->equity_1h` score `-1.2388` n `210` status `ready` deltaP `1.4828` edge `-0.0021` maxDD `-4.2147`
- `market_context_high->metal_1h` score `-1.353` n `210` status `ready` deltaP `-4.3256` edge `-0.0032` maxDD `-2.1239`
- `market_context_high->fx_4h` score `-1.6349` n `210` status `ready` deltaP `1.9062` edge `-0.0011` maxDD `-3.3635`
- `market_context_high->unknown_4h` score `-1.7519` n `210` status `ready` deltaP `-17.5232` edge `0.2114` maxDD `-10.5788`
- `market_context_high->crypto_major_4h` score `-1.9277` n `210` status `ready` deltaP `6.3618` edge `0.0419` maxDD `-16.8495`
- `market_context_high->metal_4h` score `-2.2185` n `210` status `ready` deltaP `-2.1109` edge `0.0157` maxDD `-5.2172`
- `market_context_high->crypto_alt_4h` score `-2.2312` n `210` status `ready` deltaP `3.4088` edge `0.0314` maxDD `-19.2145`
- `market_context_high->fx_24h` score `-3.8352` n `166` status `ready` deltaP `-5.6405` edge `-0.0006` maxDD `-9.2795`
- `market_context_high->metal_24h` score `-4.5634` n `166` status `ready` deltaP `0.4148` edge `0.059` maxDD `-10.3637`
- `market_context_high->equity_4h` score `-4.9258` n `210` status `ready` deltaP `6.4387` edge `-0.0265` maxDD `-27.1529`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
