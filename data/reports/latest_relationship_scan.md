# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-29T17:37:35.511383+00:00`
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

- `news_risk_high->unknown_24h` score `2589.1339` n `139` status `ready` deltaP `1.3889` edge `215.7519` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `16.0309` n `139` status `ready` deltaP `31.1988` edge `1.5231` maxDD `-29.2814`
- `news_risk_high->equity_24h` score `9.7867` n `139` status `ready` deltaP `33.2271` edge `0.8487` maxDD `-11.039`
- `news_risk_high->crypto_major_24h` score `7.8361` n `139` status `ready` deltaP `24.8938` edge `0.9305` maxDD `-26.1424`
- `news_risk_high->index_24h` score `4.1474` n `139` status `ready` deltaP `38.5117` edge `0.1584` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `3.7234` n `139` status `ready` deltaP `31.586` edge `0.2852` maxDD `-6.8392`
- `news_risk_high->equity_4h` score `2.8863` n `142` status `ready` deltaP `29.0472` edge `0.207` maxDD `-9.143`
- `news_risk_high->crypto_alt_4h` score `1.6099` n `142` status `ready` deltaP `10.1576` edge `0.3324` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `1.0703` n `142` status `ready` deltaP `8.1682` edge `0.1258` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.7474` n `142` status `ready` deltaP `8.6004` edge `0.0709` maxDD `-1.9431`
- `news_risk_high->index_1h` score `0.5629` n `142` status `ready` deltaP `9.6483` edge `0.0116` maxDD `-0.3214`
- `news_risk_high->index_4h` score `0.1888` n `142` status `ready` deltaP `10.3594` edge `0.032` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-0.2356` n `142` status `ready` deltaP `3.188` edge `0.0768` maxDD `-7.2607`
- `news_risk_high->metal_1h` score `-0.4666` n `142` status `ready` deltaP `1.4632` edge `0.0143` maxDD `-0.7016`
- `news_risk_high->metal_4h` score `-1.2138` n `142` status `ready` deltaP `-6.4776` edge `0.037` maxDD `-3.6214`
- `news_risk_high->fx_4h` score `-1.2842` n `142` status `ready` deltaP `9.4362` edge `-0.0062` maxDD `-3.0414`
- `news_risk_high->crypto_major_4h` score `-1.4584` n `142` status `ready` deltaP `-3.4632` edge `0.1076` maxDD `-13.719`
- `news_risk_high->fx_1h` score `-1.769` n `142` status `ready` deltaP `-8.3959` edge `-0.0034` maxDD `-1.0436`
- `news_risk_high->commodity_1h` score `-1.9087` n `142` status `ready` deltaP `-9.9034` edge `-0.0112` maxDD `-3.3986`
- `news_risk_high->commodity_4h` score `-2.3797` n `142` status `ready` deltaP `-10.0695` edge `0.0039` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
