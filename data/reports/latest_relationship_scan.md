# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-07T12:37:31.694775+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11740`

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

- `market_context_high->commodity_4h` score `1.1753` n `119` status `ready` deltaP `13.3301` edge `0.0937` maxDD `-2.7703`
- `market_context_high->commodity_1h` score `0.5542` n `120` status `ready` deltaP `8.6976` edge `0.0298` maxDD `-1.3282`
- `market_context_high->fx_24h` score `0.4783` n `112` status `ready` deltaP `19.8635` edge `0.0486` maxDD `-4.2424`
- `market_context_high->metal_24h` score `0.314` n `112` status `ready` deltaP `0.3026` edge `0.1338` maxDD `-2.4386`
- `market_context_high->fx_1h` score `0.1326` n `120` status `ready` deltaP `7.5` edge `-0.0031` maxDD `-0.8679`
- `market_context_high->fx_4h` score `-0.1416` n `119` status `ready` deltaP `9.4256` edge `0.005` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.581` n `120` status `ready` deltaP `-2.5898` edge `-0.0087` maxDD `-1.5489`
- `market_context_high->index_1h` score `-0.6183` n `120` status `ready` deltaP `-2.2904` edge `-0.0106` maxDD `-1.6054`
- `market_context_high->crypto_alt_1h` score `-0.8315` n `120` status `ready` deltaP `-3.5928` edge `-0.0116` maxDD `-3.0178`
- `market_context_high->equity_1h` score `-1.188` n `120` status `ready` deltaP `4.6308` edge `-0.0267` maxDD `-10.5179`
- `market_context_high->crypto_alt_4h` score `-1.4028` n `119` status `ready` deltaP `0.2754` edge `-0.0427` maxDD `-5.7857`
- `market_context_high->index_4h` score `-1.5271` n `119` status `ready` deltaP `-6.2205` edge `-0.0293` maxDD `-4.6675`
- `market_context_high->index_24h` score `-1.7933` n `112` status `ready` deltaP `-1.5711` edge `0.0714` maxDD `-7.4964`
- `market_context_high->metal_4h` score `-1.8` n `119` status `ready` deltaP `-2.9924` edge `-0.0132` maxDD `-3.0147`
- `market_context_high->crypto_major_1h` score `-2.6273` n `120` status `ready` deltaP `-6.3673` edge `-0.0423` maxDD `-7.4022`
- `market_context_high->crypto_alt_24h` score `-3.725` n `112` status `ready` deltaP `-10.1717` edge `-0.0983` maxDD `-4.5445`
- `market_context_high->equity_4h` score `-5.9827` n `119` status `ready` deltaP `0.2049` edge `-0.2395` maxDD `-34.9766`
- `market_context_high->commodity_24h` score `-6.0269` n `112` status `ready` deltaP `11.2106` edge `0.0291` maxDD `-52.7876`
- `market_context_high->crypto_major_4h` score `-7.6501` n `119` status `ready` deltaP `-7.9871` edge `-0.1742` maxDD `-26.4717`
- `market_context_high->unknown_1h` score `-8.1367` n `120` status `ready` deltaP `0.9381` edge `-0.6396` maxDD `-1.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
