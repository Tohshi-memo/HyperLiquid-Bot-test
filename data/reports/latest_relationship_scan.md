# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-27T02:37:26.546008+00:00`
- Price records: `672`
- Market context records: `8049`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11848`

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

- `market_context_high->equity_24h` score `20.2595` n `74` status `ready` deltaP `35.463` edge `1.5429` maxDD `-4.9489`
- `market_context_high->equity_4h` score `8.5389` n `87` status `ready` deltaP `33.3351` edge `0.5373` maxDD `-2.5032`
- `market_context_high->metal_24h` score `8.4128` n `74` status `ready` deltaP `35.8752` edge `0.4619` maxDD `0.0`
- `market_context_high->commodity_24h` score `5.7107` n `74` status `ready` deltaP `37.0579` edge `0.3443` maxDD `-6.2367`
- `market_context_high->index_4h` score `3.2833` n `87` status `ready` deltaP `31.5881` edge `0.0818` maxDD `-0.5022`
- `market_context_high->equity_1h` score `2.5587` n `87` status `ready` deltaP `16.5221` edge `0.1464` maxDD `-2.1322`
- `market_context_high->index_24h` score `2.546` n `74` status `ready` deltaP `14.2934` edge `0.1839` maxDD `-1.3621`
- `market_context_high->metal_4h` score `2.2877` n `87` status `ready` deltaP `20.9963` edge `0.1129` maxDD `-0.979`
- `market_context_high->fx_24h` score `1.4749` n `74` status `ready` deltaP `30.5167` edge `0.056` maxDD `-0.6283`
- `market_context_high->index_1h` score `1.1626` n `87` status `ready` deltaP `15.2712` edge `0.0218` maxDD `-0.4716`
- `market_context_high->metal_1h` score `0.8015` n `87` status `ready` deltaP `11.3738` edge `0.0288` maxDD `-0.6936`
- `market_context_high->crypto_major_1h` score `0.6454` n `87` status `ready` deltaP `9.9198` edge `0.0287` maxDD `-1.6171`
- `market_context_high->crypto_major_4h` score `0.5234` n `87` status `ready` deltaP `7.9531` edge `0.1624` maxDD `-6.7444`
- `market_context_high->crypto_alt_4h` score `0.4258` n `87` status `ready` deltaP `4.2` edge `0.1192` maxDD `-3.9374`
- `market_context_high->fx_4h` score `0.0666` n `87` status `ready` deltaP `7.8796` edge `0.0063` maxDD `-0.3563`
- `market_context_high->crypto_alt_1h` score `-0.2484` n `87` status `ready` deltaP `0.4732` edge `0.0194` maxDD `-1.4603`
- `market_context_high->commodity_1h` score `-0.3993` n `87` status `ready` deltaP `1.879` edge `-0.0014` maxDD `-1.9855`
- `market_context_high->fx_1h` score `-0.4234` n `87` status `ready` deltaP `-2.7772` edge `0.0006` maxDD `-0.2428`
- `market_context_high->commodity_4h` score `-0.8242` n `87` status `ready` deltaP `5.8067` edge `0.0058` maxDD `-5.3478`
- `market_context_high->unknown_1h` score `-2.2607` n `87` status `ready` deltaP `4.7181` edge `-0.1775` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
