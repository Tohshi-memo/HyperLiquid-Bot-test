# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-16T11:52:30.392604+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11471`

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

- `news_risk_high->unknown_4h` score `367.399` n `83` status `ready` deltaP `-21.0531` edge `30.8464` maxDD `-4.1571`
- `news_risk_high->crypto_alt_24h` score `23.8563` n `78` status `ready` deltaP `47.7698` edge `1.7086` maxDD `-1.4564`
- `news_risk_high->crypto_major_24h` score `21.0193` n `78` status `ready` deltaP `39.7303` edge `1.6338` maxDD `-9.098`
- `news_risk_high->equity_24h` score `15.084` n `78` status `ready` deltaP `47.5961` edge `1.1171` maxDD `-6.5262`
- `news_risk_high->index_24h` score `7.7736` n `78` status `ready` deltaP `54.3002` edge `0.3034` maxDD `-0.075`
- `news_risk_high->metal_24h` score `6.612` n `78` status `ready` deltaP `37.9674` edge `0.3433` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `5.3502` n `52` status `ready` deltaP `34.0278` edge `0.219` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.3502` n `52` status `ready` deltaP `34.0278` edge `0.219` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.0511` n `149` status `ready` deltaP `27.3164` edge `0.208` maxDD `-0.8682`
- `risk_on_high->fx_24h` score `2.3645` n `52` status `ready` deltaP `31.9311` edge `-0.0116` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.3645` n `52` status `ready` deltaP `31.9311` edge `-0.0116` maxDD `-0.0054`
- `market_context_high->fx_24h` score `2.2296` n `149` status `ready` deltaP `29.1562` edge `0.013` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `2.1148` n `52` status `ready` deltaP `27.6618` edge `0.0268` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.1148` n `52` status `ready` deltaP `27.6618` edge `0.0268` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.0146` n `149` status `ready` deltaP `24.1641` edge `0.0486` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.8952` n `149` status `ready` deltaP `14.2648` edge `0.0172` maxDD `-0.3491`
- `risk_on_high->crypto_alt_4h` score `0.5559` n `52` status `ready` deltaP `10.7646` edge `0.161` maxDD `-6.2526`
- `risk_on_and_context->crypto_alt_4h` score `0.5559` n `52` status `ready` deltaP `10.7646` edge `0.161` maxDD `-6.2526`
- `news_risk_high->index_4h` score `0.5393` n `83` status `ready` deltaP `14.9372` edge `0.0324` maxDD `-0.6935`
- `risk_on_high->commodity_1h` score `0.2719` n `52` status `ready` deltaP `7.3469` edge `0.0089` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
