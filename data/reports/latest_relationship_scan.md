# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-08T22:22:27.770230+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `64`

- Symbol pattern count: `6521`

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

- `market_context_high->unknown_4h` score `53.158` n `42` status `ready` deltaP `-3.3464` edge `4.4969` maxDD `-0.9139`
- `market_context_high->equity_24h` score `4.8396` n `37` status `ready` deltaP `11.2472` edge `0.7578` maxDD `-31.3588`
- `market_context_high->fx_4h` score `2.0047` n `42` status `ready` deltaP `23.2723` edge `0.035` maxDD `-0.1807`
- `market_context_high->index_4h` score `1.3014` n `42` status `ready` deltaP `19.2945` edge `0.031` maxDD `-2.4279`
- `market_context_high->index_24h` score `1.1659` n `37` status `ready` deltaP `14.6913` edge `0.1146` maxDD `-2.7123`
- `market_context_high->fx_24h` score `0.8726` n `37` status `ready` deltaP `10.9422` edge `0.0086` maxDD `-0.0397`
- `market_context_high->equity_1h` score `0.4783` n `54` status `ready` deltaP `3.3489` edge `0.131` maxDD `-4.0272`
- `market_context_high->commodity_1h` score `0.2847` n `54` status `ready` deltaP `11.3717` edge `0.0153` maxDD `-1.7019`
- `market_context_high->commodity_4h` score `0.0509` n `42` status `ready` deltaP `2.9326` edge `0.0301` maxDD `-1.633`
- `market_context_high->commodity_24h` score `-0.0732` n `37` status `ready` deltaP `2.5667` edge `0.093` maxDD `-6.5601`
- `market_context_high->metal_1h` score `-0.0877` n `54` status `ready` deltaP `2.301` edge `0.0062` maxDD `-0.6226`
- `market_context_high->index_1h` score `-0.3245` n `54` status `ready` deltaP `-2.2067` edge `0.0211` maxDD `-0.506`
- `market_context_high->fx_1h` score `-0.4764` n `54` status `ready` deltaP `-5.3892` edge `0.0063` maxDD `-0.1825`
- `market_context_high->crypto_alt_1h` score `-1.2608` n `54` status `ready` deltaP `2.1346` edge `-0.0331` maxDD `-7.0884`
- `market_context_high->metal_4h` score `-1.5024` n `42` status `ready` deltaP `-6.3226` edge `-0.0372` maxDD `-1.0015`
- `market_context_high->metal_24h` score `-1.5861` n `37` status `ready` deltaP `7.6999` edge `-0.1282` maxDD `-1.4245`
- `market_context_high->crypto_major_1h` score `-1.7285` n `54` status `ready` deltaP `-0.2606` edge `-0.0671` maxDD `-7.8882`
- `market_context_high->equity_4h` score `-1.9359` n `42` status `ready` deltaP `18.0387` edge `0.0464` maxDD `-24.9053`
- `market_context_high->crypto_alt_4h` score `-3.1734` n `42` status `ready` deltaP `12.1371` edge `-0.0969` maxDD `-17.5435`
- `market_context_high->crypto_major_4h` score `-5.7915` n `42` status `ready` deltaP `-0.2831` edge `-0.237` maxDD `-17.4991`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
