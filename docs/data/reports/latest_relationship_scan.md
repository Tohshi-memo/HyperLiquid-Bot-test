# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-27T22:07:26.462310+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7854`

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

- `news_risk_high->unknown_24h` score `720.2112` n `136` status `ready` deltaP `1.2153` edge `60.0095` maxDD `0.0`
- `news_risk_high->index_24h` score `1.3535` n `136` status `ready` deltaP `17.688` edge `0.0644` maxDD `-2.2287`
- `news_risk_high->crypto_alt_24h` score `1.2186` n `136` status `ready` deltaP `14.6446` edge `0.3991` maxDD `-29.2814`
- `news_risk_high->metal_24h` score `0.8383` n `136` status `ready` deltaP `19.5977` edge `0.1247` maxDD `-6.8392`
- `news_risk_high->equity_4h` score `-0.0505` n `139` status `ready` deltaP `15.5883` edge `0.0528` maxDD `-9.2079`
- `news_risk_high->index_1h` score `-0.0815` n `139` status `ready` deltaP `2.7636` edge `0.0038` maxDD `-0.3214`
- `news_risk_high->crypto_alt_1h` score `-0.0941` n `139` status `ready` deltaP `4.323` edge `0.0544` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `-0.2701` n `139` status `ready` deltaP `2.7636` edge `0.0252` maxDD `-1.957`
- `news_risk_high->metal_1h` score `-0.7329` n `139` status `ready` deltaP `-0.3059` edge `0.0039` maxDD `-0.7016`
- `news_risk_high->fx_4h` score `-1.0341` n `139` status `ready` deltaP `13.0308` edge `0.0019` maxDD `-3.0414`
- `news_risk_high->fx_1h` score `-1.062` n `139` status `ready` deltaP `-7.022` edge `-0.0013` maxDD `-1.0436`
- `news_risk_high->equity_24h` score `-1.0671` n `136` status `ready` deltaP `11.8975` edge `0.0874` maxDD `-11.1179`
- `news_risk_high->crypto_major_1h` score `-1.1538` n `139` status `ready` deltaP `-4.0441` edge `0.0073` maxDD `-7.2607`
- `news_risk_high->index_4h` score `-1.1988` n `139` status `ready` deltaP `-3.2505` edge `0.0071` maxDD `-1.493`
- `news_risk_high->crypto_alt_4h` score `-1.8237` n `139` status `ready` deltaP `1.3336` edge `0.1051` maxDD `-15.9436`
- `news_risk_high->metal_4h` score `-1.8796` n `139` status `ready` deltaP `-13.8818` edge `0.001` maxDD `-3.6214`
- `news_risk_high->commodity_1h` score `-1.9072` n `139` status `ready` deltaP `-9.9201` edge `-0.0109` maxDD `-3.3986`
- `news_risk_high->crypto_major_24h` score `-2.9853` n `136` status `ready` deltaP `8.4252` edge `0.1385` maxDD `-26.1424`
- `news_risk_high->crypto_major_4h` score `-3.5557` n `139` status `ready` deltaP `-12.8652` edge `-0.0986` maxDD `-13.719`
- `news_risk_high->commodity_4h` score `-3.6478` n `139` status `ready` deltaP `-9.7978` edge `0.0032` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
