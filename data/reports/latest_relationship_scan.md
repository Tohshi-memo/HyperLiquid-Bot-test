# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-29T09:37:28.198242+00:00`
- Price records: `672`
- Market context records: `5131`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5560`

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

- `market_context_high->unknown_24h` score `30.8232` n `61` status `ready` deltaP `28.8991` edge `2.4102` maxDD `-1.4072`
- `market_context_high->unknown_1h` score `8.3169` n `128` status `ready` deltaP `8.9586` edge `0.6975` maxDD `-2.7986`
- `market_context_high->unknown_4h` score `7.3646` n `119` status `ready` deltaP `20.0604` edge `0.5822` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `4.9525` n `119` status `ready` deltaP `14.4637` edge `0.4762` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `3.498` n `119` status `ready` deltaP `12.2476` edge `0.4391` maxDD `-14.0065`
- `market_context_high->commodity_24h` score `1.7943` n `61` status `ready` deltaP `22.2677` edge `0.1674` maxDD `-4.1987`
- `market_context_high->equity_4h` score `0.7614` n `119` status `ready` deltaP `8.1318` edge `0.1731` maxDD `-7.4425`
- `market_context_high->crypto_alt_1h` score `0.6605` n `128` status `ready` deltaP `4.5893` edge `0.1206` maxDD `-5.0257`
- `market_context_high->equity_1h` score `0.6063` n `128` status `ready` deltaP `6.8161` edge `0.0644` maxDD `-2.745`
- `market_context_high->crypto_major_1h` score `0.588` n `128` status `ready` deltaP `6.9517` edge `0.1272` maxDD `-6.9639`
- `market_context_high->metal_24h` score `0.3807` n `61` status `ready` deltaP `2.1915` edge `0.2181` maxDD `-11.4122`
- `market_context_high->metal_1h` score `0.0397` n `128` status `ready` deltaP `5.5716` edge `0.0194` maxDD `-1.4501`
- `market_context_high->index_1h` score `-0.0808` n `128` status `ready` deltaP `4.3553` edge `0.0146` maxDD `-1.0296`
- `market_context_high->index_4h` score `-0.4973` n `119` status `ready` deltaP `5.22` edge `0.0355` maxDD `-2.9391`
- `market_context_high->crypto_alt_24h` score `-0.4993` n `61` status `ready` deltaP `14.3244` edge `0.5418` maxDD `-50.438`
- `market_context_high->commodity_1h` score `-0.5215` n `128` status `ready` deltaP `1.497` edge `0.0001` maxDD `-2.155`
- `market_context_high->metal_4h` score `-0.5505` n `119` status `ready` deltaP `2.6171` edge `0.053` maxDD `-4.6157`
- `market_context_high->fx_1h` score `-0.7159` n `128` status `ready` deltaP `-3.8221` edge `-0.0022` maxDD `-0.7944`
- `market_context_high->fx_4h` score `-0.997` n `119` status `ready` deltaP `-3.0936` edge `0.0001` maxDD `-1.9169`
- `market_context_high->crypto_major_24h` score `-1.1068` n `61` status `ready` deltaP `15.1155` edge `0.5422` maxDD `-52.4829`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
