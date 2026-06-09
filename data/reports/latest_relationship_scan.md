# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-09T22:07:26.674349+00:00`
- Price records: `672`
- Market context records: `3423`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13158`

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

- `risk_on_high->crypto_alt_24h` score `56.1628` n `32` status `ready` deltaP `59.2014` edge `4.3007` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `56.1628` n `32` status `ready` deltaP `59.2014` edge `4.3007` maxDD `-0.8779`
- `risk_on_high->crypto_major_24h` score `56.0534` n `32` status `ready` deltaP `58.3333` edge `4.2865` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `56.0534` n `32` status `ready` deltaP `58.3333` edge `4.2865` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `45.6293` n `32` status `ready` deltaP `56.0764` edge `3.4286` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `45.6293` n `32` status `ready` deltaP `56.0764` edge `3.4286` maxDD `0.0`
- `risk_on_high->index_24h` score `23.9411` n `32` status `ready` deltaP `51.3889` edge `1.6525` maxDD `0.0`
- `risk_on_and_context->index_24h` score `23.9411` n `32` status `ready` deltaP `51.3889` edge `1.6525` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `22.3886` n `154` status `ready` deltaP `20.1186` edge `2.5275` maxDD `-56.6728`
- `market_context_high->crypto_major_24h` score `21.1759` n `154` status `ready` deltaP `24.4453` edge `2.3748` maxDD `-54.8486`
- `market_context_high->equity_24h` score `20.4105` n `154` status `ready` deltaP `33.3491` edge `2.1198` maxDD `-40.9667`
- `risk_on_high->crypto_major_4h` score `14.6552` n `32` status `ready` deltaP `26.2195` edge `1.1587` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `14.6552` n `32` status `ready` deltaP `26.2195` edge `1.1587` maxDD `-5.9781`
- `risk_on_high->metal_24h` score `13.353` n `32` status `ready` deltaP `28.9931` edge `0.9456` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `13.353` n `32` status `ready` deltaP `28.9931` edge `0.9456` maxDD `-0.7574`
- `market_context_high->index_24h` score `12.7484` n `154` status `ready` deltaP `36.4538` edge `1.041` maxDD `-15.0661`
- `risk_on_high->crypto_alt_4h` score `6.2908` n `32` status `ready` deltaP `6.1738` edge `0.6675` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `6.2908` n `32` status `ready` deltaP `6.1738` edge `0.6675` maxDD `-11.7537`
- `market_context_high->metal_24h` score `4.4186` n `154` status `ready` deltaP `23.8795` edge `0.8613` maxDD `-25.9879`
- `risk_on_high->equity_4h` score `4.2744` n `32` status `ready` deltaP `16.3872` edge `0.5522` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
