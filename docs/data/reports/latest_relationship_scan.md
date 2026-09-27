# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-27T23:26:11.936146+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7638`

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

- `news_risk_high->unknown_24h` score `720.414` n `136` status `ready` deltaP `1.2153` edge `60.0264` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `1.5906` n `136` status `ready` deltaP `14.6446` edge `0.4301` maxDD `-29.2814`
- `news_risk_high->index_24h` score `1.4878` n `136` status `ready` deltaP `18.556` edge `0.0698` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `0.933` n `136` status `ready` deltaP `20.4657` edge `0.1268` maxDD `-6.8392`
- `news_risk_high->equity_4h` score `0.0825` n `139` status `ready` deltaP `16.3505` edge `0.0588` maxDD `-9.2079`
- `news_risk_high->index_1h` score `-0.0252` n `139` status `ready` deltaP `3.3624` edge `0.0045` maxDD `-0.3214`
- `news_risk_high->crypto_alt_1h` score `-0.0341` n `139` status `ready` deltaP `4.4727` edge `0.0584` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `-0.1682` n `139` status `ready` deltaP `3.5121` edge `0.0287` maxDD `-1.957`
- `news_risk_high->metal_1h` score `-0.7125` n `139` status `ready` deltaP `-0.1562` edge `0.0046` maxDD `-0.7016`
- `news_risk_high->equity_24h` score `-0.7283` n `136` status `ready` deltaP `12.5919` edge `0.111` maxDD `-11.1179`
- `news_risk_high->fx_4h` score `-1.0372` n `139` status `ready` deltaP `13.0308` edge `0.0015` maxDD `-3.0414`
- `news_risk_high->crypto_major_1h` score `-1.0766` n `139` status `ready` deltaP `-3.4453` edge `0.0132` maxDD `-7.2607`
- `news_risk_high->fx_1h` score `-1.0869` n `139` status `ready` deltaP `-7.4711` edge `-0.0015` maxDD `-1.0436`
- `news_risk_high->index_4h` score `-1.1222` n `139` status `ready` deltaP `-2.4883` edge `0.0084` maxDD `-1.493`
- `news_risk_high->crypto_alt_4h` score `-1.7103` n `139` status `ready` deltaP `1.7909` edge `0.1115` maxDD `-15.9436`
- `news_risk_high->metal_4h` score `-1.8624` n `139` status `ready` deltaP `-13.7293` edge `0.0022` maxDD `-3.6214`
- `news_risk_high->commodity_1h` score `-1.9064` n `139` status `ready` deltaP `-10.0698` edge `-0.0098` maxDD `-3.3986`
- `news_risk_high->crypto_major_24h` score `-2.2427` n `136` status `ready` deltaP `9.2933` edge `0.1946` maxDD `-26.1424`
- `news_risk_high->crypto_major_4h` score `-3.4373` n `139` status `ready` deltaP `-12.103` edge `-0.0885` maxDD `-13.719`
- `news_risk_high->commodity_4h` score `-3.6574` n `139` status `ready` deltaP `-9.7978` edge `0.0024` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
