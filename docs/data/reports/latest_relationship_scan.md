# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-29T19:22:24.125769+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11336`

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

- `news_risk_high->unknown_24h` score `30.0049` n `59` status `ready` deltaP `3.2221` edge `2.5763` maxDD `-4.1232`
- `risk_on_high->crypto_alt_4h` score `12.2142` n `34` status `ready` deltaP `47.0588` edge `0.71` maxDD `-0.1367`
- `risk_on_and_context->crypto_alt_4h` score `12.2142` n `34` status `ready` deltaP `47.0588` edge `0.71` maxDD `-0.1367`
- `market_context_high->unknown_24h` score `11.3707` n `104` status `ready` deltaP `20.9535` edge `0.8811` maxDD `-3.1917`
- `news_risk_high->crypto_alt_24h` score `10.7215` n `59` status `ready` deltaP `29.2226` edge `1.5173` maxDD `-22.3391`
- `risk_on_high->crypto_major_4h` score `8.083` n `34` status `ready` deltaP `39.0424` edge `0.4409` maxDD `-1.208`
- `risk_on_and_context->crypto_major_4h` score `8.083` n `34` status `ready` deltaP `39.0424` edge `0.4409` maxDD `-1.208`
- `news_risk_high->unknown_4h` score `5.8904` n `68` status `ready` deltaP `7.6309` edge `0.499` maxDD `-1.7205`
- `market_context_high->metal_24h` score `4.6946` n `104` status `ready` deltaP `34.415` edge `0.2637` maxDD `-3.1535`
- `risk_on_high->metal_4h` score `3.0065` n `34` status `ready` deltaP `32.9448` edge `0.0395` maxDD `-0.0208`
- `risk_on_and_context->metal_4h` score `3.0065` n `34` status `ready` deltaP `32.9448` edge `0.0395` maxDD `-0.0208`
- `news_risk_high->unknown_1h` score `2.6062` n `68` status `ready` deltaP `0.8366` edge `0.2473` maxDD `-0.8558`
- `news_risk_high->fx_4h` score `2.3165` n `68` status `ready` deltaP `34.0477` edge `0.021` maxDD `-0.3953`
- `market_context_high->unknown_4h` score `2.2354` n `134` status `ready` deltaP `18.386` edge `0.1069` maxDD `-0.7887`
- `risk_on_high->metal_1h` score `1.4453` n `44` status `ready` deltaP `19.883` edge `0.0093` maxDD `-0.0463`
- `risk_on_and_context->metal_1h` score `1.4453` n `44` status `ready` deltaP `19.883` edge `0.0093` maxDD `-0.0463`
- `risk_on_high->unknown_4h` score `1.1893` n `34` status `ready` deltaP `28.2192` edge `-0.0695` maxDD `-0.5615`
- `risk_on_and_context->unknown_4h` score `1.1893` n `34` status `ready` deltaP `28.2192` edge `-0.0695` maxDD `-0.5615`
- `risk_on_high->equity_4h` score `0.9411` n `34` status `ready` deltaP `7.344` edge `0.0544` maxDD `-0.3281`
- `risk_on_and_context->equity_4h` score `0.9411` n `34` status `ready` deltaP `7.344` edge `0.0544` maxDD `-0.3281`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
