# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-27T03:22:33.529704+00:00`
- Price records: `672`
- Market context records: `8052`
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

- `market_context_high->equity_24h` score `20.2048` n `74` status `ready` deltaP `35.2897` edge `1.5395` maxDD `-4.9489`
- `market_context_high->equity_4h` score `8.5547` n `87` status `ready` deltaP `33.4875` edge `0.5376` maxDD `-2.5032`
- `market_context_high->metal_24h` score `8.402` n `74` status `ready` deltaP `35.8752` edge `0.461` maxDD `0.0`
- `market_context_high->commodity_24h` score `5.7179` n `74` status `ready` deltaP `37.0579` edge `0.3449` maxDD `-6.2367`
- `market_context_high->index_4h` score `3.3003` n `87` status `ready` deltaP `31.7406` edge `0.0822` maxDD `-0.5022`
- `market_context_high->index_24h` score `2.5484` n `74` status `ready` deltaP `14.2934` edge `0.1841` maxDD `-1.3621`
- `market_context_high->equity_1h` score `2.5204` n `87` status `ready` deltaP `16.2227` edge `0.1452` maxDD `-2.1322`
- `market_context_high->metal_4h` score `2.2889` n `87` status `ready` deltaP `20.9963` edge `0.113` maxDD `-0.979`
- `market_context_high->fx_24h` score `1.4385` n `74` status `ready` deltaP `29.9968` edge `0.0548` maxDD `-0.6283`
- `market_context_high->index_1h` score `1.1362` n `87` status `ready` deltaP `14.9718` edge `0.0216` maxDD `-0.4716`
- `market_context_high->metal_1h` score `0.8506` n `87` status `ready` deltaP `11.8229` edge `0.0299` maxDD `-0.6936`
- `market_context_high->crypto_major_1h` score `0.6562` n `87` status `ready` deltaP `10.0695` edge `0.0286` maxDD `-1.6171`
- `market_context_high->crypto_major_4h` score `0.5018` n `87` status `ready` deltaP `7.9531` edge `0.1606` maxDD `-6.7444`
- `market_context_high->crypto_alt_4h` score `0.379` n `87` status `ready` deltaP `4.2` edge `0.1153` maxDD `-3.9374`
- `market_context_high->fx_4h` score `0.0382` n `87` status `ready` deltaP `7.4222` edge `0.0057` maxDD `-0.3563`
- `market_context_high->crypto_alt_1h` score `-0.2771` n `87` status `ready` deltaP `0.1738` edge `0.019` maxDD `-1.4603`
- `market_context_high->commodity_1h` score `-0.3993` n `87` status `ready` deltaP `1.879` edge `-0.0014` maxDD `-1.9855`
- `market_context_high->fx_1h` score `-0.4071` n `87` status `ready` deltaP `-2.4778` edge `0.0007` maxDD `-0.2428`
- `market_context_high->commodity_4h` score `-0.8234` n `87` status `ready` deltaP `5.8067` edge `0.0059` maxDD `-5.3478`
- `market_context_high->unknown_1h` score `-2.2834` n `87` status `ready` deltaP `4.5684` edge `-0.1784` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
