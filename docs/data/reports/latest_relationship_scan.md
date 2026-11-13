# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-13T01:37:28.750105+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11760`

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

- `market_context_high->unknown_24h` score `298.0261` n `84` status `ready` deltaP `6.2996` edge `24.8076` maxDD `-0.4606`
- `market_context_high->unknown_4h` score `62.4674` n `94` status `ready` deltaP `7.8004` edge `5.1984` maxDD `-0.9162`
- `news_risk_high->equity_24h` score `30.525` n `53` status `ready` deltaP `26.2022` edge `2.4397` maxDD `-3.6503`
- `market_context_high->equity_24h` score `22.5076` n `84` status `ready` deltaP `23.9335` edge `1.7867` maxDD `-1.983`
- `news_risk_high->crypto_major_24h` score `12.1519` n `53` status `ready` deltaP `38.7448` edge `1.4962` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `9.4633` n `53` status `ready` deltaP `32.7341` edge `0.6834` maxDD `-7.0416`
- `market_context_high->crypto_alt_24h` score `9.2693` n `84` status `ready` deltaP `44.6925` edge `1.3` maxDD `-25.4331`
- `news_risk_high->commodity_24h` score `7.0847` n `53` status `ready` deltaP `43.2292` edge `0.3022` maxDD `0.0`
- `market_context_high->metal_24h` score `6.6042` n `84` status `ready` deltaP `40.253` edge `0.3233` maxDD `-0.3044`
- `news_risk_high->metal_4h` score `4.5124` n `53` status `ready` deltaP `43.1949` edge `0.1257` maxDD `-1.0104`
- `market_context_high->index_24h` score `4.343` n `84` status `ready` deltaP `24.6776` edge `0.2069` maxDD `-0.0934`
- `news_risk_high->index_24h` score `3.9347` n `53` status `ready` deltaP `22.8806` edge `0.2057` maxDD `-0.4279`
- `news_risk_high->commodity_4h` score `3.0655` n `53` status `ready` deltaP `27.9309` edge `0.0946` maxDD `-0.3611`
- `news_risk_high->equity_1h` score `2.988` n `53` status `ready` deltaP `16.8173` edge `0.1999` maxDD `-3.7082`
- `news_risk_high->crypto_major_4h` score `2.6387` n `53` status `ready` deltaP `19.3713` edge `0.2395` maxDD `-9.2335`
- `news_risk_high->metal_1h` score `2.1199` n `53` status `ready` deltaP `25.1412` edge `0.0345` maxDD `-0.3692`
- `news_risk_high->crypto_alt_24h` score `1.8317` n `53` status `ready` deltaP `14.7733` edge `0.5869` maxDD `-29.0448`
- `news_risk_high->index_4h` score `1.6895` n `53` status `ready` deltaP `18.0022` edge `0.0644` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.4086` n `53` status `ready` deltaP `24.5168` edge `0.181` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.0932` n `53` status `ready` deltaP `15.5293` edge `0.0177` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
