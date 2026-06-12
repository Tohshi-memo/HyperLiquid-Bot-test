# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-12T03:07:24.335513+00:00`
- Price records: `672`
- Market context records: `3647`
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

- `risk_on_high->crypto_major_24h` score `37.2124` n `32` status `ready` deltaP `42.3611` edge `2.8229` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `37.2124` n `32` status `ready` deltaP `42.3611` edge `2.8229` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `33.576` n `32` status `ready` deltaP `44.4444` edge `2.5017` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `33.576` n `32` status `ready` deltaP `44.4444` edge `2.5017` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `29.4178` n `32` status `ready` deltaP `41.4931` edge `2.19` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `29.4178` n `32` status `ready` deltaP `41.4931` edge `2.19` maxDD `-0.8779`
- `risk_on_high->index_24h` score `19.1076` n `32` status `ready` deltaP `44.4444` edge `1.296` maxDD `0.0`
- `risk_on_and_context->index_24h` score `19.1076` n `32` status `ready` deltaP `44.4444` edge `1.296` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `11.6292` n `32` status `ready` deltaP `20.8841` edge `0.9421` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `11.6292` n `32` status `ready` deltaP `20.8841` edge `0.9421` maxDD `-5.9781`
- `risk_on_high->metal_24h` score `11.0664` n `32` status `ready` deltaP `30.0347` edge `0.7481` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `11.0664` n `32` status `ready` deltaP `30.0347` edge `0.7481` maxDD `-0.7574`
- `market_context_high->equity_24h` score `9.288` n `157` status `ready` deltaP `21.5145` edge `1.197` maxDD `-35.3144`
- `market_context_high->index_24h` score `8.7115` n `157` status `ready` deltaP `29.7947` edge `0.6989` maxDD `-11.3924`
- `market_context_high->metal_24h` score `3.4122` n `157` status `ready` deltaP `24.342` edge `0.6704` maxDD `-21.6171`
- `market_context_high->crypto_major_24h` score `3.2074` n `157` status `ready` deltaP `8.5434` edge `0.917` maxDD `-49.5335`
- `risk_on_high->crypto_alt_4h` score `3.059` n `32` status `ready` deltaP `1.2957` edge `0.4307` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `3.059` n `32` status `ready` deltaP `1.2957` edge `0.4307` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `2.5006` n `32` status `ready` deltaP `9.6799` edge `0.3695` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `2.5006` n `32` status `ready` deltaP `9.6799` edge `0.3695` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
