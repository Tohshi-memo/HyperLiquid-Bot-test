# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-29T18:07:34.537688+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7160`

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

- `news_risk_high->unknown_24h` score `2589.6451` n `139` status `ready` deltaP `1.3889` edge `215.7945` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `15.9589` n `139` status `ready` deltaP `31.1988` edge `1.5171` maxDD `-29.2814`
- `news_risk_high->equity_24h` score `9.7025` n `139` status `ready` deltaP `32.8799` edge `0.844` maxDD `-11.039`
- `news_risk_high->crypto_major_24h` score `7.7617` n `139` status `ready` deltaP `24.8938` edge `0.9243` maxDD `-26.1424`
- `news_risk_high->index_24h` score `4.1354` n `139` status `ready` deltaP `38.5117` edge `0.1574` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `3.7006` n `139` status `ready` deltaP `31.586` edge `0.2833` maxDD `-6.8392`
- `news_risk_high->equity_4h` score `2.9227` n `142` status `ready` deltaP `29.3521` edge `0.208` maxDD `-9.143`
- `news_risk_high->crypto_alt_4h` score `1.7315` n `142` status `ready` deltaP `10.4625` edge `0.3405` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `1.0967` n `142` status `ready` deltaP `8.3179` edge `0.127` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.7474` n `142` status `ready` deltaP `8.6004` edge `0.0709` maxDD `-1.9431`
- `news_risk_high->index_1h` score `0.5497` n `142` status `ready` deltaP `9.4986` edge `0.0115` maxDD `-0.3214`
- `news_risk_high->index_4h` score `0.2156` n `142` status `ready` deltaP `10.6643` edge `0.0322` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-0.2122` n `142` status `ready` deltaP `3.4874` edge `0.0778` maxDD `-7.2607`
- `news_risk_high->metal_1h` score `-0.4666` n `142` status `ready` deltaP `1.4632` edge `0.0143` maxDD `-0.7016`
- `news_risk_high->metal_4h` score `-1.202` n `142` status `ready` deltaP `-6.3251` edge `0.0375` maxDD `-3.6214`
- `news_risk_high->fx_4h` score `-1.2834` n `142` status `ready` deltaP `9.4362` edge `-0.0061` maxDD `-3.0414`
- `news_risk_high->crypto_major_4h` score `-1.4021` n `142` status `ready` deltaP `-3.3108` edge `0.1138` maxDD `-13.719`
- `news_risk_high->fx_1h` score `-1.769` n `142` status `ready` deltaP `-8.3959` edge `-0.0034` maxDD `-1.0436`
- `news_risk_high->commodity_1h` score `-1.8869` n `142` status `ready` deltaP `-9.604` edge `-0.0104` maxDD `-3.3986`
- `news_risk_high->commodity_4h` score `-2.3656` n `142` status `ready` deltaP `-9.9171` edge `0.0047` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
