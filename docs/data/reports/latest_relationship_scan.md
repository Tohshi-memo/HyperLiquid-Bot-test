# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-17T20:07:31.796809+00:00`
- Price records: `672`
- Market context records: `7063`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11502`

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

- `market_context_high->fx_4h` score `0.6217` n `186` status `ready` deltaP `16.5617` edge `0.0114` maxDD `-0.9333`
- `market_context_high->fx_1h` score `-0.2139` n `186` status `ready` deltaP `3.7634` edge `0.0022` maxDD `-0.276`
- `market_context_high->crypto_alt_1h` score `-0.3059` n `186` status `ready` deltaP `1.967` edge `0.0341` maxDD `-4.5815`
- `market_context_high->unknown_1h` score `-0.4983` n `186` status `ready` deltaP `-0.7421` edge `0.0269` maxDD `-1.7447`
- `market_context_high->crypto_major_1h` score `-0.5747` n `186` status `ready` deltaP `4.1787` edge `0.0337` maxDD `-7.1523`
- `market_context_high->index_1h` score `-0.7723` n `186` status `ready` deltaP `-0.6133` edge `-0.0038` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-0.8032` n `186` status `ready` deltaP `-3.6283` edge `-0.002` maxDD `-2.1427`
- `market_context_high->commodity_1h` score `-0.8769` n `186` status `ready` deltaP `-4.784` edge `-0.0189` maxDD `-1.9306`
- `market_context_high->unknown_4h` score `-0.9353` n `186` status `ready` deltaP `-5.3698` edge `0.1213` maxDD `-4.742`
- `market_context_high->commodity_4h` score `-1.6282` n `186` status `ready` deltaP `-7.1564` edge `-0.045` maxDD `-2.9494`
- `market_context_high->equity_1h` score `-1.8777` n `186` status `ready` deltaP `4.4025` edge `-0.0278` maxDD `-14.716`
- `market_context_high->index_4h` score `-2.3201` n `186` status `ready` deltaP `0.954` edge `-0.0339` maxDD `-12.2591`
- `market_context_high->commodity_24h` score `-2.4572` n `186` status `ready` deltaP `-2.6378` edge `-0.0563` maxDD `-4.4704`
- `market_context_high->crypto_alt_4h` score `-2.8758` n `186` status `ready` deltaP `0.9064` edge `0.0038` maxDD `-22.2831`
- `market_context_high->crypto_major_4h` score `-3.0256` n `186` status `ready` deltaP `2.9931` edge `0.0206` maxDD `-24.6094`
- `market_context_high->fx_24h` score `-3.5428` n `186` status `ready` deltaP `-0.1232` edge `-0.0117` maxDD `-3.9503`
- `market_context_high->metal_4h` score `-3.5809` n `186` status `ready` deltaP `0.4065` edge `-0.0028` maxDD `-5.5324`
- `market_context_high->unknown_24h` score `-3.8867` n `186` status `ready` deltaP `-15.1826` edge `0.1176` maxDD `-23.5076`
- `market_context_high->equity_4h` score `-7.8919` n `186` status `ready` deltaP `4.4929` edge `-0.1547` maxDD `-63.963`
- `market_context_high->metal_24h` score `-15.4714` n `186` status `ready` deltaP `-20.3741` edge `-0.0941` maxDD `-44.4154`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
