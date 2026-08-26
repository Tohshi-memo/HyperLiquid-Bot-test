# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-26T20:52:28.178283+00:00`
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

- `news_risk_high->unknown_24h` score `48.3833` n `50` status `ready` deltaP `11.5717` edge `3.9548` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `12.7715` n `50` status `ready` deltaP `36.5872` edge `0.8645` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `12.5255` n `50` status `ready` deltaP `27.0793` edge `0.8732` maxDD `-0.1281`
- `news_risk_high->equity_24h` score `7.7466` n `50` status `ready` deltaP `33.3955` edge `0.516` maxDD `-4.7801`
- `news_risk_high->index_24h` score `4.0319` n `50` status `ready` deltaP `39.9862` edge `0.0846` maxDD `-0.2147`
- `news_risk_high->fx_4h` score `3.5076` n `50` status `ready` deltaP `41.3902` edge `0.0254` maxDD `-0.0559`
- `market_context_high->unknown_4h` score `3.3857` n `137` status `ready` deltaP `25.78` edge `0.1511` maxDD `-0.5994`
- `news_risk_high->unknown_1h` score `2.7835` n `50` status `ready` deltaP `15.9281` edge `0.1613` maxDD `-0.8426`
- `news_risk_high->metal_24h` score `2.3433` n `50` status `ready` deltaP `33.4059` edge `-0.0232` maxDD `-0.0053`
- `news_risk_high->equity_4h` score `1.5646` n `50` status `ready` deltaP `19.4451` edge `0.0778` maxDD `-2.164`
- `market_context_high->unknown_1h` score `1.4145` n `137` status `ready` deltaP `13.3004` edge `0.0741` maxDD `-1.5916`
- `news_risk_high->fx_1h` score `1.3479` n `50` status `ready` deltaP `18.4072` edge `0.0066` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `1.3311` n `50` status `ready` deltaP `17.1138` edge `0.0249` maxDD `-0.2455`
- `news_risk_high->commodity_1h` score `0.5175` n `50` status `ready` deltaP `14.2994` edge `0.0023` maxDD `-0.5024`
- `news_risk_high->metal_1h` score `0.1155` n `50` status `ready` deltaP `5.7006` edge `-0.0006` maxDD `-0.1413`
- `news_risk_high->index_4h` score `0.1144` n `50` status `ready` deltaP `6.4756` edge `0.0061` maxDD `-0.1788`
- `news_risk_high->index_1h` score `0.1116` n `50` status `ready` deltaP `6.9102` edge `0.0022` maxDD `-0.0505`
- `news_risk_high->metal_4h` score `0.0409` n `50` status `ready` deltaP `8.9878` edge `-0.0034` maxDD `-0.249`
- `market_context_high->unknown_24h` score `-0.0322` n `133` status `ready` deltaP `5.5567` edge `0.033` maxDD `-3.1513`
- `market_context_high->fx_1h` score `-0.4029` n `137` status `ready` deltaP `3.3415` edge `-0.0007` maxDD `-0.8587`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
