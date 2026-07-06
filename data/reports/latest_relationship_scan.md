# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-06T00:37:25.636645+00:00`
- Price records: `672`
- Market context records: `5828`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10076`

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

- `market_context_high->equity_4h` score `0.4888` n `275` status `ready` deltaP `7.1419` edge `0.1389` maxDD `-6.9958`
- `market_context_high->fx_1h` score `-0.2537` n `275` status `ready` deltaP `2.3424` edge `0.0004` maxDD `-0.5499`
- `market_context_high->equity_24h` score `-0.4021` n `247` status `ready` deltaP `15.3431` edge `0.3721` maxDD `-31.6316`
- `market_context_high->commodity_1h` score `-0.5269` n `275` status `ready` deltaP `-0.7599` edge `-0.0016` maxDD `-2.2045`
- `market_context_high->equity_1h` score `-0.5546` n `275` status `ready` deltaP `3.221` edge `0.033` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.5896` n `275` status `ready` deltaP `2.5139` edge `0.0012` maxDD `-2.0339`
- `market_context_high->index_1h` score `-0.5967` n `275` status `ready` deltaP `0.6102` edge `0.0042` maxDD `-0.7819`
- `market_context_high->crypto_major_1h` score `-0.8999` n `275` status `ready` deltaP `3.0915` edge `0.0365` maxDD `-6.2348`
- `market_context_high->crypto_alt_1h` score `-1.0696` n `275` status `ready` deltaP `1.4872` edge `0.0344` maxDD `-6.6758`
- `market_context_high->index_4h` score `-1.1501` n `275` status `ready` deltaP `1.0172` edge `0.0145` maxDD `-3.165`
- `market_context_high->fx_24h` score `-1.5222` n `247` status `ready` deltaP `9.2316` edge `0.0251` maxDD `-5.5435`
- `market_context_high->fx_4h` score `-1.5775` n `275` status `ready` deltaP `-1.1313` edge `0.0002` maxDD `-2.2593`
- `market_context_high->metal_4h` score `-2.2246` n `275` status `ready` deltaP `-5.0709` edge `-0.0455` maxDD `-9.1388`
- `market_context_high->commodity_4h` score `-2.7056` n `275` status `ready` deltaP `-1.3586` edge `-0.0166` maxDD `-8.6511`
- `market_context_high->index_24h` score `-2.8343` n `247` status `ready` deltaP `3.5531` edge `0.0274` maxDD `-18.1572`
- `market_context_high->crypto_major_4h` score `-3.0428` n `275` status `ready` deltaP `6.8354` edge `0.1381` maxDD `-25.6458`
- `market_context_high->crypto_alt_4h` score `-4.8088` n `275` status `ready` deltaP `4.1724` edge `0.0723` maxDD `-28.7346`
- `market_context_high->commodity_24h` score `-5.7619` n `247` status `ready` deltaP `-12.2927` edge `-0.0608` maxDD `-30.3426`
- `market_context_high->metal_24h` score `-6.6762` n `247` status `ready` deltaP `-1.4311` edge `-0.2216` maxDD `-15.0169`
- `market_context_high->crypto_alt_24h` score `-12.623` n `247` status `ready` deltaP `-10.4469` edge `-0.518` maxDD `-61.7883`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
