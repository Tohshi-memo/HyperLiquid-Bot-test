# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-18T04:37:22.913730+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11837`

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

- `market_context_high->crypto_major_24h` score `3.3892` n `73` status `ready` deltaP `9.7078` edge `0.3385` maxDD `-4.9964`
- `market_context_high->commodity_24h` score `0.549` n `73` status `ready` deltaP `12.6469` edge `0.1694` maxDD `-4.666`
- `market_context_high->metal_24h` score `0.3258` n `73` status `ready` deltaP `4.8384` edge `0.0716` maxDD `-2.1368`
- `market_context_high->commodity_4h` score `0.2312` n `101` status `ready` deltaP `9.4799` edge `0.0411` maxDD `-2.4692`
- `market_context_high->metal_4h` score `0.2259` n `101` status `ready` deltaP `10.7763` edge `0.0147` maxDD `-1.273`
- `market_context_high->crypto_major_4h` score `0.1704` n `101` status `ready` deltaP `6.9669` edge `0.0775` maxDD `-3.1677`
- `market_context_high->index_1h` score `0.0416` n `104` status `ready` deltaP `6.6617` edge `0.0029` maxDD `-0.3584`
- `market_context_high->equity_1h` score `-0.0815` n `104` status `ready` deltaP `3.1956` edge `0.0285` maxDD `-1.8201`
- `market_context_high->unknown_1h` score `-0.1146` n `104` status `ready` deltaP `7.0705` edge `-0.0324` maxDD `-0.6096`
- `market_context_high->fx_4h` score `-0.2635` n `101` status `ready` deltaP `4.0735` edge `0.0016` maxDD `-0.3904`
- `market_context_high->metal_1h` score `-0.4933` n `104` status `ready` deltaP `-1.3243` edge `-0.0027` maxDD `-1.1376`
- `market_context_high->fx_1h` score `-0.5065` n `104` status `ready` deltaP `-1.1746` edge `0.0018` maxDD `-0.2273`
- `market_context_high->index_4h` score `-0.6383` n `101` status `ready` deltaP `-2.8662` edge `0.0018` maxDD `-0.4949`
- `market_context_high->commodity_1h` score `-0.6419` n `104` status `ready` deltaP `-3.4834` edge `0.0022` maxDD `-1.5684`
- `market_context_high->crypto_alt_1h` score `-0.6812` n `104` status `ready` deltaP `-1.6237` edge `0.0097` maxDD `-2.8964`
- `market_context_high->crypto_alt_4h` score `-0.8545` n `101` status `ready` deltaP `5.0652` edge `0.0604` maxDD `-8.2974`
- `market_context_high->crypto_major_1h` score `-0.8712` n `104` status `ready` deltaP `-2.6716` edge `0.0004` maxDD `-3.5426`
- `market_context_high->index_24h` score `-1.0693` n `73` status `ready` deltaP `3.3356` edge `-0.0758` maxDD `-2.682`
- `market_context_high->equity_4h` score `-1.0837` n `101` status `ready` deltaP `-5.4592` edge `0.0015` maxDD `-3.6565`
- `market_context_high->unknown_24h` score `-1.235` n `73` status `ready` deltaP `5.0117` edge `-0.0822` maxDD `-0.9967`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
