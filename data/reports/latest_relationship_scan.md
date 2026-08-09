# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-09T10:22:26.259574+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8841`

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

- `market_context_high->equity_24h` score `3.792` n `103` status `ready` deltaP `4.5729` edge `0.5915` maxDD `-21.1456`
- `market_context_high->metal_24h` score `2.6258` n `103` status `ready` deltaP `12.2118` edge `0.195` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.1438` n `143` status `ready` deltaP `14.7472` edge `0.0643` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.7773` n `143` status `ready` deltaP `10.6916` edge `0.0278` maxDD `-0.7439`
- `market_context_high->fx_24h` score `0.7634` n `103` status `ready` deltaP `21.575` edge `0.0407` maxDD `-1.9329`
- `market_context_high->index_24h` score `0.561` n `103` status `ready` deltaP `9.1002` edge `0.1644` maxDD `-5.9181`
- `market_context_high->fx_1h` score `-0.3073` n `143` status `ready` deltaP `4.1456` edge `-0.0037` maxDD `-0.9639`
- `market_context_high->index_1h` score `-0.4065` n `143` status `ready` deltaP `-1.2436` edge `-0.0049` maxDD `-0.7809`
- `market_context_high->fx_4h` score `-0.4761` n `143` status `ready` deltaP `5.8279` edge `-0.0032` maxDD `-1.6928`
- `market_context_high->metal_1h` score `-0.6729` n `143` status `ready` deltaP `-4.5883` edge `-0.0061` maxDD `-0.9664`
- `market_context_high->index_4h` score `-0.8368` n `143` status `ready` deltaP `-0.1535` edge `-0.0082` maxDD `-1.1743`
- `market_context_high->equity_1h` score `-0.8725` n `143` status `ready` deltaP `0.2618` edge `0.0084` maxDD `-4.6286`
- `market_context_high->metal_4h` score `-0.9647` n `143` status `ready` deltaP `-0.8986` edge `-0.0168` maxDD `-2.7373`
- `market_context_high->crypto_alt_1h` score `-1.8569` n `143` status `ready` deltaP `-9.8342` edge `-0.025` maxDD `-2.4677`
- `market_context_high->equity_4h` score `-2.4761` n `143` status `ready` deltaP `-0.9615` edge `-0.0662` maxDD `-7.6983`
- `market_context_high->crypto_major_1h` score `-3.0597` n `143` status `ready` deltaP `-9.9389` edge `-0.0565` maxDD `-7.2436`
- `market_context_high->crypto_major_24h` score `-3.4785` n `103` status `ready` deltaP `4.6572` edge `-0.0715` maxDD `-14.2873`
- `market_context_high->crypto_alt_4h` score `-3.5099` n `143` status `ready` deltaP `-6.1424` edge `-0.0859` maxDD `-6.585`
- `market_context_high->crypto_alt_24h` score `-5.3487` n `103` status `ready` deltaP `-14.7031` edge `-0.2034` maxDD `-4.5445`
- `market_context_high->unknown_1h` score `-7.7813` n `143` status `ready` deltaP `-5.6447` edge `-0.5661` maxDD `-1.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
