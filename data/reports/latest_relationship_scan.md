# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-26T21:22:25.006009+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14792`

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

- `news_risk_high->unknown_24h` score `48.5753` n `50` status `ready` deltaP `11.5717` edge `3.9708` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `12.9431` n `50` status `ready` deltaP `36.5872` edge `0.8788` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `12.5496` n `50` status `ready` deltaP `27.0793` edge `0.8752` maxDD `-0.1274`
- `news_risk_high->equity_24h` score `7.6189` n `50` status `ready` deltaP `32.8774` edge `0.5095` maxDD `-4.8351`
- `news_risk_high->index_24h` score `3.9959` n `50` status `ready` deltaP `39.6408` edge `0.0839` maxDD `-0.2147`
- `news_risk_high->fx_4h` score `3.521` n `50` status `ready` deltaP `41.5427` edge `0.0255` maxDD `-0.0559`
- `market_context_high->unknown_4h` score `3.4043` n `137` status `ready` deltaP `25.78` edge `0.1525` maxDD `-0.5871`
- `news_risk_high->unknown_1h` score `2.7709` n `50` status `ready` deltaP `15.7784` edge `0.1613` maxDD `-0.8463`
- `news_risk_high->metal_24h` score `2.3913` n `50` status `ready` deltaP `33.7513` edge `-0.0215` maxDD `-0.0053`
- `news_risk_high->equity_4h` score `1.5444` n `50` status `ready` deltaP `19.4451` edge `0.0758` maxDD `-2.1389`
- `market_context_high->unknown_1h` score `1.4043` n `137` status `ready` deltaP `13.1507` edge `0.0743` maxDD `-1.5954`
- `news_risk_high->fx_1h` score `1.3467` n `50` status `ready` deltaP `18.4072` edge `0.0065` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `1.322` n `50` status `ready` deltaP `17.2635` edge `0.023` maxDD `-0.2338`
- `news_risk_high->commodity_1h` score `0.5183` n `50` status `ready` deltaP `14.2994` edge `0.0024` maxDD `-0.5024`
- `news_risk_high->metal_1h` score `0.1248` n `50` status `ready` deltaP `5.8503` edge `-0.0004` maxDD `-0.1413`
- `news_risk_high->index_4h` score `0.1132` n `50` status `ready` deltaP `6.4756` edge `0.006` maxDD `-0.1788`
- `news_risk_high->index_1h` score `0.11` n `50` status `ready` deltaP `6.9102` edge `0.002` maxDD `-0.0505`
- `market_context_high->unknown_24h` score `0.0908` n `133` status `ready` deltaP `5.5567` edge `0.0436` maxDD `-3.1794`
- `news_risk_high->metal_4h` score `0.0543` n `50` status `ready` deltaP `9.1402` edge `-0.0033` maxDD `-0.249`
- `market_context_high->fx_1h` score `-0.4037` n `137` status `ready` deltaP `3.3415` edge `-0.0008` maxDD `-0.8587`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
