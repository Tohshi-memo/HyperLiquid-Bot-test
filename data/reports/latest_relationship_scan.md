# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-27T02:07:17.615149+00:00`
- Price records: `672`
- Market context records: `1998`
- Flow alert records: `7643`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7585`

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

- `market_context_high->crypto_major_4h` score `8.5797` n `221` status `ready` deltaP `30.1608` edge `0.5669` maxDD `-1.9063`
- `market_context_high->crypto_alt_4h` score `7.9788` n `221` status `ready` deltaP `23.8453` edge `0.6204` maxDD `-5.1574`
- `market_context_high->unknown_4h` score `5.0616` n `221` status `ready` deltaP `17.2056` edge `0.3845` maxDD `-2.8588`
- `market_context_high->equity_4h` score `2.5777` n `221` status `ready` deltaP `15.5943` edge `0.2203` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `2.4842` n `186` status `ready` deltaP `15.7442` edge `0.6341` maxDD `-35.8966`
- `market_context_high->metal_24h` score `1.663` n `186` status `ready` deltaP `16.7072` edge `0.2698` maxDD `-12.7414`
- `market_context_high->crypto_major_1h` score `1.2794` n `221` status `ready` deltaP `10.9397` edge `0.1323` maxDD `-3.2225`
- `market_context_high->equity_24h` score `1.1509` n `186` status `ready` deltaP `14.5732` edge `0.4886` maxDD `-33.1875`
- `market_context_high->crypto_alt_1h` score `1.0144` n `221` status `ready` deltaP `9.0003` edge `0.1359` maxDD `-4.9097`
- `market_context_high->index_4h` score `0.8754` n `221` status `ready` deltaP `9.107` edge `0.0806` maxDD `-1.8022`
- `market_context_high->fx_24h` score `0.6855` n `186` status `ready` deltaP `15.8197` edge `0.0291` maxDD `-1.1952`
- `market_context_high->crypto_major_24h` score `0.5346` n `186` status `ready` deltaP `20.3749` edge `0.7673` maxDD `-62.3533`
- `market_context_high->index_24h` score `0.1105` n `186` status `ready` deltaP `2.8576` edge `0.113` maxDD `-4.1604`
- `market_context_high->equity_1h` score `-0.0773` n `221` status `ready` deltaP `4.6794` edge `0.0412` maxDD `-2.6402`
- `market_context_high->index_1h` score `-0.6096` n `221` status `ready` deltaP `-0.1585` edge `0.0093` maxDD `-1.3898`
- `market_context_high->fx_1h` score `-0.6096` n `221` status `ready` deltaP `-2.1791` edge `-0.0004` maxDD `-0.3914`
- `market_context_high->unknown_1h` score `-0.902` n `221` status `ready` deltaP `2.3695` edge `-0.019` maxDD `-3.0902`
- `market_context_high->metal_1h` score `-0.9458` n `221` status `ready` deltaP `1.7436` edge `0.0007` maxDD `-6.3532`
- `market_context_high->fx_4h` score `-1.1262` n `221` status `ready` deltaP `-7.9861` edge `-0.003` maxDD `-1.0513`
- `market_context_high->commodity_1h` score `-1.8481` n `221` status `ready` deltaP `2.4853` edge `0.0023` maxDD `-15.7972`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
