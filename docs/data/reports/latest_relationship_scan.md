# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-27T22:22:23.754407+00:00`
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

- `news_risk_high->unknown_24h` score `52.2726` n `50` status `ready` deltaP `11.6319` edge `4.2785` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `22.9086` n `50` status `ready` deltaP `37.8403` edge `1.7009` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `12.7002` n `50` status `ready` deltaP `24.7927` edge `0.903` maxDD `-0.1279`
- `news_risk_high->metal_24h` score `4.8976` n `50` status `ready` deltaP `46.0903` edge `0.1051` maxDD `-0.0053`
- `news_risk_high->equity_24h` score `4.6486` n `50` status `ready` deltaP `26.5347` edge `0.3033` maxDD `-4.7584`
- `news_risk_high->fx_4h` score `3.8493` n `50` status `ready` deltaP `44.8963` edge `0.0305` maxDD `-0.0559`
- `news_risk_high->unknown_1h` score `2.9875` n `50` status `ready` deltaP `16.5269` edge `0.1744` maxDD `-0.8495`
- `market_context_high->unknown_24h` score `2.8482` n `128` status `ready` deltaP `5.3819` edge `0.2747` maxDD `-3.1917`
- `news_risk_high->index_24h` score `2.6962` n `50` status `ready` deltaP `30.5347` edge `0.0362` maxDD `-0.2064`
- `market_context_high->unknown_4h` score `2.2572` n `148` status `ready` deltaP `17.9549` edge `0.1091` maxDD `-0.5894`
- `news_risk_high->fx_1h` score `1.5324` n `50` status `ready` deltaP `20.503` edge `0.008` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `1.2098` n `50` status `ready` deltaP `17.1138` edge `0.0146` maxDD `-0.2301`
- `news_risk_high->equity_4h` score `0.9173` n `50` status `ready` deltaP `19.5976` edge `0.0221` maxDD `-2.105`
- `market_context_high->unknown_1h` score `0.8641` n `148` status `ready` deltaP `8.8242` edge `0.0582` maxDD `-1.6015`
- `news_risk_high->commodity_1h` score `0.5082` n `50` status `ready` deltaP `14.1497` edge `0.0021` maxDD `-0.5024`
- `news_risk_high->index_1h` score `0.1133` n `50` status `ready` deltaP `7.2096` edge `0.0004` maxDD `-0.0486`
- `news_risk_high->metal_1h` score `0.0781` n `50` status `ready` deltaP `5.1018` edge `-0.0014` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `-0.0917` n `50` status `ready` deltaP `7.6159` edge `-0.0053` maxDD `-0.249`
- `news_risk_high->index_4h` score `-0.1171` n `50` status `ready` deltaP `4.7988` edge `-0.0021` maxDD `-0.1719`
- `market_context_high->metal_4h` score `-0.4408` n `148` status `ready` deltaP `6.4808` edge `-0.008` maxDD `-3.3377`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
