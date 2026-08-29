# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-29T21:37:28.607791+00:00`
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

- `news_risk_high->unknown_24h` score `26.6412` n `50` status `ready` deltaP `-1.3542` edge `2.3265` maxDD `-4.1232`
- `market_context_high->unknown_24h` score `12.3739` n `104` status `ready` deltaP `20.9535` edge `0.9647` maxDD `-3.1917`
- `news_risk_high->crypto_alt_24h` score `9.4347` n `50` status `ready` deltaP `24.9514` edge `1.3808` maxDD `-22.3391`
- `risk_on_high->crypto_alt_4h` score `9.296` n `42` status `ready` deltaP `35.1045` edge `0.5588` maxDD `-0.4529`
- `risk_on_and_context->crypto_alt_4h` score `9.296` n `42` status `ready` deltaP `35.1045` edge `0.5588` maxDD `-0.4529`
- `risk_on_high->crypto_major_4h` score `7.0906` n `42` status `ready` deltaP `37.1225` edge `0.371` maxDD `-1.208`
- `risk_on_and_context->crypto_major_4h` score `7.0906` n `42` status `ready` deltaP `37.1225` edge `0.371` maxDD `-1.208`
- `news_risk_high->unknown_4h` score `6.7779` n `59` status `ready` deltaP `3.7541` edge `0.5988` maxDD `-1.7205`
- `market_context_high->metal_24h` score `4.685` n `104` status `ready` deltaP `34.415` edge `0.2629` maxDD `-3.1535`
- `risk_on_high->metal_4h` score `3.0827` n `42` status `ready` deltaP `34.1681` edge `0.0377` maxDD `-0.0208`
- `risk_on_and_context->metal_4h` score `3.0827` n `42` status `ready` deltaP `34.1681` edge `0.0377` maxDD `-0.0208`
- `news_risk_high->unknown_1h` score `2.838` n `59` status `ready` deltaP `-1.7558` edge `0.2839` maxDD `-0.8558`
- `risk_on_high->equity_4h` score `1.8285` n `42` status `ready` deltaP `14.6269` edge `0.0798` maxDD `-0.3281`
- `risk_on_and_context->equity_4h` score `1.8285` n `42` status `ready` deltaP `14.6269` edge `0.0798` maxDD `-0.3281`
- `market_context_high->unknown_4h` score `1.7652` n `143` status `ready` deltaP `17.3727` edge `0.0783` maxDD `-1.0945`
- `market_context_high->unknown_1h` score `1.5915` n `155` status `ready` deltaP `8.5996` edge `0.1234` maxDD `-1.5148`
- `risk_on_high->metal_1h` score `1.4947` n `53` status `ready` deltaP `20.5909` edge `0.0087` maxDD `-0.0463`
- `risk_on_and_context->metal_1h` score `1.4947` n `53` status `ready` deltaP `20.5909` edge `0.0087` maxDD `-0.0463`
- `news_risk_high->fx_4h` score `1.3375` n `59` status `ready` deltaP `31.3817` edge `0.0172` maxDD `-0.3953`
- `risk_on_high->unknown_1h` score `1.1889` n `53` status `ready` deltaP `1.1864` edge `0.1351` maxDD `-1.5148`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
