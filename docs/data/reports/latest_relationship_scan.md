# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-06T02:22:31.433057+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11685`

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

- `market_context_high->unknown_24h` score `12.5032` n `90` status `ready` deltaP `4.4445` edge `1.0166` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `2.927` n `109` status `ready` deltaP `-1.9551` edge `0.3565` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.2228` n `109` status `ready` deltaP `14.209` edge `0.0918` maxDD `-2.7703`
- `market_context_high->metal_24h` score `0.7869` n `90` status `ready` deltaP `2.0139` edge `0.2043` maxDD `-2.6802`
- `market_context_high->fx_24h` score `0.7822` n `90` status `ready` deltaP `24.5486` edge `0.0572` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.3832` n `109` status `ready` deltaP `7.4603` edge `0.0238` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.0835` n `109` status `ready` deltaP `6.5813` edge `-0.0019` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.1383` n `109` status `ready` deltaP `9.0093` edge `0.0082` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.5565` n `109` status `ready` deltaP `-2.0093` edge `-0.0085` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.7128` n `109` status `ready` deltaP `-2.9075` edge `-0.0186` maxDD `-1.6054`
- `market_context_high->metal_4h` score `-0.9185` n `109` status `ready` deltaP `1.4126` edge `-0.0037` maxDD `-3.211`
- `market_context_high->crypto_alt_24h` score `-1.2718` n `90` status `ready` deltaP `0.7291` edge `-0.0236` maxDD `-4.5445`
- `market_context_high->crypto_alt_1h` score `-1.4222` n `109` status `ready` deltaP `-4.5391` edge `-0.0172` maxDD `-3.0178`
- `market_context_high->index_24h` score `-1.7432` n `90` status `ready` deltaP `-5.5209` edge `0.0328` maxDD `-7.8922`
- `market_context_high->equity_1h` score `-1.7785` n `109` status `ready` deltaP `1.5685` edge `-0.0849` maxDD `-10.619`
- `market_context_high->index_4h` score `-2.1628` n `109` status `ready` deltaP `-13.43` edge `-0.0623` maxDD `-4.7021`
- `market_context_high->crypto_alt_4h` score `-2.1661` n `109` status `ready` deltaP `0.9272` edge `-0.0477` maxDD `-5.7857`
- `market_context_high->crypto_major_1h` score `-3.2719` n `109` status `ready` deltaP `-11.1493` edge `-0.061` maxDD `-7.6533`
- `market_context_high->unknown_1h` score `-3.2825` n `109` status `ready` deltaP `1.8829` edge `-0.2414` maxDD `-1.2421`
- `market_context_high->commodity_24h` score `-6.0895` n `90` status `ready` deltaP `10.3125` edge `-0.028` maxDD `-51.0493`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
