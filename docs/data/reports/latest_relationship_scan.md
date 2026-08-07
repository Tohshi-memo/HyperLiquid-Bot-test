# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-07T12:26:13.021006+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11739`

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

- `market_context_high->commodity_4h` score `1.1499` n `119` status `ready` deltaP `13.1776` edge `0.0926` maxDD `-2.7703`
- `market_context_high->commodity_1h` score `0.5184` n `119` status `ready` deltaP `8.3405` edge `0.0292` maxDD `-1.3282`
- `market_context_high->fx_24h` score `0.4665` n `112` status `ready` deltaP `19.6965` edge `0.0482` maxDD `-4.2424`
- `market_context_high->metal_24h` score `0.3394` n `112` status `ready` deltaP `0.4695` edge `0.1348` maxDD `-2.4386`
- `market_context_high->fx_1h` score `0.1147` n `119` status `ready` deltaP `7.8335` edge `-0.0025` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.1511` n `119` status `ready` deltaP `9.2732` edge `0.0048` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.6003` n `119` status `ready` deltaP `-2.8393` edge `-0.0095` maxDD `-1.5489`
- `market_context_high->crypto_alt_1h` score `-0.8011` n `119` status `ready` deltaP `-3.1726` edge `-0.0105` maxDD `-3.0178`
- `market_context_high->index_1h` score `-0.9952` n `119` status `ready` deltaP `-2.6896` edge `-0.0116` maxDD `-1.6054`
- `market_context_high->equity_1h` score `-1.2359` n `119` status `ready` deltaP `4.3086` edge `-0.0307` maxDD `-10.5179`
- `market_context_high->crypto_alt_4h` score `-1.3902` n `119` status `ready` deltaP `0.4278` edge `-0.0421` maxDD `-5.7857`
- `market_context_high->index_4h` score `-1.5263` n `119` status `ready` deltaP `-6.2205` edge `-0.0292` maxDD `-4.6675`
- `market_context_high->index_24h` score `-1.7692` n `112` status `ready` deltaP `-1.4042` edge `0.0723` maxDD `-7.4964`
- `market_context_high->metal_4h` score `-1.7976` n `119` status `ready` deltaP `-2.9924` edge `-0.013` maxDD `-3.0147`
- `market_context_high->crypto_major_1h` score `-2.6606` n `119` status `ready` deltaP `-6.6938` edge `-0.0429` maxDD `-7.4022`
- `market_context_high->crypto_alt_24h` score `-3.719` n `112` status `ready` deltaP `-10.1717` edge `-0.0978` maxDD `-4.5445`
- `market_context_high->equity_4h` score `-5.9795` n `119` status `ready` deltaP `0.2049` edge `-0.2391` maxDD `-34.9766`
- `market_context_high->commodity_24h` score `-6.037` n `112` status `ready` deltaP `11.2106` edge `0.0278` maxDD `-52.7876`
- `market_context_high->crypto_major_4h` score `-7.6091` n `119` status `ready` deltaP `-7.8346` edge `-0.1718` maxDD `-26.4717`
- `market_context_high->unknown_1h` score `-8.0817` n `119` status `ready` deltaP `1.3863` edge `-0.638` maxDD `-1.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
