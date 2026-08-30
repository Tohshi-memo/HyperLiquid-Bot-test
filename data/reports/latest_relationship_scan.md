# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-30T16:22:24.646689+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11584`

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

- `risk_on_high->unknown_4h` score `10.2438` n `58` status `ready` deltaP `25.2891` edge `0.7279` maxDD `-1.0945`
- `risk_on_and_context->unknown_4h` score `10.2438` n `58` status `ready` deltaP `25.2891` edge `0.7279` maxDD `-1.0945`
- `market_context_high->unknown_4h` score `6.3873` n `148` status `ready` deltaP `20.9089` edge `0.4399` maxDD `-1.0945`
- `risk_on_high->crypto_major_4h` score `4.6331` n `58` status `ready` deltaP `23.8804` edge `0.2552` maxDD `-0.5985`
- `risk_on_and_context->crypto_major_4h` score `4.6331` n `58` status `ready` deltaP `23.8804` edge `0.2552` maxDD `-0.5985`
- `market_context_high->metal_24h` score `4.523` n `116` status `ready` deltaP `36.2308` edge `0.2373` maxDD `-3.1535`
- `risk_on_high->unknown_1h` score `3.6844` n `69` status `ready` deltaP `9.4811` edge `0.2641` maxDD `-0.2885`
- `risk_on_and_context->unknown_1h` score `3.6844` n `69` status `ready` deltaP `9.4811` edge `0.2641` maxDD `-0.2885`
- `risk_on_high->equity_4h` score `3.4878` n `58` status `ready` deltaP `31.7862` edge `0.0974` maxDD `-0.1594`
- `risk_on_and_context->equity_4h` score `3.4878` n `58` status `ready` deltaP `31.7862` edge `0.0974` maxDD `-0.1594`
- `market_context_high->unknown_1h` score `2.7794` n `160` status `ready` deltaP `11.5644` edge `0.1954` maxDD `-0.9372`
- `risk_on_high->index_4h` score `2.7684` n `58` status `ready` deltaP `33.6627` edge `0.0148` maxDD `-0.0147`
- `risk_on_and_context->index_4h` score `2.7684` n `58` status `ready` deltaP `33.6627` edge `0.0148` maxDD `-0.0147`
- `risk_on_high->crypto_alt_4h` score `2.2927` n `58` status `ready` deltaP `11.7641` edge `0.2638` maxDD `-1.5298`
- `risk_on_and_context->crypto_alt_4h` score `2.2927` n `58` status `ready` deltaP `11.7641` edge `0.2638` maxDD `-1.5298`
- `risk_on_high->metal_1h` score `1.9203` n `69` status `ready` deltaP `24.8178` edge `0.0117` maxDD `-0.0366`
- `risk_on_and_context->metal_1h` score `1.9203` n `69` status `ready` deltaP `24.8178` edge `0.0117` maxDD `-0.0366`
- `risk_on_high->metal_4h` score `1.8585` n `58` status `ready` deltaP `23.1077` edge `0.0306` maxDD `-0.0488`
- `risk_on_and_context->metal_4h` score `1.8585` n `58` status `ready` deltaP `23.1077` edge `0.0306` maxDD `-0.0488`
- `risk_on_high->equity_1h` score `1.2833` n `69` status `ready` deltaP `16.5235` edge `0.0202` maxDD `-0.2062`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
