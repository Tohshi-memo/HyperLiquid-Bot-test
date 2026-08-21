# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-21T00:07:26.575036+00:00`
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

- `market_context_high->equity_1h` score `0.533` n `105` status `ready` deltaP `10.067` edge `0.0588` maxDD `-3.1861`
- `market_context_high->equity_4h` score `0.4797` n `105` status `ready` deltaP `6.7219` edge `0.1581` maxDD `-8.3685`
- `market_context_high->index_1h` score `0.4197` n `105` status `ready` deltaP `11.4557` edge `0.0073` maxDD `-0.5622`
- `market_context_high->fx_4h` score `-0.0098` n `105` status `ready` deltaP `6.5708` edge `0.0052` maxDD `-0.3539`
- `market_context_high->commodity_24h` score `-0.1285` n `96` status `ready` deltaP `4.6875` edge `0.1356` maxDD `-4.666`
- `market_context_high->metal_4h` score `-0.1617` n `105` status `ready` deltaP `7.5973` edge `-0.0138` maxDD `-1.273`
- `market_context_high->fx_1h` score `-0.1944` n `105` status `ready` deltaP `1.075` edge `0.0038` maxDD `-0.2043`
- `market_context_high->metal_1h` score `-0.2065` n `105` status `ready` deltaP `3.2378` edge `-0.0001` maxDD `-0.4291`
- `market_context_high->unknown_1h` score `-0.2144` n `105` status `ready` deltaP `8.6784` edge `-0.053` maxDD `-0.4843`
- `market_context_high->index_4h` score `-0.2175` n `105` status `ready` deltaP `6.6478` edge `0.0202` maxDD `-1.7252`
- `market_context_high->crypto_alt_1h` score `-0.5664` n `105` status `ready` deltaP `0.8013` edge `0.0022` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-0.717` n `105` status `ready` deltaP `1.2375` edge `-0.0157` maxDD `-2.7581`
- `market_context_high->commodity_4h` score `-0.7433` n `105` status `ready` deltaP `-2.5` edge `0.0064` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.8016` n `105` status `ready` deltaP `-6.6267` edge `-0.002` maxDD `-1.1941`
- `market_context_high->crypto_alt_4h` score `-1.6202` n `105` status `ready` deltaP `4.5863` edge `-0.0386` maxDD `-5.4926`
- `market_context_high->crypto_major_4h` score `-1.9685` n `105` status `ready` deltaP `6.6826` edge `-0.1065` maxDD `-3.1677`
- `market_context_high->index_24h` score `-3.6038` n `96` status `ready` deltaP `1.0416` edge `-0.0522` maxDD `-18.3411`
- `market_context_high->fx_24h` score `-3.869` n `96` status `ready` deltaP `-21.1805` edge `-0.0229` maxDD `-1.9981`
- `market_context_high->unknown_24h` score `-3.9253` n `96` status `ready` deltaP `14.5833` edge `-0.3737` maxDD `-1.0505`
- `market_context_high->metal_24h` score `-4.9463` n `96` status `ready` deltaP `-21.0069` edge `-0.1633` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
