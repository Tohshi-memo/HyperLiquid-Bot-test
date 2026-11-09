# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-09T00:52:28.166953+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `64`

- Symbol pattern count: `6537`

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

- `market_context_high->equity_24h` score `7.062` n `35` status `ready` deltaP `14.1815` edge `0.846` maxDD `-25.83`
- `market_context_high->index_24h` score `1.0996` n `35` status `ready` deltaP `13.5515` edge `0.1137` maxDD `-2.7123`
- `market_context_high->fx_24h` score `0.7529` n `35` status `ready` deltaP `10.5556` edge `0.0012` maxDD `-0.0397`
- `market_context_high->commodity_24h` score `0.6867` n `35` status `ready` deltaP `4.9801` edge `0.1406` maxDD `-3.8612`
- `market_context_high->metal_1h` score `0.5181` n `62` status `ready` deltaP `8.2142` edge `0.0212` maxDD `-0.6226`
- `market_context_high->commodity_4h` score `0.3624` n `50` status `ready` deltaP `5.2561` edge `0.0503` maxDD `-1.1102`
- `market_context_high->fx_4h` score `-0.0598` n `50` status `ready` deltaP `7.4634` edge `0.0132` maxDD `-0.6503`
- `market_context_high->equity_1h` score `-0.1543` n `62` status `ready` deltaP `0.3332` edge `0.0977` maxDD `-5.5762`
- `market_context_high->commodity_1h` score `-0.2899` n `62` status `ready` deltaP `3.6073` edge `0.0064` maxDD `-1.7019`
- `market_context_high->index_4h` score `-0.4478` n `50` status `ready` deltaP `5.3902` edge `-0.0005` maxDD `-2.4279`
- `market_context_high->metal_4h` score `-0.4862` n `50` status `ready` deltaP `1.0488` edge `-0.0168` maxDD `-1.2025`
- `market_context_high->unknown_4h` score `-0.5324` n `50` status `ready` deltaP `-0.4512` edge `0.0034` maxDD `-0.9139`
- `market_context_high->index_1h` score `-0.5816` n `62` status `ready` deltaP `-4.5055` edge `0.0138` maxDD `-0.6664`
- `market_context_high->fx_1h` score `-0.774` n `62` status `ready` deltaP `-9.18` edge `-0.0001` maxDD `-0.3682`
- `market_context_high->crypto_alt_1h` score `-1.2156` n `62` status `ready` deltaP `5.5389` edge `-0.0035` maxDD `-10.1421`
- `market_context_high->metal_24h` score `-1.7761` n `35` status `ready` deltaP `5.5953` edge `-0.13` maxDD `-1.4245`
- `market_context_high->crypto_major_1h` score `-2.2249` n `62` status `ready` deltaP `0.2173` edge `-0.0768` maxDD `-11.7911`
- `market_context_high->equity_4h` score `-5.8541` n `50` status `ready` deltaP `4.8963` edge `-0.155` maxDD `-24.9053`
- `market_context_high->crypto_major_24h` score `-6.9986` n `35` status `ready` deltaP `-7.5397` edge `-0.0993` maxDD `-28.6921`
- `market_context_high->crypto_alt_4h` score `-9.6779` n `50` status `ready` deltaP `1.2805` edge `-0.3812` maxDD `-29.0395`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
