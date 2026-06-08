# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-08T09:37:27.612227+00:00`
- Price records: `672`
- Market context records: `3268`
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

- `risk_on_high->crypto_major_4h` score `16.5439` n `32` status `ready` deltaP `31.7073` edge `1.2795` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `16.5439` n `32` status `ready` deltaP `31.7073` edge `1.2795` maxDD `-5.9781`
- `market_context_high->crypto_alt_24h` score `13.8026` n `103` status `ready` deltaP `15.8727` edge `2.6479` maxDD `-70.3986`
- `market_context_high->commodity_24h` score `12.3748` n `103` status `ready` deltaP `44.3484` edge `0.7784` maxDD `-2.0927`
- `market_context_high->index_24h` score `9.0621` n `103` status `ready` deltaP `29.0588` edge `0.8169` maxDD `-16.1026`
- `risk_on_high->crypto_alt_4h` score `7.8194` n `32` status `ready` deltaP `12.5762` edge `0.7522` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `7.8194` n `32` status `ready` deltaP `12.5762` edge `0.7522` maxDD `-11.7537`
- `market_context_high->equity_24h` score `6.2463` n `103` status `ready` deltaP `17.6595` edge `1.5247` maxDD `-53.663`
- `risk_on_high->equity_4h` score `3.9534` n `32` status `ready` deltaP `15.9299` edge `0.5141` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `3.9534` n `32` status `ready` deltaP `15.9299` edge `0.5141` maxDD `-5.7426`
- `risk_on_high->crypto_major_1h` score `2.2131` n `32` status `ready` deltaP `8.0651` edge `0.3369` maxDD `-5.8885`
- `risk_on_and_context->crypto_major_1h` score `2.2131` n `32` status `ready` deltaP `8.0651` edge `0.3369` maxDD `-5.8885`
- `market_context_high->commodity_4h` score `2.1139` n `165` status `ready` deltaP `19.0762` edge `0.1448` maxDD `-3.9989`
- `risk_on_high->index_4h` score `1.3617` n `32` status `ready` deltaP `3.125` edge `0.2125` maxDD `-1.7001`
- `risk_on_and_context->index_4h` score `1.3617` n `32` status `ready` deltaP `3.125` edge `0.2125` maxDD `-1.7001`
- `market_context_high->crypto_major_24h` score `0.959` n `103` status `ready` deltaP `17.86` edge `2.0738` maxDD `-152.2601`
- `risk_on_high->metal_1h` score `0.3437` n `32` status `ready` deltaP `6.6991` edge `0.0679` maxDD `-1.4793`
- `risk_on_and_context->metal_1h` score `0.3437` n `32` status `ready` deltaP `6.6991` edge `0.0679` maxDD `-1.4793`
- `risk_on_high->crypto_alt_1h` score `0.3015` n `32` status `ready` deltaP `1.1976` edge `0.1744` maxDD `-8.1649`
- `risk_on_and_context->crypto_alt_1h` score `0.3015` n `32` status `ready` deltaP `1.1976` edge `0.1744` maxDD `-8.1649`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
