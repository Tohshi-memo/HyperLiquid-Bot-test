# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-10T09:37:18.615647+00:00`
- Price records: `672`
- Market context records: `962`
- Flow alert records: `2695`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `1440`

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

- `market_context_high->crypto_major_24h` score `14.9296` n `154` status `ready` deltaP `33.5588` edge `1.0538` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `9.1312` n `154` status `ready` deltaP `10.0694` edge `0.6938` maxDD `0.0`
- `market_context_high->equity_24h` score `1.2414` n `154` status `ready` deltaP `1.6234` edge `0.3531` maxDD `-10.5047`
- `market_context_high->index_24h` score `0.5045` n `154` status `ready` deltaP `0.1127` edge `0.2408` maxDD `-5.9609`
- `market_context_high->fx_1h` score `-0.3565` n `204` status `ready` deltaP `1.6908` edge `0.0011` maxDD `-0.3124`
- `market_context_high->commodity_1h` score `-0.3882` n `204` status `ready` deltaP `1.6995` edge `0.0371` maxDD `-3.7959`
- `market_context_high->equity_1h` score `-0.5456` n `204` status `ready` deltaP `2.1604` edge `0.017` maxDD `-4.4826`
- `market_context_high->fx_4h` score `-0.6724` n `192` status `ready` deltaP `1.7149` edge `0.002` maxDD `-1.6381`
- `market_context_high->index_1h` score `-0.6947` n `204` status `ready` deltaP `3.2347` edge `0.0059` maxDD `-2.8282`
- `market_context_high->equity_4h` score `-1.2339` n `192` status `ready` deltaP `2.6677` edge `0.0946` maxDD `-10.5498`
- `market_context_high->unknown_1h` score `-1.3177` n `204` status `ready` deltaP `-2.6007` edge `-0.0153` maxDD `-3.5069`
- `market_context_high->index_4h` score `-1.5366` n `192` status `ready` deltaP `-0.4319` edge `0.0271` maxDD `-6.5149`
- `market_context_high->crypto_major_1h` score `-1.599` n `204` status `ready` deltaP `6.4283` edge `-0.0038` maxDD `-11.4508`
- `market_context_high->crypto_alt_1h` score `-1.8019` n `204` status `ready` deltaP `2.2514` edge `-0.0212` maxDD `-8.1842`
- `market_context_high->metal_1h` score `-1.8954` n `204` status `ready` deltaP `-2.5155` edge `-0.0303` maxDD `-9.0076`
- `market_context_high->crypto_major_4h` score `-2.4701` n `192` status `ready` deltaP `8.9939` edge `0.1048` maxDD `-22.648`
- `market_context_high->commodity_4h` score `-2.5423` n `192` status `ready` deltaP `-0.7749` edge `0.0809` maxDD `-13.0076`
- `market_context_high->crypto_alt_4h` score `-3.2724` n `192` status `ready` deltaP `-2.2485` edge `0.0201` maxDD `-15.2248`
- `market_context_high->unknown_4h` score `-3.3137` n `192` status `ready` deltaP `6.6565` edge `-0.1327` maxDD `-8.3588`
- `market_context_high->unknown_24h` score `-4.08` n `154` status `ready` deltaP `6.1057` edge `-0.0132` maxDD `-33.7129`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
