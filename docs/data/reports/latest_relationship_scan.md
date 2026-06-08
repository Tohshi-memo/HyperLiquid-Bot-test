# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-08T17:52:29.741188+00:00`
- Price records: `672`
- Market context records: `3302`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13151`

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

- `risk_on_high->crypto_major_4h` score `15.8515` n `32` status `ready` deltaP `29.878` edge `1.234` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `15.8515` n `32` status `ready` deltaP `29.878` edge `1.234` maxDD `-5.9781`
- `market_context_high->crypto_alt_24h` score `14.1954` n `119` status `ready` deltaP `19.4065` edge `2.6747` maxDD `-70.3986`
- `market_context_high->index_24h` score `9.9885` n `119` status `ready` deltaP `31.714` edge `0.8764` maxDD `-16.1026`
- `market_context_high->commodity_24h` score `9.0196` n `119` status `ready` deltaP `35.1935` edge `0.6355` maxDD `-5.8128`
- `market_context_high->equity_24h` score `7.8307` n `119` status `ready` deltaP `22.8379` edge `1.6933` maxDD `-53.663`
- `risk_on_high->crypto_alt_4h` score `7.5277` n `32` status `ready` deltaP `10.5945` edge `0.7411` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `7.5277` n `32` status `ready` deltaP `10.5945` edge `0.7411` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `3.64` n `32` status `ready` deltaP `14.253` edge `0.4851` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `3.64` n `32` status `ready` deltaP `14.253` edge `0.4851` maxDD `-5.7426`
- `market_context_high->commodity_4h` score `2.1059` n `180` status `ready` deltaP `19.3361` edge `0.1424` maxDD `-3.9989`
- `risk_on_high->crypto_major_1h` score `2.0814` n `32` status `ready` deltaP `7.1669` edge `0.326` maxDD `-5.8885`
- `risk_on_and_context->crypto_major_1h` score `2.0814` n `32` status `ready` deltaP `7.1669` edge `0.326` maxDD `-5.8885`
- `market_context_high->crypto_major_24h` score `1.8091` n `119` status `ready` deltaP `20.0937` edge `2.1679` maxDD `-152.2601`
- `risk_on_high->index_4h` score `1.1286` n `32` status `ready` deltaP `1.2957` edge `0.1948` maxDD `-1.7001`
- `risk_on_and_context->index_4h` score `1.1286` n `32` status `ready` deltaP `1.2957` edge `0.1948` maxDD `-1.7001`
- `risk_on_high->metal_1h` score `0.3079` n `32` status `ready` deltaP `6.6991` edge `0.0633` maxDD `-1.4793`
- `risk_on_and_context->metal_1h` score `0.3079` n `32` status `ready` deltaP `6.6991` edge `0.0633` maxDD `-1.4793`
- `risk_on_high->crypto_alt_1h` score `0.2649` n `32` status `ready` deltaP `0.7485` edge `0.1727` maxDD `-8.1649`
- `risk_on_and_context->crypto_alt_1h` score `0.2649` n `32` status `ready` deltaP `0.7485` edge `0.1727` maxDD `-8.1649`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
