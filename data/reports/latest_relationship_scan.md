# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-21T03:37:16.077427+00:00`
- Price records: `672`
- Market context records: `1385`
- Flow alert records: `5901`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8804`

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

- `market_context_high->crypto_major_24h` score `13.2744` n `154` status `ready` deltaP `29.3087` edge `1.024` maxDD `-8.0553`
- `market_context_high->metal_24h` score `11.7508` n `154` status `ready` deltaP `12.7277` edge `1.0611` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `11.5085` n `154` status `ready` deltaP `28.7811` edge `0.9688` maxDD `-15.1306`
- `market_context_high->index_24h` score `4.1637` n `154` status `ready` deltaP `20.5966` edge `0.3183` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.6236` n `154` status `ready` deltaP `13.7423` edge `0.3597` maxDD `-14.2815`
- `market_context_high->equity_4h` score `1.6712` n `182` status `ready` deltaP `8.6337` edge `0.1647` maxDD `-3.6396`
- `market_context_high->index_1h` score `0.0285` n `194` status `ready` deltaP `4.9016` edge `0.0162` maxDD `-1.7205`
- `market_context_high->fx_24h` score `0.0035` n `154` status `ready` deltaP `9.3592` edge `0.0428` maxDD `-1.3925`
- `market_context_high->equity_1h` score `-0.0654` n `194` status `ready` deltaP `2.9554` edge `0.0307` maxDD `-2.8014`
- `market_context_high->metal_4h` score `-0.0727` n `182` status `ready` deltaP `10.7159` edge `0.0656` maxDD `-6.4478`
- `market_context_high->fx_1h` score `-0.3548` n `194` status `ready` deltaP `2.9091` edge `-0.0024` maxDD `-0.3914`
- `market_context_high->index_4h` score `-0.4819` n `182` status `ready` deltaP `0.7857` edge `0.0635` maxDD `-3.7119`
- `market_context_high->crypto_alt_1h` score `-0.485` n `194` status `ready` deltaP `2.0603` edge `0.0329` maxDD `-3.6309`
- `market_context_high->metal_1h` score `-0.5487` n `194` status `ready` deltaP `5.5359` edge `0.0006` maxDD `-4.2945`
- `market_context_high->commodity_1h` score `-0.8151` n `194` status `ready` deltaP `-0.9815` edge `0.0001` maxDD `-2.252`
- `market_context_high->crypto_alt_4h` score `-1.1887` n `182` status `ready` deltaP `8.1597` edge `0.1785` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `-1.2593` n `182` status `ready` deltaP `4.6117` edge `0.1352` maxDD `-13.3376`
- `market_context_high->crypto_major_1h` score `-1.2636` n `194` status `ready` deltaP `-0.5664` edge `0.005` maxDD `-6.1883`
- `market_context_high->fx_4h` score `-1.8176` n `182` status `ready` deltaP `-6.4058` edge `-0.0117` maxDD `-1.4313`
- `market_context_high->unknown_4h` score `-3.3506` n `182` status `ready` deltaP `4.2683` edge `-0.2309` maxDD `-11.1695`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
