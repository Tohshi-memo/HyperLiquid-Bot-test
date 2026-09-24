# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-24T18:37:31.349116+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10053`

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

- `market_context_high->unknown_1h` score `86.9587` n `47` status `ready` deltaP `10.116` edge `7.1862` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `44.3513` n `47` status `ready` deltaP `30.4226` edge `3.5324` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `29.6248` n `47` status `ready` deltaP `24.782` edge `2.3415` maxDD `-2.7051`
- `market_context_high->equity_24h` score `24.6791` n `47` status `ready` deltaP `30.2489` edge `1.8905` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.8286` n `47` status `ready` deltaP `34.7628` edge `0.4336` maxDD `-0.3705`
- `news_risk_high->crypto_major_24h` score `4.1614` n `88` status `ready` deltaP `-0.6944` edge `1.4424` maxDD `-63.6743`
- `market_context_high->metal_24h` score `3.8496` n `47` status `ready` deltaP `32.975` edge `0.1248` maxDD `-0.2401`
- `news_risk_high->crypto_alt_1h` score `3.3732` n `112` status `ready` deltaP `16.9109` edge `0.2174` maxDD `-1.5895`
- `market_context_high->index_4h` score `3.0057` n `47` status `ready` deltaP `34.3312` edge `0.037` maxDD `-0.2323`
- `news_risk_high->crypto_major_1h` score `2.8512` n `112` status `ready` deltaP `18.857` edge `0.1554` maxDD `-1.8141`
- `news_risk_high->crypto_major_4h` score `2.5557` n `109` status `ready` deltaP `17.0144` edge `0.3127` maxDD `-13.719`
- `news_risk_high->crypto_alt_4h` score `2.5501` n `109` status `ready` deltaP `9.5309` edge `0.3941` maxDD `-15.9436`
- `market_context_high->equity_4h` score `2.4853` n `47` status `ready` deltaP `17.2969` edge `0.1336` maxDD `-1.3444`
- `news_risk_high->crypto_alt_24h` score `2.1352` n `88` status `ready` deltaP `-2.6358` edge `0.9926` maxDD `-49.7699`
- `news_risk_high->fx_4h` score `1.6914` n `109` status `ready` deltaP `24.442` edge `0.0416` maxDD `-0.421`
- `news_risk_high->commodity_24h` score `1.3746` n `88` status `ready` deltaP `17.6452` edge `0.0859` maxDD `-1.7857`
- `news_risk_high->metal_1h` score `1.2642` n `112` status `ready` deltaP `17.5791` edge `0.025` maxDD `-0.6142`
- `news_risk_high->metal_24h` score `1.0439` n `88` status `ready` deltaP `24.416` edge `0.1159` maxDD `-7.2536`
- `market_context_high->index_1h` score `1.0242` n `47` status `ready` deltaP `15.3586` edge `0.0108` maxDD `-0.2275`
- `news_risk_high->fx_24h` score `0.9993` n `88` status `ready` deltaP `26.1205` edge `0.1171` maxDD `-1.7159`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
