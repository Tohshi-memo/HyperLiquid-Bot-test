# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-19T10:07:31.681525+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11762`

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

- `market_context_high->crypto_major_24h` score `2.1675` n `96` status `ready` deltaP `7.2916` edge `0.2528` maxDD `-4.9964`
- `market_context_high->equity_4h` score `1.7605` n `96` status `ready` deltaP `10.2388` edge `0.1673` maxDD `-2.4411`
- `market_context_high->equity_1h` score `1.6965` n `96` status `ready` deltaP `14.4025` edge `0.0755` maxDD `-0.4112`
- `market_context_high->metal_4h` score `1.3564` n `96` status `ready` deltaP `19.1565` edge `0.0429` maxDD `-1.273`
- `market_context_high->crypto_major_4h` score `1.1331` n `96` status `ready` deltaP `11.7632` edge `0.1181` maxDD `-3.1677`
- `market_context_high->commodity_24h` score `0.9634` n `96` status `ready` deltaP `12.5` edge `0.2235` maxDD `-4.666`
- `market_context_high->index_1h` score `0.9402` n `96` status `ready` deltaP `16.0616` edge `0.01` maxDD `-0.0982`
- `market_context_high->unknown_1h` score `0.218` n `96` status `ready` deltaP `8.3084` edge `-0.0145` maxDD `-0.4843`
- `market_context_high->crypto_alt_4h` score `0.2084` n `96` status `ready` deltaP `9.9085` edge `0.0783` maxDD `-5.4926`
- `market_context_high->metal_1h` score `0.2003` n `96` status `ready` deltaP `6.4184` edge `0.0126` maxDD `-0.4291`
- `market_context_high->index_4h` score `0.0863` n `96` status `ready` deltaP `7.6473` edge `0.0217` maxDD `-0.5728`
- `market_context_high->fx_4h` score `0.0779` n `96` status `ready` deltaP `8.2571` edge `0.0052` maxDD `-0.3539`
- `market_context_high->unknown_24h` score `0.0368` n `96` status `ready` deltaP `16.3194` edge `-0.0551` maxDD `-1.0505`
- `market_context_high->fx_1h` score `-0.3432` n `96` status `ready` deltaP `-1.6218` edge `0.0027` maxDD `-0.2043`
- `market_context_high->crypto_major_1h` score `-0.3573` n `96` status `ready` deltaP `3.1312` edge `0.0178` maxDD `-2.7581`
- `market_context_high->crypto_alt_1h` score `-0.4392` n `96` status `ready` deltaP `1.7777` edge `0.012` maxDD `-2.413`
- `market_context_high->commodity_4h` score `-0.5386` n `96` status `ready` deltaP `1.3466` edge `0.007` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.911` n `96` status `ready` deltaP `-8.0402` edge `-0.0066` maxDD `-1.1941`
- `market_context_high->metal_24h` score `-2.2058` n `96` status `ready` deltaP `-3.6458` edge `0.0723` maxDD `-11.4635`
- `market_context_high->fx_24h` score `-4.0845` n `96` status `ready` deltaP `-23.7847` edge `-0.0235` maxDD `-1.9981`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
