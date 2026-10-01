# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-01T05:22:28.032045+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6754`

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

- `market_context_high->unknown_1h` score `324.6016` n `50` status `ready` deltaP `6.8323` edge `27.0095` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `280.9192` n `50` status `ready` deltaP `6.8598` edge `23.3642` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `19.1992` n `131` status `ready` deltaP `29.2025` edge `1.4262` maxDD `-1.0093`
- `market_context_high->crypto_major_4h` score `6.9293` n `50` status `ready` deltaP `18.7622` edge `0.5227` maxDD `-3.294`
- `news_risk_high->crypto_major_24h` score `6.4646` n `131` status `ready` deltaP `23.4892` edge `0.6975` maxDD `-15.8971`
- `news_risk_high->equity_24h` score `6.2752` n `131` status `ready` deltaP `24.1836` edge `0.5966` maxDD `-9.4579`
- `market_context_high->crypto_major_24h` score `3.849` n `30` status `ready` deltaP `24.5834` edge `0.4712` maxDD `-9.3299`
- `market_context_high->crypto_alt_4h` score `3.8457` n `50` status `ready` deltaP `14.0549` edge `0.3561` maxDD `-7.6792`
- `news_risk_high->equity_4h` score `3.0151` n `131` status `ready` deltaP `24.9686` edge `0.1812` maxDD `-5.0451`
- `market_context_high->crypto_major_1h` score `2.9651` n `50` status `ready` deltaP `15.0479` edge `0.1918` maxDD `-2.2692`
- `market_context_high->fx_4h` score `2.8413` n `50` status `ready` deltaP `32.0793` edge `0.0364` maxDD `-0.0791`
- `news_risk_high->index_24h` score `2.6733` n `131` status `ready` deltaP `25.3936` edge `0.1013` maxDD `-0.4916`
- `market_context_high->crypto_alt_1h` score `2.6291` n `50` status `ready` deltaP `12.8563` edge `0.1997` maxDD `-3.6387`
- `market_context_high->crypto_alt_24h` score `2.325` n `30` status `ready` deltaP `7.3959` edge `0.3154` maxDD `-11.6768`
- `news_risk_high->metal_24h` score `1.9484` n `131` status `ready` deltaP `22.9789` edge `0.224` maxDD `-2.192`
- `news_risk_high->crypto_alt_4h` score `1.4747` n `131` status `ready` deltaP `9.7038` edge `0.2739` maxDD `-11.9226`
- `market_context_high->fx_1h` score `1.4172` n `50` status `ready` deltaP `20.0419` edge `0.0109` maxDD `-0.113`
- `news_risk_high->equity_1h` score `0.6608` n `131` status `ready` deltaP `6.7125` edge `0.0647` maxDD `-1.0171`
- `news_risk_high->crypto_alt_1h` score `0.5734` n `131` status `ready` deltaP `7.1616` edge `0.0911` maxDD `-4.2849`
- `news_risk_high->index_1h` score `0.3452` n `131` status `ready` deltaP `7.2965` edge `0.0089` maxDD `-0.302`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
