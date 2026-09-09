# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-09T22:07:26.399484+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10242`

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

- `risk_on_high->crypto_alt_24h` score `12.5661` n `117` status `ready` deltaP `26.1084` edge `0.8961` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `12.5661` n `117` status `ready` deltaP `26.1084` edge `0.8961` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `7.5186` n `241` status `ready` deltaP `18.7636` edge `0.5842` maxDD `-3.9523`
- `risk_on_high->crypto_major_24h` score `6.7682` n `117` status `ready` deltaP `21.7949` edge `1.1292` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `6.7682` n `117` status `ready` deltaP `21.7949` edge `1.1292` maxDD `-24.5429`
- `risk_on_high->crypto_alt_4h` score `6.3493` n `117` status `ready` deltaP `34.7509` edge `0.3346` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `6.3493` n `117` status `ready` deltaP `34.7509` edge `0.3346` maxDD `-1.9733`
- `risk_on_high->crypto_major_4h` score `4.4331` n `117` status `ready` deltaP `24.914` edge `0.2892` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.4331` n `117` status `ready` deltaP `24.914` edge `0.2892` maxDD `-3.8693`
- `risk_on_high->index_24h` score `2.6396` n `117` status `ready` deltaP `26.429` edge `0.048` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `2.6396` n `117` status `ready` deltaP `26.429` edge `0.048` maxDD `-0.0051`
- `market_context_high->index_24h` score `1.9181` n `241` status `ready` deltaP `21.5242` edge `0.0557` maxDD `-0.1483`
- `market_context_high->equity_24h` score `1.7229` n `241` status `ready` deltaP `9.8958` edge `0.0776` maxDD `0.0`
- `risk_on_high->crypto_alt_1h` score `1.0881` n `117` status `ready` deltaP `4.2467` edge `0.0976` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `1.0881` n `117` status `ready` deltaP `4.2467` edge `0.0976` maxDD `-1.1521`
- `risk_on_high->equity_24h` score `1.0377` n `117` status `ready` deltaP `9.8958` edge `0.0205` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `1.0377` n `117` status `ready` deltaP `9.8958` edge `0.0205` maxDD `0.0`
- `risk_on_high->metal_24h` score `0.7933` n `117` status `ready` deltaP `19.7383` edge `0.0857` maxDD `-0.9131`
- `risk_on_and_context->metal_24h` score `0.7933` n `117` status `ready` deltaP `19.7383` edge `0.0857` maxDD `-0.9131`
- `risk_on_high->equity_1h` score `0.4604` n `117` status `ready` deltaP `14.5223` edge `-0.0053` maxDD `-2.2516`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
