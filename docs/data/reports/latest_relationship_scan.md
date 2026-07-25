# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-25T10:37:30.715971+00:00`
- Price records: `672`
- Market context records: `7869`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14667`

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

- `market_context_high->equity_24h` score `12.4082` n `120` status `ready` deltaP `29.145` edge `0.9739` maxDD `-6.0681`
- `market_context_high->metal_24h` score `2.4915` n `121` status `ready` deltaP `14.4549` edge `0.2637` maxDD `-1.8622`
- `market_context_high->equity_4h` score `2.2898` n `121` status `ready` deltaP `9.3221` edge `0.3564` maxDD `-5.6655`
- `market_context_high->crypto_major_4h` score `1.5965` n `121` status `ready` deltaP `17.2874` edge `0.1896` maxDD `-6.7444`
- `market_context_high->commodity_24h` score `1.3704` n `120` status `ready` deltaP `21.2174` edge `0.1311` maxDD `-7.0012`
- `market_context_high->crypto_alt_4h` score `1.3358` n `121` status `ready` deltaP `12.2001` edge `0.1417` maxDD `-3.9374`
- `market_context_high->crypto_major_1h` score `1.2706` n `121` status `ready` deltaP `14.1634` edge `0.0514` maxDD `-1.5286`
- `market_context_high->fx_24h` score `1.0304` n `120` status `ready` deltaP `28.855` edge `0.0485` maxDD `-3.0343`
- `market_context_high->equity_1h` score `0.6982` n `121` status `ready` deltaP `10.1059` edge `0.1039` maxDD `-4.2072`
- `market_context_high->crypto_alt_1h` score `0.3866` n `121` status `ready` deltaP `5.216` edge `0.0407` maxDD `-1.4603`
- `market_context_high->commodity_4h` score `0.3172` n `121` status `ready` deltaP `7.0033` edge `0.0391` maxDD `-1.0817`
- `market_context_high->index_1h` score `0.2397` n `121` status `ready` deltaP `8.5263` edge `0.0169` maxDD `-0.7743`
- `market_context_high->commodity_1h` score `0.0015` n `121` status `ready` deltaP `4.8494` edge `0.0137` maxDD `-0.6722`
- `market_context_high->index_4h` score `-0.1577` n `121` status `ready` deltaP `10.7603` edge `0.053` maxDD `-1.263`
- `market_context_high->fx_1h` score `-0.3017` n `121` status `ready` deltaP `0.036` edge `-0.0002` maxDD `-0.4304`
- `market_context_high->metal_4h` score `-0.6475` n `121` status `ready` deltaP `4.6576` edge `0.0861` maxDD `-1.3551`
- `market_context_high->metal_1h` score `-0.9406` n `121` status `ready` deltaP `0.0235` edge `0.0218` maxDD `-0.6936`
- `market_context_high->index_24h` score `-1.2021` n `120` status `ready` deltaP `-3.2319` edge `0.1041` maxDD `-1.9519`
- `market_context_high->fx_4h` score `-1.2961` n `121` status `ready` deltaP `-2.5324` edge `0.0004` maxDD `-1.6415`
- `market_context_high->crypto_alt_24h` score `-1.5298` n `121` status `ready` deltaP `14.4305` edge `0.2372` maxDD `-28.3623`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
