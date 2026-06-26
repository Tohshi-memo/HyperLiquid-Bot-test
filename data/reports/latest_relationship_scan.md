# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-26T18:22:38.052219+00:00`
- Price records: `672`
- Market context records: `4853`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7632`

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

- `market_context_high->unknown_1h` score `13.5053` n `110` status `ready` deltaP `10.6206` edge `1.0964` maxDD `-1.674`
- `market_context_high->unknown_4h` score `11.2336` n `103` status `ready` deltaP `28.8095` edge `0.7972` maxDD `-1.917`
- `market_context_high->crypto_alt_4h` score `5.812` n `103` status `ready` deltaP `18.6834` edge `0.495` maxDD `-7.8181`
- `market_context_high->crypto_major_4h` score `5.6537` n `103` status `ready` deltaP `15.3534` edge `0.4912` maxDD `-7.1265`
- `market_context_high->unknown_24h` score `5.217` n `91` status `ready` deltaP `25.8166` edge `0.2969` maxDD `-1.4072`
- `market_context_high->metal_4h` score `1.5881` n `103` status `ready` deltaP `11.9509` edge `0.1189` maxDD `-1.9651`
- `market_context_high->equity_4h` score `0.8151` n `103` status `ready` deltaP `10.9564` edge `0.1696` maxDD `-6.3852`
- `market_context_high->index_4h` score `0.5226` n `103` status `ready` deltaP `10.7477` edge `0.0416` maxDD `-0.7006`
- `market_context_high->crypto_major_1h` score `0.4243` n `110` status `ready` deltaP `6.0207` edge `0.1181` maxDD `-5.6406`
- `market_context_high->crypto_alt_1h` score `0.395` n `110` status `ready` deltaP `7.8715` edge `0.1004` maxDD `-5.5126`
- `market_context_high->equity_1h` score `0.2036` n `110` status `ready` deltaP `4.0855` edge `0.0586` maxDD `-2.779`
- `market_context_high->metal_1h` score `-0.2048` n `110` status `ready` deltaP `0.2449` edge `0.0301` maxDD `-1.3057`
- `market_context_high->commodity_1h` score `-0.2051` n `110` status `ready` deltaP `3.5819` edge `0.0158` maxDD `-1.278`
- `market_context_high->fx_4h` score `-0.2762` n `103` status `ready` deltaP `4.1603` edge `0.0073` maxDD `-0.9686`
- `market_context_high->index_1h` score `-0.5172` n `110` status `ready` deltaP `-0.1388` edge `0.0101` maxDD `-0.7054`
- `market_context_high->commodity_4h` score `-0.707` n `103` status `ready` deltaP `7.6338` edge `0.0074` maxDD `-4.377`
- `market_context_high->fx_1h` score `-1.319` n `110` status `ready` deltaP `-6.7175` edge `-0.0038` maxDD `-0.5734`
- `market_context_high->fx_24h` score `-2.0328` n `91` status `ready` deltaP `-8.2456` edge `-0.0134` maxDD `-2.749`
- `market_context_high->index_24h` score `-4.9211` n `91` status `ready` deltaP `-9.9226` edge `-0.1562` maxDD `-24.6845`
- `market_context_high->commodity_24h` score `-5.6309` n `91` status `ready` deltaP `9.291` edge `-0.0203` maxDD `-27.5371`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
