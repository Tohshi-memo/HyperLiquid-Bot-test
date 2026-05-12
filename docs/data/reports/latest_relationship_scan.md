# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-12T03:07:23.507617+00:00`
- Price records: `672`
- Market context records: `988`
- Flow alert records: `3212`
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

- `market_context_high->crypto_major_24h` score `13.117` n `210` status `ready` deltaP `31.3016` edge `0.9178` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `5.4811` n `210` status `ready` deltaP `10.6287` edge `0.3859` maxDD `0.0`
- `market_context_high->fx_1h` score `-0.3655` n `211` status `ready` deltaP `1.7721` edge `-0.0006` maxDD `-0.3124`
- `market_context_high->commodity_1h` score `-0.4335` n `211` status `ready` deltaP `3.1431` edge `0.0237` maxDD `-3.7959`
- `market_context_high->equity_1h` score `-0.7082` n `211` status `ready` deltaP `0.9528` edge `0.0115` maxDD `-4.4826`
- `market_context_high->index_24h` score `-0.7244` n `210` status `ready` deltaP `2.7816` edge `0.1206` maxDD `-5.9609`
- `market_context_high->fx_4h` score `-0.7314` n `210` status `ready` deltaP `0.7756` edge `0.0007` maxDD `-1.6381`
- `market_context_high->index_1h` score `-0.8191` n `211` status `ready` deltaP `2.294` edge `0.0018` maxDD `-2.8282`
- `market_context_high->unknown_1h` score `-1.1927` n `211` status `ready` deltaP `-1.0835` edge `-0.015` maxDD `-3.5069`
- `market_context_high->crypto_major_1h` score `-1.2497` n `211` status `ready` deltaP `4.738` edge `-0.0195` maxDD `-11.4508`
- `market_context_high->equity_24h` score `-1.2558` n `210` status `ready` deltaP `4.2643` edge `0.1274` maxDD `-10.5047`
- `market_context_high->equity_4h` score `-1.5681` n `210` status `ready` deltaP `1.4899` edge `0.0746` maxDD `-10.5498`
- `market_context_high->index_4h` score `-1.7966` n `210` status `ready` deltaP `-2.0473` edge `0.0162` maxDD `-6.5149`
- `market_context_high->metal_1h` score `-1.9856` n `211` status `ready` deltaP `-1.6556` edge `-0.0476` maxDD `-9.0076`
- `market_context_high->crypto_alt_1h` score `-2.2205` n `211` status `ready` deltaP `-0.7762` edge `-0.0359` maxDD `-8.1842`
- `market_context_high->crypto_major_4h` score `-2.9608` n `210` status `ready` deltaP `7.0602` edge `0.0768` maxDD `-22.648`
- `market_context_high->unknown_4h` score `-3.2026` n `210` status `ready` deltaP `7.7003` edge `-0.1304` maxDD `-8.3588`
- `market_context_high->commodity_4h` score `-3.2917` n `210` status `ready` deltaP `-2.2569` edge `0.0575` maxDD `-13.0076`
- `market_context_high->crypto_alt_4h` score `-3.487` n `210` status `ready` deltaP `-2.4266` edge `0.0034` maxDD `-15.2248`
- `market_context_high->fx_24h` score `-3.5767` n `210` status `ready` deltaP `-1.2931` edge `-0.022` maxDD `-20.2343`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
