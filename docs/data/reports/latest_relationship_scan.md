# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-30T02:52:23.087713+00:00`
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

- `risk_on_high->unknown_4h` score `6.4415` n `62` status `ready` deltaP `21.9808` edge `0.4331` maxDD `-1.0945`
- `risk_on_and_context->unknown_4h` score `6.4415` n `62` status `ready` deltaP `21.9808` edge `0.4331` maxDD `-1.0945`
- `market_context_high->metal_24h` score `4.6603` n `104` status `ready` deltaP `34.2414` edge `0.262` maxDD `-3.1535`
- `risk_on_high->crypto_major_4h` score `4.4643` n `62` status `ready` deltaP `25.3738` edge `0.2388` maxDD `-1.208`
- `risk_on_and_context->crypto_major_4h` score `4.4643` n `62` status `ready` deltaP `25.3738` edge `0.2388` maxDD `-1.208`
- `market_context_high->unknown_4h` score `4.2164` n `164` status `ready` deltaP `18.5976` edge `0.2744` maxDD `-1.0945`
- `risk_on_high->crypto_alt_4h` score `2.9733` n `62` status `ready` deltaP `16.8273` edge `0.3167` maxDD `-1.4818`
- `risk_on_and_context->crypto_alt_4h` score `2.9733` n `62` status `ready` deltaP `16.8273` edge `0.3167` maxDD `-1.4818`
- `risk_on_high->equity_4h` score `2.6261` n `62` status `ready` deltaP `23.6969` edge `0.0858` maxDD `-0.3281`
- `risk_on_and_context->equity_4h` score `2.6261` n `62` status `ready` deltaP `23.6969` edge `0.0858` maxDD `-0.3281`
- `risk_on_high->unknown_1h` score `2.0473` n `66` status `ready` deltaP `3.6065` edge `0.1905` maxDD `-1.5148`
- `risk_on_and_context->unknown_1h` score `2.0473` n `66` status `ready` deltaP `3.6065` edge `0.1905` maxDD `-1.5148`
- `risk_on_high->metal_4h` score `2.0149` n `62` status `ready` deltaP `25.3344` edge `0.0286` maxDD `-0.0336`
- `risk_on_and_context->metal_4h` score `2.0149` n `62` status `ready` deltaP `25.3344` edge `0.0286` maxDD `-0.0336`
- `market_context_high->unknown_1h` score `1.9594` n `168` status `ready` deltaP `9.613` edge `0.1473` maxDD `-1.5148`
- `risk_on_high->index_4h` score `1.7456` n `62` status `ready` deltaP `24.764` edge `0.0113` maxDD `-0.1405`
- `risk_on_and_context->index_4h` score `1.7456` n `62` status `ready` deltaP `24.764` edge `0.0113` maxDD `-0.1405`
- `risk_on_high->metal_1h` score `1.1789` n `66` status `ready` deltaP `16.8527` edge `0.0073` maxDD `-0.0463`
- `risk_on_and_context->metal_1h` score `1.1789` n `66` status `ready` deltaP `16.8527` edge `0.0073` maxDD `-0.0463`
- `news_risk_high->fx_4h` score `0.5677` n `38` status `ready` deltaP `17.7632` edge `0.0093` maxDD `-0.3953`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
