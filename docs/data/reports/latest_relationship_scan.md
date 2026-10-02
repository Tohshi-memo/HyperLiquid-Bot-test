# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-02T13:07:30.686679+00:00`
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

- `market_context_high->unknown_1h` score `360.4029` n `50` status `ready` deltaP `11.024` edge `29.965` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `292.0808` n `50` status `ready` deltaP `10.9756` edge `24.2669` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `15.4674` n `73` status `ready` deltaP `39.795` edge `1.0446` maxDD `-1.0093`
- `news_risk_high->equity_24h` score `9.8747` n `73` status `ready` deltaP `34.3155` edge `0.6426` maxDD `-2.8784`
- `market_context_high->crypto_major_24h` score `9.6651` n `50` status `ready` deltaP `33.5625` edge `0.7233` maxDD `-9.3299`
- `market_context_high->crypto_alt_24h` score `8.9637` n `50` status `ready` deltaP `16.5347` edge `0.8077` maxDD `-11.6768`
- `market_context_high->crypto_major_4h` score `6.597` n `50` status `ready` deltaP `16.0183` edge `0.5133` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `4.6339` n `50` status `ready` deltaP `13.9024` edge `0.4228` maxDD `-7.6792`
- `news_risk_high->crypto_alt_4h` score `4.3159` n `112` status `ready` deltaP `18.9024` edge `0.368` maxDD `-6.4152`
- `market_context_high->fx_4h` score `2.9443` n `50` status `ready` deltaP `32.8415` edge `0.0399` maxDD `-0.0791`
- `market_context_high->crypto_alt_1h` score `2.8774` n `50` status `ready` deltaP `13.7545` edge `0.2144` maxDD `-3.6387`
- `market_context_high->crypto_major_1h` score `2.8369` n `50` status `ready` deltaP `13.7006` edge `0.1901` maxDD `-2.2692`
- `news_risk_high->equity_4h` score `2.2988` n `112` status `ready` deltaP `22.0601` edge `0.1141` maxDD `-2.9013`
- `market_context_high->equity_24h` score `2.2451` n `50` status `ready` deltaP `10.5347` edge `0.4038` maxDD `-11.8957`
- `news_risk_high->crypto_major_24h` score `1.9471` n `73` status `ready` deltaP `7.7269` edge `0.5135` maxDD `-15.8971`
- `market_context_high->fx_1h` score `1.4891` n `50` status `ready` deltaP `20.7904` edge `0.0119` maxDD `-0.113`
- `news_risk_high->metal_24h` score `1.2385` n `73` status `ready` deltaP `11.9673` edge `0.2064` maxDD `-2.192`
- `news_risk_high->crypto_major_4h` score `0.8842` n `112` status `ready` deltaP `12.304` edge `0.2623` maxDD `-10.477`
- `market_context_high->index_24h` score `0.8557` n `50` status `ready` deltaP `14.4444` edge `0.0705` maxDD `-1.2338`
- `news_risk_high->index_24h` score `0.7564` n `73` status `ready` deltaP `14.3074` edge `0.0494` maxDD `-0.4916`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
