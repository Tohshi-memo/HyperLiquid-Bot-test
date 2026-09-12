# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-12T20:52:35.597714+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12779`

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

- `market_context_high->unknown_24h` score `11504.1528` n `72` status `ready` deltaP `12.6736` edge `958.6001` maxDD `-0.082`
- `risk_on_high->unknown_24h` score `11300.5105` n `32` status `ready` deltaP `15.4514` edge `941.6062` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `11300.5105` n `32` status `ready` deltaP `15.4514` edge `941.6062` maxDD `0.0`
- `news_risk_high->unknown_1h` score `383.3428` n `82` status `ready` deltaP `-5.5499` edge `32.0244` maxDD `-1.7068`
- `news_risk_high->crypto_major_24h` score `19.345` n `73` status `ready` deltaP `41.7975` edge `1.4675` maxDD `-8.0589`
- `news_risk_high->crypto_alt_24h` score `17.3645` n `73` status `ready` deltaP `30.9955` edge `1.2892` maxDD `-2.2369`
- `risk_on_high->crypto_alt_24h` score `14.0333` n `32` status `ready` deltaP `34.5486` edge `0.9621` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `14.0333` n `32` status `ready` deltaP `34.5486` edge `0.9621` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `13.0717` n `72` status `ready` deltaP `27.9514` edge `0.9857` maxDD `-3.9523`
- `risk_on_high->equity_24h` score `10.1896` n `32` status `ready` deltaP `43.0556` edge `0.5621` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `10.1896` n `32` status `ready` deltaP `43.0556` edge `0.5621` maxDD `0.0`
- `market_context_high->equity_24h` score `9.7144` n `72` status `ready` deltaP `43.0556` edge `0.5225` maxDD `0.0`
- `news_risk_high->equity_24h` score `8.1798` n `73` status `ready` deltaP `21.1378` edge `0.6509` maxDD `-4.1468`
- `news_risk_high->index_24h` score `6.5822` n `73` status `ready` deltaP `44.442` edge `0.2699` maxDD `-0.0797`
- `news_risk_high->metal_24h` score `5.9688` n `73` status `ready` deltaP `36.6866` edge `0.2969` maxDD `-0.526`
- `risk_on_high->index_24h` score `5.3797` n `32` status `ready` deltaP `53.6458` edge `0.0949` maxDD `-0.005`
- `risk_on_and_context->index_24h` score `5.3797` n `32` status `ready` deltaP `53.6458` edge `0.0949` maxDD `-0.005`
- `market_context_high->index_24h` score `3.328` n `72` status `ready` deltaP `35.9375` edge `0.0771` maxDD `-0.1483`
- `market_context_high->commodity_24h` score `2.8414` n `72` status `ready` deltaP `31.9445` edge `0.0377` maxDD `-0.1105`
- `risk_on_high->crypto_alt_4h` score `2.7813` n `47` status `ready` deltaP `22.188` edge `0.2958` maxDD `-3.6385`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
