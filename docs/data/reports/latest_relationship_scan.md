# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-27T23:22:17.299158+00:00`
- Price records: `672`
- Market context records: `2086`
- Flow alert records: `7899`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9146`

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

- `market_context_high->crypto_major_4h` score `10.3057` n `194` status `ready` deltaP `36.315` edge `0.6697` maxDD `-1.9063`
- `market_context_high->crypto_alt_4h` score `10.1468` n `194` status `ready` deltaP `30.4705` edge `0.7569` maxDD `-5.1574`
- `market_context_high->unknown_4h` score `7.3303` n `194` status `ready` deltaP `24.8806` edge `0.5199` maxDD `-2.6599`
- `market_context_high->unknown_24h` score `4.7941` n `193` status `ready` deltaP `21.6523` edge `0.7872` maxDD `-35.8966`
- `market_context_high->equity_4h` score `4.0144` n `194` status `ready` deltaP `21.673` edge `0.2995` maxDD `-5.0894`
- `market_context_high->index_4h` score `2.3919` n `194` status `ready` deltaP `17.818` edge `0.1489` maxDD `-1.8022`
- `market_context_high->crypto_major_1h` score `2.2131` n `194` status `ready` deltaP `15.9964` edge `0.1764` maxDD `-3.2225`
- `market_context_high->index_24h` score `1.8936` n `193` status `ready` deltaP `10.7607` edge `0.2089` maxDD `-4.1604`
- `market_context_high->crypto_alt_1h` score `1.8268` n `194` status `ready` deltaP `12.2708` edge `0.1818` maxDD `-4.9097`
- `market_context_high->equity_24h` score `1.7939` n `193` status `ready` deltaP `21.8307` edge `0.4938` maxDD `-33.1875`
- `market_context_high->equity_1h` score `0.6241` n `194` status `ready` deltaP `9.5917` edge `0.0669` maxDD `-2.6402`
- `market_context_high->unknown_1h` score `0.5323` n `194` status `ready` deltaP `5.2534` edge `0.0813` maxDD `-3.0902`
- `market_context_high->crypto_major_24h` score `0.2246` n `193` status `ready` deltaP `21.1647` edge `0.7362` maxDD `-62.3533`
- `market_context_high->index_1h` score `-0.0124` n `194` status `ready` deltaP `4.7704` edge `0.0262` maxDD `-1.3898`
- `market_context_high->fx_24h` score `-0.1336` n `193` status `ready` deltaP `14.7561` edge `0.0298` maxDD `-2.811`
- `market_context_high->metal_4h` score `-0.148` n `194` status `ready` deltaP `13.2999` edge `0.1535` maxDD `-11.3602`
- `market_context_high->metal_1h` score `-0.4291` n `194` status `ready` deltaP `5.238` edge `0.0314` maxDD `-5.166`
- `market_context_high->fx_1h` score `-0.8483` n `194` status `ready` deltaP `-1.4137` edge `0.0015` maxDD `-0.3548`
- `market_context_high->fx_4h` score `-1.3237` n `194` status `ready` deltaP `-3.5203` edge `0.0013` maxDD `-1.0513`
- `market_context_high->metal_24h` score `-1.4147` n `193` status `ready` deltaP `10.9687` edge `0.1991` maxDD `-23.2095`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
