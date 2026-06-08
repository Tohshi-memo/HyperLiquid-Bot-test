# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-08T09:52:26.631639+00:00`
- Price records: `672`
- Market context records: `3269`
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

- `risk_on_high->crypto_major_4h` score `16.4885` n `32` status `ready` deltaP `31.5549` edge `1.2759` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `16.4885` n `32` status `ready` deltaP `31.5549` edge `1.2759` maxDD `-5.9781`
- `market_context_high->crypto_alt_24h` score `13.8` n `104` status `ready` deltaP `16.2126` edge `2.6453` maxDD `-70.3986`
- `market_context_high->commodity_24h` score `12.3354` n `104` status `ready` deltaP `44.2308` edge `0.7759` maxDD `-2.0927`
- `market_context_high->index_24h` score `9.1009` n `104` status `ready` deltaP `29.2735` edge `0.8187` maxDD `-16.1026`
- `risk_on_high->crypto_alt_4h` score `7.7664` n `32` status `ready` deltaP `12.4238` edge `0.7488` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `7.7664` n `32` status `ready` deltaP `12.4238` edge `0.7488` maxDD `-11.7537`
- `market_context_high->equity_24h` score `6.32` n `104` status `ready` deltaP `18.0422` edge `1.5316` maxDD `-53.663`
- `risk_on_high->equity_4h` score `3.926` n `32` status `ready` deltaP `15.7774` edge `0.5116` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `3.926` n `32` status `ready` deltaP `15.7774` edge `0.5116` maxDD `-5.7426`
- `risk_on_high->crypto_major_1h` score `2.1975` n `32` status `ready` deltaP `7.9154` edge `0.3359` maxDD `-5.8885`
- `risk_on_and_context->crypto_major_1h` score `2.1975` n `32` status `ready` deltaP `7.9154` edge `0.3359` maxDD `-5.8885`
- `market_context_high->commodity_4h` score `2.1321` n `165` status `ready` deltaP `19.2286` edge `0.1453` maxDD `-3.9989`
- `risk_on_high->index_4h` score `1.3468` n `32` status `ready` deltaP `2.9726` edge `0.2116` maxDD `-1.7001`
- `risk_on_and_context->index_4h` score `1.3468` n `32` status `ready` deltaP `2.9726` edge `0.2116` maxDD `-1.7001`
- `market_context_high->crypto_major_24h` score `1.0428` n `104` status `ready` deltaP `18.2559` edge `2.0819` maxDD `-152.2601`
- `risk_on_high->metal_1h` score `0.3453` n `32` status `ready` deltaP `6.6991` edge `0.0681` maxDD `-1.4793`
- `risk_on_and_context->metal_1h` score `0.3453` n `32` status `ready` deltaP `6.6991` edge `0.0681` maxDD `-1.4793`
- `risk_on_high->crypto_alt_1h` score `0.2937` n `32` status `ready` deltaP `1.1976` edge `0.1734` maxDD `-8.1649`
- `risk_on_and_context->crypto_alt_1h` score `0.2937` n `32` status `ready` deltaP `1.1976` edge `0.1734` maxDD `-8.1649`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
