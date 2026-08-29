# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-29T17:52:24.631864+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11330`

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

- `news_risk_high->unknown_24h` score `32.99` n `63` status `ready` deltaP `4.8363` edge `2.8143` maxDD `-4.1232`
- `news_risk_high->crypto_alt_24h` score `17.1467` n `63` status `ready` deltaP `30.7292` edge `1.5616` maxDD `-22.3391`
- `market_context_high->unknown_24h` score `10.5619` n `104` status `ready` deltaP `20.9535` edge `0.8137` maxDD `-3.1917`
- `news_risk_high->unknown_4h` score `5.9166` n `73` status `ready` deltaP `9.1881` edge `0.4908` maxDD `-1.7205`
- `market_context_high->metal_24h` score `4.7018` n `104` status `ready` deltaP `34.415` edge `0.2643` maxDD `-3.1535`
- `news_risk_high->unknown_1h` score `2.7954` n `73` status `ready` deltaP `2.8567` edge `0.2496` maxDD `-0.8558`
- `market_context_high->unknown_4h` score `2.5551` n `128` status `ready` deltaP `19.3979` edge `0.1268` maxDD `-0.7887`
- `news_risk_high->fx_4h` score `2.4236` n `73` status `ready` deltaP `35.251` edge `0.0219` maxDD `-0.3953`
- `risk_on_high->metal_1h` score `1.2762` n `40` status `ready` deltaP `17.7545` edge `0.0094` maxDD `-0.0463`
- `risk_on_and_context->metal_1h` score `1.2762` n `40` status `ready` deltaP `17.7545` edge `0.0094` maxDD `-0.0463`
- `market_context_high->crypto_major_4h` score `0.8376` n `128` status `ready` deltaP `21.1318` edge `0.274` maxDD `-20.9394`
- `market_context_high->unknown_1h` score `0.727` n `140` status `ready` deltaP `8.4731` edge `0.0522` maxDD `-1.5148`
- `news_risk_high->equity_24h` score `0.476` n `63` status `ready` deltaP `16.8155` edge `0.2398` maxDD `-18.9364`
- `news_risk_high->fx_1h` score `0.4691` n `73` status `ready` deltaP `13.9939` edge `0.0057` maxDD `-0.108`
- `risk_on_high->crypto_alt_1h` score `0.411` n `40` status `ready` deltaP `10.7036` edge `0.0289` maxDD `-2.1381`
- `risk_on_and_context->crypto_alt_1h` score `0.411` n `40` status `ready` deltaP `10.7036` edge `0.0289` maxDD `-2.1381`
- `market_context_high->crypto_alt_4h` score `0.2989` n `128` status `ready` deltaP `23.4184` edge `0.3534` maxDD `-31.4361`
- `news_risk_high->commodity_1h` score `0.2444` n `73` status `ready` deltaP `8.9041` edge `0.004` maxDD `-0.5618`
- `news_risk_high->index_24h` score `-0.057` n `63` status `ready` deltaP `11.2848` edge `0.0037` maxDD `-2.2325`
- `market_context_high->metal_4h` score `-0.1045` n `128` status `ready` deltaP `9.8895` edge `0.0124` maxDD `-3.3377`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
