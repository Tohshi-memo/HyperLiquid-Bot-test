# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-30T07:52:37.600751+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7486`

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

- `news_risk_high->unknown_24h` score `962.2372` n `135` status `ready` deltaP `1.9097` edge `80.1737` maxDD `0.0`
- `market_context_high->unknown_1h` score `634.5752` n `37` status `ready` deltaP `9.7305` edge `52.8164` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `18.0685` n `135` status `ready` deltaP `28.5532` edge `1.3363` maxDD `-1.0093`
- `news_risk_high->equity_24h` score `8.0337` n `135` status `ready` deltaP `27.6852` edge `0.7198` maxDD `-9.4579`
- `news_risk_high->crypto_major_24h` score `7.6209` n `135` status `ready` deltaP `23.9931` edge `0.7905` maxDD `-15.8971`
- `news_risk_high->index_24h` score `3.7708` n `135` status `ready` deltaP `33.8773` edge `0.1362` maxDD `-0.4916`
- `news_risk_high->metal_24h` score `3.4055` n `135` status `ready` deltaP `26.0532` edge `0.2375` maxDD `-2.192`
- `news_risk_high->equity_4h` score `2.9` n `135` status `ready` deltaP `29.3236` edge `0.2063` maxDD `-9.143`
- `news_risk_high->crypto_alt_4h` score `1.818` n `135` status `ready` deltaP `10.9598` edge `0.3444` maxDD `-15.9436`
- `market_context_high->crypto_alt_1h` score `1.4443` n `37` status `ready` deltaP `8.8607` edge `0.1276` maxDD `-3.6387`
- `market_context_high->crypto_major_1h` score `1.4374` n `37` status `ready` deltaP `7.9463` edge `0.1278` maxDD `-3.546`
- `news_risk_high->crypto_alt_1h` score `1.097` n `135` status `ready` deltaP `9.4012` edge `0.1198` maxDD `-4.2849`
- `market_context_high->equity_1h` score `0.981` n `37` status `ready` deltaP `14.2661` edge `0.0732` maxDD `-2.4027`
- `market_context_high->fx_1h` score `0.945` n `37` status `ready` deltaP `14.2499` edge `0.006` maxDD `-0.113`
- `news_risk_high->equity_1h` score `0.9044` n `135` status `ready` deltaP `9.4012` edge `0.075` maxDD `-1.6514`
- `market_context_high->metal_1h` score `0.8497` n `37` status `ready` deltaP `10.0502` edge `0.0259` maxDD `-0.4338`
- `news_risk_high->index_1h` score `0.4921` n `135` status `ready` deltaP `8.8179` edge `0.011` maxDD `-0.302`
- `market_context_high->index_1h` score `0.3629` n `37` status `ready` deltaP `7.0562` edge `0.0169` maxDD `-0.3627`
- `news_risk_high->index_4h` score `-0.16` n `135` status `ready` deltaP `6.6441` edge `0.0277` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-0.5851` n `135` status `ready` deltaP `2.0403` edge `0.0659` maxDD `-7.2607`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
