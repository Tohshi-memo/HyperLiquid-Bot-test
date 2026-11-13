# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-13T04:22:26.264802+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11820`

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

- `market_context_high->unknown_24h` score `285.2965` n `84` status `ready` deltaP `6.2996` edge `23.7468` maxDD `-0.4606`
- `market_context_high->unknown_4h` score `55.7716` n `94` status `ready` deltaP `7.0382` edge `4.6455` maxDD `-0.9162`
- `news_risk_high->equity_24h` score `31.2142` n `53` status `ready` deltaP `28.1119` edge `2.4844` maxDD `-3.6503`
- `market_context_high->equity_24h` score `23.1968` n `84` status `ready` deltaP `25.8432` edge `1.8314` maxDD `-1.983`
- `news_risk_high->crypto_major_24h` score `12.6356` n `53` status `ready` deltaP `39.092` edge `1.5559` maxDD `-12.7247`
- `market_context_high->crypto_alt_24h` score `9.775` n `84` status `ready` deltaP `46.6022` edge `1.3521` maxDD `-25.4331`
- `news_risk_high->equity_4h` score `9.4933` n `53` status `ready` deltaP `32.7341` edge `0.6859` maxDD `-7.0416`
- `market_context_high->metal_24h` score `6.8674` n `84` status `ready` deltaP `42.1627` edge `0.3325` maxDD `-0.3044`
- `news_risk_high->commodity_24h` score `6.76` n `53` status `ready` deltaP `41.8403` edge `0.2844` maxDD `0.0`
- `market_context_high->index_24h` score `4.4333` n `84` status `ready` deltaP `25.372` edge `0.2098` maxDD `-0.0934`
- `news_risk_high->metal_4h` score `4.2895` n `53` status `ready` deltaP `41.5181` edge `0.1183` maxDD `-1.0104`
- `news_risk_high->index_24h` score `4.025` n `53` status `ready` deltaP `23.575` edge `0.2086` maxDD `-0.4279`
- `news_risk_high->commodity_4h` score `3.2283` n `53` status `ready` deltaP `29.4553` edge `0.098` maxDD `-0.3611`
- `news_risk_high->equity_1h` score `3.1823` n `53` status `ready` deltaP `17.4161` edge `0.2121` maxDD `-3.7082`
- `news_risk_high->crypto_major_4h` score `2.8163` n `53` status `ready` deltaP `19.3713` edge `0.2543` maxDD `-9.2335`
- `news_risk_high->crypto_alt_24h` score `2.3373` n `53` status `ready` deltaP `16.683` edge `0.639` maxDD `-29.0448`
- `news_risk_high->metal_1h` score `2.0372` n `53` status `ready` deltaP `24.3927` edge `0.0326` maxDD `-0.3692`
- `news_risk_high->index_4h` score `1.6591` n `53` status `ready` deltaP `17.6973` edge `0.0639` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.6111` n `53` status `ready` deltaP `25.1265` edge `0.2029` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.1603` n `53` status `ready` deltaP `16.1281` edge `0.0193` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
