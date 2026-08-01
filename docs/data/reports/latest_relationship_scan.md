# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-01T10:22:28.505407+00:00`
- Price records: `672`
- Market context records: `8611`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5898`

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

- `news_risk_high->unknown_24h` score `4964.8414` n `62` status `ready` deltaP `34.4496` edge `413.5492` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `18.7227` n `38` status `ready` deltaP `51.5188` edge `1.2565` maxDD `-2.1786`
- `news_risk_high->equity_4h` score `5.9082` n `62` status `ready` deltaP `19.7329` edge `0.4205` maxDD `-3.4427`
- `news_risk_high->index_4h` score `2.4742` n `62` status `ready` deltaP `21.6503` edge `0.0809` maxDD `-0.191`
- `market_context_high->crypto_major_24h` score `2.254` n `38` status `ready` deltaP `8.8479` edge `0.5626` maxDD `-21.2759`
- `market_context_high->fx_24h` score `1.9611` n `38` status `ready` deltaP `30.6395` edge `0.0821` maxDD `-0.4622`
- `news_risk_high->equity_1h` score `1.7215` n `62` status `ready` deltaP `15.6944` edge `0.0865` maxDD `-2.4803`
- `market_context_high->crypto_alt_4h` score `1.7074` n `62` status `ready` deltaP `12.5227` edge `0.1545` maxDD `-5.323`
- `news_risk_high->crypto_major_4h` score `1.0492` n `62` status `ready` deltaP `7.1365` edge `0.1645` maxDD `-3.5385`
- `news_risk_high->crypto_alt_1h` score `0.4273` n `62` status `ready` deltaP `8.2142` edge `0.0527` maxDD `-1.8813`
- `news_risk_high->crypto_alt_4h` score `0.3771` n `62` status `ready` deltaP `10.9098` edge `0.1148` maxDD `-5.8012`
- `news_risk_high->crypto_major_1h` score `0.3034` n `62` status `ready` deltaP `6.1522` edge `0.0491` maxDD `-2.0972`
- `news_risk_high->fx_4h` score `0.168` n `62` status `ready` deltaP `13.0432` edge `0.0228` maxDD `-0.6604`
- `news_risk_high->metal_4h` score `0.1194` n `62` status `ready` deltaP `4.4263` edge `0.0334` maxDD `-0.8085`
- `news_risk_high->fx_1h` score `0.1143` n `62` status `ready` deltaP `5.7369` edge `0.0045` maxDD `-0.2475`
- `news_risk_high->index_1h` score `0.0565` n `62` status `ready` deltaP `4.4717` edge `0.0091` maxDD `-0.5338`
- `news_risk_high->metal_1h` score `0.0404` n `62` status `ready` deltaP `5.3699` edge `0.0079` maxDD `-0.5599`
- `market_context_high->metal_24h` score `-0.0957` n `38` status `ready` deltaP `1.9155` edge `0.0672` maxDD `-2.0458`
- `market_context_high->fx_4h` score `-0.1441` n `62` status `ready` deltaP `8.2045` edge `0.0129` maxDD `-1.3685`
- `market_context_high->index_24h` score `-0.2422` n `38` status `ready` deltaP `13.1807` edge `0.0086` maxDD `-4.8683`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
