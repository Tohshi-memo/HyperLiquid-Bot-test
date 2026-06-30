# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-30T16:37:33.828321+00:00`
- Price records: `672`
- Market context records: `5265`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9598`

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

- `market_context_high->unknown_24h` score `26.1669` n `147` status `ready` deltaP `29.8895` edge `1.9903` maxDD `-0.3859`
- `market_context_high->crypto_major_24h` score `10.3227` n `147` status `ready` deltaP `28.4297` edge `1.0311` maxDD `-22.166`
- `market_context_high->crypto_alt_4h` score `4.1767` n `161` status `ready` deltaP `15.1264` edge `0.4113` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `3.745` n `161` status `ready` deltaP `14.0594` edge `0.4476` maxDD `-14.0065`
- `market_context_high->equity_24h` score `3.4548` n `147` status `ready` deltaP `19.5118` edge `0.7207` maxDD `-40.0306`
- `market_context_high->unknown_4h` score `1.5683` n `161` status `ready` deltaP `15.8565` edge `0.1272` maxDD `-5.5109`
- `market_context_high->equity_4h` score `0.6409` n `161` status `ready` deltaP `8.6512` edge `0.1596` maxDD `-7.4425`
- `market_context_high->fx_24h` score `0.5173` n `147` status `ready` deltaP `12.6666` edge `0.0482` maxDD `-0.8294`
- `market_context_high->crypto_alt_1h` score `0.4728` n `173` status `ready` deltaP `4.568` edge `0.1051` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `0.2329` n `173` status `ready` deltaP `5.5285` edge `0.1071` maxDD `-6.9639`
- `market_context_high->index_24h` score `0.2228` n `147` status `ready` deltaP `21.0247` edge `0.0519` maxDD `-7.413`
- `market_context_high->crypto_alt_24h` score `0.0441` n `147` status `ready` deltaP `15.4018` edge `0.5325` maxDD `-38.6949`
- `market_context_high->equity_1h` score `0.042` n `173` status `ready` deltaP `6.2442` edge `0.0584` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.0318` n `173` status `ready` deltaP `5.3875` edge `0.0118` maxDD `-1.0296`
- `market_context_high->metal_1h` score `-0.2043` n `173` status `ready` deltaP `4.2686` edge `0.0137` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.2608` n `173` status `ready` deltaP `1.6407` edge `0.0004` maxDD `-0.5823`
- `market_context_high->index_4h` score `-0.6813` n `161` status `ready` deltaP `5.0201` edge `0.0215` maxDD `-2.9391`
- `market_context_high->fx_4h` score `-0.7591` n `161` status `ready` deltaP `0.6447` edge `0.0013` maxDD `-1.567`
- `market_context_high->unknown_1h` score `-1.2959` n `173` status `ready` deltaP `7.209` edge `-0.0919` maxDD `-2.7986`
- `market_context_high->commodity_1h` score `-1.4064` n `173` status `ready` deltaP `-3.3497` edge `-0.0072` maxDD `-3.0135`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
