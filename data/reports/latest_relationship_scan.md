# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-31T01:00:59.517259+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11748`

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

- `risk_on_high->crypto_alt_24h` score `20.7034` n `55` status `ready` deltaP `44.9747` edge `1.4735` maxDD `-3.1772`
- `risk_on_and_context->crypto_alt_24h` score `20.7034` n `55` status `ready` deltaP `44.9747` edge `1.4735` maxDD `-3.1772`
- `risk_on_high->unknown_4h` score `9.6568` n `88` status `ready` deltaP `31.1669` edge `0.6398` maxDD `-1.0945`
- `risk_on_and_context->unknown_4h` score `9.6568` n `88` status `ready` deltaP `31.1669` edge `0.6398` maxDD `-1.0945`
- `risk_on_high->crypto_major_24h` score `7.7822` n `55` status `ready` deltaP `25.7418` edge `0.6187` maxDD `-9.0103`
- `risk_on_and_context->crypto_major_24h` score `7.7822` n `55` status `ready` deltaP `25.7418` edge `0.6187` maxDD `-9.0103`
- `market_context_high->unknown_4h` score `6.1541` n `149` status `ready` deltaP `21.054` edge `0.4195` maxDD `-1.0945`
- `risk_on_high->fx_24h` score `6.0606` n `55` status `ready` deltaP `67.8819` edge `0.0525` maxDD `0.0`
- `risk_on_and_context->fx_24h` score `6.0606` n `55` status `ready` deltaP `67.8819` edge `0.0525` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `5.1116` n `112` status `ready` deltaP `20.7093` edge `0.537` maxDD `-17.2607`
- `market_context_high->crypto_alt_24h` score `4.6647` n `112` status `ready` deltaP `21.8254` edge `0.8715` maxDD `-27.517`
- `risk_on_high->unknown_1h` score `4.3693` n `94` status `ready` deltaP `12.5621` edge `0.3048` maxDD `-0.2885`
- `risk_on_and_context->unknown_1h` score `4.3693` n `94` status `ready` deltaP `12.5621` edge `0.3048` maxDD `-0.2885`
- `risk_on_high->metal_24h` score `4.1643` n `55` status `ready` deltaP `39.3656` edge `0.1318` maxDD `-0.7767`
- `risk_on_and_context->metal_24h` score `4.1643` n `55` status `ready` deltaP `39.3656` edge `0.1318` maxDD `-0.7767`
- `market_context_high->metal_24h` score `3.8633` n `112` status `ready` deltaP `30.7292` edge `0.219` maxDD `-3.1535`
- `market_context_high->unknown_1h` score `3.1804` n `161` status `ready` deltaP `9.8728` edge `0.2401` maxDD `-0.9372`
- `risk_on_high->equity_24h` score `0.9335` n `55` status `ready` deltaP `18.7153` edge `0.0338` maxDD `-3.7955`
- `risk_on_and_context->equity_24h` score `0.9335` n `55` status `ready` deltaP `18.7153` edge `0.0338` maxDD `-3.7955`
- `risk_on_high->commodity_24h` score `0.9214` n `55` status `ready` deltaP `10.1736` edge `0.1491` maxDD `-0.5706`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
