# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-19T23:22:14.587826+00:00`
- Price records: `672`
- Market context records: `1265`
- Flow alert records: `5551`
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

- `market_context_high->crypto_major_24h` score `17.9641` n `128` status `ready` deltaP `41.5798` edge `1.333` maxDD `-8.0553`
- `market_context_high->metal_24h` score `9.6479` n `128` status `ready` deltaP `4.8611` edge `0.9383` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `8.3055` n `128` status `ready` deltaP `24.2187` edge `0.7323` maxDD `-15.1306`
- `market_context_high->unknown_4h` score `8.2396` n `128` status `ready` deltaP `5.9832` edge `0.7684` maxDD `-6.7322`
- `market_context_high->index_24h` score `4.7702` n `128` status `ready` deltaP `25.8681` edge `0.3337` maxDD `-5.3574`
- `market_context_high->equity_4h` score `3.7302` n `128` status `ready` deltaP `19.2263` edge `0.249` maxDD `-3.6396`
- `market_context_high->equity_24h` score `3.6335` n `128` status `ready` deltaP `23.9583` edge `0.5388` maxDD `-14.2815`
- `market_context_high->commodity_24h` score `2.3167` n `128` status `ready` deltaP `-11.1111` edge `0.4153` maxDD `-6.8535`
- `market_context_high->unknown_24h` score `2.2998` n `128` status `ready` deltaP `1.5625` edge `0.4542` maxDD `-10.1706`
- `market_context_high->index_4h` score `1.8426` n `128` status `ready` deltaP `15.2629` edge `0.1201` maxDD `-2.1308`
- `market_context_high->metal_4h` score `0.799` n `128` status `ready` deltaP `17.8926` edge `0.0904` maxDD `-6.4478`
- `market_context_high->index_1h` score `0.6673` n `136` status `ready` deltaP `9.6601` edge `0.0229` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.6581` n `136` status `ready` deltaP `6.393` edge `0.0491` maxDD `-1.2834`
- `market_context_high->metal_1h` score `0.458` n `136` status `ready` deltaP `12.2711` edge `0.0174` maxDD `-2.2164`
- `market_context_high->crypto_major_4h` score `0.307` n `128` status `ready` deltaP `8.4414` edge `0.1752` maxDD `-8.3693`
- `market_context_high->fx_24h` score `0.0885` n `128` status `ready` deltaP `3.5591` edge `0.0301` maxDD `-0.3831`
- `market_context_high->crypto_alt_4h` score `-0.2819` n `128` status `ready` deltaP `9.6227` edge `0.1962` maxDD `-16.7194`
- `market_context_high->fx_1h` score `-0.3531` n `136` status `ready` deltaP `2.7519` edge `-0.0022` maxDD `-0.3124`
- `market_context_high->crypto_alt_1h` score `-0.3986` n `136` status `ready` deltaP `0.6825` edge `0.0314` maxDD `-3.6309`
- `market_context_high->crypto_major_1h` score `-0.6394` n `136` status `ready` deltaP `0.7353` edge `0.0041` maxDD `-4.9451`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
