# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-26T13:22:32.595119+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8396`

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

- `market_context_high->unknown_4h` score `15.7551` n `144` status `ready` deltaP `-0.1863` edge `1.3477` maxDD `-1.016`
- `market_context_high->metal_24h` score `0.5736` n `113` status `ready` deltaP `28.2709` edge `0.1521` maxDD `-7.3625`
- `market_context_high->fx_4h` score `0.206` n `144` status `ready` deltaP `10.2473` edge `0.0087` maxDD `-0.4545`
- `market_context_high->fx_1h` score `0.1095` n `151` status `ready` deltaP `6.4411` edge `0.002` maxDD `-0.1986`
- `market_context_high->fx_24h` score `0.011` n `113` status `ready` deltaP `19.446` edge `0.029` maxDD `-1.2451`
- `market_context_high->metal_1h` score `-0.255` n `151` status `ready` deltaP `6.6592` edge `0.0021` maxDD `-1.6682`
- `market_context_high->commodity_1h` score `-0.3115` n `151` status `ready` deltaP `1.9957` edge `0.0108` maxDD `-1.0053`
- `market_context_high->index_24h` score `-0.4167` n `113` status `ready` deltaP `11.4768` edge `-0.0017` maxDD `-4.925`
- `market_context_high->commodity_4h` score `-0.4883` n `144` status `ready` deltaP `5.9112` edge `0.0428` maxDD `-1.165`
- `market_context_high->index_1h` score `-0.565` n `151` status `ready` deltaP `-0.9071` edge `-0.0012` maxDD `-1.2155`
- `market_context_high->metal_4h` score `-1.0283` n `144` status `ready` deltaP `6.3855` edge `-0.0034` maxDD `-5.3474`
- `market_context_high->crypto_major_1h` score `-1.1953` n `151` status `ready` deltaP `2.1047` edge `-0.0092` maxDD `-9.3126`
- `market_context_high->index_4h` score `-1.9056` n `144` status `ready` deltaP `-5.7249` edge `-0.0187` maxDD `-4.3282`
- `market_context_high->equity_1h` score `-2.2437` n `151` status `ready` deltaP `-1.1609` edge `-0.0513` maxDD `-12.2891`
- `market_context_high->crypto_alt_1h` score `-2.3291` n `151` status `ready` deltaP `-2.5261` edge `-0.0333` maxDD `-13.2099`
- `market_context_high->crypto_major_24h` score `-4.401` n `113` status `ready` deltaP `-2.0726` edge `-0.0647` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-4.9472` n `144` status `ready` deltaP `-2.3205` edge `-0.1148` maxDD `-32.9851`
- `market_context_high->equity_24h` score `-6.1387` n `113` status `ready` deltaP `-2.8178` edge `-0.2107` maxDD `-36.6024`
- `market_context_high->commodity_24h` score `-6.4739` n `113` status `ready` deltaP `-18.8191` edge `-0.1456` maxDD `-24.0477`
- `market_context_high->equity_4h` score `-7.7214` n `144` status `ready` deltaP `-4.1328` edge `-0.2362` maxDD `-45.7601`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
