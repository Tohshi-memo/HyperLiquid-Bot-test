# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-08T22:52:27.465771+00:00`
- Price records: `672`
- Market context records: `3324`
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

- `risk_on_high->crypto_major_4h` score `15.8255` n `32` status `ready` deltaP `30.1829` edge `1.2298` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `15.8255` n `32` status `ready` deltaP `30.1829` edge `1.2298` maxDD `-5.9781`
- `market_context_high->crypto_alt_24h` score `15.4012` n `139` status `ready` deltaP `22.5845` edge `2.8081` maxDD `-70.3986`
- `market_context_high->index_24h` score `11.2152` n `139` status `ready` deltaP `34.1476` edge `0.9624` maxDD `-16.1026`
- `market_context_high->equity_24h` score `9.8249` n `139` status `ready` deltaP `27.2744` edge `1.9194` maxDD `-53.663`
- `risk_on_high->crypto_alt_4h` score `7.2368` n `32` status `ready` deltaP `9.2226` edge `0.726` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `7.2368` n `32` status `ready` deltaP `9.2226` edge `0.726` maxDD `-11.7537`
- `market_context_high->crypto_major_24h` score `3.5386` n `139` status `ready` deltaP `23.997` edge `2.3636` maxDD `-152.2601`
- `risk_on_high->equity_4h` score `3.5359` n `32` status `ready` deltaP `13.7957` edge `0.4748` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `3.5359` n `32` status `ready` deltaP `13.7957` edge `0.4748` maxDD `-5.7426`
- `risk_on_high->crypto_major_1h` score `2.104` n `32` status `ready` deltaP `7.3166` edge `0.3279` maxDD `-5.8885`
- `risk_on_and_context->crypto_major_1h` score `2.104` n `32` status `ready` deltaP `7.3166` edge `0.3279` maxDD `-5.8885`
- `market_context_high->commodity_4h` score `1.8058` n `186` status `ready` deltaP `17.2207` edge `0.1315` maxDD `-3.9989`
- `market_context_high->commodity_24h` score `1.7274` n `139` status `ready` deltaP `24.5966` edge `0.4662` maxDD `-22.3638`
- `risk_on_high->index_4h` score `1.0359` n `32` status `ready` deltaP `0.5335` edge `0.188` maxDD `-1.7001`
- `risk_on_and_context->index_4h` score `1.0359` n `32` status `ready` deltaP `0.5335` edge `0.188` maxDD `-1.7001`
- `risk_on_high->metal_1h` score `0.297` n `32` status `ready` deltaP `6.5494` edge `0.0629` maxDD `-1.4793`
- `risk_on_and_context->metal_1h` score `0.297` n `32` status `ready` deltaP `6.5494` edge `0.0629` maxDD `-1.4793`
- `risk_on_high->crypto_alt_1h` score `0.2774` n `32` status `ready` deltaP `0.7485` edge `0.1743` maxDD `-8.1649`
- `risk_on_and_context->crypto_alt_1h` score `0.2774` n `32` status `ready` deltaP `0.7485` edge `0.1743` maxDD `-8.1649`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
