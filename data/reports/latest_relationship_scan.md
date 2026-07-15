# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-15T12:37:28.479618+00:00`
- Price records: `672`
- Market context records: `6817`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11692`

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

- `market_context_high->unknown_24h` score `0.8445` n `176` status `ready` deltaP `-1.5467` edge `0.4938` maxDD `-12.3511`
- `market_context_high->commodity_24h` score `0.3767` n `176` status `ready` deltaP `10.9217` edge `0.1454` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `-0.2754` n `198` status `ready` deltaP `5.666` edge `0.0129` maxDD `-4.2122`
- `market_context_high->fx_1h` score `-0.4055` n `198` status `ready` deltaP `-0.5232` edge `0.0` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.5185` n `198` status `ready` deltaP `3.1967` edge `0.0119` maxDD `-3.7803`
- `market_context_high->index_1h` score `-0.8139` n `198` status `ready` deltaP `-3.8726` edge `-0.0043` maxDD `-0.9382`
- `market_context_high->metal_1h` score `-0.9979` n `198` status `ready` deltaP `-6.4901` edge `-0.0108` maxDD `-1.9098`
- `market_context_high->commodity_1h` score `-1.0447` n `198` status `ready` deltaP `-2.0021` edge `-0.0054` maxDD `-2.1314`
- `market_context_high->commodity_4h` score `-1.3534` n `186` status `ready` deltaP `-2.2702` edge `-0.0094` maxDD `-5.5853`
- `market_context_high->fx_4h` score `-1.3536` n `186` status `ready` deltaP `5.2551` edge `-0.0022` maxDD `-2.1765`
- `market_context_high->index_4h` score `-1.6385` n `186` status `ready` deltaP `2.2079` edge `-0.0288` maxDD `-6.3458`
- `market_context_high->equity_1h` score `-1.7221` n `198` status `ready` deltaP `0.1482` edge `-0.0318` maxDD `-4.6821`
- `market_context_high->unknown_1h` score `-1.7677` n `198` status `ready` deltaP `-5.8353` edge `-0.0183` maxDD `-3.2083`
- `market_context_high->metal_4h` score `-2.8649` n `186` status `ready` deltaP `-5.6665` edge `-0.0312` maxDD `-5.5324`
- `market_context_high->crypto_major_4h` score `-3.3162` n `186` status `ready` deltaP `-1.0261` edge `-0.0856` maxDD `-16.9508`
- `market_context_high->unknown_4h` score `-3.4828` n `186` status `ready` deltaP `-13.8113` edge `0.0384` maxDD `-10.2579`
- `market_context_high->crypto_alt_4h` score `-3.5236` n `186` status `ready` deltaP `-1.7244` edge `-0.0819` maxDD `-20.6678`
- `market_context_high->fx_24h` score `-4.4672` n `176` status `ready` deltaP `-9.7853` edge `-0.0034` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-5.0257` n `186` status `ready` deltaP `-0.4164` edge `-0.1877` maxDD `-29.3079`
- `market_context_high->metal_24h` score `-9.65` n `176` status `ready` deltaP `-21.9697` edge `-0.2422` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
