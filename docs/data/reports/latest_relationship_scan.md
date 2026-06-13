# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-13T01:52:26.815193+00:00`
- Price records: `672`
- Market context records: `3744`
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

- `risk_on_high->crypto_major_24h` score `28.5537` n `32` status `ready` deltaP `29.1667` edge `2.1893` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `28.5537` n `32` status `ready` deltaP `29.1667` edge `2.1893` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `22.3384` n `32` status `ready` deltaP `33.6806` edge `1.637` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `22.3384` n `32` status `ready` deltaP `33.6806` edge `1.637` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `21.0968` n `32` status `ready` deltaP `30.5556` edge `1.5695` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `21.0968` n `32` status `ready` deltaP `30.5556` edge `1.5695` maxDD `-0.8779`
- `risk_on_high->index_24h` score `11.4148` n `32` status `ready` deltaP `31.25` edge `0.7429` maxDD `0.0`
- `risk_on_and_context->index_24h` score `11.4148` n `32` status `ready` deltaP `31.25` edge `0.7429` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `10.0309` n `32` status `ready` deltaP `18.1402` edge `0.8272` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `10.0309` n `32` status `ready` deltaP `18.1402` edge `0.8272` maxDD `-5.9781`
- `market_context_high->equity_24h` score `6.0271` n `159` status `ready` deltaP `17.3284` edge `0.6303` maxDD `-12.8184`
- `market_context_high->index_24h` score `5.422` n `159` status `ready` deltaP `26.8475` edge `0.3868` maxDD `-7.1159`
- `market_context_high->metal_24h` score `4.5904` n `159` status `ready` deltaP `27.4207` edge `0.3429` maxDD `-9.1203`
- `market_context_high->crypto_major_24h` score `4.4496` n `159` status `ready` deltaP `7.1345` edge `0.7696` maxDD `-31.0425`
- `market_context_high->crypto_major_4h` score `1.7696` n `168` status `ready` deltaP `8.914` edge `0.2781` maxDD `-10.5381`
- `risk_on_high->metal_24h` score `1.3636` n `32` status `ready` deltaP `14.4097` edge `0.0437` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `1.3636` n `32` status `ready` deltaP `14.4097` edge `0.0437` maxDD `-0.7574`
- `risk_on_high->crypto_alt_4h` score `1.2381` n `32` status `ready` deltaP `-0.9909` edge `0.2942` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `1.2381` n `32` status `ready` deltaP `-0.9909` edge `0.2942` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `1.1857` n `32` status `ready` deltaP `7.0884` edge `0.2182` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
