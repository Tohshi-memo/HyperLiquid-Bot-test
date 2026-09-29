# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-29T00:37:29.516541+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7166`

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

- `news_risk_high->unknown_24h` score `2650.8096` n `139` status `ready` deltaP `1.2153` edge `220.8927` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `12.2658` n `139` status `ready` deltaP `28.5946` edge `1.2267` maxDD `-29.2814`
- `news_risk_high->equity_24h` score `7.9021` n `139` status `ready` deltaP `28.1924` edge `0.7262` maxDD `-11.1179`
- `news_risk_high->crypto_major_24h` score `7.0856` n `139` status `ready` deltaP `23.8521` edge `0.8749` maxDD `-26.1424`
- `news_risk_high->index_24h` score `3.6752` n `139` status `ready` deltaP `33.8242` edge `0.1503` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `3.0876` n `139` status `ready` deltaP `26.2041` edge `0.2681` maxDD `-6.8392`
- `news_risk_high->equity_4h` score `2.5839` n `139` status `ready` deltaP `27.1736` edge `0.1951` maxDD `-9.2079`
- `news_risk_high->crypto_alt_4h` score `0.9527` n `139` status `ready` deltaP `8.4982` edge `0.2887` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `0.6399` n `139` status `ready` deltaP `7.0176` edge `0.0976` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.5811` n `139` status `ready` deltaP `7.8534` edge `0.0622` maxDD `-1.957`
- `news_risk_high->index_1h` score `0.4851` n `139` status `ready` deltaP `9.051` edge `0.0091` maxDD `-0.3214`
- `news_risk_high->index_4h` score `-0.1161` n `139` status `ready` deltaP `7.2678` edge `0.0272` maxDD `-1.493`
- `news_risk_high->metal_1h` score `-0.4812` n `139` status `ready` deltaP `1.7899` edge `0.0109` maxDD `-0.7016`
- `news_risk_high->crypto_major_1h` score `-0.6012` n `139` status `ready` deltaP `0.2972` edge `0.0492` maxDD `-7.2607`
- `news_risk_high->fx_1h` score `-1.2419` n `139` status `ready` deltaP `-10.1657` edge `-0.0034` maxDD `-1.0436`
- `news_risk_high->fx_4h` score `-1.3486` n `139` status `ready` deltaP `8.1527` edge `-0.0059` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.4169` n `139` status `ready` deltaP `-9.0037` edge `0.0278` maxDD `-3.6214`
- `news_risk_high->crypto_major_4h` score `-1.922` n `139` status `ready` deltaP `-5.853` edge `0.0641` maxDD `-13.719`
- `news_risk_high->commodity_1h` score `-2.0022` n `139` status `ready` deltaP `-11.4171` edge `-0.0131` maxDD `-3.3986`
- `news_risk_high->commodity_4h` score `-3.7654` n `139` status `ready` deltaP `-10.7124` edge `-0.0005` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
