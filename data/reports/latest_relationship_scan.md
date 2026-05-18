# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-18T16:52:16.571915+00:00`
- Price records: `672`
- Market context records: `1136`
- Flow alert records: `5173`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8739`

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

- `market_context_high->crypto_major_24h` score `19.4256` n `151` status `ready` deltaP `42.1104` edge `1.4152` maxDD `-5.5043`
- `market_context_high->crypto_alt_24h` score `9.13` n `151` status `ready` deltaP `18.4672` edge `0.7996` maxDD `-12.2838`
- `market_context_high->equity_24h` score `7.3171` n `151` status `ready` deltaP `17.9463` edge `0.5587` maxDD `-4.8203`
- `market_context_high->index_24h` score `5.7144` n `151` status `ready` deltaP `16.5574` edge `0.4075` maxDD `-2.668`
- `market_context_high->metal_24h` score `5.5912` n `151` status `ready` deltaP `-1.7477` edge `0.6443` maxDD `-6.3373`
- `market_context_high->equity_4h` score `2.0512` n `168` status `ready` deltaP `10.7942` edge `0.1653` maxDD `-3.6396`
- `market_context_high->index_4h` score `0.915` n `168` status `ready` deltaP `8.1373` edge `0.0903` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.4798` n `168` status `ready` deltaP `7.346` edge `0.0227` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.4239` n `168` status `ready` deltaP `3.329` edge `0.0509` maxDD `-1.3546`
- `market_context_high->crypto_major_4h` score `0.1881` n `168` status `ready` deltaP `8.914` edge `0.1568` maxDD `-8.3693`
- `market_context_high->fx_1h` score `0.1124` n `168` status `ready` deltaP `8.0161` edge `0.0015` maxDD `-0.3124`
- `market_context_high->crypto_major_1h` score `0.0814` n `168` status `ready` deltaP `6.9825` edge `0.0368` maxDD `-4.1256`
- `market_context_high->metal_1h` score `-0.234` n `168` status `ready` deltaP `6.8007` edge `-0.0038` maxDD `-2.2164`
- `market_context_high->crypto_alt_1h` score `-0.2574` n `168` status `ready` deltaP `2.9441` edge `0.0432` maxDD `-3.4088`
- `market_context_high->fx_4h` score `-0.7358` n `168` status `ready` deltaP `0.6315` edge `0.0011` maxDD `-1.6381`
- `market_context_high->commodity_1h` score `-0.7886` n `168` status `ready` deltaP `-2.3738` edge `-0.0045` maxDD `-3.7959`
- `market_context_high->crypto_alt_4h` score `-0.9259` n `168` status `ready` deltaP `6.1484` edge `0.1368` maxDD `-16.7194`
- `market_context_high->metal_4h` score `-2.4223` n `168` status `ready` deltaP `6.5476` edge `-0.0501` maxDD `-9.2991`
- `market_context_high->commodity_4h` score `-3.2081` n `168` status `ready` deltaP `-12.0354` edge `-0.0143` maxDD `-13.0076`
- `market_context_high->unknown_24h` score `-3.317` n `151` status `ready` deltaP `2.8123` edge `-0.0222` maxDD `-10.1706`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
