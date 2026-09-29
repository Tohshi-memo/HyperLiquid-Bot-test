# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-29T05:37:31.452004+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7198`

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

- `news_risk_high->unknown_24h` score `2625.6708` n `139` status `ready` deltaP `1.2153` edge `218.7978` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `15.3815` n `139` status `ready` deltaP `32.0669` edge `1.4632` maxDD `-29.2814`
- `news_risk_high->equity_24h` score `9.3907` n `139` status `ready` deltaP `31.6646` edge `0.8271` maxDD `-11.1179`
- `news_risk_high->crypto_major_24h` score `8.8466` n `139` status `ready` deltaP `27.3243` edge `0.9985` maxDD `-26.1424`
- `news_risk_high->index_24h` score `3.9674` n `139` status `ready` deltaP `36.0811` edge `0.1596` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `3.6239` n `139` status `ready` deltaP `29.5027` edge `0.2908` maxDD `-6.8392`
- `news_risk_high->equity_4h` score `2.4785` n `139` status `ready` deltaP `27.3261` edge `0.1853` maxDD `-9.2079`
- `news_risk_high->crypto_alt_4h` score `1.4041` n `139` status `ready` deltaP `9.5653` edge `0.3192` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `0.7358` n `139` status `ready` deltaP `7.1673` edge `0.1046` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.6134` n `139` status `ready` deltaP `8.4522` edge `0.0609` maxDD `-1.957`
- `news_risk_high->index_1h` score `0.4623` n `139` status `ready` deltaP `8.7516` edge `0.0092` maxDD `-0.3214`
- `news_risk_high->index_4h` score `-0.1245` n `139` status `ready` deltaP `7.2678` edge `0.0265` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-0.5693` n `139` status `ready` deltaP `0.5966` edge `0.0513` maxDD `-7.2607`
- `news_risk_high->metal_1h` score `-0.5759` n `139` status `ready` deltaP `0.742` edge `0.01` maxDD `-0.7016`
- `news_risk_high->fx_1h` score `-1.2178` n `139` status `ready` deltaP `-9.7166` edge `-0.0033` maxDD `-1.0436`
- `news_risk_high->fx_4h` score `-1.3241` n `139` status `ready` deltaP `8.61` edge `-0.0058` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.4561` n `139` status `ready` deltaP `-9.1562` edge `0.0238` maxDD `-3.6214`
- `news_risk_high->crypto_major_4h` score `-1.7549` n `139` status `ready` deltaP `-4.7859` edge `0.0784` maxDD `-13.719`
- `news_risk_high->commodity_1h` score `-2.0108` n `139` status `ready` deltaP `-11.5668` edge `-0.0132` maxDD `-3.3986`
- `news_risk_high->commodity_4h` score `-3.8769` n `139` status `ready` deltaP `-11.6271` edge `-0.0037` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
