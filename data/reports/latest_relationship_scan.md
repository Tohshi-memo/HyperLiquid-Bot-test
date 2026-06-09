# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-09T00:37:23.129074+00:00`
- Price records: `672`
- Market context records: `3332`
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

- `risk_on_high->crypto_major_24h` score `62.2308` n `31` status `ready` deltaP `66.8403` edge `4.7403` maxDD `0.0`
- `risk_on_and_context->crypto_major_24h` score `62.2308` n `31` status `ready` deltaP `66.8403` edge `4.7403` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `57.4465` n `31` status `ready` deltaP `61.1111` edge `4.3798` maxDD `0.0`
- `risk_on_and_context->crypto_alt_24h` score `57.4465` n `31` status `ready` deltaP `61.1111` edge `4.3798` maxDD `0.0`
- `risk_on_high->equity_24h` score `46.8297` n `31` status `ready` deltaP `56.7708` edge `3.524` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `46.8297` n `31` status `ready` deltaP `56.7708` edge `3.524` maxDD `0.0`
- `risk_on_high->index_24h` score `23.015` n `31` status `ready` deltaP `50.8681` edge `1.5788` maxDD `0.0`
- `risk_on_and_context->index_24h` score `23.015` n `31` status `ready` deltaP `50.8681` edge `1.5788` maxDD `0.0`
- `risk_on_high->metal_24h` score `16.0668` n `31` status `ready` deltaP `35.4502` edge `1.1287` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `16.0668` n `31` status `ready` deltaP `35.4502` edge `1.1287` maxDD `-0.7574`
- `risk_on_high->crypto_major_4h` score `15.8771` n `32` status `ready` deltaP `30.1829` edge `1.2341` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `15.8771` n `32` status `ready` deltaP `30.1829` edge `1.2341` maxDD `-5.9781`
- `market_context_high->crypto_alt_24h` score `14.6987` n `146` status `ready` deltaP `22.7549` edge `2.7169` maxDD `-70.3986`
- `market_context_high->index_24h` score `11.4262` n `146` status `ready` deltaP `34.4297` edge `0.9781` maxDD `-16.1026`
- `market_context_high->equity_24h` score `10.1746` n `146` status `ready` deltaP `28.6886` edge `1.9548` maxDD `-53.663`
- `risk_on_high->crypto_alt_4h` score `7.4221` n `32` status `ready` deltaP `9.6799` edge `0.7384` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `7.4221` n `32` status `ready` deltaP `9.6799` edge `0.7384` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `3.5367` n `32` status `ready` deltaP `13.7957` edge `0.4749` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `3.5367` n `32` status `ready` deltaP `13.7957` edge `0.4749` maxDD `-5.7426`
- `market_context_high->crypto_major_24h` score `3.006` n `146` status `ready` deltaP `24.3745` edge `2.2928` maxDD `-152.2601`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
