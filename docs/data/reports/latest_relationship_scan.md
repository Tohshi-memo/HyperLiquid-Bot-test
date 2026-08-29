# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-29T21:07:23.965464+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11432`

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

- `news_risk_high->unknown_24h` score `27.5387` n `52` status `ready` deltaP `-0.2004` edge `2.3936` maxDD `-4.1232`
- `market_context_high->unknown_24h` score `12.1447` n `104` status `ready` deltaP `20.9535` edge `0.9456` maxDD `-3.1917`
- `news_risk_high->crypto_alt_24h` score `9.7652` n `52` status `ready` deltaP `26.0283` edge `1.416` maxDD `-22.3391`
- `risk_on_high->crypto_alt_4h` score `9.4461` n `41` status `ready` deltaP `35.061` edge `0.5716` maxDD `-0.4529`
- `risk_on_and_context->crypto_alt_4h` score `9.4461` n `41` status `ready` deltaP `35.061` edge `0.5716` maxDD `-0.4529`
- `risk_on_high->crypto_major_4h` score `7.1744` n `41` status `ready` deltaP `37.1951` edge `0.3775` maxDD `-1.208`
- `risk_on_and_context->crypto_major_4h` score `7.1744` n `41` status `ready` deltaP `37.1951` edge `0.3775` maxDD `-1.208`
- `news_risk_high->unknown_4h` score `6.6232` n `61` status `ready` deltaP `4.8655` edge `0.5785` maxDD `-1.7205`
- `market_context_high->metal_24h` score `4.6862` n `104` status `ready` deltaP `34.415` edge `0.263` maxDD `-3.1535`
- `risk_on_high->metal_4h` score `3.0712` n `41` status `ready` deltaP `33.9939` edge `0.0379` maxDD `-0.0208`
- `risk_on_and_context->metal_4h` score `3.0712` n `41` status `ready` deltaP `33.9939` edge `0.0379` maxDD `-0.0208`
- `news_risk_high->unknown_1h` score `2.7535` n `61` status `ready` deltaP `-1.9117` edge `0.2779` maxDD `-0.8558`
- `market_context_high->unknown_4h` score `1.7866` n `141` status `ready` deltaP `17.085` edge `0.082` maxDD `-1.0945`
- `risk_on_high->equity_4h` score `1.7345` n `41` status `ready` deltaP `13.872` edge `0.077` maxDD `-0.3281`
- `risk_on_and_context->equity_4h` score `1.7345` n `41` status `ready` deltaP `13.872` edge `0.077` maxDD `-0.3281`
- `risk_on_high->metal_1h` score `1.4107` n `51` status `ready` deltaP `19.555` edge `0.0086` maxDD `-0.0463`
- `risk_on_and_context->metal_1h` score `1.4107` n `51` status `ready` deltaP `19.555` edge `0.0086` maxDD `-0.0463`
- `news_risk_high->fx_4h` score `1.3814` n `61` status `ready` deltaP `32.0772` edge `0.0182` maxDD `-0.3953`
- `market_context_high->unknown_1h` score `1.1554` n `153` status `ready` deltaP `8.3529` edge `0.0887` maxDD `-1.5148`
- `risk_on_high->index_4h` score `1.0228` n `41` status `ready` deltaP `16.4634` edge `0.0064` maxDD `-0.1405`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
