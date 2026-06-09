# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-09T21:22:25.739324+00:00`
- Price records: `672`
- Market context records: `3420`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13116`

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

- `risk_on_high->crypto_major_24h` score `55.9058` n `32` status `ready` deltaP `58.3333` edge `4.2742` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `55.9058` n `32` status `ready` deltaP `58.3333` edge `4.2742` maxDD `-0.0083`
- `risk_on_high->crypto_alt_24h` score `55.8872` n `32` status `ready` deltaP `58.6806` edge `4.2812` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `55.8872` n `32` status `ready` deltaP `58.6806` edge `4.2812` maxDD `-0.8779`
- `risk_on_high->equity_24h` score `45.7217` n `32` status `ready` deltaP `56.0764` edge `3.4363` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `45.7217` n `32` status `ready` deltaP `56.0764` edge `3.4363` maxDD `0.0`
- `risk_on_high->index_24h` score `23.9363` n `32` status `ready` deltaP `51.3889` edge `1.6521` maxDD `0.0`
- `risk_on_and_context->index_24h` score `23.9363` n `32` status `ready` deltaP `51.3889` edge `1.6521` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `22.1129` n `154` status `ready` deltaP `19.5978` edge `2.508` maxDD `-56.6728`
- `market_context_high->crypto_major_24h` score `21.0283` n `154` status `ready` deltaP `24.4453` edge `2.3625` maxDD `-54.8486`
- `market_context_high->equity_24h` score `20.5029` n `154` status `ready` deltaP `33.3491` edge `2.1275` maxDD `-40.9667`
- `risk_on_high->crypto_major_4h` score `14.7044` n `32` status `ready` deltaP `26.2195` edge `1.1628` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `14.7044` n `32` status `ready` deltaP `26.2195` edge `1.1628` maxDD `-5.9781`
- `risk_on_high->metal_24h` score `13.395` n `32` status `ready` deltaP `28.9931` edge `0.9491` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `13.395` n `32` status `ready` deltaP `28.9931` edge `0.9491` maxDD `-0.7574`
- `market_context_high->index_24h` score `12.7436` n `154` status `ready` deltaP `36.4538` edge `1.0406` maxDD `-15.0661`
- `risk_on_high->crypto_alt_4h` score `6.3716` n `32` status `ready` deltaP `6.4787` edge `0.6722` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `6.3716` n `32` status `ready` deltaP `6.4787` edge `0.6722` maxDD `-11.7537`
- `market_context_high->metal_24h` score `4.4459` n `154` status `ready` deltaP `23.8795` edge `0.8648` maxDD `-25.9879`
- `risk_on_high->equity_4h` score `4.3317` n `32` status `ready` deltaP `16.8445` edge `0.5565` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
