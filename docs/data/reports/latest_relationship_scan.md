# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-30T03:07:48.251912+00:00`
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

- `risk_on_high->unknown_4h` score `6.9154` n `63` status `ready` deltaP `22.0843` edge `0.4719` maxDD `-1.0945`
- `risk_on_and_context->unknown_4h` score `6.9154` n `63` status `ready` deltaP `22.0843` edge `0.4719` maxDD `-1.0945`
- `market_context_high->metal_24h` score `4.6603` n `104` status `ready` deltaP `34.2414` edge `0.262` maxDD `-3.1535`
- `market_context_high->unknown_4h` score `4.3613` n `165` status `ready` deltaP `18.5634` edge `0.2867` maxDD `-1.0945`
- `risk_on_high->crypto_major_4h` score `4.2439` n `63` status `ready` deltaP `24.1193` edge `0.2288` maxDD `-1.208`
- `risk_on_and_context->crypto_major_4h` score `4.2439` n `63` status `ready` deltaP `24.1193` edge `0.2288` maxDD `-1.208`
- `risk_on_high->crypto_alt_4h` score `2.83` n `63` status `ready` deltaP `15.7521` edge `0.3061` maxDD `-1.5298`
- `risk_on_and_context->crypto_alt_4h` score `2.83` n `63` status `ready` deltaP `15.7521` edge `0.3061` maxDD `-1.5298`
- `risk_on_high->equity_4h` score `2.6262` n `63` status `ready` deltaP `23.8773` edge `0.0846` maxDD `-0.3281`
- `risk_on_and_context->equity_4h` score `2.6262` n `63` status `ready` deltaP `23.8773` edge `0.0846` maxDD `-0.3281`
- `risk_on_high->unknown_1h` score `2.0485` n `66` status `ready` deltaP `3.6065` edge `0.1906` maxDD `-1.5148`
- `risk_on_and_context->unknown_1h` score `2.0485` n `66` status `ready` deltaP `3.6065` edge `0.1906` maxDD `-1.5148`
- `market_context_high->unknown_1h` score `1.9606` n `168` status `ready` deltaP `9.613` edge `0.1474` maxDD `-1.5148`
- `risk_on_high->metal_4h` score `1.9012` n `63` status `ready` deltaP `24.0031` edge `0.028` maxDD `-0.0336`
- `risk_on_and_context->metal_4h` score `1.9012` n `63` status `ready` deltaP `24.0031` edge `0.028` maxDD `-0.0336`
- `risk_on_high->index_4h` score `1.7613` n `63` status `ready` deltaP `24.9444` edge `0.0114` maxDD `-0.1405`
- `risk_on_and_context->index_4h` score `1.7613` n `63` status `ready` deltaP `24.9444` edge `0.0114` maxDD `-0.1405`
- `risk_on_high->metal_1h` score `1.1789` n `66` status `ready` deltaP `16.8527` edge `0.0073` maxDD `-0.0463`
- `risk_on_and_context->metal_1h` score `1.1789` n `66` status `ready` deltaP `16.8527` edge `0.0073` maxDD `-0.0463`
- `news_risk_high->fx_4h` score `0.639` n `37` status `ready` deltaP `19.1044` edge `0.0095` maxDD `-0.3953`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
