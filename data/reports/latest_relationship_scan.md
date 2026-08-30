# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-30T19:52:23.118292+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11690`

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

- `risk_on_high->crypto_alt_24h` score `25.9677` n `39` status `ready` deltaP `51.0417` edge `1.8237` maxDD `0.0`
- `risk_on_and_context->crypto_alt_24h` score `25.9677` n `39` status `ready` deltaP `51.0417` edge `1.8237` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `16.2392` n `39` status `ready` deltaP `44.9653` edge `1.0535` maxDD `0.0`
- `risk_on_and_context->crypto_major_24h` score `16.2392` n `39` status `ready` deltaP `44.9653` edge `1.0535` maxDD `0.0`
- `risk_on_high->unknown_4h` score `9.3632` n `69` status `ready` deltaP `28.0377` edge `0.6362` maxDD `-1.0945`
- `risk_on_and_context->unknown_4h` score `9.3632` n `69` status `ready` deltaP `28.0377` edge `0.6362` maxDD `-1.0945`
- `risk_on_high->equity_24h` score `6.4247` n `39` status `ready` deltaP `39.5833` edge `0.2715` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `6.4247` n `39` status `ready` deltaP `39.5833` edge `0.2715` maxDD `0.0`
- `risk_on_high->fx_24h` score `6.3546` n `39` status `ready` deltaP `71.5278` edge `0.0527` maxDD `0.0`
- `risk_on_and_context->fx_24h` score `6.3546` n `39` status `ready` deltaP `71.5278` edge `0.0527` maxDD `0.0`
- `risk_on_high->metal_24h` score `6.2331` n `39` status `ready` deltaP `53.2986` edge `0.1641` maxDD `0.0`
- `risk_on_and_context->metal_24h` score `6.2331` n `39` status `ready` deltaP `53.2986` edge `0.1641` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `5.4053` n `69` status `ready` deltaP `27.7284` edge `0.2939` maxDD `-0.5985`
- `risk_on_and_context->crypto_major_4h` score `5.4053` n `69` status `ready` deltaP `27.7284` edge `0.2939` maxDD `-0.5985`
- `market_context_high->unknown_4h` score `5.3705` n `149` status `ready` deltaP `21.054` edge `0.3542` maxDD `-1.0945`
- `market_context_high->metal_24h` score `4.5809` n `117` status `ready` deltaP `37.0593` edge `0.2366` maxDD `-3.1535`
- `risk_on_high->crypto_alt_4h` score `4.5318` n `69` status `ready` deltaP `17.811` edge `0.3072` maxDD `-1.5298`
- `risk_on_and_context->crypto_alt_4h` score `4.5318` n `69` status `ready` deltaP `17.811` edge `0.3072` maxDD `-1.5298`
- `risk_on_high->equity_4h` score `3.7081` n `69` status `ready` deltaP `33.9851` edge `0.1011` maxDD `-0.1594`
- `risk_on_and_context->equity_4h` score `3.7081` n `69` status `ready` deltaP `33.9851` edge `0.1011` maxDD `-0.1594`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
