# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-07T01:07:50.859220+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10761`

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

- `risk_on_high->unknown_24h` score `378.8621` n `103` status `ready` deltaP `26.7361` edge `31.3936` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `378.8621` n `103` status `ready` deltaP `26.7361` edge `31.3936` maxDD `0.0`
- `market_context_high->unknown_1h` score `21.0599` n `250` status `ready` deltaP `-3.6084` edge `1.8515` maxDD `-2.4626`
- `risk_on_high->crypto_major_24h` score `19.7084` n `103` status `ready` deltaP `33.6232` edge `1.4699` maxDD `-1.4687`
- `risk_on_and_context->crypto_major_24h` score `19.7084` n `103` status `ready` deltaP `33.6232` edge `1.4699` maxDD `-1.4687`
- `risk_on_high->crypto_alt_24h` score `13.6804` n `103` status `ready` deltaP `30.0347` edge `0.9398` maxDD `0.0`
- `risk_on_and_context->crypto_alt_24h` score `13.6804` n `103` status `ready` deltaP `30.0347` edge `0.9398` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `8.7284` n `192` status `ready` deltaP `23.7847` edge `0.6263` maxDD `-2.5998`
- `market_context_high->equity_24h` score `6.6652` n `192` status `ready` deltaP `23.0903` edge `0.4015` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `6.4437` n `123` status `ready` deltaP `30.5386` edge `0.339` maxDD `-0.116`
- `risk_on_and_context->crypto_alt_4h` score `6.4437` n `123` status `ready` deltaP `30.5386` edge `0.339` maxDD `-0.116`
- `risk_on_high->equity_24h` score `5.764` n `103` status `ready` deltaP `23.0903` edge `0.3264` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `5.764` n `103` status `ready` deltaP `23.0903` edge `0.3264` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `4.4008` n `123` status `ready` deltaP `24.3902` edge `0.29` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.4008` n `123` status `ready` deltaP `24.3902` edge `0.29` maxDD `-3.8693`
- `risk_on_high->index_24h` score `2.7789` n `103` status `ready` deltaP `23.4763` edge `0.0793` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `2.7789` n `103` status `ready` deltaP `23.4763` edge `0.0793` maxDD `-0.0051`
- `market_context_high->index_24h` score `2.6221` n `192` status `ready` deltaP `21.7014` edge `0.0953` maxDD `-0.0505`
- `risk_on_high->crypto_alt_1h` score `0.8565` n `127` status `ready` deltaP `4.2317` edge `0.0784` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `0.8565` n `127` status `ready` deltaP `4.2317` edge `0.0784` maxDD `-1.1521`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
