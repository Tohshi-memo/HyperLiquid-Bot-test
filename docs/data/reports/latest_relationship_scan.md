# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-08T11:39:28.266726+00:00`
- Price records: `672`
- Market context records: `6083`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11147`

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

- `news_risk_high->fx_24h` score `8.1606` n `30` status `ready` deltaP `72.7431` edge `0.1951` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `5.3285` n `30` status `ready` deltaP `31.5277` edge `0.2486` maxDD `-0.5131`
- `news_risk_high->fx_4h` score `4.3163` n `32` status `ready` deltaP `44.8933` edge `0.065` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.4326` n `32` status `ready` deltaP `29.1916` edge `0.022` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.9553` n `203` status `ready` deltaP `10.1338` edge `0.1871` maxDD `-2.671`
- `news_risk_high->crypto_major_1h` score `1.1256` n `32` status `ready` deltaP `13.0801` edge `0.1038` maxDD `-2.0691`
- `news_risk_high->commodity_24h` score `0.7026` n `30` status `ready` deltaP `18.9584` edge `-0.0473` maxDD `-0.3101`
- `news_risk_high->crypto_alt_1h` score `0.6135` n `32` status `ready` deltaP `8.7762` edge `0.0663` maxDD `-1.6923`
- `news_risk_high->index_24h` score `0.1008` n `30` status `ready` deltaP `9.2361` edge `0.0385` maxDD `-2.3058`
- `market_context_high->metal_1h` score `-0.2987` n `203` status `ready` deltaP `4.5109` edge `0.0115` maxDD `-2.0564`
- `market_context_high->fx_1h` score `-0.4617` n `203` status `ready` deltaP `0.9896` edge `-0.0005` maxDD `-0.5659`
- `market_context_high->equity_1h` score `-0.4905` n `203` status `ready` deltaP `2.3038` edge `0.0333` maxDD `-4.2573`
- `market_context_high->metal_4h` score `-0.6213` n `203` status `ready` deltaP `5.291` edge `0.0317` maxDD `-3.4996`
- `news_risk_high->metal_1h` score `-0.7139` n `32` status `ready` deltaP `-1.6467` edge `-0.0308` maxDD `-1.6464`
- `market_context_high->crypto_alt_1h` score `-0.7276` n `203` status `ready` deltaP `5.0662` edge `0.0482` maxDD `-9.3536`
- `market_context_high->commodity_1h` score `-0.7447` n `203` status `ready` deltaP `-1.893` edge `-0.0048` maxDD `-0.5708`
- `market_context_high->index_4h` score `-0.7675` n `203` status `ready` deltaP `3.0735` edge `0.0281` maxDD `-1.4259`
- `market_context_high->crypto_major_1h` score `-0.7762` n `203` status `ready` deltaP `5.0906` edge `0.0433` maxDD `-9.807`
- `news_risk_high->index_1h` score `-0.9769` n `32` status `ready` deltaP `-7.878` edge `-0.0164` maxDD `-1.1725`
- `market_context_high->index_1h` score `-1.1409` n `203` status `ready` deltaP `-1.705` edge `0.0046` maxDD `-1.0646`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
