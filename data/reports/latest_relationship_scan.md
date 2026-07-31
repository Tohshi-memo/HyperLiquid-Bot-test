# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-31T20:22:32.075294+00:00`
- Price records: `672`
- Market context records: `8548`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5925`

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

- `news_risk_high->unknown_24h` score `5436.304` n `58` status `ready` deltaP `42.0617` edge `452.787` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `5.5407` n `64` status `ready` deltaP `19.8933` edge `0.3888` maxDD `-3.4427`
- `market_context_high->crypto_alt_4h` score `1.9138` n `62` status `ready` deltaP `13.513` edge `0.1651` maxDD `-5.323`
- `news_risk_high->index_4h` score `1.8989` n `64` status `ready` deltaP `15.4345` edge `0.0744` maxDD `-0.191`
- `news_risk_high->equity_1h` score `1.6846` n `64` status `ready` deltaP `15.9525` edge `0.0817` maxDD `-2.4803`
- `news_risk_high->crypto_major_4h` score `0.9825` n `64` status `ready` deltaP `6.2881` edge `0.1616` maxDD `-3.5385`
- `news_risk_high->crypto_alt_4h` score `0.653` n `64` status `ready` deltaP `13.1098` edge `0.1355` maxDD `-5.8012`
- `news_risk_high->crypto_alt_1h` score `0.4905` n `64` status `ready` deltaP `8.561` edge `0.0585` maxDD `-1.8813`
- `news_risk_high->crypto_major_1h` score `0.3735` n `64` status `ready` deltaP `7.064` edge `0.052` maxDD `-2.0972`
- `news_risk_high->fx_1h` score `0.0698` n `64` status `ready` deltaP `4.9869` edge `0.0038` maxDD `-0.2475`
- `news_risk_high->index_1h` score `-0.0034` n `64` status `ready` deltaP `3.4712` edge `0.0081` maxDD `-0.5338`
- `news_risk_high->metal_4h` score `-0.0475` n `64` status `ready` deltaP `1.5625` edge `0.0311` maxDD `-0.8085`
- `news_risk_high->fx_4h` score `-0.0963` n `64` status `ready` deltaP `10.0991` edge `0.0204` maxDD `-0.6604`
- `news_risk_high->metal_1h` score `-0.1742` n `64` status `ready` deltaP `2.8069` edge `0.0071` maxDD `-0.5599`
- `market_context_high->fx_4h` score `-0.2646` n `62` status `ready` deltaP `6.9237` edge `0.0114` maxDD `-1.3685`
- `market_context_high->commodity_1h` score `-0.2873` n `62` status `ready` deltaP `4.1578` edge `-0.002` maxDD `-2.0038`
- `market_context_high->fx_1h` score `-0.2949` n `62` status `ready` deltaP `1.9123` edge `-0.0003` maxDD `-0.6874`
- `market_context_high->crypto_alt_1h` score `-0.4862` n `62` status `ready` deltaP `-2.4773` edge `0.0169` maxDD `-3.0178`
- `market_context_high->index_1h` score `-0.7884` n `62` status `ready` deltaP `0.4974` edge `-0.0161` maxDD `-1.5667`
- `market_context_high->commodity_4h` score `-0.9503` n `62` status `ready` deltaP `2.0604` edge `0.0159` maxDD `-5.4508`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
