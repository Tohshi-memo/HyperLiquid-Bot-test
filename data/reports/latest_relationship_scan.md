# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-09T13:37:26.559780+00:00`
- Price records: `672`
- Market context records: `3387`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13080`

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

- `risk_on_high->crypto_major_24h` score `55.5506` n `32` status `ready` deltaP `58.3333` edge `4.2446` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `55.5506` n `32` status `ready` deltaP `58.3333` edge `4.2446` maxDD `-0.0083`
- `risk_on_high->crypto_alt_24h` score `53.6057` n `32` status `ready` deltaP `54.6875` edge `4.1177` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `53.6057` n `32` status `ready` deltaP `54.6875` edge `4.1177` maxDD `-0.8779`
- `risk_on_high->equity_24h` score `45.4838` n `32` status `ready` deltaP `56.5972` edge `3.413` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `45.4838` n `32` status `ready` deltaP `56.5972` edge `3.413` maxDD `0.0`
- `risk_on_high->index_24h` score `23.147` n `32` status `ready` deltaP `50.8681` edge `1.5898` maxDD `0.0`
- `risk_on_and_context->index_24h` score `23.147` n `32` status `ready` deltaP `50.8681` edge `1.5898` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `21.7266` n `156` status `ready` deltaP `18.7099` edge `2.4843` maxDD `-56.8787`
- `market_context_high->equity_24h` score `17.1678` n `156` status `ready` deltaP `30.9562` edge `2.0593` maxDD `-53.4685`
- `market_context_high->crypto_major_24h` score `16.598` n `156` status `ready` deltaP `23.6378` edge `2.291` maxDD `-78.2336`
- `risk_on_high->crypto_major_4h` score `15.157` n `32` status `ready` deltaP `28.2012` edge `1.1873` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `15.157` n `32` status `ready` deltaP `28.2012` edge `1.1873` maxDD `-5.9781`
- `risk_on_high->metal_24h` score `13.9155` n `32` status `ready` deltaP `29.5139` edge `0.989` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `13.9155` n `32` status `ready` deltaP `29.5139` edge `0.989` maxDD `-0.7574`
- `market_context_high->index_24h` score `11.7781` n `156` status `ready` deltaP `35.4835` edge `1.0004` maxDD `-16.1026`
- `risk_on_high->crypto_alt_4h` score `6.9512` n `32` status `ready` deltaP `8.3079` edge `0.7083` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `6.9512` n `32` status `ready` deltaP `8.3079` edge `0.7083` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `3.6038` n `32` status `ready` deltaP `14.7104` edge `0.4774` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `3.6038` n `32` status `ready` deltaP `14.7104` edge `0.4774` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
