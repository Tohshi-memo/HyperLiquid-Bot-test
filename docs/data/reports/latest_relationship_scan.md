# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-17T13:52:14.321607+00:00`
- Price records: `672`
- Market context records: `1017`
- Flow alert records: `4838`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8634`

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

- `market_context_high->crypto_major_24h` score `13.5735` n `195` status `ready` deltaP `32.427` edge `0.9738` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `4.3692` n `195` status `ready` deltaP `11.1151` edge `0.4134` maxDD `-9.5387`
- `market_context_high->equity_24h` score `0.7617` n `195` status `ready` deltaP `7.3941` edge `0.202` maxDD `-8.0253`
- `market_context_high->index_24h` score `0.5554` n `195` status `ready` deltaP `6.7263` edge `0.1676` maxDD `-4.6259`
- `market_context_high->fx_1h` score `-0.1784` n `195` status `ready` deltaP `3.3303` edge `0.0005` maxDD `-0.3124`
- `market_context_high->commodity_1h` score `-0.445` n `195` status `ready` deltaP `2.7153` edge `0.0256` maxDD `-3.7959`
- `market_context_high->equity_1h` score `-0.7839` n `195` status `ready` deltaP `-0.8038` edge `0.0169` maxDD `-4.4826`
- `market_context_high->index_1h` score `-0.8252` n `195` status `ready` deltaP `1.7825` edge `0.0047` maxDD `-2.8282`
- `market_context_high->fx_4h` score `-0.8696` n `195` status `ready` deltaP `3.5968` edge `0.0032` maxDD `-1.6381`
- `market_context_high->crypto_major_1h` score `-1.2121` n `195` status `ready` deltaP `4.891` edge `-0.0157` maxDD `-11.4508`
- `market_context_high->crypto_alt_1h` score `-1.3117` n `195` status `ready` deltaP `-0.8391` edge `-0.0186` maxDD `-8.1842`
- `market_context_high->equity_4h` score `-1.3336` n `195` status `ready` deltaP `2.3804` edge `0.0882` maxDD `-10.5498`
- `market_context_high->index_4h` score `-1.4838` n `195` status `ready` deltaP `-0.3916` edge `0.0266` maxDD `-6.1444`
- `market_context_high->metal_1h` score `-1.8202` n `195` status `ready` deltaP `0.2088` edge `-0.0404` maxDD `-8.8816`
- `market_context_high->crypto_major_4h` score `-2.7854` n `195` status `ready` deltaP `7.4226` edge `0.089` maxDD `-22.648`
- `market_context_high->crypto_alt_4h` score `-2.8023` n `195` status `ready` deltaP `0.1477` edge `0.0433` maxDD `-15.2248`
- `market_context_high->commodity_4h` score `-3.2646` n `195` status `ready` deltaP `-2.6688` edge `0.0625` maxDD `-13.0076`
- `market_context_high->fx_24h` score `-3.2974` n `195` status `ready` deltaP `0.7633` edge `-0.0202` maxDD `-19.2774`
- `market_context_high->metal_4h` score `-4.3589` n `195` status `ready` deltaP `-2.6392` edge `-0.1639` maxDD `-23.5207`
- `market_context_high->metal_24h` score `-6.3457` n `195` status `ready` deltaP `-8.9445` edge `0.2341` maxDD `-45.5958`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
