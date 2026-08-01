# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-01T06:07:27.536958+00:00`
- Price records: `672`
- Market context records: `8592`
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

- `news_risk_high->unknown_24h` score `4749.582` n `64` status `ready` deltaP `35.9375` edge `395.601` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `5.8828` n `64` status `ready` deltaP `20.9604` edge `0.4102` maxDD `-3.4427`
- `news_risk_high->index_4h` score `2.1762` n `64` status `ready` deltaP `18.3308` edge `0.0782` maxDD `-0.191`
- `news_risk_high->equity_1h` score `1.8379` n `64` status `ready` deltaP `17.2998` edge `0.0855` maxDD `-2.4803`
- `market_context_high->crypto_alt_4h` score `1.5367` n `62` status `ready` deltaP `11.3788` edge `0.1479` maxDD `-5.323`
- `news_risk_high->crypto_major_4h` score `0.9666` n `64` status `ready` deltaP `5.9832` edge `0.1616` maxDD `-3.5385`
- `news_risk_high->crypto_alt_1h` score `0.4111` n `64` status `ready` deltaP `7.8125` edge `0.0533` maxDD `-1.8813`
- `news_risk_high->crypto_alt_4h` score `0.4079` n `64` status `ready` deltaP `10.9756` edge `0.1183` maxDD `-5.8012`
- `news_risk_high->crypto_major_1h` score `0.3618` n `64` status `ready` deltaP `7.064` edge `0.0505` maxDD `-2.0972`
- `news_risk_high->fx_4h` score `0.0862` n `64` status `ready` deltaP `12.0808` edge `0.0224` maxDD `-0.6604`
- `news_risk_high->fx_1h` score `0.0807` n `64` status `ready` deltaP `5.1366` edge `0.0042` maxDD `-0.2475`
- `news_risk_high->index_1h` score `0.0581` n `64` status `ready` deltaP `4.5191` edge `0.009` maxDD `-0.5338`
- `news_risk_high->metal_4h` score `0.0316` n `64` status `ready` deltaP `2.9345` edge `0.0321` maxDD `-0.8085`
- `market_context_high->fx_4h` score `-0.082` n `62` status `ready` deltaP `8.9054` edge `0.0134` maxDD `-1.3685`
- `news_risk_high->metal_1h` score `-0.1575` n `64` status `ready` deltaP `2.9566` edge `0.0075` maxDD `-0.5599`
- `market_context_high->fx_1h` score `-0.284` n `62` status `ready` deltaP `2.062` edge `0.0001` maxDD `-0.6874`
- `market_context_high->commodity_1h` score `-0.3122` n `62` status `ready` deltaP `4.1578` edge `-0.0052` maxDD `-2.0038`
- `market_context_high->crypto_alt_1h` score `-0.5657` n `62` status `ready` deltaP `-3.2258` edge `0.0117` maxDD `-3.0178`
- `market_context_high->index_1h` score `-0.6938` n `62` status `ready` deltaP `1.5453` edge `-0.0152` maxDD `-1.5667`
- `market_context_high->metal_1h` score `-0.9984` n `62` status `ready` deltaP `-3.2934` edge `-0.0118` maxDD `-1.6224`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
