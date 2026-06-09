# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-09T01:37:20.871263+00:00`
- Price records: `672`
- Market context records: `3336`
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

- `risk_on_high->crypto_major_24h` score `61.777` n `31` status `ready` deltaP `66.4931` edge `4.7048` maxDD `0.0`
- `risk_on_and_context->crypto_major_24h` score `61.777` n `31` status `ready` deltaP `66.4931` edge `4.7048` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `57.1866` n `31` status `ready` deltaP `60.9375` edge `4.3593` maxDD `0.0`
- `risk_on_and_context->crypto_alt_24h` score `57.1866` n `31` status `ready` deltaP `60.9375` edge `4.3593` maxDD `0.0`
- `risk_on_high->equity_24h` score `46.8789` n `31` status `ready` deltaP `56.7708` edge `3.5281` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `46.8789` n `31` status `ready` deltaP `56.7708` edge `3.5281` maxDD `0.0`
- `risk_on_high->index_24h` score `23.093` n `31` status `ready` deltaP `50.8681` edge `1.5853` maxDD `0.0`
- `risk_on_and_context->index_24h` score `23.093` n `31` status `ready` deltaP `50.8681` edge `1.5853` maxDD `0.0`
- `risk_on_high->metal_24h` score `16.0481` n `31` status `ready` deltaP `35.2766` edge `1.1283` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `16.0481` n `31` status `ready` deltaP `35.2766` edge `1.1283` maxDD `-0.7574`
- `risk_on_high->crypto_major_4h` score `15.9971` n `32` status `ready` deltaP `30.1829` edge `1.2441` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `15.9971` n `32` status `ready` deltaP `30.1829` edge `1.2441` maxDD `-5.9781`
- `market_context_high->crypto_alt_24h` score `14.128` n `150` status `ready` deltaP `21.6042` edge `2.6514` maxDD `-70.3986`
- `market_context_high->index_24h` score `11.5669` n `150` status `ready` deltaP `34.8681` edge `0.9869` maxDD `-16.1026`
- `market_context_high->equity_24h` score `10.3181` n `150` status `ready` deltaP `29.4375` edge `1.9682` maxDD `-53.663`
- `risk_on_high->crypto_alt_4h` score `7.6325` n `32` status `ready` deltaP `9.9848` edge `0.7539` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `7.6325` n `32` status `ready` deltaP `9.9848` edge `0.7539` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `3.63` n `32` status `ready` deltaP `14.4055` edge `0.4828` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `3.63` n `32` status `ready` deltaP `14.4055` edge `0.4828` maxDD `-5.7426`
- `market_context_high->crypto_major_24h` score `2.4946` n `150` status `ready` deltaP `23.8264` edge `2.2309` maxDD `-152.2601`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
