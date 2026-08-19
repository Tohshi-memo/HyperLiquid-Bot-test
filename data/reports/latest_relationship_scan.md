# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-19T10:52:30.276542+00:00`
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

- `market_context_high->crypto_major_24h` score `2.0874` n `96` status `ready` deltaP `6.7708` edge `0.2496` maxDD `-4.9964`
- `market_context_high->equity_4h` score `1.7761` n `96` status `ready` deltaP `10.2388` edge `0.1686` maxDD `-2.4411`
- `market_context_high->equity_1h` score `1.7085` n `96` status `ready` deltaP `14.4025` edge `0.0765` maxDD `-0.4112`
- `market_context_high->metal_4h` score `1.3394` n `96` status `ready` deltaP `19.004` edge `0.0425` maxDD `-1.273`
- `market_context_high->crypto_major_4h` score `1.0557` n `96` status `ready` deltaP `11.3059` edge `0.1147` maxDD `-3.1677`
- `market_context_high->index_1h` score `0.9294` n `96` status `ready` deltaP `15.9119` edge `0.0101` maxDD `-0.0982`
- `market_context_high->commodity_24h` score `0.9066` n `96` status `ready` deltaP `11.9792` edge `0.2197` maxDD `-4.666`
- `market_context_high->unknown_1h` score `0.2312` n `96` status `ready` deltaP `8.4581` edge `-0.0144` maxDD `-0.4843`
- `market_context_high->metal_1h` score `0.1847` n `96` status `ready` deltaP `6.2687` edge `0.0123` maxDD `-0.4291`
- `market_context_high->crypto_alt_4h` score `0.1708` n `96` status `ready` deltaP `9.6037` edge `0.0772` maxDD `-5.4926`
- `market_context_high->unknown_24h` score `0.1084` n `96` status `ready` deltaP `16.8402` edge `-0.0526` maxDD `-1.0505`
- `market_context_high->fx_4h` score `0.1048` n `96` status `ready` deltaP `8.7144` edge `0.0056` maxDD `-0.3539`
- `market_context_high->index_4h` score `0.0863` n `96` status `ready` deltaP `7.6473` edge `0.0217` maxDD `-0.5728`
- `market_context_high->fx_1h` score `-0.3261` n `96` status `ready` deltaP `-1.3224` edge `0.0029` maxDD `-0.2043`
- `market_context_high->crypto_major_1h` score `-0.3393` n `96` status `ready` deltaP `3.4306` edge `0.0181` maxDD `-2.7581`
- `market_context_high->crypto_alt_1h` score `-0.4384` n `96` status `ready` deltaP `1.7777` edge `0.0121` maxDD `-2.413`
- `market_context_high->commodity_4h` score `-0.5584` n `96` status `ready` deltaP `1.0417` edge `0.0065` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.9024` n `96` status `ready` deltaP `-7.8905` edge `-0.0065` maxDD `-1.1941`
- `market_context_high->metal_24h` score `-2.2105` n `96` status `ready` deltaP `-3.6458` edge `0.0717` maxDD `-11.4635`
- `market_context_high->fx_24h` score `-4.0272` n `96` status `ready` deltaP `-23.2639` edge `-0.0222` maxDD `-1.9981`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
