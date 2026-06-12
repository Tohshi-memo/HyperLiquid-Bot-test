# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-12T01:37:41.359125+00:00`
- Price records: `672`
- Market context records: `3640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13163`

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

- `risk_on_high->crypto_major_24h` score `38.3434` n `32` status `ready` deltaP `43.4028` edge `2.9102` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `38.3434` n `32` status `ready` deltaP `43.4028` edge `2.9102` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `35.0057` n `32` status `ready` deltaP `45.4861` edge `2.6139` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `35.0057` n `32` status `ready` deltaP `45.4861` edge `2.6139` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `30.6447` n `32` status `ready` deltaP `42.5347` edge `2.2853` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `30.6447` n `32` status `ready` deltaP `42.5347` edge `2.2853` maxDD `-0.8779`
- `risk_on_high->index_24h` score `19.9625` n `32` status `ready` deltaP `45.4861` edge `1.3603` maxDD `0.0`
- `risk_on_and_context->index_24h` score `19.9625` n `32` status `ready` deltaP `45.4861` edge `1.3603` maxDD `0.0`
- `risk_on_high->metal_24h` score `12.0437` n `32` status `ready` deltaP `31.0764` edge `0.8226` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `12.0437` n `32` status `ready` deltaP `31.0764` edge `0.8226` maxDD `-0.7574`
- `risk_on_high->crypto_major_4h` score `11.9874` n `32` status `ready` deltaP `21.3415` edge `0.9689` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `11.9874` n `32` status `ready` deltaP `21.3415` edge `0.9689` maxDD `-5.9781`
- `market_context_high->equity_24h` score `10.7177` n `157` status `ready` deltaP `22.5562` edge `1.3092` maxDD `-35.3144`
- `market_context_high->index_24h` score `9.5665` n `157` status `ready` deltaP `30.8364` edge `0.7632` maxDD `-11.3924`
- `market_context_high->crypto_major_24h` score `4.3384` n `157` status `ready` deltaP `9.5851` edge `1.0043` maxDD `-49.5335`
- `market_context_high->metal_24h` score `4.0475` n `157` status `ready` deltaP `25.3837` edge `0.7449` maxDD `-21.6171`
- `risk_on_high->crypto_alt_4h` score `3.4666` n `32` status `ready` deltaP `1.9055` edge `0.4606` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `3.4666` n `32` status `ready` deltaP `1.9055` edge `0.4606` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `2.5893` n `32` status `ready` deltaP `10.4421` edge `0.3758` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `2.5893` n `32` status `ready` deltaP `10.4421` edge `0.3758` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
