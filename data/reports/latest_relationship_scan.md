# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-13T10:52:27.532000+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `10524`

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

- `market_context_high->unknown_24h` score `353.5339` n `74` status `ready` deltaP `5.9779` edge `29.4354` maxDD `-0.4606`
- `news_risk_high->equity_24h` score `32.6958` n `53` status `ready` deltaP `31.9314` edge `2.5824` maxDD `-3.6503`
- `market_context_high->equity_24h` score `26.0157` n `74` status `ready` deltaP `27.5713` edge `2.0866` maxDD `-5.8613`
- `market_context_high->unknown_4h` score `25.9641` n `80` status `ready` deltaP `5.2439` edge `2.1735` maxDD `-0.9162`
- `news_risk_high->crypto_major_24h` score `14.1098` n `53` status `ready` deltaP `42.3906` edge `1.7229` maxDD `-12.7247`
- `market_context_high->crypto_alt_24h` score `10.9983` n `74` status `ready` deltaP `50.0938` edge `1.4229` maxDD `-22.4123`
- `news_risk_high->equity_4h` score `10.5334` n `53` status `ready` deltaP `35.3255` edge `0.7553` maxDD `-7.0416`
- `market_context_high->metal_24h` score `7.0831` n `74` status `ready` deltaP `43.8907` edge `0.3559` maxDD `-1.6597`
- `news_risk_high->commodity_24h` score `6.0064` n `53` status `ready` deltaP `38.1944` edge `0.2459` maxDD `0.0`
- `news_risk_high->metal_4h` score `4.612` n `53` status `ready` deltaP `44.1096` edge `0.1279` maxDD `-1.0104`
- `market_context_high->index_24h` score `4.6079` n `74` status `ready` deltaP `23.6017` edge `0.2358` maxDD `-0.0653`
- `news_risk_high->index_24h` score `4.1665` n `53` status `ready` deltaP `24.4431` edge `0.2146` maxDD `-0.4279`
- `news_risk_high->equity_1h` score `3.289` n `53` status `ready` deltaP `17.5658` edge `0.22` maxDD `-3.7082`
- `news_risk_high->crypto_major_4h` score `3.2683` n `53` status `ready` deltaP `19.9811` edge `0.2879` maxDD `-9.2335`
- `news_risk_high->commodity_4h` score `3.1289` n `53` status `ready` deltaP `28.6931` edge `0.0948` maxDD `-0.3611`
- `news_risk_high->crypto_alt_24h` score `3.1142` n `53` status `ready` deltaP `19.9816` edge `0.7166` maxDD `-29.0448`
- `news_risk_high->metal_1h` score `2.0912` n `53` status `ready` deltaP `24.6921` edge `0.0351` maxDD `-0.3692`
- `news_risk_high->index_4h` score `1.9502` n `53` status `ready` deltaP `20.1363` edge `0.0719` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.8516` n `53` status `ready` deltaP `26.346` edge `0.2256` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.1723` n `53` status `ready` deltaP `16.1281` edge `0.0203` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
