# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-27T16:22:23.598102+00:00`
- Price records: `672`
- Market context records: `2056`
- Flow alert records: `7811`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9125`

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

- `market_context_high->crypto_major_4h` score `9.4602` n `205` status `ready` deltaP `33.2317` edge `0.6198` maxDD `-1.9063`
- `market_context_high->crypto_alt_4h` score `8.7474` n `205` status `ready` deltaP `25.4573` edge `0.6737` maxDD `-5.1574`
- `market_context_high->unknown_4h` score `6.3569` n `205` status `ready` deltaP `20.2134` edge `0.4699` maxDD `-2.6599`
- `market_context_high->unknown_24h` score `3.7497` n `205` status `ready` deltaP `17.6876` edge `0.7266` maxDD `-35.8966`
- `market_context_high->equity_4h` score `3.3412` n `205` status `ready` deltaP `18.628` edge `0.2637` maxDD `-5.0894`
- `market_context_high->index_4h` score `1.901` n `205` status `ready` deltaP `14.7561` edge `0.1284` maxDD `-1.8022`
- `market_context_high->crypto_major_1h` score `1.6627` n `206` status `ready` deltaP `13.2565` edge `0.1488` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `1.2366` n `206` status `ready` deltaP `10.1128` edge `0.147` maxDD `-4.9097`
- `market_context_high->equity_24h` score `1.192` n `205` status `ready` deltaP `18.5669` edge `0.4654` maxDD `-33.1875`
- `market_context_high->index_24h` score `1.0691` n `205` status `ready` deltaP `7.0689` edge `0.1648` maxDD `-4.1604`
- `market_context_high->equity_1h` score `0.4021` n `206` status `ready` deltaP `8.2714` edge `0.0572` maxDD `-2.6402`
- `market_context_high->unknown_1h` score `0.27` n `206` status `ready` deltaP `4.8093` edge `0.0624` maxDD `-3.0902`
- `market_context_high->index_1h` score `-0.1079` n `206` status `ready` deltaP `3.9068` edge `0.024` maxDD `-1.3898`
- `market_context_high->fx_24h` score `-0.3807` n `205` status `ready` deltaP `12.5065` edge `0.0242` maxDD `-2.811`
- `market_context_high->crypto_major_24h` score `-0.4846` n `205` status `ready` deltaP `18.7805` edge `0.693` maxDD `-62.3533`
- `market_context_high->metal_4h` score `-0.6887` n `205` status `ready` deltaP `11.0061` edge `0.1315` maxDD `-11.9812`
- `market_context_high->fx_1h` score `-0.7783` n `206` status `ready` deltaP `-0.4491` edge `0.0009` maxDD `-0.3548`
- `market_context_high->metal_1h` score `-0.8183` n `206` status `ready` deltaP `3.9969` edge `0.0239` maxDD `-5.166`
- `market_context_high->fx_4h` score `-1.4308` n `205` status `ready` deltaP `-4.6037` edge `-0.0004` maxDD `-1.0513`
- `market_context_high->commodity_1h` score `-1.9301` n `206` status `ready` deltaP `1.9417` edge `-0.0046` maxDD `-15.7972`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
