# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-20T23:07:25.179066+00:00`
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

- `market_context_high->equity_4h` score `0.5669` n `105` status `ready` deltaP `7.3316` edge `0.1613` maxDD `-8.3685`
- `market_context_high->equity_1h` score `0.5354` n `105` status `ready` deltaP `10.067` edge `0.059` maxDD `-3.1861`
- `market_context_high->index_1h` score `0.4065` n `105` status `ready` deltaP `11.306` edge `0.0072` maxDD `-0.5622`
- `market_context_high->fx_4h` score `-0.0074` n `105` status `ready` deltaP `6.5708` edge `0.0055` maxDD `-0.3539`
- `market_context_high->commodity_24h` score `-0.1223` n `96` status `ready` deltaP `4.6875` edge `0.1364` maxDD `-4.666`
- `market_context_high->metal_4h` score `-0.1286` n `105` status `ready` deltaP `8.0546` edge `-0.0126` maxDD `-1.273`
- `market_context_high->fx_1h` score `-0.171` n `105` status `ready` deltaP `1.5241` edge `0.0038` maxDD `-0.2043`
- `market_context_high->metal_1h` score `-0.191` n `105` status `ready` deltaP `3.3875` edge `0.0002` maxDD `-0.4291`
- `market_context_high->index_4h` score `-0.1993` n `105` status `ready` deltaP `6.9527` edge `0.0205` maxDD `-1.7252`
- `market_context_high->unknown_1h` score `-0.3547` n `105` status `ready` deltaP `8.2293` edge `-0.0617` maxDD `-0.4843`
- `market_context_high->crypto_alt_1h` score `-0.5454` n `105` status `ready` deltaP `0.951` edge `0.0039` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-0.6827` n `105` status `ready` deltaP `1.5369` edge `-0.0133` maxDD `-2.7581`
- `market_context_high->commodity_4h` score `-0.7789` n `105` status `ready` deltaP `-3.1098` edge `0.0059` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.811` n `105` status `ready` deltaP `-6.7764` edge `-0.0022` maxDD `-1.1941`
- `market_context_high->crypto_alt_4h` score `-1.4754` n `105` status `ready` deltaP `5.196` edge `-0.0306` maxDD `-5.4926`
- `market_context_high->crypto_major_4h` score `-1.8454` n `105` status `ready` deltaP `7.2924` edge `-0.1003` maxDD `-3.1677`
- `market_context_high->index_24h` score `-3.6053` n `96` status `ready` deltaP `1.0416` edge `-0.0524` maxDD `-18.3411`
- `market_context_high->unknown_24h` score `-3.6418` n `96` status `ready` deltaP `15.2777` edge `-0.3547` maxDD `-1.0505`
- `market_context_high->fx_24h` score `-3.8582` n `96` status `ready` deltaP `-21.1805` edge `-0.022` maxDD `-1.9981`
- `market_context_high->metal_24h` score `-4.9494` n `96` status `ready` deltaP `-21.0069` edge `-0.1637` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
