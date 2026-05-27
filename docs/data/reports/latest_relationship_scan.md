# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-27T12:54:16.268318+00:00`
- Price records: `672`
- Market context records: `2041`
- Flow alert records: `7767`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9105`

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

- `market_context_high->crypto_major_4h` score `8.9516` n `205` status `ready` deltaP `31.2699` edge `0.5905` maxDD `-1.9063`
- `market_context_high->crypto_alt_4h` score `8.3991` n `205` status `ready` deltaP `24.5534` edge `0.6507` maxDD `-5.1574`
- `market_context_high->unknown_4h` score `6.1113` n `205` status `ready` deltaP `19.6189` edge `0.4534` maxDD `-2.6599`
- `market_context_high->equity_4h` score `2.9273` n `205` status `ready` deltaP `16.9938` edge `0.2401` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `1.9783` n `204` status `ready` deltaP `17.4452` edge `0.5806` maxDD `-35.8966`
- `market_context_high->crypto_major_1h` score `1.6016` n `205` status `ready` deltaP `12.9268` edge `0.1459` maxDD `-3.2225`
- `market_context_high->index_4h` score `1.4426` n `205` status `ready` deltaP `12.9713` edge `0.1021` maxDD `-1.8022`
- `market_context_high->crypto_alt_1h` score `1.2989` n `205` status `ready` deltaP `10.3819` edge `0.1504` maxDD `-4.9097`
- `market_context_high->equity_24h` score `0.6827` n `204` status `ready` deltaP `16.5801` edge `0.4362` maxDD `-33.1875`
- `market_context_high->index_24h` score `0.5333` n `204` status `ready` deltaP `4.9019` edge `0.1346` maxDD `-4.1604`
- `market_context_high->equity_1h` score `0.2296` n `205` status `ready` deltaP `7.0601` edge `0.0509` maxDD `-2.6402`
- `market_context_high->unknown_1h` score `0.1141` n `205` status `ready` deltaP `4.345` edge `0.0525` maxDD `-3.0902`
- `market_context_high->index_1h` score `-0.2834` n `205` status `ready` deltaP `2.7034` edge `0.0174` maxDD `-1.3898`
- `market_context_high->fx_24h` score `-0.5523` n `204` status `ready` deltaP `10.6113` edge `0.0219` maxDD `-2.7598`
- `market_context_high->metal_1h` score `-0.7592` n `205` status `ready` deltaP `4.5567` edge `0.0251` maxDD `-5.166`
- `market_context_high->fx_1h` score `-0.8278` n `205` status `ready` deltaP `-0.9924` edge `0.0004` maxDD `-0.3548`
- `market_context_high->metal_4h` score `-1.0515` n `205` status `ready` deltaP `9.321` edge `0.1125` maxDD `-11.9812`
- `market_context_high->fx_4h` score `-1.4708` n `205` status `ready` deltaP `-5.0434` edge `-0.0008` maxDD `-1.0513`
- `market_context_high->crypto_major_24h` score `-1.6522` n `204` status `ready` deltaP `16.6955` edge `0.6096` maxDD `-62.3533`
- `market_context_high->commodity_1h` score `-1.8925` n `205` status `ready` deltaP `2.1564` edge `-0.0012` maxDD `-15.7972`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
