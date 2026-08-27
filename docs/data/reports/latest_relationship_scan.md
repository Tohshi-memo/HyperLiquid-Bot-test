# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-27T12:52:35.813317+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14748`

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

- `news_risk_high->unknown_24h` score `51.3389` n `50` status `ready` deltaP `11.5717` edge `4.2011` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `19.2096` n `50` status `ready` deltaP `37.6235` edge `1.3941` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `12.6326` n `50` status `ready` deltaP `26.3171` edge `0.8872` maxDD `-0.1279`
- `news_risk_high->equity_24h` score `4.6249` n `50` status `ready` deltaP `25.6235` edge `0.3074` maxDD `-4.7584`
- `news_risk_high->metal_24h` score `4.3136` n `50` status `ready` deltaP `44.4594` edge `0.0673` maxDD `-0.0053`
- `news_risk_high->fx_4h` score `4.0235` n `50` status `ready` deltaP `46.878` edge `0.0318` maxDD `-0.0559`
- `market_context_high->unknown_4h` score `3.3289` n `133` status `ready` deltaP `24.0464` edge `0.1578` maxDD `-0.5894`
- `news_risk_high->unknown_1h` score `2.9455` n `50` status `ready` deltaP `16.8263` edge `0.1689` maxDD `-0.8495`
- `news_risk_high->index_24h` score `2.6888` n `50` status `ready` deltaP `30.1416` edge `0.0382` maxDD `-0.2064`
- `market_context_high->unknown_24h` score `1.9146` n `128` status `ready` deltaP `5.3217` edge `0.1973` maxDD `-3.1917`
- `news_risk_high->fx_1h` score `1.5827` n `50` status `ready` deltaP `21.1018` edge `0.0082` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `1.1534` n `50` status `ready` deltaP `16.9641` edge `0.0109` maxDD `-0.2301`
- `market_context_high->unknown_1h` score `1.1171` n `144` status `ready` deltaP `11.1319` edge `0.0639` maxDD `-1.6015`
- `news_risk_high->commodity_1h` score `0.5829` n `50` status `ready` deltaP `15.3473` edge `0.0037` maxDD `-0.5024`
- `news_risk_high->equity_4h` score `0.5605` n `50` status `ready` deltaP `17.4634` edge `0.0066` maxDD `-2.105`
- `news_risk_high->index_1h` score `0.1343` n `50` status `ready` deltaP `7.6587` edge `0.0001` maxDD `-0.0486`
- `news_risk_high->metal_1h` score `0.089` n `50` status `ready` deltaP `5.4012` edge `-0.002` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `-0.1077` n `50` status `ready` deltaP `7.311` edge `-0.0046` maxDD `-0.249`
- `news_risk_high->index_4h` score `-0.1573` n `50` status `ready` deltaP `4.3415` edge `-0.0024` maxDD `-0.1719`
- `market_context_high->fx_1h` score `-0.5551` n `144` status `ready` deltaP `0.4907` edge `-0.0012` maxDD `-0.8587`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
