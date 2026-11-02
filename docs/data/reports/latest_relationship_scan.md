# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-02T07:07:28.815454+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5157`

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

- `market_context_high->unknown_24h` score `6211.4563` n `34` status `ready` deltaP `1.3889` edge `517.6121` maxDD `0.0`
- `market_context_high->unknown_4h` score `590.3465` n `39` status `ready` deltaP `8.8415` edge `49.1366` maxDD `0.0`
- `market_context_high->unknown_1h` score `149.4403` n `39` status `ready` deltaP `7.7269` edge `12.4129` maxDD `-0.2178`
- `market_context_high->equity_24h` score `19.4274` n `34` status `ready` deltaP `41.6769` edge `1.3647` maxDD `-1.5546`
- `news_risk_high->crypto_alt_24h` score `12.5033` n `98` status `ready` deltaP `31.0906` edge `0.9854` maxDD `-8.0585`
- `market_context_high->commodity_24h` score `7.2804` n `34` status `ready` deltaP `42.9432` edge `0.3515` maxDD `-0.8203`
- `market_context_high->index_24h` score `6.8322` n `34` status `ready` deltaP `49.1319` edge `0.2418` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `6.2187` n `39` status `ready` deltaP `26.2586` edge `0.3726` maxDD `-1.6876`
- `market_context_high->equity_4h` score `5.5673` n `39` status `ready` deltaP `9.6819` edge `0.4696` maxDD `-2.283`
- `market_context_high->crypto_major_4h` score `4.867` n `39` status `ready` deltaP `24.3316` edge `0.277` maxDD `-1.6901`
- `market_context_high->equity_1h` score `3.0873` n `39` status `ready` deltaP `10.9397` edge `0.2244` maxDD `-1.2043`
- `news_risk_high->crypto_alt_4h` score `2.4787` n `126` status `ready` deltaP `10.0803` edge `0.278` maxDD `-7.4246`
- `market_context_high->crypto_alt_1h` score `2.4368` n `39` status `ready` deltaP `9.2738` edge `0.1854` maxDD `-1.5324`
- `market_context_high->crypto_major_1h` score `2.1456` n `39` status `ready` deltaP `11.2391` edge `0.1429` maxDD `-1.1219`
- `market_context_high->index_4h` score `1.8822` n `39` status `ready` deltaP `19.481` edge `0.0553` maxDD `-0.5995`
- `market_context_high->crypto_alt_24h` score `1.7518` n `34` status `ready` deltaP `-7.4449` edge `0.3474` maxDD `-8.8096`
- `market_context_high->metal_4h` score `1.6742` n `39` status `ready` deltaP `19.5904` edge `0.0514` maxDD `-0.7323`
- `market_context_high->fx_1h` score `1.4359` n `39` status `ready` deltaP `18.7817` edge `0.0116` maxDD `-0.0388`
- `market_context_high->commodity_4h` score `1.2224` n `39` status `ready` deltaP `23.3193` edge `0.0425` maxDD `-1.633`
- `market_context_high->metal_1h` score `0.4959` n `39` status `ready` deltaP `10.1528` edge `0.0216` maxDD `-0.3895`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
