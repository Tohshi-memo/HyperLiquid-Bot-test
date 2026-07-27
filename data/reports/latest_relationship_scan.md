# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-27T02:22:27.535247+00:00`
- Price records: `672`
- Market context records: `8048`
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

- `market_context_high->equity_24h` score `20.2926` n `74` status `ready` deltaP `35.6363` edge `1.5445` maxDD `-4.9489`
- `market_context_high->equity_4h` score `8.5231` n `87` status `ready` deltaP `33.1826` edge `0.537` maxDD `-2.5032`
- `market_context_high->metal_24h` score `8.4176` n `74` status `ready` deltaP `35.8752` edge `0.4623` maxDD `0.0`
- `market_context_high->commodity_24h` score `5.7071` n `74` status `ready` deltaP `37.0579` edge `0.344` maxDD `-6.2367`
- `market_context_high->index_4h` score `3.2687` n `87` status `ready` deltaP `31.4357` edge `0.0816` maxDD `-0.5022`
- `market_context_high->equity_1h` score `2.5839` n `87` status `ready` deltaP `16.6718` edge `0.1475` maxDD `-2.1322`
- `market_context_high->index_24h` score `2.5622` n `74` status `ready` deltaP `14.4667` edge `0.1841` maxDD `-1.3621`
- `market_context_high->metal_4h` score `2.2743` n `87` status `ready` deltaP `20.8438` edge `0.1128` maxDD `-0.979`
- `market_context_high->fx_24h` score `1.4878` n `74` status `ready` deltaP `30.69` edge `0.0565` maxDD `-0.6283`
- `market_context_high->index_1h` score `1.1757` n `87` status `ready` deltaP `15.4209` edge `0.0219` maxDD `-0.4716`
- `market_context_high->metal_1h` score `0.8015` n `87` status `ready` deltaP `11.3738` edge `0.0288` maxDD `-0.6936`
- `market_context_high->crypto_major_1h` score `0.6454` n `87` status `ready` deltaP `9.9198` edge `0.0287` maxDD `-1.6171`
- `market_context_high->crypto_major_4h` score `0.521` n `87` status `ready` deltaP `7.9531` edge `0.1622` maxDD `-6.7444`
- `market_context_high->crypto_alt_4h` score `0.4306` n `87` status `ready` deltaP `4.2` edge `0.1196` maxDD `-3.9374`
- `market_context_high->fx_4h` score `0.0761` n `87` status `ready` deltaP `8.032` edge `0.0065` maxDD `-0.3563`
- `market_context_high->crypto_alt_1h` score `-0.2472` n `87` status `ready` deltaP `0.4732` edge `0.0195` maxDD `-1.4603`
- `market_context_high->commodity_1h` score `-0.3985` n `87` status `ready` deltaP `1.879` edge `-0.0013` maxDD `-1.9855`
- `market_context_high->fx_1h` score `-0.4148` n `87` status `ready` deltaP `-2.6275` edge `0.0007` maxDD `-0.2428`
- `market_context_high->commodity_4h` score `-0.8219` n `87` status `ready` deltaP `5.8067` edge `0.0061` maxDD `-5.3478`
- `market_context_high->unknown_1h` score `-2.2655` n `87` status `ready` deltaP `4.7181` edge `-0.1779` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
