# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-07T15:52:24.719714+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10441`

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

- `risk_on_high->unknown_24h` score `353.8384` n `95` status `ready` deltaP `24.3056` edge `29.3245` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `353.8384` n `95` status `ready` deltaP `24.3056` edge `29.3245` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `21.5503` n `95` status `ready` deltaP `37.7267` edge `1.6022` maxDD `-1.9619`
- `risk_on_and_context->crypto_major_24h` score `21.5503` n `95` status `ready` deltaP `37.7267` edge `1.6022` maxDD `-1.9619`
- `risk_on_high->crypto_alt_24h` score `14.9037` n `95` status `ready` deltaP `32.2917` edge `1.0267` maxDD `0.0`
- `risk_on_and_context->crypto_alt_24h` score `14.9037` n `95` status `ready` deltaP `32.2917` edge `1.0267` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `8.1678` n `207` status `ready` deltaP `24.5622` edge `0.5744` maxDD `-2.5998`
- `risk_on_high->crypto_alt_4h` score `5.4097` n `117` status `ready` deltaP `29.1106` edge `0.2939` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.4097` n `117` status `ready` deltaP `29.1106` edge `0.2939` maxDD `-1.9733`
- `market_context_high->equity_24h` score `4.7724` n `207` status `ready` deltaP `17.5347` edge `0.2808` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `4.7123` n `117` status `ready` deltaP `25.5238` edge `0.3084` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.7123` n `117` status `ready` deltaP `25.5238` edge `0.3084` maxDD `-3.8693`
- `risk_on_high->equity_24h` score `4.1292` n `95` status `ready` deltaP `17.5347` edge `0.2272` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `4.1292` n `95` status `ready` deltaP `17.5347` edge `0.2272` maxDD `0.0`
- `risk_on_high->index_24h` score `2.1841` n `95` status `ready` deltaP `18.8907` edge `0.0603` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `2.1841` n `95` status `ready` deltaP `18.8907` edge `0.0603` maxDD `-0.0051`
- `market_context_high->index_24h` score `1.412` n `207` status `ready` deltaP `13.3529` edge `0.068` maxDD `-0.1483`
- `risk_on_high->crypto_alt_1h` score `0.9477` n `117` status `ready` deltaP `4.3964` edge `0.0849` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `0.9477` n `117` status `ready` deltaP `4.3964` edge `0.0849` maxDD `-1.1521`
- `risk_on_high->metal_24h` score `0.7023` n `95` status `ready` deltaP `16.1422` edge `0.098` maxDD `-0.9131`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
