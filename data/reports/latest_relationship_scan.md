# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-09T06:37:26.451817+00:00`
- Price records: `672`
- Market context records: `3357`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13077`

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

- `risk_on_high->crypto_major_24h` score `57.7218` n `32` status `ready` deltaP `61.4583` edge `4.4047` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `57.7218` n `32` status `ready` deltaP `61.4583` edge `4.4047` maxDD `-0.0083`
- `risk_on_high->crypto_alt_24h` score `54.0067` n `32` status `ready` deltaP `56.25` edge `4.1407` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `54.0067` n `32` status `ready` deltaP `56.25` edge `4.1407` maxDD `-0.8779`
- `risk_on_high->equity_24h` score `46.3197` n `32` status `ready` deltaP `56.7708` edge `3.4815` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `46.3197` n `32` status `ready` deltaP `56.7708` edge `3.4815` maxDD `0.0`
- `risk_on_high->index_24h` score `23.2034` n `32` status `ready` deltaP `50.8681` edge `1.5945` maxDD `0.0`
- `risk_on_and_context->index_24h` score `23.2034` n `32` status `ready` deltaP `50.8681` edge `1.5945` maxDD `0.0`
- `risk_on_high->metal_24h` score `15.6316` n `32` status `ready` deltaP `34.375` edge `1.0996` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `15.6316` n `32` status `ready` deltaP `34.375` edge `1.0996` maxDD `-0.7574`
- `risk_on_high->crypto_major_4h` score `15.614` n `32` status `ready` deltaP `28.9634` edge `1.2203` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `15.614` n `32` status `ready` deltaP `28.9634` edge `1.2203` maxDD `-5.9781`
- `market_context_high->index_24h` score `12.276` n `165` status `ready` deltaP `36.3226` edge `1.0363` maxDD `-16.1026`
- `market_context_high->crypto_alt_24h` score `12.1466` n `165` status `ready` deltaP `16.9508` edge `2.4284` maxDD `-70.3986`
- `market_context_high->equity_24h` score `10.8778` n `165` status `ready` deltaP `31.9223` edge `2.0234` maxDD `-53.663`
- `risk_on_high->crypto_alt_4h` score `7.516` n `32` status `ready` deltaP `8.9177` edge `0.7513` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `7.516` n `32` status `ready` deltaP `8.9177` edge `0.7513` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `3.6216` n `32` status `ready` deltaP `14.5579` edge `0.4807` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `3.6216` n `32` status `ready` deltaP `14.5579` edge `0.4807` maxDD `-5.7426`
- `risk_on_high->crypto_major_1h` score `1.9684` n `32` status `ready` deltaP `5.9693` edge `0.3195` maxDD `-5.8885`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
