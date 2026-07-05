# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-05T21:52:30.530865+00:00`
- Price records: `672`
- Market context records: `5816`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10006`

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

- `market_context_high->equity_4h` score `0.2564` n `286` status `ready` deltaP `6.1125` edge `0.1264` maxDD `-6.9958`
- `market_context_high->equity_24h` score `0.0065` n `248` status `ready` deltaP `15.3954` edge `0.4058` maxDD `-31.6316`
- `market_context_high->fx_1h` score `-0.191` n `286` status `ready` deltaP `3.3971` edge `0.0014` maxDD `-0.5499`
- `market_context_high->commodity_1h` score `-0.566` n `286` status `ready` deltaP `-1.3505` edge `-0.0025` maxDD `-2.2187`
- `market_context_high->metal_1h` score `-0.6227` n `286` status `ready` deltaP `2.2497` edge `0.0002` maxDD `-2.0339`
- `market_context_high->index_1h` score `-0.6554` n `286` status `ready` deltaP `0.0021` edge `0.0028` maxDD `-0.9472`
- `market_context_high->equity_1h` score `-0.7055` n `286` status `ready` deltaP `2.3555` edge `0.0262` maxDD `-5.0555`
- `market_context_high->crypto_major_1h` score `-0.8709` n `286` status `ready` deltaP `3.1992` edge `0.0382` maxDD `-6.2348`
- `market_context_high->crypto_alt_1h` score `-1.0477` n `286` status `ready` deltaP `1.7012` edge `0.0348` maxDD `-6.6758`
- `market_context_high->index_4h` score `-1.2257` n `286` status `ready` deltaP `0.0437` edge `0.0113` maxDD `-3.165`
- `market_context_high->fx_4h` score `-1.4506` n `286` status `ready` deltaP `0.7708` edge `0.0038` maxDD `-2.2593`
- `market_context_high->fx_24h` score `-1.4746` n `248` status `ready` deltaP `9.4422` edge `0.0298` maxDD `-5.5435`
- `market_context_high->metal_4h` score `-2.1424` n `286` status `ready` deltaP `-3.9548` edge `-0.0424` maxDD `-9.1388`
- `market_context_high->crypto_major_4h` score `-2.6946` n `286` status `ready` deltaP `8.0228` edge `0.1592` maxDD `-25.6458`
- `market_context_high->commodity_4h` score `-2.7175` n `286` status `ready` deltaP `-1.4327` edge `-0.0171` maxDD `-8.6511`
- `market_context_high->index_24h` score `-2.8159` n `248` status `ready` deltaP `3.7131` edge `0.0287` maxDD `-18.1572`
- `market_context_high->crypto_alt_4h` score `-4.4205` n `286` status `ready` deltaP `5.4857` edge `0.0959` maxDD `-28.7346`
- `market_context_high->commodity_24h` score `-5.8661` n `248` status `ready` deltaP `-12.4608` edge `-0.0629` maxDD `-31.1542`
- `market_context_high->metal_24h` score `-8.0103` n `248` status `ready` deltaP `-3.6178` edge `-0.2318` maxDD `-18.2616`
- `market_context_high->crypto_major_24h` score `-12.1977` n `248` status `ready` deltaP `-3.3714` edge `-0.2952` maxDD `-36.5708`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
