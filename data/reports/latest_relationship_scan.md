# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-28T04:07:31.801694+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7786`

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

- `news_risk_high->unknown_24h` score `590.772` n `139` status `ready` deltaP `1.2153` edge `49.2229` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `2.5604` n `139` status `ready` deltaP `15.053` edge `0.5082` maxDD `-29.2814`
- `news_risk_high->index_24h` score `1.7587` n `139` status `ready` deltaP `19.5881` edge `0.0855` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `0.9678` n `139` status `ready` deltaP `20.3013` edge `0.1308` maxDD `-6.8392`
- `news_risk_high->equity_4h` score `0.6046` n `139` status `ready` deltaP `18.3322` edge `0.0891` maxDD `-9.2079`
- `news_risk_high->equity_24h` score `0.3744` n `139` status `ready` deltaP `13.9563` edge `0.1938` maxDD `-11.1179`
- `news_risk_high->crypto_alt_1h` score `0.2141` n `139` status `ready` deltaP `5.3709` edge `0.0731` maxDD `-4.2849`
- `news_risk_high->index_1h` score `0.0946` n `139` status `ready` deltaP `4.7097` edge `0.0055` maxDD `-0.3214`
- `news_risk_high->equity_1h` score `0.0069` n `139` status `ready` deltaP `4.2606` edge `0.0383` maxDD `-1.957`
- `news_risk_high->crypto_major_24h` score `-0.4494` n `139` status `ready` deltaP `10.4841` edge `0.3361` maxDD `-26.1424`
- `news_risk_high->metal_1h` score `-0.6011` n `139` status `ready` deltaP `0.742` edge `0.0079` maxDD `-0.7016`
- `news_risk_high->index_4h` score `-0.8669` n `139` status `ready` deltaP `0.1031` edge `0.0124` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-0.9722` n `139` status `ready` deltaP `-2.3974` edge `0.0196` maxDD `-7.2607`
- `news_risk_high->crypto_alt_4h` score `-1.0609` n `139` status `ready` deltaP `3.7726` edge `0.1524` maxDD `-15.9436`
- `news_risk_high->fx_1h` score `-1.108` n `139` status `ready` deltaP `-7.7705` edge `-0.0022` maxDD `-1.0436`
- `news_risk_high->fx_4h` score `-1.1795` n `139` status `ready` deltaP `10.7442` edge `-0.0015` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.7448` n `139` status `ready` deltaP `-13.1196` edge `0.0132` maxDD `-3.6214`
- `news_risk_high->commodity_1h` score `-1.9516` n `139` status `ready` deltaP `-10.6686` edge `-0.0116` maxDD `-3.3986`
- `news_risk_high->crypto_major_4h` score `-3.1691` n `139` status `ready` deltaP `-10.4262` edge `-0.0653` maxDD `-13.719`
- `news_risk_high->commodity_4h` score `-3.4972` n `139` status `ready` deltaP `-8.4258` edge `0.0066` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
