# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-09T01:37:31.647490+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `64`

- Symbol pattern count: `6543`

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

- `market_context_high->equity_24h` score `8.4027` n `34` status `ready` deltaP `15.7782` edge `0.9091` maxDD `-22.7914`
- `market_context_high->index_24h` score `1.2422` n `34` status `ready` deltaP `15.4003` edge `0.1147` maxDD `-2.6491`
- `market_context_high->commodity_24h` score `1.1825` n `34` status `ready` deltaP `6.5768` edge `0.1753` maxDD `-2.4036`
- `market_context_high->metal_1h` score `0.7262` n `64` status `ready` deltaP `9.375` edge `0.0308` maxDD `-0.6226`
- `market_context_high->fx_24h` score `0.6959` n `34` status `ready` deltaP `10.4882` edge `-0.0031` maxDD `-0.0397`
- `market_context_high->commodity_4h` score `0.3983` n `52` status `ready` deltaP `3.0253` edge `0.0519` maxDD `-1.1102`
- `market_context_high->equity_1h` score `0.0411` n `64` status `ready` deltaP `1.9461` edge `0.112` maxDD `-5.5762`
- `market_context_high->metal_4h` score `-0.1266` n `52` status `ready` deltaP `4.5146` edge `0.0062` maxDD `-1.2025`
- `market_context_high->index_4h` score `-0.3614` n `52` status `ready` deltaP `7.0825` edge `-0.0007` maxDD `-2.4279`
- `market_context_high->commodity_1h` score `-0.3632` n `64` status `ready` deltaP `3.256` edge `0.0068` maxDD `-1.7019`
- `market_context_high->fx_4h` score `-0.4183` n `52` status `ready` deltaP `3.4592` edge `0.0078` maxDD `-0.7596`
- `market_context_high->index_1h` score `-0.4649` n `64` status `ready` deltaP `-2.7414` edge `0.017` maxDD `-0.6664`
- `market_context_high->fx_1h` score `-0.6834` n `64` status `ready` deltaP `-7.4663` edge `0.0001` maxDD `-0.3682`
- `market_context_high->crypto_alt_1h` score `-0.7957` n `64` status `ready` deltaP `8.5142` edge `0.0305` maxDD `-10.1421`
- `market_context_high->metal_24h` score `-1.9323` n `34` status `ready` deltaP `4.1667` edge `-0.1335` maxDD `-1.4245`
- `market_context_high->crypto_major_1h` score `-1.9832` n `64` status `ready` deltaP `1.8806` edge `-0.0569` maxDD `-11.7911`
- `market_context_high->crypto_major_24h` score `-6.2601` n `34` status `ready` deltaP `-6.6993` edge `-0.0656` maxDD `-26.9129`
- `market_context_high->equity_4h` score `-6.5489` n `52` status `ready` deltaP `1.4306` edge `-0.1773` maxDD `-24.9053`
- `market_context_high->crypto_alt_4h` score `-10.6459` n `52` status `ready` deltaP `-1.7237` edge `-0.4006` maxDD `-31.3386`
- `market_context_high->crypto_alt_24h` score `-11.0945` n `34` status `ready` deltaP `-20.0368` edge `-0.2579` maxDD `-35.9782`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
