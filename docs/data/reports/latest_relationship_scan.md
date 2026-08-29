# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-29T08:52:24.597986+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11796`

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

- `news_risk_high->unknown_24h` score `53.5903` n `53` status `ready` deltaP `17.6035` edge `4.3761` maxDD `-1.2078`
- `news_risk_high->crypto_alt_24h` score `28.4182` n `53` status `ready` deltaP `41.0868` edge `2.2241` maxDD `-8.7194`
- `market_context_high->unknown_24h` score `8.1785` n `119` status `ready` deltaP `16.5412` edge `0.6445` maxDD `-3.1917`
- `news_risk_high->unknown_4h` score `6.2371` n `80` status `ready` deltaP `10.6707` edge `0.5076` maxDD `-1.7183`
- `news_risk_high->crypto_major_24h` score `6.1523` n `53` status `ready` deltaP `23.3425` edge `0.5031` maxDD `-10.0154`
- `market_context_high->metal_24h` score `3.6793` n `119` status `ready` deltaP `30.5891` edge `0.2046` maxDD `-3.1535`
- `news_risk_high->equity_24h` score `3.6357` n `53` status `ready` deltaP `25.7731` edge `0.4329` maxDD `-8.4222`
- `news_risk_high->metal_24h` score `3.5845` n `53` status `ready` deltaP `39.8486` edge `0.0678` maxDD `-1.7801`
- `news_risk_high->unknown_1h` score `2.662` n `80` status `ready` deltaP `5.524` edge `0.2207` maxDD `-0.8558`
- `market_context_high->unknown_4h` score `2.5651` n `119` status `ready` deltaP `19.7043` edge `0.1231` maxDD `-0.5894`
- `news_risk_high->fx_4h` score `2.3035` n `80` status `ready` deltaP `33.75` edge `0.0219` maxDD `-0.3953`
- `news_risk_high->index_24h` score `1.8942` n `53` status `ready` deltaP `22.255` edge `0.0339` maxDD `-0.6202`
- `market_context_high->unknown_1h` score `1.1512` n `120` status `ready` deltaP `8.8573` edge `0.0819` maxDD `-1.6015`
- `news_risk_high->fx_1h` score `0.6381` n `80` status `ready` deltaP `12.994` edge `0.0054` maxDD `-0.108`
- `news_risk_high->commodity_1h` score `0.4898` n `80` status `ready` deltaP `13.3982` edge `0.0055` maxDD `-0.5618`
- `market_context_high->metal_4h` score `-0.1585` n `119` status `ready` deltaP `9.2257` edge `0.0099` maxDD `-3.3377`
- `market_context_high->fx_1h` score `-0.3335` n `120` status `ready` deltaP `4.6607` edge `-0.0006` maxDD `-0.8587`
- `news_risk_high->index_1h` score `-0.3988` n `80` status `ready` deltaP `0.1572` edge `-0.0085` maxDD `-0.8275`
- `news_risk_high->commodity_4h` score `-0.5545` n `80` status `ready` deltaP `7.8049` edge `0.011` maxDD `-2.0635`
- `news_risk_high->index_4h` score `-0.5776` n `80` status `ready` deltaP `1.0061` edge `-0.0166` maxDD `-1.7996`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
