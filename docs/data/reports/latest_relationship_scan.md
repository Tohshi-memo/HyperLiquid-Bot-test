# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-13T20:37:24.496659+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `10548`

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

- `market_context_high->unknown_24h` score `370.0976` n `75` status `ready` deltaP `2.8889` edge `30.8363` maxDD `-0.4606`
- `news_risk_high->equity_24h` score `34.3432` n `53` status `ready` deltaP `34.0147` edge `2.7058` maxDD `-3.6503`
- `market_context_high->equity_24h` score `26.1096` n `75` status `ready` deltaP `28.5555` edge `2.1396` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `17.013` n `75` status `ready` deltaP `47.5834` edge `1.352` maxDD `-16.4511`
- `news_risk_high->crypto_major_24h` score `14.4848` n `53` status `ready` deltaP `42.0434` edge `1.7733` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `10.8974` n `53` status `ready` deltaP `34.7158` edge `0.7897` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `5.813` n `53` status `ready` deltaP `37.8472` edge `0.2321` maxDD `0.0`
- `market_context_high->index_24h` score `5.0189` n `75` status `ready` deltaP `27.2986` edge `0.2454` maxDD `-0.0653`
- `news_risk_high->metal_4h` score `4.8653` n `53` status `ready` deltaP `46.0913` edge `0.1358` maxDD `-1.0104`
- `news_risk_high->index_24h` score `4.3379` n `53` status `ready` deltaP `25.3111` edge `0.2231` maxDD `-0.4279`
- `market_context_high->metal_24h` score `4.0363` n `75` status `ready` deltaP `40.6389` edge `0.3357` maxDD `-3.7989`
- `news_risk_high->equity_1h` score `3.4174` n `53` status `ready` deltaP `17.7155` edge `0.2297` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.29` n `53` status `ready` deltaP `29.9126` edge `0.1001` maxDD `-0.3611`
- `news_risk_high->crypto_major_4h` score `3.0885` n `53` status `ready` deltaP `19.2189` edge `0.278` maxDD `-9.2335`
- `news_risk_high->metal_1h` score `2.2517` n `53` status `ready` deltaP `26.3388` edge `0.0375` maxDD `-0.3692`
- `news_risk_high->index_4h` score `1.9446` n `53` status `ready` deltaP `19.5266` edge `0.0755` maxDD `-0.8235`
- `news_risk_high->crypto_alt_24h` score `1.8526` n `53` status `ready` deltaP `14.4261` edge `0.5919` maxDD `-29.0448`
- `news_risk_high->crypto_alt_4h` score `1.7285` n `53` status `ready` deltaP `25.5838` edge `0.2149` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.1723` n `53` status `ready` deltaP `15.9784` edge `0.0213` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.5754` n `53` status `ready` deltaP `16.5461` edge `0.0614` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
