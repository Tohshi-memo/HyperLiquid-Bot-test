# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-30T12:37:33.276810+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7492`

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

- `market_context_high->unknown_1h` score `403.465` n `51` status `ready` deltaP `7.9194` edge `33.5742` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `321.4437` n `44` status `ready` deltaP `8.2317` edge `26.7321` maxDD `0.0`
- `news_risk_high->unknown_24h` score `69.55` n `135` status `ready` deltaP `1.9097` edge `5.7831` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `16.1272` n `135` status `ready` deltaP `26.8171` edge `1.1861` maxDD `-1.0093`
- `news_risk_high->equity_24h` score `6.8824` n `135` status `ready` deltaP `25.4282` edge `0.6389` maxDD `-9.4579`
- `news_risk_high->crypto_major_24h` score `6.3717` n `135` status `ready` deltaP `23.9931` edge `0.6864` maxDD `-15.8971`
- `market_context_high->crypto_major_4h` score `4.8344` n `44` status `ready` deltaP `14.551` edge `0.3762` maxDD `-3.294`
- `news_risk_high->index_24h` score `3.3971` n `135` status `ready` deltaP `31.6204` edge `0.1201` maxDD `-0.4916`
- `market_context_high->fx_4h` score `3.3716` n `44` status `ready` deltaP `37.6386` edge `0.0431` maxDD `-0.0449`
- `news_risk_high->metal_24h` score `2.9408` n `135` status `ready` deltaP `23.2754` edge `0.2173` maxDD `-2.192`
- `news_risk_high->equity_4h` score `2.5619` n `135` status `ready` deltaP `27.6468` edge `0.1893` maxDD `-9.143`
- `market_context_high->crypto_major_1h` score `2.3154` n `51` status `ready` deltaP `14.8409` edge `0.155` maxDD `-3.546`
- `market_context_high->crypto_alt_1h` score `2.0406` n `51` status `ready` deltaP `12.7598` edge `0.1513` maxDD `-3.6387`
- `market_context_high->fx_1h` score `1.4789` n `51` status `ready` deltaP `20.7086` edge `0.0116` maxDD `-0.113`
- `market_context_high->crypto_alt_4h` score `1.2156` n `44` status `ready` deltaP `10.4213` edge `0.2157` maxDD `-7.6792`
- `news_risk_high->equity_1h` score `0.8936` n `135` status `ready` deltaP `9.5509` edge `0.0731` maxDD `-1.6514`
- `news_risk_high->crypto_alt_1h` score `0.8356` n `135` status `ready` deltaP `8.0539` edge `0.107` maxDD `-4.2849`
- `news_risk_high->crypto_alt_4h` score `0.5413` n `135` status `ready` deltaP `8.2159` edge `0.2563` maxDD `-15.9436`
- `news_risk_high->index_1h` score `0.479` n `135` status `ready` deltaP `8.6682` edge `0.0109` maxDD `-0.302`
- `market_context_high->commodity_1h` score `-0.0103` n `51` status `ready` deltaP `9.1229` edge `-0.0075` maxDD `-2.3717`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
