# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-09T04:52:24.495474+00:00`
- Price records: `672`
- Market context records: `3350`
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

- `risk_on_high->crypto_major_24h` score `58.6398` n `32` status `ready` deltaP `62.6736` edge `4.4731` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `58.6398` n `32` status `ready` deltaP `62.6736` edge `4.4731` maxDD `-0.0083`
- `risk_on_high->crypto_alt_24h` score `54.5407` n `32` status `ready` deltaP `57.4653` edge `4.1771` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `54.5407` n `32` status `ready` deltaP `57.4653` edge `4.1771` maxDD `-0.8779`
- `risk_on_high->equity_24h` score `46.6353` n `32` status `ready` deltaP `56.7708` edge `3.5078` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `46.6353` n `32` status `ready` deltaP `56.7708` edge `3.5078` maxDD `0.0`
- `risk_on_high->index_24h` score `23.2346` n `32` status `ready` deltaP `50.8681` edge `1.5971` maxDD `0.0`
- `risk_on_and_context->index_24h` score `23.2346` n `32` status `ready` deltaP `50.8681` edge `1.5971` maxDD `0.0`
- `risk_on_high->metal_24h` score `16.0264` n `32` status `ready` deltaP `35.5903` edge `1.1244` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `16.0264` n `32` status `ready` deltaP `35.5903` edge `1.1244` maxDD `-0.7574`
- `risk_on_high->crypto_major_4h` score `15.9669` n `32` status `ready` deltaP `30.0305` edge `1.2426` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `15.9669` n `32` status `ready` deltaP `30.0305` edge `1.2426` maxDD `-5.9781`
- `market_context_high->crypto_alt_24h` score `12.4292` n `163` status `ready` deltaP `17.6455` edge `2.46` maxDD `-70.3986`
- `market_context_high->index_24h` score `12.1873` n `163` status `ready` deltaP `36.1442` edge `1.0301` maxDD `-16.1026`
- `market_context_high->equity_24h` score `10.8986` n `163` status `ready` deltaP `31.6174` edge `2.0281` maxDD `-53.663`
- `risk_on_high->crypto_alt_4h` score `7.8219` n `32` status `ready` deltaP `9.8323` edge `0.7707` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `7.8219` n `32` status `ready` deltaP `9.8323` edge `0.7707` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `3.7122` n `32` status `ready` deltaP `14.7104` edge `0.4913` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `3.7122` n `32` status `ready` deltaP `14.7104` edge `0.4913` maxDD `-5.7426`
- `risk_on_high->crypto_major_1h` score `2.072` n `32` status `ready` deltaP `6.7178` edge `0.3278` maxDD `-5.8885`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
