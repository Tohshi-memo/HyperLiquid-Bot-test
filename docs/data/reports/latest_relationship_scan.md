# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-27T08:52:27.324982+00:00`
- Price records: `672`
- Market context records: `8076`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11784`

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

- `market_context_high->equity_24h` score `20.1566` n `84` status `ready` deltaP `36.5767` edge `1.5269` maxDD `-4.9489`
- `news_risk_high->equity_4h` score `8.8181` n `32` status `ready` deltaP `35.3659` edge `0.5037` maxDD `-0.037`
- `market_context_high->equity_4h` score `8.3806` n `87` status `ready` deltaP `32.4205` edge `0.5302` maxDD `-2.5032`
- `market_context_high->metal_24h` score `8.2628` n `84` status `ready` deltaP `35.8752` edge `0.4494` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `7.0171` n `32` status `ready` deltaP `32.622` edge `0.387` maxDD `-0.2447`
- `news_risk_high->equity_1h` score `3.42` n `42` status `ready` deltaP `27.9441` edge `0.1303` maxDD `-1.1944`
- `market_context_high->index_4h` score `3.2905` n `87` status `ready` deltaP `31.5881` edge `0.0824` maxDD `-0.5022`
- `market_context_high->index_24h` score `2.9606` n `84` status `ready` deltaP `18.637` edge `0.1895` maxDD `-1.3621`
- `news_risk_high->unknown_1h` score `2.7536` n `42` status `ready` deltaP `2.8443` edge `0.2382` maxDD `-0.8826`
- `news_risk_high->crypto_alt_4h` score `2.6544` n `32` status `ready` deltaP `23.8567` edge `0.2194` maxDD `-1.3848`
- `news_risk_high->index_4h` score `2.5197` n `32` status `ready` deltaP `20.8841` edge `0.0898` maxDD `-0.191`
- `market_context_high->metal_4h` score `2.4128` n `87` status `ready` deltaP `22.2158` edge `0.1152` maxDD `-0.979`
- `market_context_high->equity_1h` score `2.355` n `87` status `ready` deltaP `14.7257` edge `0.1414` maxDD `-2.1322`
- `market_context_high->fx_24h` score `2.3194` n `84` status `ready` deltaP `31.0101` edge `0.0569` maxDD `-0.6283`
- `news_risk_high->fx_4h` score `1.7795` n `32` status `ready` deltaP `23.7043` edge `0.0209` maxDD `-0.1179`
- `market_context_high->commodity_24h` score `1.1723` n `84` status `ready` deltaP `26.6011` edge `0.2204` maxDD `-13.4624`
- `market_context_high->index_1h` score `1.129` n `87` status `ready` deltaP `14.9718` edge `0.021` maxDD `-0.4716`
- `news_risk_high->metal_4h` score `0.9833` n `32` status `ready` deltaP `9.6799` edge `0.0642` maxDD `-0.7433`
- `market_context_high->metal_1h` score `0.8003` n `87` status `ready` deltaP `11.2241` edge `0.0297` maxDD `-0.6936`
- `news_risk_high->crypto_major_1h` score `0.5154` n `42` status `ready` deltaP `1.7822` edge `0.0708` maxDD `-1.1783`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
