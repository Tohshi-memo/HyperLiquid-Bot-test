# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-26T19:08:22.501975+00:00`
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

- `news_risk_high->unknown_24h` score `47.9729` n `50` status `ready` deltaP `11.5717` edge `3.9206` maxDD `0.0`
- `news_risk_high->unknown_4h` score `12.4429` n `50` status `ready` deltaP `26.8267` edge `0.868` maxDD `-0.1281`
- `news_risk_high->crypto_alt_24h` score `11.7244` n `50` status `ready` deltaP `35.3782` edge `0.7853` maxDD `-2.8629`
- `news_risk_high->equity_24h` score `7.8781` n `50` status `ready` deltaP `34.2591` edge `0.5212` maxDD `-4.7801`
- `news_risk_high->index_24h` score `4.1256` n `50` status `ready` deltaP `41.0225` edge `0.0855` maxDD `-0.2147`
- `news_risk_high->fx_4h` score `3.4835` n `50` status `ready` deltaP `41.0881` edge `0.0254` maxDD `-0.0559`
- `market_context_high->unknown_4h` score `3.3031` n `137` status `ready` deltaP `25.5274` edge `0.1459` maxDD `-0.5994`
- `news_risk_high->unknown_1h` score `2.6468` n `50` status `ready` deltaP `15.3293` edge `0.1539` maxDD `-0.8426`
- `news_risk_high->metal_24h` score `2.1506` n `50` status `ready` deltaP `32.1969` edge `-0.0312` maxDD `-0.0053`
- `news_risk_high->equity_4h` score `1.4892` n `50` status `ready` deltaP `19.3131` edge `0.0724` maxDD `-2.164`
- `news_risk_high->fx_1h` score `1.3479` n `50` status `ready` deltaP `18.4072` edge `0.0066` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `1.2795` n `50` status `ready` deltaP `16.8144` edge `0.0226` maxDD `-0.2455`
- `market_context_high->unknown_1h` score `1.2778` n `137` status `ready` deltaP `12.7016` edge `0.0667` maxDD `-1.5916`
- `news_risk_high->commodity_1h` score `0.5097` n `50` status `ready` deltaP `14.1497` edge `0.0023` maxDD `-0.5024`
- `news_risk_high->index_1h` score `0.1201` n `50` status `ready` deltaP `7.0599` edge `0.0023` maxDD `-0.0505`
- `news_risk_high->index_4h` score `0.0954` n `50` status `ready` deltaP `6.3283` edge `0.0055` maxDD `-0.1788`
- `news_risk_high->metal_1h` score `0.068` n `50` status `ready` deltaP `4.9521` edge `-0.0017` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `-0.0508` n `50` status `ready` deltaP `8.0973` edge `-0.0051` maxDD `-0.249`
- `market_context_high->fx_1h` score `-0.4029` n `137` status `ready` deltaP `3.3415` edge `-0.0007` maxDD `-0.8587`
- `market_context_high->unknown_24h` score `-0.4426` n `133` status `ready` deltaP `5.5567` edge `-0.0012` maxDD `-3.1513`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
