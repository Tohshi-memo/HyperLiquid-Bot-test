# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-26T20:22:28.462578+00:00`
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

- `news_risk_high->unknown_24h` score `48.2861` n `50` status `ready` deltaP `11.5717` edge `3.9467` maxDD `0.0`
- `news_risk_high->unknown_4h` score `12.5207` n `50` status `ready` deltaP `27.0793` edge `0.8728` maxDD `-0.1281`
- `news_risk_high->crypto_alt_24h` score `12.5135` n `50` status `ready` deltaP `36.2418` edge `0.8453` maxDD `-2.8629`
- `news_risk_high->equity_24h` score `7.8043` n `50` status `ready` deltaP `33.7409` edge `0.5185` maxDD `-4.7801`
- `news_risk_high->index_24h` score `4.0607` n `50` status `ready` deltaP `40.3316` edge `0.0847` maxDD `-0.2147`
- `news_risk_high->fx_4h` score `3.4832` n `50` status `ready` deltaP `41.0854` edge `0.0254` maxDD `-0.0559`
- `market_context_high->unknown_4h` score `3.3809` n `137` status `ready` deltaP `25.78` edge `0.1507` maxDD `-0.5994`
- `news_risk_high->unknown_1h` score `2.7319` n `50` status `ready` deltaP `15.6287` edge `0.159` maxDD `-0.8426`
- `news_risk_high->metal_24h` score `2.288` n `50` status `ready` deltaP `33.0604` edge `-0.0255` maxDD `-0.0053`
- `news_risk_high->equity_4h` score `1.5778` n `50` status `ready` deltaP `19.4451` edge `0.0789` maxDD `-2.164`
- `market_context_high->unknown_1h` score `1.3629` n `137` status `ready` deltaP `13.001` edge `0.0718` maxDD `-1.5916`
- `news_risk_high->fx_1h` score `1.3479` n `50` status `ready` deltaP `18.4072` edge `0.0066` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `1.3347` n `50` status `ready` deltaP `17.1138` edge `0.0252` maxDD `-0.2455`
- `news_risk_high->commodity_1h` score `0.5004` n `50` status `ready` deltaP `14.0` edge `0.0021` maxDD `-0.5024`
- `news_risk_high->index_4h` score `0.1156` n `50` status `ready` deltaP `6.4756` edge `0.0062` maxDD `-0.1788`
- `news_risk_high->index_1h` score `0.103` n `50` status `ready` deltaP `6.7605` edge `0.0021` maxDD `-0.0505`
- `news_risk_high->metal_1h` score `0.0968` n `50` status `ready` deltaP `5.4012` edge `-0.001` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `0.0129` n `50` status `ready` deltaP `8.6829` edge `-0.0037` maxDD `-0.249`
- `market_context_high->unknown_24h` score `-0.1294` n `133` status `ready` deltaP `5.5567` edge `0.0249` maxDD `-3.1513`
- `market_context_high->fx_1h` score `-0.4029` n `137` status `ready` deltaP `3.3415` edge `-0.0007` maxDD `-0.8587`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
