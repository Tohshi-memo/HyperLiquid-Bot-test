# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-30T05:22:26.156988+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11504`

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

- `risk_on_high->unknown_4h` score `8.6637` n `62` status `ready` deltaP `22.743` edge `0.6132` maxDD `-1.0945`
- `risk_on_and_context->unknown_4h` score `8.6637` n `62` status `ready` deltaP `22.743` edge `0.6132` maxDD `-1.0945`
- `market_context_high->unknown_4h` score `5.0094` n `164` status `ready` deltaP `19.3598` edge `0.3354` maxDD `-1.0945`
- `market_context_high->metal_24h` score `4.6432` n `100` status `ready` deltaP `33.4722` edge `0.2657` maxDD `-3.1535`
- `risk_on_high->crypto_major_4h` score `4.3895` n `62` status `ready` deltaP `23.7609` edge `0.2357` maxDD `-0.5985`
- `risk_on_and_context->crypto_major_4h` score `4.3895` n `62` status `ready` deltaP `23.7609` edge `0.2357` maxDD `-0.5985`
- `risk_on_high->unknown_1h` score `3.1469` n `62` status `ready` deltaP `7.4126` edge `0.2359` maxDD `-0.5126`
- `risk_on_and_context->unknown_1h` score `3.1469` n `62` status `ready` deltaP `7.4126` edge `0.2359` maxDD `-0.5126`
- `risk_on_high->equity_4h` score `3.1352` n `62` status `ready` deltaP `28.6241` edge `0.0891` maxDD `-0.1594`
- `risk_on_and_context->equity_4h` score `3.1352` n `62` status `ready` deltaP `28.6241` edge `0.0891` maxDD `-0.1594`
- `risk_on_high->crypto_alt_4h` score `2.3532` n `62` status `ready` deltaP `13.6015` edge `0.2593` maxDD `-1.5298`
- `risk_on_and_context->crypto_alt_4h` score `2.3532` n `62` status `ready` deltaP `13.6015` edge `0.2593` maxDD `-1.5298`
- `market_context_high->unknown_1h` score `2.3512` n `164` status `ready` deltaP `11.0122` edge `0.1634` maxDD `-0.9372`
- `risk_on_high->index_4h` score `2.2919` n `62` status `ready` deltaP `28.6881` edge `0.0128` maxDD `-0.0453`
- `risk_on_and_context->index_4h` score `2.2919` n `62` status `ready` deltaP `28.6881` edge `0.0128` maxDD `-0.0453`
- `risk_on_high->metal_4h` score `1.7498` n `62` status `ready` deltaP `22.1086` edge `0.0282` maxDD `-0.0488`
- `risk_on_and_context->metal_4h` score `1.7498` n `62` status `ready` deltaP `22.1086` edge `0.0282` maxDD `-0.0488`
- `risk_on_high->metal_1h` score `1.5912` n `62` status `ready` deltaP `21.1995` edge `0.0083` maxDD `-0.0291`
- `risk_on_and_context->metal_1h` score `1.5912` n `62` status `ready` deltaP `21.1995` edge `0.0083` maxDD `-0.0291`
- `news_risk_high->unknown_1h` score `1.2543` n `32` status `ready` deltaP `-13.4543` edge `0.2244` maxDD `-0.7475`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
