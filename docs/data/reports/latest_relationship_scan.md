# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-27T02:52:24.231883+00:00`
- Price records: `672`
- Market context records: `8050`
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

- `market_context_high->equity_24h` score `20.2511` n `74` status `ready` deltaP `35.463` edge `1.5422` maxDD `-4.9489`
- `market_context_high->equity_4h` score `8.5413` n `87` status `ready` deltaP `33.3351` edge `0.5375` maxDD `-2.5032`
- `market_context_high->metal_24h` score `8.4104` n `74` status `ready` deltaP `35.8752` edge `0.4617` maxDD `0.0`
- `market_context_high->commodity_24h` score `5.7131` n `74` status `ready` deltaP `37.0579` edge `0.3445` maxDD `-6.2367`
- `market_context_high->index_4h` score `3.2845` n `87` status `ready` deltaP `31.5881` edge `0.0819` maxDD `-0.5022`
- `market_context_high->index_24h` score `2.5472` n `74` status `ready` deltaP `14.2934` edge `0.184` maxDD `-1.3621`
- `market_context_high->equity_1h` score `2.5384` n `87` status `ready` deltaP `16.3724` edge `0.1457` maxDD `-2.1322`
- `market_context_high->metal_4h` score `2.301` n `87` status `ready` deltaP `21.1487` edge `0.113` maxDD `-0.979`
- `market_context_high->fx_24h` score `1.4628` n `74` status `ready` deltaP `30.3434` edge `0.0556` maxDD `-0.6283`
- `market_context_high->index_1h` score `1.1506` n `87` status `ready` deltaP `15.1215` edge `0.0218` maxDD `-0.4716`
- `market_context_high->metal_1h` score `0.8182` n `87` status `ready` deltaP `11.5235` edge `0.0292` maxDD `-0.6936`
- `market_context_high->crypto_major_1h` score `0.6406` n `87` status `ready` deltaP `9.9198` edge `0.0283` maxDD `-1.6171`
- `market_context_high->crypto_major_4h` score `0.5138` n `87` status `ready` deltaP `7.9531` edge `0.1616` maxDD `-6.7444`
- `market_context_high->crypto_alt_4h` score `0.4078` n `87` status `ready` deltaP `4.2` edge `0.1177` maxDD `-3.9374`
- `market_context_high->fx_4h` score `0.0571` n `87` status `ready` deltaP `7.7271` edge `0.0061` maxDD `-0.3563`
- `market_context_high->crypto_alt_1h` score `-0.2652` n `87` status `ready` deltaP `0.3235` edge `0.019` maxDD `-1.4603`
- `market_context_high->commodity_1h` score `-0.3993` n `87` status `ready` deltaP `1.879` edge `-0.0014` maxDD `-1.9855`
- `market_context_high->fx_1h` score `-0.4234` n `87` status `ready` deltaP `-2.7772` edge `0.0006` maxDD `-0.2428`
- `market_context_high->commodity_4h` score `-0.8329` n `87` status `ready` deltaP `5.6542` edge `0.0057` maxDD `-5.3478`
- `market_context_high->unknown_1h` score `-2.2667` n `87` status `ready` deltaP `4.7181` edge `-0.178` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
