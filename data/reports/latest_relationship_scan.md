# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-08T22:22:28.268382+00:00`
- Price records: `672`
- Market context records: `3322`
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

- `risk_on_high->crypto_major_4h` score `15.8097` n `32` status `ready` deltaP `30.0305` edge `1.2295` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `15.8097` n `32` status `ready` deltaP `30.0305` edge `1.2295` maxDD `-5.9781`
- `market_context_high->crypto_alt_24h` score `15.5577` n `137` status `ready` deltaP `22.354` edge `2.8297` maxDD `-70.3986`
- `market_context_high->index_24h` score `11.1059` n `137` status `ready` deltaP `33.9061` edge `0.9549` maxDD `-16.1026`
- `market_context_high->equity_24h` score `9.6949` n `137` status `ready` deltaP `26.8438` edge `1.9056` maxDD `-53.663`
- `risk_on_high->crypto_alt_4h` score `7.2272` n `32` status `ready` deltaP `9.2226` edge `0.7252` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `7.2272` n `32` status `ready` deltaP `9.2226` edge `0.7252` maxDD `-11.7537`
- `market_context_high->crypto_major_24h` score `3.6481` n `137` status `ready` deltaP `23.7037` edge `2.3796` maxDD `-152.2601`
- `risk_on_high->equity_4h` score `3.5359` n `32` status `ready` deltaP `13.7957` edge `0.4748` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `3.5359` n `32` status `ready` deltaP `13.7957` edge `0.4748` maxDD `-5.7426`
- `market_context_high->commodity_24h` score `2.0888` n `137` status `ready` deltaP `25.4943` edge `0.48` maxDD `-20.907`
- `risk_on_high->crypto_major_1h` score `2.0704` n `32` status `ready` deltaP `7.1669` edge `0.3246` maxDD `-5.8885`
- `risk_on_and_context->crypto_major_1h` score `2.0704` n `32` status `ready` deltaP `7.1669` edge `0.3246` maxDD `-5.8885`
- `market_context_high->commodity_4h` score `1.8482` n `186` status `ready` deltaP `17.5255` edge `0.133` maxDD `-3.9989`
- `risk_on_high->index_4h` score `1.0429` n `32` status `ready` deltaP `0.5335` edge `0.1889` maxDD `-1.7001`
- `risk_on_and_context->index_4h` score `1.0429` n `32` status `ready` deltaP `0.5335` edge `0.1889` maxDD `-1.7001`
- `risk_on_high->metal_1h` score `0.2759` n `32` status `ready` deltaP `6.25` edge `0.0622` maxDD `-1.4793`
- `risk_on_and_context->metal_1h` score `0.2759` n `32` status `ready` deltaP `6.25` edge `0.0622` maxDD `-1.4793`
- `risk_on_high->crypto_alt_1h` score `0.2275` n `32` status `ready` deltaP `0.4491` edge `0.1699` maxDD `-8.1649`
- `risk_on_and_context->crypto_alt_1h` score `0.2275` n `32` status `ready` deltaP `0.4491` edge `0.1699` maxDD `-8.1649`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
