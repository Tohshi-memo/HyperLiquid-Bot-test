# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-29T06:37:35.279087+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7376`

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

- `news_risk_high->unknown_24h` score `2619.93` n `139` status `ready` deltaP `1.2153` edge `218.3194` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `15.8559` n `139` status `ready` deltaP `32.7613` edge `1.4981` maxDD `-29.2814`
- `news_risk_high->equity_24h` score `9.6982` n `139` status `ready` deltaP `32.3591` edge `0.8481` maxDD `-11.1179`
- `news_risk_high->crypto_major_24h` score `9.0129` n `139` status `ready` deltaP `27.498` edge `1.0112` maxDD `-26.1424`
- `news_risk_high->index_24h` score `4.0481` n `139` status `ready` deltaP `36.7756` edge `0.1617` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `3.7251` n `139` status `ready` deltaP `30.1971` edge `0.2946` maxDD `-6.8392`
- `news_risk_high->equity_4h` score `2.5135` n `139` status `ready` deltaP `27.4785` edge `0.1872` maxDD `-9.2079`
- `news_risk_high->crypto_alt_4h` score `1.2731` n `139` status `ready` deltaP `9.4128` edge `0.3093` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `0.9564` n `142` status `ready` deltaP `7.8688` edge `0.1183` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.7428` n `142` status `ready` deltaP `9.0495` edge `0.0677` maxDD `-1.957`
- `news_risk_high->index_1h` score `0.5137` n `142` status `ready` deltaP `9.1992` edge `0.0105` maxDD `-0.3214`
- `news_risk_high->index_4h` score `-0.0831` n `139` status `ready` deltaP `7.7251` edge `0.0269` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-0.4148` n `142` status `ready` deltaP `1.5413` edge `0.0648` maxDD `-7.2607`
- `news_risk_high->metal_1h` score `-0.5002` n `142` status `ready` deltaP `1.4632` edge `0.0115` maxDD `-0.7016`
- `news_risk_high->fx_4h` score `-1.3264` n `139` status `ready` deltaP `8.61` edge `-0.0061` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.4529` n `139` status `ready` deltaP `-9.1562` edge `0.0242` maxDD `-3.6214`
- `news_risk_high->crypto_major_4h` score `-1.8066` n `139` status `ready` deltaP `-4.9384` edge `0.0728` maxDD `-13.719`
- `news_risk_high->fx_1h` score `-1.8876` n `142` status `ready` deltaP `-9.8929` edge `-0.0033` maxDD `-1.0436`
- `news_risk_high->commodity_1h` score `-2.0606` n `142` status `ready` deltaP `-12.2986` edge `-0.0147` maxDD `-3.3986`
- `news_risk_high->commodity_4h` score `-3.9773` n `139` status `ready` deltaP `-12.2368` edge `-0.008` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
