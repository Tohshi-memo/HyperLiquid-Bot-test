# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-06T05:07:25.400839+00:00`
- Price records: `672`
- Market context records: `3040`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6988`

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

- `market_context_high->crypto_alt_24h` score `24.3379` n `99` status `ready` deltaP `12.2001` edge `2.3385` maxDD `-22.6673`
- `market_context_high->unknown_24h` score `13.3639` n `99` status `ready` deltaP `23.9741` edge `1.0003` maxDD `-1.7175`
- `market_context_high->commodity_24h` score `13.0202` n `99` status `ready` deltaP `42.8977` edge `0.8231` maxDD `-1.2589`
- `market_context_high->equity_24h` score `8.8876` n `99` status `ready` deltaP `23.3744` edge `1.2588` maxDD `-18.3486`
- `market_context_high->index_24h` score `8.5434` n `99` status `ready` deltaP `22.964` edge `0.6844` maxDD `-4.7103`
- `market_context_high->commodity_4h` score `2.6337` n `129` status `ready` deltaP `17.8637` edge `0.1651` maxDD `-2.8438`
- `market_context_high->commodity_1h` score `-0.07` n `131` status `ready` deltaP `1.7736` edge `0.0246` maxDD `-1.7142`
- `market_context_high->index_1h` score `-0.4476` n `131` status `ready` deltaP `3.8694` edge `0.0188` maxDD `-4.1586`
- `market_context_high->unknown_4h` score `-0.4596` n `129` status `ready` deltaP `1.8506` edge `0.0547` maxDD `-3.7602`
- `market_context_high->fx_1h` score `-0.5282` n `131` status `ready` deltaP `-4.6624` edge `0.0002` maxDD `-0.2801`
- `market_context_high->unknown_1h` score `-0.6876` n `131` status `ready` deltaP `4.4076` edge `-0.0136` maxDD `-3.1801`
- `market_context_high->crypto_alt_1h` score `-0.691` n `131` status `ready` deltaP `6.1446` edge `0.0834` maxDD `-14.7034`
- `market_context_high->equity_1h` score `-0.6917` n `131` status `ready` deltaP `3.3151` edge `0.0295` maxDD `-8.2221`
- `market_context_high->index_4h` score `-0.995` n `129` status `ready` deltaP `12.4078` edge `0.059` maxDD `-16.8761`
- `market_context_high->crypto_major_1h` score `-1.0693` n `131` status `ready` deltaP `4.1093` edge `0.0618` maxDD `-15.1032`
- `market_context_high->fx_4h` score `-1.1711` n `129` status `ready` deltaP `-9.398` edge `-0.004` maxDD `-1.0127`
- `market_context_high->metal_1h` score `-1.1761` n `131` status `ready` deltaP `-1.8627` edge `-0.0031` maxDD `-7.154`
- `market_context_high->fx_24h` score `-1.3839` n `99` status `ready` deltaP `-1.6256` edge `-0.0173` maxDD `-0.6418`
- `market_context_high->equity_4h` score `-2.9982` n `129` status `ready` deltaP `9.2326` edge `0.0468` maxDD `-34.4188`
- `market_context_high->crypto_alt_4h` score `-3.3467` n `129` status `ready` deltaP `17.7171` edge `0.2573` maxDD `-58.6918`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
