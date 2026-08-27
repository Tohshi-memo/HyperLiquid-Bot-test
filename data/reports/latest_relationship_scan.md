# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-27T22:37:28.526210+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11831`

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

- `news_risk_high->unknown_24h` score `52.2774` n `50` status `ready` deltaP `11.6319` edge `4.2789` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `23.0514` n `50` status `ready` deltaP `37.8403` edge `1.7128` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `12.6808` n `50` status `ready` deltaP `24.6402` edge `0.9024` maxDD `-0.1279`
- `news_risk_high->metal_24h` score `4.9072` n `50` status `ready` deltaP `46.0903` edge `0.1059` maxDD `-0.0053`
- `news_risk_high->equity_24h` score `4.6889` n `50` status `ready` deltaP `26.7083` edge `0.3055` maxDD `-4.7584`
- `news_risk_high->fx_4h` score `3.8347` n `50` status `ready` deltaP `44.7439` edge `0.0303` maxDD `-0.0559`
- `news_risk_high->unknown_1h` score `2.9851` n `50` status `ready` deltaP `16.5269` edge `0.1742` maxDD `-0.8495`
- `market_context_high->unknown_24h` score `2.853` n `128` status `ready` deltaP `5.3819` edge `0.2751` maxDD `-3.1917`
- `news_risk_high->index_24h` score `2.7149` n `50` status `ready` deltaP `30.7083` edge `0.0366` maxDD `-0.2064`
- `market_context_high->unknown_4h` score `2.2378` n `148` status `ready` deltaP `17.8024` edge `0.1085` maxDD `-0.5894`
- `news_risk_high->fx_1h` score `1.5192` n `50` status `ready` deltaP `20.3533` edge `0.0079` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `1.223` n `50` status `ready` deltaP `17.2635` edge `0.0147` maxDD `-0.2301`
- `news_risk_high->equity_4h` score `0.9269` n `50` status `ready` deltaP `19.5976` edge `0.0229` maxDD `-2.105`
- `market_context_high->unknown_1h` score `0.8617` n `148` status `ready` deltaP `8.8242` edge `0.058` maxDD `-1.6015`
- `news_risk_high->commodity_1h` score `0.5082` n `50` status `ready` deltaP `14.1497` edge `0.0021` maxDD `-0.5024`
- `news_risk_high->index_1h` score `0.1211` n `50` status `ready` deltaP `7.3593` edge `0.0004` maxDD `-0.0486`
- `news_risk_high->metal_1h` score `0.0781` n `50` status `ready` deltaP `5.1018` edge `-0.0014` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `-0.0905` n `50` status `ready` deltaP `7.6159` edge `-0.0052` maxDD `-0.249`
- `news_risk_high->index_4h` score `-0.1171` n `50` status `ready` deltaP `4.7988` edge `-0.0021` maxDD `-0.1719`
- `market_context_high->metal_4h` score `-0.44` n `148` status `ready` deltaP `6.4808` edge `-0.0079` maxDD `-3.3377`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
