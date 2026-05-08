# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-08T09:22:20.061558+00:00`
- Price records: `633`
- Market context records: `740`
- Flow alert records: `2090`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `1117`

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

- `market_context_high->crypto_major_24h` score `12.6462` n `146` status `ready` deltaP `30.1421` edge `0.8863` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.5892` n `146` status `ready` deltaP `7.695` edge `0.5026` maxDD `-0.0508`
- `market_context_high->index_24h` score `0.1158` n `146` status `ready` deltaP `1.3737` edge `0.2` maxDD `-5.9609`
- `market_context_high->fx_4h` score `-0.2861` n `155` status `ready` deltaP `6.1737` edge `0.0093` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.3745` n `159` status `ready` deltaP `3.5995` edge `0.0026` maxDD `-0.291`
- `market_context_high->equity_24h` score `-0.5827` n `146` status `ready` deltaP `-0.2673` edge `0.2137` maxDD `-10.5047`
- `market_context_high->commodity_1h` score `-0.637` n `159` status `ready` deltaP `1.0898` edge `0.0371` maxDD `-3.7959`
- `market_context_high->equity_1h` score `-0.6448` n `159` status `ready` deltaP `-0.4558` edge `0.0014` maxDD `-4.4826`
- `market_context_high->index_1h` score `-0.8495` n `159` status `ready` deltaP `1.4642` edge `0.0048` maxDD `-2.8282`
- `market_context_high->crypto_major_1h` score `-1.0686` n `159` status `ready` deltaP `5.7153` edge `-0.0028` maxDD `-11.4508`
- `market_context_high->crypto_alt_1h` score `-1.4409` n `159` status `ready` deltaP `4.2286` edge `-0.0168` maxDD `-8.1842`
- `market_context_high->unknown_1h` score `-1.5362` n `159` status `ready` deltaP `-4.5065` edge `-0.0208` maxDD `-3.5069`
- `market_context_high->crypto_major_4h` score `-1.5543` n `155` status `ready` deltaP `17.4863` edge `0.1245` maxDD `-22.648`
- `market_context_high->index_4h` score `-1.7678` n `155` status `ready` deltaP `1.7029` edge `-0.0064` maxDD `-6.5149`
- `market_context_high->crypto_alt_4h` score `-2.1658` n `155` status `ready` deltaP `2.4134` edge `0.0604` maxDD `-15.2248`
- `market_context_high->equity_4h` score `-2.5816` n `155` status `ready` deltaP `-1.2335` edge `0.0083` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.0849` n `159` status `ready` deltaP `-3.4566` edge `-0.0381` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.7103` n `155` status `ready` deltaP `-5.7739` edge `0.0794` maxDD `-13.0076`
- `market_context_high->unknown_4h` score `-3.7705` n `155` status `ready` deltaP `5.041` edge `-0.16` maxDD `-8.3588`
- `market_context_high->fx_24h` score `-5.3566` n `146` status `ready` deltaP `-15.323` edge `-0.0674` maxDD `-21.0414`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
