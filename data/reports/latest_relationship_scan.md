# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-29T17:52:31.236728+00:00`
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

- `news_risk_high->unknown_24h` score `2589.3967` n `139` status `ready` deltaP `1.3889` edge `215.7738` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `15.9997` n `139` status `ready` deltaP `31.1988` edge `1.5205` maxDD `-29.2814`
- `news_risk_high->equity_24h` score `9.7464` n `139` status `ready` deltaP `33.0535` edge `0.8465` maxDD `-11.039`
- `news_risk_high->crypto_major_24h` score `7.8025` n `139` status `ready` deltaP `24.8938` edge `0.9277` maxDD `-26.1424`
- `news_risk_high->index_24h` score `4.1426` n `139` status `ready` deltaP `38.5117` edge `0.158` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `3.7138` n `139` status `ready` deltaP `31.586` edge `0.2844` maxDD `-6.8392`
- `news_risk_high->equity_4h` score `2.9057` n `142` status `ready` deltaP `29.1996` edge `0.2076` maxDD `-9.143`
- `news_risk_high->crypto_alt_4h` score `1.6797` n `142` status `ready` deltaP `10.3101` edge `0.3372` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `1.0799` n `142` status `ready` deltaP `8.1682` edge `0.1266` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.7486` n `142` status `ready` deltaP `8.6004` edge `0.071` maxDD `-1.9431`
- `news_risk_high->index_1h` score `0.5629` n `142` status `ready` deltaP `9.6483` edge `0.0116` maxDD `-0.3214`
- `news_risk_high->index_4h` score `0.2022` n `142` status `ready` deltaP `10.5118` edge `0.0321` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-0.2247` n `142` status `ready` deltaP `3.3377` edge `0.0772` maxDD `-7.2607`
- `news_risk_high->metal_1h` score `-0.4642` n `142` status `ready` deltaP `1.4632` edge `0.0145` maxDD `-0.7016`
- `news_risk_high->metal_4h` score `-1.2028` n `142` status `ready` deltaP `-6.3251` edge `0.0374` maxDD `-3.6214`
- `news_risk_high->fx_4h` score `-1.2834` n `142` status `ready` deltaP `9.4362` edge `-0.0061` maxDD `-3.0414`
- `news_risk_high->crypto_major_4h` score `-1.4208` n `142` status `ready` deltaP `-3.3108` edge `0.1114` maxDD `-13.719`
- `news_risk_high->fx_1h` score `-1.769` n `142` status `ready` deltaP `-8.3959` edge `-0.0034` maxDD `-1.0436`
- `news_risk_high->commodity_1h` score `-1.9001` n `142` status `ready` deltaP `-9.7537` edge `-0.0111` maxDD `-3.3986`
- `news_risk_high->commodity_4h` score `-2.379` n `142` status `ready` deltaP `-10.0695` edge `0.004` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
