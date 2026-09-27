# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-27T20:37:30.049687+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7928`

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

- `news_risk_high->unknown_24h` score `719.8284` n `136` status `ready` deltaP `1.2153` edge `59.9776` maxDD `0.0`
- `news_risk_high->index_24h` score `1.27` n `136` status `ready` deltaP `17.5143` edge `0.0586` maxDD `-2.2287`
- `news_risk_high->crypto_alt_24h` score `0.8562` n `136` status `ready` deltaP `14.6446` edge `0.3689` maxDD `-29.2814`
- `news_risk_high->metal_24h` score `0.7454` n `136` status `ready` deltaP `18.556` edge `0.1239` maxDD `-6.8392`
- `news_risk_high->index_1h` score `-0.1235` n `139` status `ready` deltaP `2.3145` edge `0.0033` maxDD `-0.3214`
- `news_risk_high->equity_4h` score `-0.1527` n `139` status `ready` deltaP `15.4358` edge `0.0453` maxDD `-9.2079`
- `news_risk_high->crypto_alt_1h` score `-0.1804` n `139` status `ready` deltaP `3.8739` edge `0.0502` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `-0.3575` n `139` status `ready` deltaP `2.0151` edge `0.0229` maxDD `-1.957`
- `news_risk_high->metal_1h` score `-0.776` n `139` status `ready` deltaP `-0.755` edge `0.0033` maxDD `-0.7016`
- `news_risk_high->fx_4h` score `-1.0697` n `139` status `ready` deltaP `12.421` edge `0.0014` maxDD `-3.0414`
- `news_risk_high->fx_1h` score `-1.0979` n `139` status `ready` deltaP `-7.6208` edge `-0.0019` maxDD `-1.0436`
- `news_risk_high->crypto_major_1h` score `-1.2114` n `139` status `ready` deltaP `-4.4932` edge `0.0029` maxDD `-7.2607`
- `news_risk_high->index_4h` score `-1.2254` n `139` status `ready` deltaP `-3.403` edge `0.0059` maxDD `-1.493`
- `news_risk_high->equity_24h` score `-1.3755` n `136` status `ready` deltaP `11.8975` edge `0.0617` maxDD `-11.1179`
- `news_risk_high->commodity_1h` score `-1.8566` n `139` status `ready` deltaP `-9.1716` edge `-0.0094` maxDD `-3.3986`
- `news_risk_high->crypto_alt_4h` score `-1.8753` n `139` status `ready` deltaP `1.3336` edge `0.1008` maxDD `-15.9436`
- `news_risk_high->metal_4h` score `-1.9215` n `139` status `ready` deltaP `-14.4915` edge `-0.0003` maxDD `-3.6214`
- `news_risk_high->commodity_4h` score `-3.5172` n `139` status `ready` deltaP `-9.0356` edge `0.009` maxDD `-8.6825`
- `news_risk_high->crypto_major_4h` score `-3.6612` n `139` status `ready` deltaP `-13.1701` edge `-0.1101` maxDD `-13.719`
- `news_risk_high->crypto_major_24h` score `-3.742` n `136` status `ready` deltaP `8.2516` edge `0.0766` maxDD `-26.1424`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
