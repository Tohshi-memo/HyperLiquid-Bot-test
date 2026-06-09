# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-09T02:07:29.061615+00:00`
- Price records: `672`
- Market context records: `3338`
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

- `risk_on_high->crypto_major_24h` score `61.552` n `31` status `ready` deltaP `66.3194` edge `4.6872` maxDD `0.0`
- `risk_on_and_context->crypto_major_24h` score `61.552` n `31` status `ready` deltaP `66.3194` edge `4.6872` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `57.0738` n `31` status `ready` deltaP `60.9375` edge `4.3499` maxDD `0.0`
- `risk_on_and_context->crypto_alt_24h` score `57.0738` n `31` status `ready` deltaP `60.9375` edge `4.3499` maxDD `0.0`
- `risk_on_high->equity_24h` score `46.8921` n `31` status `ready` deltaP `56.7708` edge `3.5292` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `46.8921` n `31` status `ready` deltaP `56.7708` edge `3.5292` maxDD `0.0`
- `risk_on_high->index_24h` score `23.1242` n `31` status `ready` deltaP `50.8681` edge `1.5879` maxDD `0.0`
- `risk_on_and_context->index_24h` score `23.1242` n `31` status `ready` deltaP `50.8681` edge `1.5879` maxDD `0.0`
- `risk_on_high->metal_24h` score `16.0704` n `31` status `ready` deltaP `35.4502` edge `1.129` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `16.0704` n `31` status `ready` deltaP `35.4502` edge `1.129` maxDD `-0.7574`
- `risk_on_high->crypto_major_4h` score `16.0693` n `32` status `ready` deltaP `30.3354` edge `1.2491` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `16.0693` n `32` status `ready` deltaP `30.3354` edge `1.2491` maxDD `-5.9781`
- `market_context_high->crypto_alt_24h` score `13.8907` n `152` status `ready` deltaP `20.8059` edge `2.6263` maxDD `-70.3986`
- `market_context_high->index_24h` score `11.6797` n `152` status `ready` deltaP `35.0786` edge `0.9949` maxDD `-16.1026`
- `market_context_high->equity_24h` score `10.4249` n `152` status `ready` deltaP `29.7971` edge `1.9795` maxDD `-53.663`
- `risk_on_high->crypto_alt_4h` score `7.7371` n `32` status `ready` deltaP `10.1372` edge `0.7616` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `7.7371` n `32` status `ready` deltaP `10.1372` edge `0.7616` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `3.6668` n `32` status `ready` deltaP `14.5579` edge `0.4865` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `3.6668` n `32` status `ready` deltaP `14.5579` edge `0.4865` maxDD `-5.7426`
- `market_context_high->crypto_major_24h` score `2.2832` n `152` status `ready` deltaP `23.5562` edge `2.2056` maxDD `-152.2601`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
