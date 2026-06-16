# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-16T04:52:33.697105+00:00`
- Price records: `672`
- Market context records: `4059`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10432`

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

- `risk_on_high->unknown_4h` score `145.0479` n `40` status `ready` deltaP `-6.9817` edge `12.3155` maxDD `-10.864`
- `risk_on_and_context->unknown_4h` score `145.0479` n `40` status `ready` deltaP `-6.9817` edge `12.3155` maxDD `-10.864`
- `market_context_high->unknown_1h` score `47.2977` n `172` status `ready` deltaP `1.7303` edge `4.0877` maxDD `-9.6211`
- `market_context_high->unknown_24h` score `37.5112` n `144` status `ready` deltaP `-8.0264` edge `3.5823` maxDD `-24.2289`
- `market_context_high->unknown_4h` score `18.7661` n `166` status `ready` deltaP `-0.6263` edge `2.1103` maxDD `-35.7161`
- `risk_on_high->equity_4h` score `3.8762` n `40` status `ready` deltaP `38.811` edge `0.069` maxDD `-0.0446`
- `risk_on_and_context->equity_4h` score `3.8762` n `40` status `ready` deltaP `38.811` edge `0.069` maxDD `-0.0446`
- `risk_on_high->equity_24h` score `3.0649` n `40` status `ready` deltaP `32.2357` edge `0.0405` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `3.0649` n `40` status `ready` deltaP `32.2357` edge `0.0405` maxDD `0.0`
- `market_context_high->index_24h` score `2.2545` n `144` status `ready` deltaP `19.9307` edge `0.055` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `1.4778` n `40` status `ready` deltaP `20.6707` edge `0.0519` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.4778` n `40` status `ready` deltaP `20.6707` edge `0.0519` maxDD `-2.6576`
- `market_context_high->equity_4h` score `1.3573` n `166` status `ready` deltaP `14.805` edge `0.1675` maxDD `-6.9137`
- `market_context_high->equity_1h` score `0.8245` n `172` status `ready` deltaP `6.371` edge `0.0822` maxDD `-2.144`
- `risk_on_high->equity_1h` score `0.5287` n `40` status `ready` deltaP `11.6617` edge `0.0054` maxDD `-0.7937`
- `risk_on_and_context->equity_1h` score `0.5287` n `40` status `ready` deltaP `11.6617` edge `0.0054` maxDD `-0.7937`
- `risk_on_high->crypto_major_1h` score `0.252` n `40` status `ready` deltaP `12.9042` edge `0.0005` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `0.252` n `40` status `ready` deltaP `12.9042` edge `0.0005` maxDD `-2.3372`
- `risk_on_high->metal_4h` score `0.2136` n `40` status `ready` deltaP `11.7073` edge `-0.0171` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `0.2136` n `40` status `ready` deltaP `11.7073` edge `-0.0171` maxDD `-1.3516`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
