# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-13T03:22:29.526475+00:00`
- Price records: `672`
- Market context records: `3750`
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

- `risk_on_high->crypto_major_24h` score `28.6187` n `32` status `ready` deltaP `29.5139` edge `2.1924` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `28.6187` n `32` status `ready` deltaP `29.5139` edge `2.1924` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `22.6534` n `32` status `ready` deltaP `34.7222` edge `1.6563` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `22.6534` n `32` status `ready` deltaP `34.7222` edge `1.6563` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `21.2199` n `32` status `ready` deltaP `30.7292` edge `1.5786` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `21.2199` n `32` status `ready` deltaP `30.7292` edge `1.5786` maxDD `-0.8779`
- `risk_on_high->index_24h` score `11.4052` n `32` status `ready` deltaP `31.25` edge `0.7421` maxDD `0.0`
- `risk_on_and_context->index_24h` score `11.4052` n `32` status `ready` deltaP `31.25` edge `0.7421` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `9.9549` n `32` status `ready` deltaP `17.8354` edge `0.8229` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `9.9549` n `32` status `ready` deltaP `17.8354` edge `0.8229` maxDD `-5.9781`
- `market_context_high->index_24h` score `5.4292` n `164` status `ready` deltaP `26.9817` edge `0.3865` maxDD `-7.1159`
- `market_context_high->equity_24h` score `5.0904` n `164` status `ready` deltaP `15.8198` edge `0.5935` maxDD `-13.6477`
- `market_context_high->metal_24h` score `4.6083` n `164` status `ready` deltaP `27.6296` edge `0.343` maxDD `-9.1203`
- `market_context_high->crypto_major_24h` score `3.8512` n `164` status `ready` deltaP `6.4194` edge `0.7245` maxDD `-31.0425`
- `market_context_high->crypto_major_4h` score `1.6936` n `168` status `ready` deltaP `8.6092` edge `0.2738` maxDD `-10.5381`
- `risk_on_high->metal_24h` score `1.3058` n `32` status `ready` deltaP `14.0625` edge `0.0412` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `1.3058` n `32` status `ready` deltaP `14.0625` edge `0.0412` maxDD `-0.7574`
- `risk_on_high->equity_4h` score `1.1628` n `32` status `ready` deltaP `6.7835` edge `0.2173` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `1.1628` n `32` status `ready` deltaP `6.7835` edge `0.2173` maxDD `-5.7426`
- `risk_on_high->crypto_major_1h` score `1.0312` n `32` status `ready` deltaP `1.9274` edge `0.2263` maxDD `-5.8885`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
