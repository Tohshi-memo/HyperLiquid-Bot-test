# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-29T17:37:27.265055+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11324`

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

- `news_risk_high->unknown_24h` score `34.4747` n `63` status `ready` deltaP `6.25` edge `2.9286` maxDD `-4.1232`
- `news_risk_high->crypto_alt_24h` score `17.4623` n `63` status `ready` deltaP `30.7292` edge `1.5879` maxDD `-22.3391`
- `market_context_high->unknown_24h` score `10.38` n `104` status `ready` deltaP `20.7799` edge `0.7997` maxDD `-3.1917`
- `news_risk_high->unknown_4h` score `5.9882` n `74` status `ready` deltaP `9.5584` edge `0.4943` maxDD `-1.7205`
- `market_context_high->metal_24h` score `4.6855` n `104` status `ready` deltaP `34.2414` edge `0.2641` maxDD `-3.1535`
- `news_risk_high->unknown_1h` score `2.7847` n `74` status `ready` deltaP `3.1883` edge `0.2465` maxDD `-0.8558`
- `market_context_high->unknown_4h` score `2.5635` n `127` status `ready` deltaP `19.2626` edge `0.1284` maxDD `-0.7887`
- `news_risk_high->fx_4h` score `2.4538` n `74` status `ready` deltaP `35.5842` edge `0.0222` maxDD `-0.3953`
- `risk_on_high->metal_1h` score `1.2147` n `39` status `ready` deltaP `16.9853` edge `0.0094` maxDD `-0.0463`
- `risk_on_and_context->metal_1h` score `1.2147` n `39` status `ready` deltaP `16.9853` edge `0.0094` maxDD `-0.0463`
- `market_context_high->crypto_major_4h` score `0.7856` n `127` status `ready` deltaP `20.9165` edge `0.2711` maxDD `-20.9394`
- `market_context_high->unknown_1h` score `0.7829` n `139` status `ready` deltaP `8.827` edge `0.0545` maxDD `-1.5148`
- `risk_on_high->crypto_alt_1h` score `0.5638` n `39` status `ready` deltaP `12.1565` edge `0.0388` maxDD `-2.1381`
- `risk_on_and_context->crypto_alt_1h` score `0.5638` n `39` status `ready` deltaP `12.1565` edge `0.0388` maxDD `-2.1381`
- `news_risk_high->equity_24h` score `0.547` n `63` status `ready` deltaP `16.8155` edge `0.2489` maxDD `-18.9364`
- `news_risk_high->fx_1h` score `0.4347` n `74` status `ready` deltaP `13.3476` edge `0.0056` maxDD `-0.108`
- `market_context_high->crypto_alt_4h` score `0.29` n `127` status `ready` deltaP `23.2031` edge `0.3541` maxDD `-31.4361`
- `news_risk_high->commodity_1h` score `0.2741` n `74` status `ready` deltaP `9.4595` edge `0.0041` maxDD `-0.5618`
- `news_risk_high->index_24h` score `-0.0492` n `63` status `ready` deltaP `11.2848` edge `0.0047` maxDD `-2.2325`
- `market_context_high->metal_4h` score `-0.112` n `127` status `ready` deltaP `9.7897` edge `0.0121` maxDD `-3.3377`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
