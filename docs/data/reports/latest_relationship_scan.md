# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-13T03:52:27.447814+00:00`
- Price records: `672`
- Market context records: `3752`
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

- `risk_on_high->crypto_major_24h` score `28.7124` n `32` status `ready` deltaP `29.8611` edge `2.1979` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `28.7124` n `32` status `ready` deltaP `29.8611` edge `2.1979` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `22.782` n `32` status `ready` deltaP `35.0694` edge `1.6647` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `22.782` n `32` status `ready` deltaP `35.0694` edge `1.6647` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `21.3105` n `32` status `ready` deltaP `30.9028` edge `1.585` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `21.3105` n `32` status `ready` deltaP `30.9028` edge `1.585` maxDD `-0.8779`
- `risk_on_high->index_24h` score `11.4184` n `32` status `ready` deltaP `31.25` edge `0.7432` maxDD `0.0`
- `risk_on_and_context->index_24h` score `11.4184` n `32` status `ready` deltaP `31.25` edge `0.7432` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `9.9937` n `32` status `ready` deltaP `18.1402` edge `0.8241` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `9.9937` n `32` status `ready` deltaP `18.1402` edge `0.8241` maxDD `-5.9781`
- `market_context_high->index_24h` score `5.4424` n `164` status `ready` deltaP `26.9817` edge `0.3876` maxDD `-7.1159`
- `market_context_high->equity_24h` score `5.219` n `164` status `ready` deltaP `16.167` edge `0.6019` maxDD `-13.6477`
- `market_context_high->metal_24h` score `4.6179` n `164` status `ready` deltaP `27.6296` edge `0.3438` maxDD `-9.1203`
- `market_context_high->crypto_major_24h` score `3.945` n `164` status `ready` deltaP `6.7666` edge `0.73` maxDD `-31.0425`
- `market_context_high->crypto_major_4h` score `1.7324` n `168` status `ready` deltaP `8.914` edge `0.275` maxDD `-10.5381`
- `risk_on_high->metal_24h` score `1.3154` n `32` status `ready` deltaP `14.0625` edge `0.042` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `1.3154` n `32` status `ready` deltaP `14.0625` edge `0.042` maxDD `-0.7574`
- `risk_on_high->equity_4h` score `1.1818` n `32` status `ready` deltaP `7.0884` edge `0.2177` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `1.1818` n `32` status `ready` deltaP `7.0884` edge `0.2177` maxDD `-5.7426`
- `risk_on_high->crypto_major_1h` score `0.9938` n `32` status `ready` deltaP `1.9274` edge `0.2215` maxDD `-5.8885`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
