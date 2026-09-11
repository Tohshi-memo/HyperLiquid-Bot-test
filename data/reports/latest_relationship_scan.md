# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-11T03:38:07.629974+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `11398`

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

- `news_risk_high->unknown_1h` score `953.9125` n `51` status `ready` deltaP `-10.4291` edge `79.6044` maxDD `-1.7068`
- `news_risk_high->unknown_4h` score `727.7628` n `39` status `ready` deltaP `-24.6053` edge `60.8759` maxDD `-2.1975`
- `risk_on_high->crypto_alt_24h` score `20.7771` n `91` status `ready` deltaP `36.3458` edge `1.5121` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `20.7771` n `91` status `ready` deltaP `36.3458` edge `1.5121` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `17.353` n `191` status `ready` deltaP `31.8927` edge `1.3162` maxDD `-3.9523`
- `risk_on_high->crypto_alt_4h` score `8.9827` n `91` status `ready` deltaP `41.7934` edge `0.5071` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.9827` n `91` status `ready` deltaP `41.7934` edge `0.5071` maxDD `-1.9733`
- `market_context_high->equity_24h` score `8.415` n `191` status `ready` deltaP `30.3819` edge `0.4987` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `7.8225` n `91` status `ready` deltaP `32.8113` edge `0.519` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `7.8225` n `91` status `ready` deltaP `32.8113` edge `0.519` maxDD `-3.8693`
- `risk_on_high->crypto_major_24h` score `7.283` n `91` status `ready` deltaP `25.021` edge `1.1737` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `7.283` n `91` status `ready` deltaP `25.021` edge `1.1737` maxDD `-24.5429`
- `risk_on_high->equity_24h` score `7.2354` n `91` status `ready` deltaP `30.3819` edge `0.4004` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `7.2354` n `91` status `ready` deltaP `30.3819` edge `0.4004` maxDD `0.0`
- `risk_on_high->index_24h` score `4.941` n `91` status `ready` deltaP `46.1825` edge `0.1081` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `4.941` n `91` status `ready` deltaP `46.1825` edge `0.1081` maxDD `-0.0051`
- `market_context_high->index_24h` score `3.9778` n `191` status `ready` deltaP `40.0551` edge `0.1038` maxDD `-0.1483`
- `risk_on_high->equity_4h` score `3.64` n `91` status `ready` deltaP `33.8029` edge `0.0873` maxDD `-0.079`
- `risk_on_and_context->equity_4h` score `3.64` n `91` status `ready` deltaP `33.8029` edge `0.0873` maxDD `-0.079`
- `market_context_high->equity_4h` score `2.5057` n `191` status `ready` deltaP `27.3073` edge `0.1123` maxDD `-2.843`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
