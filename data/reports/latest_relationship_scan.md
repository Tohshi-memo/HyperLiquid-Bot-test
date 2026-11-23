# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-23T03:52:33.012632+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5282`

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

- `market_context_high->unknown_1h` score `16016.1892` n `84` status `ready` deltaP `2.2954` edge `1334.6833` maxDD `-0.6271`
- `market_context_high->unknown_4h` score `10769.2381` n `82` status `ready` deltaP `3.5061` edge `897.427` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1337.8197` n `31` status `ready` deltaP `4.1771` edge `111.4747` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1184.1829` n `31` status `ready` deltaP `3.9388` edge `98.6613` maxDD `-0.119`
- `news_risk_high->equity_4h` score `11.5393` n `31` status `ready` deltaP `37.8344` edge `0.7576` maxDD `-2.1911`
- `news_risk_high->crypto_alt_4h` score `11.0131` n `31` status `ready` deltaP `25.6933` edge `0.8335` maxDD `-5.2957`
- `news_risk_high->crypto_major_4h` score `6.6148` n `31` status `ready` deltaP `14.1866` edge `0.8952` maxDD `-7.6714`
- `news_risk_high->equity_1h` score `3.9522` n `31` status `ready` deltaP `19.8377` edge `0.2158` maxDD `-0.163`
- `news_risk_high->index_4h` score `3.42` n `31` status `ready` deltaP `35.8527` edge `0.072` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.7046` n `31` status `ready` deltaP `31.6931` edge `0.0226` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.4571` n `31` status `ready` deltaP `9.8609` edge `0.2954` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.0923` n `31` status `ready` deltaP `8.813` edge `0.2452` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.5446` n `31` status `ready` deltaP `29.2833` edge `0.0307` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `1.5199` n `31` status `ready` deltaP `20.894` edge `0.1113` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.8438` n `31` status `ready` deltaP `18.2779` edge `0.0261` maxDD `-0.5151`
- `market_context_high->fx_4h` score `0.1252` n `82` status `ready` deltaP `11.2804` edge `0.0141` maxDD `-0.5264`
- `market_context_high->metal_1h` score `-0.1063` n `84` status `ready` deltaP `3.8993` edge `0.0122` maxDD `-1.4794`
- `news_risk_high->commodity_1h` score `-0.1064` n `31` status `ready` deltaP `0.932` edge `0.0111` maxDD `-0.0947`
- `market_context_high->index_1h` score `-0.1445` n `84` status `ready` deltaP `3.4289` edge `0.0042` maxDD `-0.9806`
- `market_context_high->metal_4h` score `-1.0895` n `82` status `ready` deltaP `5.9452` edge `0.01` maxDD `-6.9009`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
