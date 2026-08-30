# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-30T15:37:22.990512+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11554`

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

- `risk_on_high->unknown_4h` score `10.2227` n `59` status `ready` deltaP `25.5813` edge `0.7242` maxDD `-1.0945`
- `risk_on_and_context->unknown_4h` score `10.2227` n `59` status `ready` deltaP `25.5813` edge `0.7242` maxDD `-1.0945`
- `market_context_high->unknown_4h` score `6.4421` n `149` status `ready` deltaP `21.054` edge `0.4435` maxDD `-1.0945`
- `market_context_high->metal_24h` score `4.5746` n `116` status `ready` deltaP `36.2308` edge `0.2416` maxDD `-3.1535`
- `risk_on_high->crypto_major_4h` score `4.5386` n `59` status `ready` deltaP `24.2895` edge `0.2446` maxDD `-0.5985`
- `risk_on_and_context->crypto_major_4h` score `4.5386` n `59` status `ready` deltaP `24.2895` edge `0.2446` maxDD `-0.5985`
- `risk_on_high->equity_4h` score `3.5469` n `59` status `ready` deltaP `31.7151` edge `0.1028` maxDD `-0.1594`
- `risk_on_and_context->equity_4h` score `3.5469` n `59` status `ready` deltaP `31.7151` edge `0.1028` maxDD `-0.1594`
- `risk_on_high->unknown_1h` score `3.3692` n `68` status `ready` deltaP `8.9909` edge `0.2411` maxDD `-0.2885`
- `risk_on_and_context->unknown_1h` score `3.3692` n `68` status `ready` deltaP `8.9909` edge `0.2411` maxDD `-0.2885`
- `risk_on_high->index_4h` score `2.7944` n `59` status `ready` deltaP `33.8673` edge `0.0156` maxDD `-0.0147`
- `risk_on_and_context->index_4h` score `2.7944` n `59` status `ready` deltaP `33.8673` edge `0.0156` maxDD `-0.0147`
- `market_context_high->unknown_1h` score `2.6654` n `160` status `ready` deltaP `11.5644` edge `0.1859` maxDD `-0.9372`
- `risk_on_high->crypto_alt_4h` score `2.3987` n `59` status `ready` deltaP `12.407` edge `0.2731` maxDD `-1.5298`
- `risk_on_and_context->crypto_alt_4h` score `2.3987` n `59` status `ready` deltaP `12.407` edge `0.2731` maxDD `-1.5298`
- `risk_on_high->metal_1h` score `1.8912` n `68` status `ready` deltaP `24.4981` edge `0.0114` maxDD `-0.0366`
- `risk_on_and_context->metal_1h` score `1.8912` n `68` status `ready` deltaP `24.4981` edge `0.0114` maxDD `-0.0366`
- `risk_on_high->metal_4h` score `1.8758` n `59` status `ready` deltaP `23.4291` edge `0.0299` maxDD `-0.0488`
- `risk_on_and_context->metal_4h` score `1.8758` n `59` status `ready` deltaP `23.4291` edge `0.0299` maxDD `-0.0488`
- `risk_on_high->equity_1h` score `1.2384` n `68` status `ready` deltaP `16.0972` edge `0.0193` maxDD `-0.2062`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
