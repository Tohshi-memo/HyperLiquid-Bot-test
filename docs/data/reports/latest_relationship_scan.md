# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-14T08:22:29.331399+00:00`
- Price records: `672`
- Market context records: `6691`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11784`

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

- `market_context_high->commodity_24h` score `0.578` n `191` status `ready` deltaP `10.603` edge `0.1643` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `0.4593` n `191` status `ready` deltaP `9.9837` edge `0.0577` maxDD `-4.2122`
- `market_context_high->unknown_24h` score `0.423` n `191` status `ready` deltaP `-1.3117` edge `0.4382` maxDD `-12.3511`
- `market_context_high->crypto_alt_1h` score `0.2291` n `191` status `ready` deltaP `6.8416` edge `0.0499` maxDD `-3.7803`
- `market_context_high->unknown_1h` score `-0.1003` n `191` status `ready` deltaP `-5.1235` edge `0.1159` maxDD `-3.2083`
- `market_context_high->fx_1h` score `-0.304` n `191` status `ready` deltaP `1.537` edge `0.001` maxDD `-0.6845`
- `market_context_high->index_1h` score `-0.4578` n `191` status `ready` deltaP `1.16` edge `0.005` maxDD `-0.7136`
- `market_context_high->equity_1h` score `-0.5034` n `191` status `ready` deltaP `4.2245` edge `0.01` maxDD `-3.8827`
- `market_context_high->metal_1h` score `-0.5274` n `191` status `ready` deltaP `-2.6539` edge `0.0026` maxDD `-1.2017`
- `market_context_high->commodity_1h` score `-0.5686` n `191` status `ready` deltaP `0.6325` edge `-0.0088` maxDD `-2.1314`
- `market_context_high->index_4h` score `-0.9346` n `191` status `ready` deltaP `10.1033` edge `0.0008` maxDD `-5.7046`
- `market_context_high->fx_4h` score `-1.3956` n `191` status `ready` deltaP `6.4192` edge `-0.0013` maxDD `-3.3001`
- `market_context_high->crypto_major_4h` score `-1.5108` n `191` status `ready` deltaP `8.0489` edge `0.0841` maxDD `-16.8495`
- `market_context_high->commodity_4h` score `-1.6689` n `191` status `ready` deltaP `-3.914` edge `-0.0384` maxDD `-5.6246`
- `market_context_high->crypto_alt_4h` score `-1.7673` n `191` status `ready` deltaP `6.001` edge `0.0736` maxDD `-19.2145`
- `market_context_high->metal_4h` score `-2.1646` n `191` status `ready` deltaP `-1.7789` edge `0.0204` maxDD `-5.2172`
- `market_context_high->unknown_4h` score `-3.3189` n `191` status `ready` deltaP `-16.3062` edge `0.0727` maxDD `-10.5788`
- `market_context_high->equity_4h` score `-5.2617` n `191` status `ready` deltaP `6.6506` edge `-0.0559` maxDD `-27.1529`
- `market_context_high->fx_24h` score `-5.3494` n `191` status `ready` deltaP `-10.5975` edge `-0.0065` maxDD `-8.8238`
- `market_context_high->metal_24h` score `-7.0143` n `191` status `ready` deltaP `-6.2627` edge `-0.009` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
