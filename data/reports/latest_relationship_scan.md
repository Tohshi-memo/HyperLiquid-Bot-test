# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-11T02:37:36.041795+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `11394`

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

- `news_risk_high->unknown_1h` score `1092.8582` n `47` status `ready` deltaP `-7.1824` edge `91.1548` maxDD `-1.1656`
- `news_risk_high->unknown_4h` score `1069.452` n `35` status `ready` deltaP `-22.3519` edge `89.3344` maxDD `-2.1509`
- `risk_on_high->crypto_alt_24h` score `20.5983` n `91` status `ready` deltaP `36.3458` edge `1.4972` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `20.5983` n `91` status `ready` deltaP `36.3458` edge `1.4972` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `16.6688` n `195` status `ready` deltaP `30.0454` edge `1.2715` maxDD `-3.9523`
- `risk_on_high->crypto_alt_4h` score `9.0371` n `91` status `ready` deltaP `42.0983` edge `0.5096` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `9.0371` n `91` status `ready` deltaP `42.0983` edge `0.5096` maxDD `-1.9733`
- `market_context_high->equity_24h` score `8.249` n `195` status `ready` deltaP `29.6875` edge `0.4895` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `7.8491` n `91` status `ready` deltaP `32.9637` edge `0.5202` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `7.8491` n `91` status `ready` deltaP `32.9637` edge `0.5202` maxDD `-3.8693`
- `risk_on_high->crypto_major_24h` score `7.2518` n `91` status `ready` deltaP `25.021` edge `1.1697` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `7.2518` n `91` status `ready` deltaP `25.021` edge `1.1697` maxDD `-24.5429`
- `risk_on_high->equity_24h` score `6.911` n `91` status `ready` deltaP `29.6875` edge `0.378` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `6.911` n `91` status `ready` deltaP `29.6875` edge `0.378` maxDD `0.0`
- `risk_on_high->index_24h` score `4.8447` n `91` status `ready` deltaP `45.488` edge `0.1047` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `4.8447` n `91` status `ready` deltaP `45.488` edge `0.1047` maxDD `-0.0051`
- `market_context_high->index_24h` score `3.9161` n `195` status `ready` deltaP `39.5539` edge `0.102` maxDD `-0.1483`
- `risk_on_high->equity_4h` score `3.6012` n `91` status `ready` deltaP `33.4981` edge `0.0861` maxDD `-0.079`
- `risk_on_and_context->equity_4h` score `3.6012` n `91` status `ready` deltaP `33.4981` edge `0.0861` maxDD `-0.079`
- `market_context_high->equity_4h` score `2.386` n `195` status `ready` deltaP `26.2453` edge `0.1094` maxDD `-2.843`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
