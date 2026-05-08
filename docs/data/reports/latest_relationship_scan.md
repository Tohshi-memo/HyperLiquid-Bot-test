# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-08T02:52:16.170325+00:00`
- Price records: `607`
- Market context records: `711`
- Flow alert records: `2009`
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

- `market_context_high->crypto_major_24h` score `11.1269` n `146` status `ready` deltaP `27.0058` edge `0.7806` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.4733` n `146` status `ready` deltaP `8.1214` edge `0.4901` maxDD `-0.0508`
- `market_context_high->fx_4h` score `-0.2533` n `149` status `ready` deltaP `6.6108` edge `0.0106` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.2987` n `149` status `ready` deltaP `2.6263` edge `0.002` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.4637` n `149` status `ready` deltaP `2.4157` edge `0.0427` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.6195` n `149` status `ready` deltaP `0.4695` edge `0.0028` maxDD `-2.8282`
- `market_context_high->index_24h` score `-0.878` n `146` status `ready` deltaP `-2.2439` edge `0.1413` maxDD `-5.9609`
- `market_context_high->crypto_major_4h` score `-1.0945` n `149` status `ready` deltaP `16.6627` edge `0.1192` maxDD `-22.648`
- `market_context_high->unknown_1h` score `-1.1622` n `149` status `ready` deltaP `-4.0825` edge `-0.0093` maxDD `-2.1602`
- `market_context_high->equity_1h` score `-1.1626` n `149` status `ready` deltaP `-1.5373` edge `-0.0056` maxDD `-4.4826`
- `market_context_high->crypto_alt_1h` score `-1.3242` n `149` status `ready` deltaP `4.8782` edge `-0.0114` maxDD `-8.1842`
- `market_context_high->crypto_major_1h` score `-1.561` n `149` status `ready` deltaP `6.4822` edge `-0.001` maxDD `-11.4508`
- `market_context_high->index_4h` score `-1.7566` n `149` status `ready` deltaP `1.9185` edge `-0.0069` maxDD `-6.5149`
- `market_context_high->equity_24h` score `-1.9177` n `146` status `ready` deltaP `-4.1447` edge `0.1283` maxDD `-10.5047`
- `market_context_high->crypto_alt_4h` score `-1.9819` n `149` status `ready` deltaP `3.7974` edge `0.0665` maxDD `-15.2248`
- `market_context_high->equity_4h` score `-2.6911` n `149` status `ready` deltaP `-1.1479` edge `-0.0014` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.3746` n `149` status `ready` deltaP `-5.0385` edge `-0.0517` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.7573` n `149` status `ready` deltaP `-6.1671` edge `0.0781` maxDD `-13.0076`
- `market_context_high->unknown_4h` score `-4.2191` n `149` status `ready` deltaP `3.3636` edge `-0.1862` maxDD `-8.3588`
- `market_context_high->fx_24h` score `-5.0881` n `146` status `ready` deltaP `-12.4558` edge `-0.0521` maxDD `-21.0414`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
