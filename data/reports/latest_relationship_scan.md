# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-01T02:07:39.993040+00:00`
- Price records: `672`
- Market context records: `5308`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9650`

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

- `market_context_high->unknown_24h` score `20.1501` n `153` status `ready` deltaP `24.04` edge `1.5279` maxDD `-0.3859`
- `market_context_high->crypto_major_24h` score `7.4984` n `153` status `ready` deltaP `25.7353` edge `0.8683` maxDD `-26.5332`
- `market_context_high->equity_24h` score `5.2807` n `153` status `ready` deltaP `19.7917` edge `0.871` maxDD `-40.0306`
- `market_context_high->crypto_alt_4h` score `3.3305` n `193` status `ready` deltaP `12.5743` edge `0.3578` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `3.2142` n `193` status `ready` deltaP `13.2748` edge `0.4086` maxDD `-14.0065`
- `market_context_high->equity_4h` score `1.9612` n `193` status `ready` deltaP `10.5894` edge `0.2567` maxDD `-7.4425`
- `market_context_high->equity_1h` score `0.5614` n `194` status `ready` deltaP `8.9111` edge `0.0839` maxDD `-5.0555`
- `market_context_high->fx_24h` score `0.5373` n `153` status `ready` deltaP `13.3068` edge `0.0456` maxDD `-0.8294`
- `market_context_high->index_24h` score `0.3407` n `153` status `ready` deltaP `20.9967` edge `0.0672` maxDD `-7.413`
- `market_context_high->crypto_alt_1h` score `0.2604` n `194` status `ready` deltaP `3.2934` edge `0.0959` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `0.1282` n `194` status `ready` deltaP `5.2395` edge `0.1003` maxDD `-6.9639`
- `market_context_high->index_1h` score `0.043` n `194` status `ready` deltaP `6.3677` edge `0.0115` maxDD `-1.0296`
- `market_context_high->metal_1h` score `-0.3171` n `194` status `ready` deltaP `2.6946` edge `0.0089` maxDD `-2.0682`
- `market_context_high->unknown_4h` score `-0.3651` n `193` status `ready` deltaP `11.32` edge `0.0038` maxDD `-5.7756`
- `market_context_high->fx_1h` score `-0.4116` n `194` status `ready` deltaP `-0.483` edge `-0.0006` maxDD `-0.5823`
- `market_context_high->index_4h` score `-0.5088` n `193` status `ready` deltaP `3.916` edge `0.0204` maxDD `-2.9391`
- `market_context_high->fx_4h` score `-0.6425` n `193` status `ready` deltaP `2.5425` edge `0.0036` maxDD `-1.567`
- `market_context_high->commodity_1h` score `-1.4347` n `194` status `ready` deltaP `-3.1761` edge `-0.0066` maxDD `-3.3428`
- `market_context_high->metal_4h` score `-2.3425` n `193` status `ready` deltaP `-7.024` edge `-0.0109` maxDD `-12.4072`
- `market_context_high->crypto_alt_24h` score `-2.9936` n `153` status `ready` deltaP `13.3476` edge `0.3682` maxDD `-53.6115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
