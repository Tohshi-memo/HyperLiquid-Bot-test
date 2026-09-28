# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-28T05:07:34.657208+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7812`

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

- `news_risk_high->unknown_24h` score `590.8296` n `139` status `ready` deltaP `1.2153` edge `49.2277` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `2.9256` n `139` status `ready` deltaP `15.7474` edge `0.534` maxDD `-29.2814`
- `news_risk_high->index_24h` score `1.8599` n `139` status `ready` deltaP `20.2825` edge `0.0893` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `1.0206` n `139` status `ready` deltaP `20.3013` edge `0.1352` maxDD `-6.8392`
- `news_risk_high->equity_4h` score `0.7878` n `139` status `ready` deltaP `18.9419` edge `0.1003` maxDD `-9.2079`
- `news_risk_high->equity_24h` score `0.7024` n `139` status `ready` deltaP `14.6507` edge `0.2165` maxDD `-11.1179`
- `news_risk_high->crypto_alt_1h` score `0.1842` n `139` status `ready` deltaP `5.2212` edge `0.0716` maxDD `-4.2849`
- `news_risk_high->crypto_major_24h` score `0.0729` n `139` status `ready` deltaP `11.1785` edge `0.375` maxDD `-26.1424`
- `news_risk_high->index_1h` score `0.0562` n `139` status `ready` deltaP `4.2606` edge `0.0053` maxDD `-0.3214`
- `news_risk_high->equity_1h` score `-0.041` n `139` status `ready` deltaP `3.8115` edge `0.0373` maxDD `-1.957`
- `news_risk_high->metal_1h` score `-0.6286` n `139` status `ready` deltaP `0.4426` edge `0.0076` maxDD `-0.7016`
- `news_risk_high->crypto_alt_4h` score `-0.759` n `139` status `ready` deltaP `4.3823` edge `0.1735` maxDD `-15.9436`
- `news_risk_high->index_4h` score `-0.8001` n `139` status `ready` deltaP `0.7129` edge `0.0139` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-0.9675` n `139` status `ready` deltaP `-2.3974` edge `0.0202` maxDD `-7.2607`
- `news_risk_high->fx_1h` score `-1.1158` n `139` status `ready` deltaP `-7.9202` edge `-0.0022` maxDD `-1.0436`
- `news_risk_high->fx_4h` score `-1.2001` n `139` status `ready` deltaP `10.4393` edge `-0.0021` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.7198` n `139` status `ready` deltaP `-12.9671` edge `0.0154` maxDD `-3.6214`
- `news_risk_high->commodity_1h` score `-1.9524` n `139` status `ready` deltaP `-10.6686` edge `-0.0117` maxDD `-3.3986`
- `news_risk_high->crypto_major_4h` score `-2.9783` n `139` status `ready` deltaP `-9.8164` edge `-0.0449` maxDD `-13.719`
- `news_risk_high->commodity_4h` score `-3.547` n `139` status `ready` deltaP `-8.8832` edge `0.0055` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
