# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-12T19:52:29.082890+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12779`

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

- `market_context_high->unknown_24h` score `10277.7549` n `76` status `ready` deltaP `12.8198` edge `856.3993` maxDD `-0.082`
- `risk_on_high->unknown_24h` score `8744.4409` n `36` status `ready` deltaP `15.4514` edge `728.6004` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `8744.4409` n `36` status `ready` deltaP `15.4514` edge `728.6004` maxDD `0.0`
- `news_risk_high->unknown_1h` score `383.1772` n `82` status `ready` deltaP `-5.4002` edge `32.0096` maxDD `-1.7068`
- `news_risk_high->crypto_major_24h` score `20.6596` n `69` status `ready` deltaP `45.8031` edge `1.5359` maxDD `-6.9028`
- `news_risk_high->crypto_alt_24h` score `17.1772` n `69` status `ready` deltaP `29.8837` edge `1.281` maxDD `-2.2369`
- `risk_on_high->crypto_alt_24h` score `15.239` n `36` status `ready` deltaP `36.2847` edge `1.051` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `15.239` n `36` status `ready` deltaP `36.2847` edge `1.051` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `13.638` n `76` status `ready` deltaP `29.121` edge `1.0251` maxDD `-3.9523`
- `risk_on_high->equity_24h` score `10.0129` n `36` status `ready` deltaP `42.3611` edge `0.552` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `10.0129` n `36` status `ready` deltaP `42.3611` edge `0.552` maxDD `0.0`
- `market_context_high->equity_24h` score `9.5989` n `76` status `ready` deltaP `42.3611` edge `0.5175` maxDD `0.0`
- `news_risk_high->equity_24h` score `9.3123` n `69` status `ready` deltaP `24.9698` edge `0.6903` maxDD `-3.1258`
- `news_risk_high->index_24h` score `6.6973` n `69` status `ready` deltaP `43.9009` edge `0.2831` maxDD `-0.0797`
- `news_risk_high->metal_24h` score `6.3695` n `69` status `ready` deltaP `40.2551` edge `0.3065` maxDD `-0.526`
- `risk_on_high->crypto_alt_4h` score `6.2648` n `47` status `ready` deltaP `30.0889` edge `0.3729` maxDD `-2.114`
- `risk_on_and_context->crypto_alt_4h` score `6.2648` n `47` status `ready` deltaP `30.0889` edge `0.3729` maxDD `-2.114`
- `risk_on_high->index_24h` score `5.138` n `36` status `ready` deltaP `51.3888` edge `0.0898` maxDD `-0.005`
- `risk_on_and_context->index_24h` score `5.138` n `36` status `ready` deltaP `51.3888` edge `0.0898` maxDD `-0.005`
- `market_context_high->index_24h` score `3.3063` n `76` status `ready` deltaP `35.8918` edge `0.0756` maxDD `-0.1483`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
