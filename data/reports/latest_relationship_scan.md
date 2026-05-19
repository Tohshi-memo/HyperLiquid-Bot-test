# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-19T22:07:17.809432+00:00`
- Price records: `672`
- Market context records: `1260`
- Flow alert records: `5535`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8809`

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

- `market_context_high->crypto_major_24h` score `17.9497` n `128` status `ready` deltaP `41.5798` edge `1.3318` maxDD `-8.0553`
- `market_context_high->metal_24h` score `9.0493` n `128` status `ready` deltaP `3.9931` edge `0.8942` maxDD `-6.3373`
- `market_context_high->unknown_4h` score `8.0901` n `128` status `ready` deltaP `5.3735` edge `0.76` maxDD `-6.7322`
- `market_context_high->crypto_alt_24h` score `7.9637` n `128` status `ready` deltaP `23.3506` edge `0.7096` maxDD `-15.1306`
- `market_context_high->index_24h` score `4.486` n `128` status `ready` deltaP `25.0` edge `0.3158` maxDD `-5.3574`
- `market_context_high->equity_4h` score `3.5252` n `128` status `ready` deltaP `18.4641` edge `0.237` maxDD `-3.6396`
- `market_context_high->equity_24h` score `3.4503` n `128` status `ready` deltaP `23.0903` edge `0.5211` maxDD `-14.2815`
- `market_context_high->commodity_24h` score `2.7353` n `128` status `ready` deltaP `-10.2431` edge `0.4444` maxDD `-6.8535`
- `market_context_high->unknown_24h` score `2.253` n `128` status `ready` deltaP `1.5625` edge `0.4503` maxDD `-10.1706`
- `market_context_high->index_4h` score `1.6664` n `128` status `ready` deltaP `14.5007` edge `0.1105` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.8698` n `131` status `ready` deltaP `11.7407` edge `0.0259` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.7951` n `131` status `ready` deltaP `7.3547` edge `0.0541` maxDD `-1.2834`
- `market_context_high->metal_4h` score `0.6063` n `128` status `ready` deltaP `17.2828` edge `0.0784` maxDD `-6.4478`
- `market_context_high->metal_1h` score `0.4503` n `131` status `ready` deltaP `12.5349` edge `0.015` maxDD `-2.2164`
- `market_context_high->crypto_major_4h` score `0.17` n `128` status `ready` deltaP `7.8316` edge `0.1617` maxDD `-8.3693`
- `market_context_high->fx_24h` score `0.1572` n `128` status `ready` deltaP `4.2535` edge `0.0312` maxDD `-0.3831`
- `market_context_high->fx_1h` score `-0.2159` n `131` status `ready` deltaP `4.4076` edge `-0.0018` maxDD `-0.3124`
- `market_context_high->crypto_alt_1h` score `-0.2609` n `131` status `ready` deltaP `1.369` edge `0.0417` maxDD `-3.4088`
- `market_context_high->crypto_alt_4h` score `-0.4549` n `128` status `ready` deltaP `8.8605` edge `0.1791` maxDD `-16.7194`
- `market_context_high->crypto_major_1h` score `-0.4644` n `131` status `ready` deltaP `1.4593` edge `0.0073` maxDD `-4.1256`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
