# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-08T17:22:29.280392+00:00`
- Price records: `672`
- Market context records: `3300`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13151`

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

- `risk_on_high->crypto_major_4h` score `15.8685` n `32` status `ready` deltaP `30.0305` edge `1.2344` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `15.8685` n `32` status `ready` deltaP `30.0305` edge `1.2344` maxDD `-5.9781`
- `market_context_high->crypto_alt_24h` score `14.085` n `117` status `ready` deltaP `18.9637` edge `2.6635` maxDD `-70.3986`
- `market_context_high->index_24h` score `9.8697` n `117` status `ready` deltaP `31.3836` edge `0.8687` maxDD `-16.1026`
- `market_context_high->commodity_24h` score `9.5987` n `117` status `ready` deltaP `36.3114` edge `0.6525` maxDD `-4.5745`
- `market_context_high->equity_24h` score `7.6476` n `117` status `ready` deltaP `22.4226` edge `1.6726` maxDD `-53.663`
- `risk_on_high->crypto_alt_4h` score `7.5737` n `32` status `ready` deltaP `10.8994` edge `0.7429` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `7.5737` n `32` status `ready` deltaP `10.8994` edge `0.7429` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `3.6863` n `32` status `ready` deltaP `14.5579` edge `0.489` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `3.6863` n `32` status `ready` deltaP `14.5579` edge `0.489` maxDD `-5.7426`
- `risk_on_high->crypto_major_1h` score `2.065` n `32` status `ready` deltaP `7.0172` edge `0.3249` maxDD `-5.8885`
- `risk_on_and_context->crypto_major_1h` score `2.065` n `32` status `ready` deltaP `7.0172` edge `0.3249` maxDD `-5.8885`
- `market_context_high->commodity_4h` score `2.0638` n `178` status `ready` deltaP `19.0052` edge `0.1411` maxDD `-3.9989`
- `market_context_high->crypto_major_24h` score `1.6139` n `117` status `ready` deltaP `19.5646` edge `2.1464` maxDD `-152.2601`
- `risk_on_high->index_4h` score `1.134` n `32` status `ready` deltaP `1.2957` edge `0.1955` maxDD `-1.7001`
- `risk_on_and_context->index_4h` score `1.134` n `32` status `ready` deltaP `1.2957` edge `0.1955` maxDD `-1.7001`
- `risk_on_high->metal_1h` score `0.2938` n `32` status `ready` deltaP `6.5494` edge `0.0625` maxDD `-1.4793`
- `risk_on_and_context->metal_1h` score `0.2938` n `32` status `ready` deltaP `6.5494` edge `0.0625` maxDD `-1.4793`
- `risk_on_high->crypto_alt_1h` score `0.2633` n `32` status `ready` deltaP `0.7485` edge `0.1725` maxDD `-8.1649`
- `risk_on_and_context->crypto_alt_1h` score `0.2633` n `32` status `ready` deltaP `0.7485` edge `0.1725` maxDD `-8.1649`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
