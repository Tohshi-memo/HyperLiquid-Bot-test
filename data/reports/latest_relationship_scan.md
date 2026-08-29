# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-29T17:22:32.178729+00:00`
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

- `news_risk_high->unknown_24h` score `35.9594` n `63` status `ready` deltaP `7.6637` edge `3.0429` maxDD `-4.1232`
- `news_risk_high->crypto_alt_24h` score `17.7359` n `63` status `ready` deltaP `30.7292` edge `1.6107` maxDD `-22.3391`
- `market_context_high->unknown_24h` score `10.1981` n `104` status `ready` deltaP `20.6063` edge `0.7857` maxDD `-3.1917`
- `news_risk_high->unknown_4h` score `6.0602` n `75` status `ready` deltaP `9.9187` edge `0.4979` maxDD `-1.7205`
- `market_context_high->metal_24h` score `4.6692` n `104` status `ready` deltaP `34.0678` edge `0.2639` maxDD `-3.1535`
- `news_risk_high->unknown_1h` score `2.7562` n `75` status `ready` deltaP `3.6567` edge `0.241` maxDD `-0.8558`
- `market_context_high->unknown_4h` score `2.5693` n `126` status `ready` deltaP `19.1251` edge `0.1298` maxDD `-0.7887`
- `news_risk_high->fx_4h` score `2.4798` n `75` status `ready` deltaP `35.9085` edge `0.0222` maxDD `-0.3953`
- `risk_on_high->metal_1h` score `1.1475` n `38` status `ready` deltaP `16.1756` edge `0.0092` maxDD `-0.0463`
- `risk_on_and_context->metal_1h` score `1.1475` n `38` status `ready` deltaP `16.1756` edge `0.0092` maxDD `-0.0463`
- `market_context_high->unknown_1h` score `0.7838` n `138` status `ready` deltaP `8.6133` edge `0.056` maxDD `-1.5148`
- `market_context_high->crypto_major_4h` score `0.7357` n `126` status `ready` deltaP `20.6978` edge `0.2684` maxDD `-20.9394`
- `risk_on_high->crypto_alt_1h` score `0.7163` n `38` status `ready` deltaP `13.6937` edge `0.0481` maxDD `-2.1381`
- `risk_on_and_context->crypto_alt_1h` score `0.7163` n `38` status `ready` deltaP `13.6937` edge `0.0481` maxDD `-2.1381`
- `news_risk_high->equity_24h` score `0.6032` n `63` status `ready` deltaP `16.8155` edge `0.2561` maxDD `-18.9364`
- `news_risk_high->fx_1h` score `0.4007` n `75` status `ready` deltaP `12.7225` edge `0.0054` maxDD `-0.108`
- `news_risk_high->commodity_1h` score `0.3022` n `75` status `ready` deltaP `10.0` edge `0.0041` maxDD `-0.5618`
- `market_context_high->crypto_alt_4h` score `0.2761` n `126` status `ready` deltaP `22.9844` edge `0.3544` maxDD `-31.4361`
- `news_risk_high->index_24h` score `-0.0445` n `63` status `ready` deltaP `11.2848` edge `0.0053` maxDD `-2.2325`
- `market_context_high->metal_4h` score `-0.1284` n `126` status `ready` deltaP `9.5335` edge `0.0117` maxDD `-3.3377`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
