# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-30T05:37:21.173032+00:00`
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

- `risk_on_high->unknown_4h` score `8.7723` n `61` status `ready` deltaP `22.631` edge `0.623` maxDD `-1.0945`
- `risk_on_and_context->unknown_4h` score `8.7723` n `61` status `ready` deltaP `22.631` edge `0.623` maxDD `-1.0945`
- `market_context_high->unknown_4h` score `5.0492` n `163` status `ready` deltaP `19.3925` edge `0.3385` maxDD `-1.0945`
- `market_context_high->metal_24h` score `4.6402` n `99` status `ready` deltaP `33.2702` edge `0.2668` maxDD `-3.1535`
- `risk_on_high->crypto_major_4h` score `4.3215` n `61` status `ready` deltaP `23.3907` edge `0.2325` maxDD `-0.5985`
- `risk_on_and_context->crypto_major_4h` score `4.3215` n `61` status `ready` deltaP `23.3907` edge `0.2325` maxDD `-0.5985`
- `risk_on_high->unknown_1h` score `3.435` n `61` status `ready` deltaP `8.5232` edge `0.2497` maxDD `-0.2885`
- `risk_on_and_context->unknown_1h` score `3.435` n `61` status `ready` deltaP `8.5232` edge `0.2497` maxDD `-0.2885`
- `risk_on_high->equity_4h` score `3.2507` n `61` status `ready` deltaP `29.873` edge `0.0904` maxDD `-0.1594`
- `risk_on_and_context->equity_4h` score `3.2507` n `61` status `ready` deltaP `29.873` edge `0.0904` maxDD `-0.1594`
- `risk_on_high->index_4h` score `2.4496` n `61` status `ready` deltaP `29.9105` edge `0.0134` maxDD `-0.0268`
- `risk_on_and_context->index_4h` score `2.4496` n `61` status `ready` deltaP `29.9105` edge `0.0134` maxDD `-0.0268`
- `market_context_high->unknown_1h` score `2.4438` n `163` status `ready` deltaP `11.4498` edge `0.1682` maxDD `-0.9372`
- `risk_on_high->crypto_alt_4h` score `2.188` n `61` status `ready` deltaP `13.0198` edge `0.242` maxDD `-1.5298`
- `risk_on_and_context->crypto_alt_4h` score `2.188` n `61` status `ready` deltaP `13.0198` edge `0.242` maxDD `-1.5298`
- `risk_on_high->metal_4h` score `1.8603` n `61` status `ready` deltaP `23.4306` edge `0.0286` maxDD `-0.0488`
- `risk_on_and_context->metal_4h` score `1.8603` n `61` status `ready` deltaP `23.4306` edge `0.0286` maxDD `-0.0488`
- `risk_on_high->metal_1h` score `1.6777` n `61` status `ready` deltaP `22.2661` edge `0.0084` maxDD `-0.0291`
- `risk_on_and_context->metal_1h` score `1.6777` n `61` status `ready` deltaP `22.2661` edge `0.0084` maxDD `-0.0291`
- `news_risk_high->unknown_1h` score `1.2555` n `32` status `ready` deltaP `-13.4543` edge `0.2245` maxDD `-0.7475`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
