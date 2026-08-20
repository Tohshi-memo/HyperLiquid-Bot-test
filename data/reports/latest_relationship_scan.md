# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-20T21:22:29.870825+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `104`

- Symbol pattern count: `12819`

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

- `market_context_high->equity_4h` score `0.7518` n `105` status `ready` deltaP `8.3987` edge `0.1696` maxDD `-8.3685`
- `market_context_high->equity_1h` score `0.5091` n `105` status `ready` deltaP `9.7676` edge `0.0588` maxDD `-3.1861`
- `market_context_high->index_1h` score `0.3694` n `105` status `ready` deltaP `10.8569` edge `0.0071` maxDD `-0.5622`
- `market_context_high->fx_4h` score `-0.0059` n `105` status `ready` deltaP `6.5708` edge `0.0057` maxDD `-0.3539`
- `market_context_high->metal_4h` score `-0.0512` n `105` status `ready` deltaP `9.1217` edge `-0.0098` maxDD `-1.273`
- `market_context_high->commodity_24h` score `-0.109` n `96` status `ready` deltaP `4.6875` edge `0.1381` maxDD `-4.666`
- `market_context_high->index_4h` score `-0.1534` n `105` status `ready` deltaP `7.7149` edge `0.0213` maxDD `-1.7252`
- `market_context_high->metal_1h` score `-0.1766` n `105` status `ready` deltaP `3.5372` edge `0.0004` maxDD `-0.4291`
- `market_context_high->fx_1h` score `-0.1866` n `105` status `ready` deltaP `1.2247` edge `0.0038` maxDD `-0.2043`
- `market_context_high->unknown_1h` score `-0.4182` n `105` status `ready` deltaP `7.7802` edge `-0.064` maxDD `-0.4843`
- `market_context_high->crypto_alt_1h` score `-0.5072` n `105` status `ready` deltaP `1.4001` edge `0.0058` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-0.689` n `105` status `ready` deltaP `1.3872` edge `-0.0131` maxDD `-2.7581`
- `market_context_high->commodity_4h` score `-0.7805` n `105` status `ready` deltaP `-3.1098` edge `0.0057` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.811` n `105` status `ready` deltaP `-6.7764` edge `-0.0022` maxDD `-1.1941`
- `market_context_high->crypto_alt_4h` score `-1.4372` n `105` status `ready` deltaP `5.0436` edge `-0.0264` maxDD `-5.4926`
- `market_context_high->crypto_major_4h` score `-1.8792` n `105` status `ready` deltaP `7.1399` edge `-0.1021` maxDD `-3.1677`
- `market_context_high->unknown_24h` score `-3.1473` n `96` status `ready` deltaP `16.493` edge `-0.3216` maxDD `-1.0505`
- `market_context_high->index_24h` score `-3.6092` n `96` status `ready` deltaP `1.0416` edge `-0.0529` maxDD `-18.3411`
- `market_context_high->fx_24h` score `-3.8414` n `96` status `ready` deltaP `-21.1805` edge `-0.0206` maxDD `-1.9981`
- `market_context_high->metal_24h` score `-4.9619` n `96` status `ready` deltaP `-21.0069` edge `-0.1653` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
