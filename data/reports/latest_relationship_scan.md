# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-13T04:07:31.417574+00:00`
- Price records: `672`
- Market context records: `3753`
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

- `risk_on_high->crypto_major_24h` score `28.7587` n `32` status `ready` deltaP `30.0347` edge `2.2006` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `28.7587` n `32` status `ready` deltaP `30.0347` edge `2.2006` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `22.8414` n `32` status `ready` deltaP `35.2431` edge `1.6685` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `22.8414` n `32` status `ready` deltaP `35.2431` edge `1.6685` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `21.3688` n `32` status `ready` deltaP `31.0764` edge `1.5887` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `21.3688` n `32` status `ready` deltaP `31.0764` edge `1.5887` maxDD `-0.8779`
- `risk_on_high->index_24h` score `11.4244` n `32` status `ready` deltaP `31.25` edge `0.7437` maxDD `0.0`
- `risk_on_and_context->index_24h` score `11.4244` n `32` status `ready` deltaP `31.25` edge `0.7437` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `10.0239` n `32` status `ready` deltaP `18.2927` edge `0.8256` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `10.0239` n `32` status `ready` deltaP `18.2927` edge `0.8256` maxDD `-5.9781`
- `market_context_high->index_24h` score `5.4247` n `163` status `ready` deltaP `26.9555` edge `0.3863` maxDD `-7.1159`
- `market_context_high->equity_24h` score `5.2572` n `163` status `ready` deltaP `16.2247` edge `0.6047` maxDD `-13.6477`
- `market_context_high->metal_24h` score `4.5996` n `163` status `ready` deltaP `27.5211` edge `0.343` maxDD `-9.1203`
- `market_context_high->crypto_major_24h` score `4.0024` n `163` status `ready` deltaP `6.7793` edge `0.7347` maxDD `-31.0425`
- `market_context_high->crypto_major_4h` score `1.718` n `167` status `ready` deltaP `8.8241` edge `0.2744` maxDD `-10.5381`
- `risk_on_high->metal_24h` score `1.3166` n `32` status `ready` deltaP `14.0625` edge `0.0421` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `1.3166` n `32` status `ready` deltaP `14.0625` edge `0.0421` maxDD `-0.7574`
- `risk_on_high->equity_4h` score `1.1794` n `32` status `ready` deltaP `7.0884` edge `0.2174` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `1.1794` n `32` status `ready` deltaP `7.0884` edge `0.2174` maxDD `-5.7426`
- `risk_on_high->crypto_major_1h` score `0.9813` n `32` status `ready` deltaP `1.9274` edge `0.2199` maxDD `-5.8885`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
