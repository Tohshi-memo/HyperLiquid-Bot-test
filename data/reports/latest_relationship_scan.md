# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-07T15:37:33.076554+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10204`

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
- `risk_on_high->crypto_major_24h` score `21.5275` n `95` status `ready` deltaP `37.7267` edge `1.6003` maxDD `-1.9619`
- `risk_on_and_context->crypto_major_24h` score `21.5275` n `95` status `ready` deltaP `37.7267` edge `1.6003` maxDD `-1.9619`
- `risk_on_high->crypto_alt_24h` score `14.8574` n `95` status `ready` deltaP `32.1181` edge `1.024` maxDD `0.0`
- `risk_on_and_context->crypto_alt_24h` score `14.8574` n `95` status `ready` deltaP `32.1181` edge `1.024` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `8.2653` n `206` status `ready` deltaP `24.8365` edge `0.5807` maxDD `-2.5998`
- `risk_on_high->crypto_alt_4h` score `5.3747` n `117` status `ready` deltaP `28.9582` edge `0.292` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.3747` n `117` status `ready` deltaP `28.9582` edge `0.292` maxDD `-1.9733`
- `market_context_high->equity_24h` score `4.8343` n `206` status `ready` deltaP `17.7083` edge `0.2848` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `4.6701` n `117` status `ready` deltaP `25.3713` edge `0.3059` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.6701` n `117` status `ready` deltaP `25.3713` edge `0.3059` maxDD `-3.8693`
- `risk_on_high->equity_24h` score `4.1647` n `95` status `ready` deltaP `17.7083` edge `0.229` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `4.1647` n `95` status `ready` deltaP `17.7083` edge `0.229` maxDD `0.0`
- `risk_on_high->index_24h` score `2.2016` n `95` status `ready` deltaP `19.0643` edge `0.0606` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `2.2016` n `95` status `ready` deltaP `19.0643` edge `0.0606` maxDD `-0.0051`
- `market_context_high->index_24h` score `1.4297` n `206` status `ready` deltaP `13.4843` edge `0.0686` maxDD `-0.1483`
- `risk_on_high->crypto_alt_1h` score `0.9057` n `117` status `ready` deltaP `4.2467` edge `0.0824` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `0.9057` n `117` status `ready` deltaP `4.2467` edge `0.0824` maxDD `-1.1521`
- `risk_on_high->metal_24h` score `0.7168` n `95` status `ready` deltaP `16.3158` edge `0.0987` maxDD `-0.9131`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
