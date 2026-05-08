# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-08T02:07:16.574935+00:00`
- Price records: `604`
- Market context records: `708`
- Flow alert records: `2000`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `901`

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

- `market_context_high->crypto_major_24h` score `10.9655` n `146` status `ready` deltaP `26.6233` edge `0.7697` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.5123` n `146` status `ready` deltaP `8.1734` edge `0.493` maxDD `-0.0508`
- `market_context_high->fx_4h` score `-0.2355` n `149` status `ready` deltaP `6.8619` edge `0.0112` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.2862` n `149` status `ready` deltaP `2.8523` edge `0.0021` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.4568` n `149` status `ready` deltaP `2.5168` edge `0.0426` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.6375` n `149` status `ready` deltaP `0.1678` edge `0.0025` maxDD `-2.8282`
- `market_context_high->index_24h` score `-0.9986` n `146` status `ready` deltaP `-2.6854` edge `0.1342` maxDD `-5.9609`
- `market_context_high->crypto_major_4h` score `-1.1212` n `149` status `ready` deltaP `16.3882` edge `0.1176` maxDD `-22.648`
- `market_context_high->unknown_1h` score `-1.1747` n `149` status `ready` deltaP `-4.1779` edge `-0.0097` maxDD `-2.1602`
- `market_context_high->equity_1h` score `-1.1992` n `149` status `ready` deltaP `-1.8457` edge `-0.0066` maxDD `-4.4826`
- `market_context_high->crypto_alt_1h` score `-1.3461` n `149` status `ready` deltaP `4.7539` edge `-0.0124` maxDD `-8.1842`
- `market_context_high->crypto_major_1h` score `-1.5926` n `149` status `ready` deltaP `6.2226` edge `-0.0019` maxDD `-11.4508`
- `market_context_high->index_4h` score `-1.7217` n `149` status `ready` deltaP `2.1146` edge `-0.0053` maxDD `-6.5149`
- `market_context_high->crypto_alt_4h` score `-1.9942` n `149` status `ready` deltaP `3.794` edge `0.0655` maxDD `-15.2248`
- `market_context_high->equity_24h` score `-2.0815` n `146` status `ready` deltaP `-4.6178` edge `0.1178` maxDD `-10.5047`
- `market_context_high->equity_4h` score `-2.6359` n `149` status `ready` deltaP `-0.9676` edge `0.002` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.4045` n `149` status `ready` deltaP `-5.3221` edge `-0.0523` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.7937` n `149` status `ready` deltaP `-6.3816` edge `0.0765` maxDD `-13.0076`
- `market_context_high->unknown_4h` score `-4.2428` n `149` status `ready` deltaP `3.2324` edge `-0.1873` maxDD `-8.3588`
- `market_context_high->fx_24h` score `-5.0574` n `146` status `ready` deltaP `-12.1059` edge `-0.0505` maxDD `-21.0414`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
