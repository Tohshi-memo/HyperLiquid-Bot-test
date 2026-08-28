# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-28T09:37:23.465784+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11608`

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

- `news_risk_high->unknown_24h` score `53.2765` n `50` status `ready` deltaP `11.6118` edge `4.3623` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `30.1578` n `50` status `ready` deltaP `38.9809` edge `2.2974` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `12.8214` n `50` status `ready` deltaP `25.7073` edge `0.907` maxDD `-0.1279`
- `news_risk_high->equity_24h` score `5.4367` n `50` status `ready` deltaP `30.1005` edge `0.3452` maxDD `-4.7584`
- `news_risk_high->metal_24h` score `5.1275` n `50` status `ready` deltaP `47.9133` edge `0.1121` maxDD `-0.0053`
- `news_risk_high->fx_4h` score `3.9601` n `50` status `ready` deltaP `46.1159` edge `0.0316` maxDD `-0.0559`
- `market_context_high->unknown_24h` score `2.767` n `133` status `ready` deltaP `5.5968` edge `0.2665` maxDD `-3.1917`
- `news_risk_high->unknown_1h` score `2.7284` n `52` status `ready` deltaP `15.6725` edge `0.1585` maxDD `-0.8495`
- `news_risk_high->index_24h` score `2.5703` n `50` status `ready` deltaP `28.9012` edge `0.0366` maxDD `-0.2064`
- `market_context_high->unknown_4h` score `2.3907` n `146` status `ready` deltaP `18.6936` edge `0.1153` maxDD `-0.5894`
- `news_risk_high->crypto_major_24h` score `2.2642` n `50` status `ready` deltaP `18.662` edge `0.1136` maxDD `-2.6128`
- `news_risk_high->equity_4h` score `1.8181` n `50` status `ready` deltaP `24.0183` edge `0.0677` maxDD `-2.105`
- `news_risk_high->fx_1h` score `1.5689` n `52` status `ready` deltaP `21.0041` edge `0.0077` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `1.2908` n `52` status `ready` deltaP `16.9622` edge `0.0227` maxDD `-0.2574`
- `market_context_high->unknown_1h` score `0.8889` n `146` status `ready` deltaP `8.7441` edge `0.0608` maxDD `-1.6015`
- `market_context_high->metal_24h` score `0.5223` n `133` status `ready` deltaP `15.3268` edge `0.0921` maxDD `-3.3934`
- `news_risk_high->commodity_1h` score `0.5162` n `52` status `ready` deltaP `14.3597` edge `0.0022` maxDD `-0.5397`
- `news_risk_high->metal_4h` score `0.2678` n `50` status `ready` deltaP `10.9695` edge `0.0023` maxDD `-0.249`
- `news_risk_high->index_4h` score `0.1334` n `50` status `ready` deltaP `7.3902` edge `0.0015` maxDD `-0.1719`
- `news_risk_high->index_1h` score `0.071` n `52` status `ready` deltaP `6.322` edge `0.0009` maxDD `-0.0486`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
