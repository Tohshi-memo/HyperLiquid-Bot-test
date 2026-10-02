# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-02T11:22:28.978210+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4842`

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

- `market_context_high->unknown_1h` score `341.185` n `50` status `ready` deltaP `10.5749` edge `28.3665` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `290.0883` n `50` status `ready` deltaP `10.5183` edge `24.1039` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `15.5442` n `73` status `ready` deltaP `39.795` edge `1.051` maxDD `-1.0093`
- `news_risk_high->equity_24h` score `10.2731` n `73` status `ready` deltaP `35.5308` edge `0.6677` maxDD `-2.8784`
- `market_context_high->crypto_major_24h` score `10.2147` n `50` status `ready` deltaP `34.7778` edge `0.761` maxDD `-9.3299`
- `market_context_high->crypto_alt_24h` score `9.0405` n `50` status `ready` deltaP `16.5347` edge `0.8141` maxDD `-11.6768`
- `market_context_high->crypto_major_4h` score `6.8441` n `50` status `ready` deltaP `16.9329` edge `0.5278` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `4.8175` n `50` status `ready` deltaP `14.8171` edge `0.432` maxDD `-7.6792`
- `news_risk_high->crypto_alt_4h` score `4.4391` n `106` status `ready` deltaP `18.402` edge `0.3816` maxDD `-6.4152`
- `market_context_high->crypto_alt_1h` score `3.0188` n `50` status `ready` deltaP `14.503` edge `0.2212` maxDD `-3.6387`
- `market_context_high->fx_4h` score `2.9443` n `50` status `ready` deltaP `32.8415` edge `0.0399` maxDD `-0.0791`
- `market_context_high->crypto_major_1h` score `2.9388` n `50` status `ready` deltaP `14.1497` edge `0.1956` maxDD `-2.2692`
- `news_risk_high->equity_4h` score `2.6009` n `106` status `ready` deltaP `24.186` edge `0.1251` maxDD `-2.9013`
- `market_context_high->equity_24h` score `2.5041` n `50` status `ready` deltaP `11.75` edge `0.4289` maxDD `-11.8957`
- `news_risk_high->crypto_major_24h` score `2.3044` n `73` status `ready` deltaP `8.9422` edge `0.5512` maxDD `-15.8971`
- `market_context_high->fx_1h` score `1.4651` n `50` status `ready` deltaP `20.491` edge `0.0119` maxDD `-0.113`
- `news_risk_high->metal_24h` score `1.2628` n `73` status `ready` deltaP `12.3145` edge `0.2072` maxDD `-2.192`
- `news_risk_high->crypto_major_4h` score `0.9311` n `106` status `ready` deltaP `12.1404` edge `0.2694` maxDD `-10.477`
- `market_context_high->index_24h` score `0.9168` n `50` status `ready` deltaP `15.1389` edge `0.0737` maxDD `-1.2338`
- `news_risk_high->crypto_alt_1h` score `0.8598` n `116` status `ready` deltaP `5.3996` edge `0.0919` maxDD `-2.4998`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
