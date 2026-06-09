# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-09T01:22:26.619078+00:00`
- Price records: `672`
- Market context records: `3335`
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

- `risk_on_high->crypto_major_24h` score `61.9145` n `31` status `ready` deltaP `66.6667` edge `4.7151` maxDD `0.0`
- `risk_on_and_context->crypto_major_24h` score `61.9145` n `31` status `ready` deltaP `66.6667` edge `4.7151` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `57.2749` n `31` status `ready` deltaP `61.1111` edge `4.3655` maxDD `0.0`
- `risk_on_and_context->crypto_alt_24h` score `57.2749` n `31` status `ready` deltaP `61.1111` edge `4.3655` maxDD `0.0`
- `risk_on_high->equity_24h` score `46.8849` n `31` status `ready` deltaP `56.7708` edge `3.5286` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `46.8849` n `31` status `ready` deltaP `56.7708` edge `3.5286` maxDD `0.0`
- `risk_on_high->index_24h` score `23.0822` n `31` status `ready` deltaP `50.8681` edge `1.5844` maxDD `0.0`
- `risk_on_and_context->index_24h` score `23.0822` n `31` status `ready` deltaP `50.8681` edge `1.5844` maxDD `0.0`
- `risk_on_high->metal_24h` score `16.0788` n `31` status `ready` deltaP `35.4502` edge `1.1297` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `16.0788` n `31` status `ready` deltaP `35.4502` edge `1.1297` maxDD `-0.7574`
- `risk_on_high->crypto_major_4h` score `15.9635` n `32` status `ready` deltaP `30.1829` edge `1.2413` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `15.9635` n `32` status `ready` deltaP `30.1829` edge `1.2413` maxDD `-5.9781`
- `market_context_high->crypto_alt_24h` score `14.2114` n `149` status `ready` deltaP `21.5138` edge `2.6627` maxDD `-70.3986`
- `market_context_high->index_24h` score `11.5139` n `149` status `ready` deltaP `34.7607` edge `0.9832` maxDD `-16.1026`
- `market_context_high->equity_24h` score `10.2555` n `149` status `ready` deltaP `29.254` edge `1.9614` maxDD `-53.663`
- `risk_on_high->crypto_alt_4h` score `7.5699` n `32` status `ready` deltaP `9.8323` edge `0.7497` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `7.5699` n `32` status `ready` deltaP `9.8323` edge `0.7497` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `3.6081` n `32` status `ready` deltaP `14.253` edge `0.481` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `3.6081` n `32` status `ready` deltaP `14.253` edge `0.481` maxDD `-5.7426`
- `market_context_high->crypto_major_24h` score `2.5769` n `149` status `ready` deltaP `23.7137` edge `2.2422` maxDD `-152.2601`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
