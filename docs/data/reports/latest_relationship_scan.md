# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-27T00:22:33.561346+00:00`
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

- `news_risk_high->unknown_24h` score `48.9953` n `50` status `ready` deltaP `11.5717` edge `4.0058` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `13.6415` n `50` status `ready` deltaP `36.5872` edge `0.937` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `12.3175` n `50` status `ready` deltaP `25.7073` edge `0.865` maxDD `-0.1274`
- `news_risk_high->equity_24h` score `6.8399` n `50` status `ready` deltaP `30.8048` edge `0.4584` maxDD `-4.8351`
- `news_risk_high->index_24h` score `3.7245` n `50` status `ready` deltaP `37.5682` edge `0.0751` maxDD `-0.2147`
- `news_risk_high->fx_4h` score `3.6938` n `50` status `ready` deltaP `43.372` edge `0.0277` maxDD `-0.0559`
- `market_context_high->unknown_4h` score `3.1722` n `137` status `ready` deltaP `24.408` edge `0.1423` maxDD `-0.5871`
- `news_risk_high->unknown_1h` score `2.6906` n `50` status `ready` deltaP `15.3293` edge `0.1576` maxDD `-0.8463`
- `news_risk_high->metal_24h` score `2.6495` n `50` status `ready` deltaP `35.8238` edge `-0.0138` maxDD `-0.0053`
- `news_risk_high->fx_1h` score `1.385` n `50` status `ready` deltaP `18.8563` edge `0.0067` maxDD `-0.0257`
- `market_context_high->unknown_1h` score `1.324` n `137` status `ready` deltaP `12.7016` edge `0.0706` maxDD `-1.5954`
- `news_risk_high->equity_1h` score `1.274` n `50` status `ready` deltaP `17.2635` edge `0.019` maxDD `-0.2338`
- `news_risk_high->equity_4h` score `1.219` n `50` status `ready` deltaP `19.2927` edge `0.0497` maxDD `-2.1389`
- `news_risk_high->commodity_1h` score `0.5175` n `50` status `ready` deltaP `14.2994` edge `0.0023` maxDD `-0.5024`
- `market_context_high->unknown_24h` score `0.5108` n `133` status `ready` deltaP `5.5567` edge `0.0786` maxDD `-3.1794`
- `news_risk_high->index_1h` score `0.103` n `50` status `ready` deltaP `6.9102` edge `0.0011` maxDD `-0.0505`
- `news_risk_high->index_4h` score `0.0724` n `50` status `ready` deltaP `6.4756` edge `0.0026` maxDD `-0.1788`
- `news_risk_high->metal_1h` score `0.0438` n `50` status `ready` deltaP `4.503` edge `-0.0018` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `-0.1557` n `50` status `ready` deltaP `7.311` edge `-0.0086` maxDD `-0.249`
- `market_context_high->fx_1h` score `-0.3788` n `137` status `ready` deltaP `3.7906` edge `-0.0006` maxDD `-0.8587`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
