# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-07T12:07:29.967541+00:00`
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

- `market_context_high->commodity_4h` score `1.1281` n `119` status `ready` deltaP `13.0252` edge `0.0918` maxDD `-2.7703`
- `market_context_high->commodity_1h` score `0.5184` n `119` status `ready` deltaP `8.3405` edge `0.0292` maxDD `-1.3282`
- `market_context_high->fx_24h` score `0.4665` n `112` status `ready` deltaP `19.6965` edge `0.0482` maxDD `-4.2424`
- `market_context_high->metal_24h` score `0.3623` n `112` status `ready` deltaP `0.6365` edge `0.1356` maxDD `-2.4386`
- `market_context_high->fx_1h` score `0.1225` n `119` status `ready` deltaP `7.9832` edge `-0.0025` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.1598` n `119` status `ready` deltaP `9.1207` edge `0.0047` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.6003` n `119` status `ready` deltaP `-2.8393` edge `-0.0095` maxDD `-1.5489`
- `market_context_high->crypto_alt_1h` score `-0.7988` n `119` status `ready` deltaP `-3.1726` edge `-0.0102` maxDD `-3.0178`
- `market_context_high->index_1h` score `-0.9796` n `119` status `ready` deltaP `-2.5399` edge `-0.0113` maxDD `-1.6054`
- `market_context_high->equity_1h` score `-1.2273` n `119` status `ready` deltaP `4.3086` edge `-0.0296` maxDD `-10.5179`
- `market_context_high->crypto_alt_4h` score `-1.3776` n `119` status `ready` deltaP `0.5803` edge `-0.0415` maxDD `-5.7857`
- `market_context_high->index_4h` score `-1.5168` n `119` status `ready` deltaP `-6.0681` edge `-0.029` maxDD `-4.6675`
- `market_context_high->index_24h` score `-1.745` n `112` status `ready` deltaP `-1.2372` edge `0.0732` maxDD `-7.4964`
- `market_context_high->metal_4h` score `-1.7964` n `119` status `ready` deltaP `-2.9924` edge `-0.0129` maxDD `-3.0147`
- `market_context_high->crypto_major_1h` score `-2.6355` n `119` status `ready` deltaP `-6.5441` edge `-0.0418` maxDD `-7.4022`
- `market_context_high->crypto_alt_24h` score `-3.713` n `112` status `ready` deltaP `-10.1717` edge `-0.0973` maxDD `-4.5445`
- `market_context_high->equity_4h` score `-5.9669` n `119` status `ready` deltaP `0.3574` edge `-0.2385` maxDD `-34.9766`
- `market_context_high->commodity_24h` score `-6.0448` n `112` status `ready` deltaP `11.2106` edge `0.0268` maxDD `-52.7876`
- `market_context_high->crypto_major_4h` score `-7.5645` n `119` status `ready` deltaP `-7.6822` edge `-0.1691` maxDD `-26.4717`
- `market_context_high->unknown_1h` score `-8.0673` n `119` status `ready` deltaP `1.536` edge `-0.6378` maxDD `-1.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
