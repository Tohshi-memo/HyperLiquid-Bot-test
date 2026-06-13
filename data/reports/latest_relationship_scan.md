# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-13T04:22:28.480319+00:00`
- Price records: `672`
- Market context records: `3754`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13153`

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

- `risk_on_high->crypto_major_24h` score `28.8242` n `32` status `ready` deltaP `30.2083` edge `2.2049` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `28.8242` n `32` status `ready` deltaP `30.2083` edge `2.2049` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `22.9033` n `32` status `ready` deltaP `35.4167` edge `1.6725` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `22.9033` n `32` status `ready` deltaP `35.4167` edge `1.6725` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `21.4475` n `32` status `ready` deltaP `31.25` edge `1.5941` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `21.4475` n `32` status `ready` deltaP `31.25` edge `1.5941` maxDD `-0.8779`
- `risk_on_high->index_24h` score `11.4292` n `32` status `ready` deltaP `31.25` edge `0.7441` maxDD `0.0`
- `risk_on_and_context->index_24h` score `11.4292` n `32` status `ready` deltaP `31.25` edge `0.7441` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `10.0649` n `32` status `ready` deltaP `18.4451` edge `0.828` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `10.0649` n `32` status `ready` deltaP `18.4451` edge `0.828` maxDD `-5.9781`
- `market_context_high->index_24h` score `5.4177` n `162` status `ready` deltaP `26.929` edge `0.3859` maxDD `-7.1159`
- `market_context_high->equity_24h` score `5.2941` n `162` status `ready` deltaP `16.2809` edge `0.6074` maxDD `-13.6477`
- `market_context_high->metal_24h` score `4.5789` n `162` status `ready` deltaP `27.4113` edge `0.342` maxDD `-9.1203`
- `market_context_high->crypto_major_24h` score `4.0248` n `162` status `ready` deltaP `6.7901` edge `0.7365` maxDD `-31.0425`
- `market_context_high->crypto_major_4h` score `1.6734` n `166` status `ready` deltaP `8.7312` edge `0.2713` maxDD `-10.5381`
- `risk_on_high->metal_24h` score `1.3202` n `32` status `ready` deltaP `14.0625` edge `0.0424` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `1.3202` n `32` status `ready` deltaP `14.0625` edge `0.0424` maxDD `-0.7574`
- `risk_on_high->equity_4h` score `1.1771` n `32` status `ready` deltaP `7.0884` edge `0.2171` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `1.1771` n `32` status `ready` deltaP `7.0884` edge `0.2171` maxDD `-5.7426`
- `risk_on_high->crypto_major_1h` score `0.9618` n `32` status `ready` deltaP `1.9274` edge `0.2174` maxDD `-5.8885`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
