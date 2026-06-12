# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-12T18:07:33.933772+00:00`
- Price records: `672`
- Market context records: `3710`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13025`

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

- `risk_on_high->crypto_major_24h` score `29.8139` n `32` status `ready` deltaP `31.9444` edge `2.2758` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `29.8139` n `32` status `ready` deltaP `31.9444` edge `2.2758` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `22.6609` n `32` status `ready` deltaP `34.2014` edge `1.6604` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `22.6609` n `32` status `ready` deltaP `34.2014` edge `1.6604` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `21.8591` n `32` status `ready` deltaP `31.25` edge `1.6284` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `21.8591` n `32` status `ready` deltaP `31.25` edge `1.6284` maxDD `-0.8779`
- `risk_on_high->index_24h` score `12.0318` n `32` status `ready` deltaP `34.0278` edge `0.7758` maxDD `0.0`
- `risk_on_and_context->index_24h` score `12.0318` n `32` status `ready` deltaP `34.0278` edge `0.7758` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `9.8419` n `32` status `ready` deltaP `16.7683` edge `0.8206` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `9.8419` n `32` status `ready` deltaP `16.7683` edge `0.8206` maxDD `-5.9781`
- `market_context_high->index_24h` score `4.6589` n `162` status `ready` deltaP `23.534` edge `0.3453` maxDD `-7.1159`
- `market_context_high->equity_24h` score `4.3864` n `162` status `ready` deltaP `15.6829` edge `0.5819` maxDD `-17.6733`
- `risk_on_high->metal_24h` score `2.4306` n `32` status `ready` deltaP `19.6181` edge `0.0979` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `2.4306` n `32` status `ready` deltaP `19.6181` edge `0.0979` maxDD `-0.7574`
- `market_context_high->metal_24h` score `1.7317` n `162` status `ready` deltaP `18.7693` edge `0.2611` maxDD `-11.3536`
- `risk_on_high->equity_4h` score `1.5304` n `32` status `ready` deltaP `8.003` edge `0.2563` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `1.5304` n `32` status `ready` deltaP `8.003` edge `0.2563` maxDD `-5.7426`
- `risk_on_high->crypto_alt_4h` score `1.4435` n `32` status `ready` deltaP `-1.753` edge `0.3164` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `1.4435` n `32` status `ready` deltaP `-1.753` edge `0.3164` maxDD `-11.7537`
- `risk_on_high->crypto_major_1h` score `0.9665` n `32` status `ready` deltaP `1.628` edge `0.22` maxDD `-5.8885`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
