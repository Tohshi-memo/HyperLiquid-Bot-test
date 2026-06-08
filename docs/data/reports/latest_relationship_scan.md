# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-08T10:22:25.504745+00:00`
- Price records: `672`
- Market context records: `3271`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10503`

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

- `risk_on_high->crypto_major_4h` score `16.4053` n `32` status `ready` deltaP `31.25` edge `1.271` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `16.4053` n `32` status `ready` deltaP `31.25` edge `1.271` maxDD `-5.9781`
- `market_context_high->crypto_alt_24h` score `13.8549` n `106` status `ready` deltaP `16.8632` edge `2.648` maxDD `-70.3986`
- `market_context_high->commodity_24h` score `12.2719` n `106` status `ready` deltaP `43.9924` edge `0.7722` maxDD `-2.0927`
- `market_context_high->index_24h` score `9.2039` n `106` status `ready` deltaP `29.6908` edge `0.8245` maxDD `-16.1026`
- `risk_on_high->crypto_alt_4h` score `7.6881` n `32` status `ready` deltaP `12.1189` edge `0.7443` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `7.6881` n `32` status `ready` deltaP `12.1189` edge `0.7443` maxDD `-11.7537`
- `market_context_high->equity_24h` score `6.5022` n `106` status `ready` deltaP `18.7861` edge `1.55` maxDD `-53.663`
- `risk_on_high->equity_4h` score `3.8735` n `32` status `ready` deltaP `15.4726` edge `0.5069` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `3.8735` n `32` status `ready` deltaP `15.4726` edge `0.5069` maxDD `-5.7426`
- `risk_on_high->crypto_major_1h` score `2.2037` n `32` status `ready` deltaP `8.0651` edge `0.3357` maxDD `-5.8885`
- `risk_on_and_context->crypto_major_1h` score `2.2037` n `32` status `ready` deltaP `8.0651` edge `0.3357` maxDD `-5.8885`
- `market_context_high->commodity_4h` score `2.1708` n `165` status `ready` deltaP `19.5335` edge `0.1465` maxDD `-3.9989`
- `risk_on_high->index_4h` score `1.3138` n `32` status `ready` deltaP `2.6677` edge `0.2094` maxDD `-1.7001`
- `risk_on_and_context->index_4h` score `1.3138` n `32` status `ready` deltaP `2.6677` edge `0.2094` maxDD `-1.7001`
- `market_context_high->crypto_major_24h` score `1.2632` n `106` status `ready` deltaP `19.0153` edge `2.1051` maxDD `-152.2601`
- `risk_on_high->metal_1h` score `0.3461` n `32` status `ready` deltaP `6.6991` edge `0.0682` maxDD `-1.4793`
- `risk_on_and_context->metal_1h` score `0.3461` n `32` status `ready` deltaP `6.6991` edge `0.0682` maxDD `-1.4793`
- `risk_on_high->crypto_alt_1h` score `0.2984` n `32` status `ready` deltaP `1.3473` edge `0.173` maxDD `-8.1649`
- `risk_on_and_context->crypto_alt_1h` score `0.2984` n `32` status `ready` deltaP `1.3473` edge `0.173` maxDD `-8.1649`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
