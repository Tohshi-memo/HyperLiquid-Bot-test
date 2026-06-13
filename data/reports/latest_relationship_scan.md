# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-13T02:07:28.970347+00:00`
- Price records: `672`
- Market context records: `3745`
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

- `risk_on_high->crypto_major_24h` score `28.5314` n `32` status `ready` deltaP `28.9931` edge `2.1886` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `28.5314` n `32` status `ready` deltaP `28.9931` edge `2.1886` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `22.3823` n `32` status `ready` deltaP `33.8542` edge `1.6395` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `22.3823` n `32` status `ready` deltaP `33.8542` edge `1.6395` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `21.104` n `32` status `ready` deltaP `30.5556` edge `1.5701` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `21.104` n `32` status `ready` deltaP `30.5556` edge `1.5701` maxDD `-0.8779`
- `risk_on_high->index_24h` score `11.4136` n `32` status `ready` deltaP `31.25` edge `0.7428` maxDD `0.0`
- `risk_on_and_context->index_24h` score `11.4136` n `32` status `ready` deltaP `31.25` edge `0.7428` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `9.9971` n `32` status `ready` deltaP `17.9878` edge `0.8254` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `9.9971` n `32` status `ready` deltaP `17.9878` edge `0.8254` maxDD `-5.9781`
- `market_context_high->equity_24h` score `5.8424` n `160` status `ready` deltaP `16.9792` edge `0.6214` maxDD `-12.8184`
- `market_context_high->index_24h` score `5.4146` n `160` status `ready` deltaP `26.875` edge `0.386` maxDD `-7.1159`
- `market_context_high->metal_24h` score `4.582` n `160` status `ready` deltaP `27.3611` edge `0.3426` maxDD `-9.1203`
- `market_context_high->crypto_major_24h` score `4.3547` n `160` status `ready` deltaP `7.1181` edge `0.7618` maxDD `-31.0425`
- `market_context_high->crypto_major_4h` score `1.7358` n `168` status `ready` deltaP `8.7616` edge `0.2763` maxDD `-10.5381`
- `risk_on_high->metal_24h` score `1.3389` n `32` status `ready` deltaP `14.2361` edge `0.0428` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `1.3389` n `32` status `ready` deltaP `14.2361` edge `0.0428` maxDD `-0.7574`
- `risk_on_high->equity_4h` score `1.1699` n `32` status `ready` deltaP `6.936` edge `0.2172` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `1.1699` n `32` status `ready` deltaP `6.936` edge `0.2172` maxDD `-5.7426`
- `risk_on_high->crypto_alt_4h` score `1.1695` n `32` status `ready` deltaP `-1.1433` edge `0.2895` maxDD `-11.7537`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
