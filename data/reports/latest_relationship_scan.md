# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-06T02:52:28.606154+00:00`
- Price records: `672`
- Market context records: `5838`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10094`

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

- `market_context_high->equity_4h` score `0.6542` n `266` status `ready` deltaP `7.6792` edge `0.1491` maxDD `-6.9958`
- `market_context_high->fx_1h` score `-0.3253` n `266` status `ready` deltaP `1.0547` edge `-0.0002` maxDD `-0.5499`
- `market_context_high->equity_1h` score `-0.4068` n `266` status `ready` deltaP `4.1691` edge `0.039` maxDD `-5.0555`
- `market_context_high->commodity_1h` score `-0.534` n `266` status `ready` deltaP `-0.9151` edge `-0.0021` maxDD `-2.1545`
- `market_context_high->index_1h` score `-0.5443` n `266` status `ready` deltaP `1.3642` edge `0.0059` maxDD `-0.7819`
- `market_context_high->equity_24h` score `-0.5775` n `238` status `ready` deltaP `15.8949` edge `0.3538` maxDD `-31.6316`
- `market_context_high->metal_1h` score `-0.6227` n `266` status `ready` deltaP `2.1892` edge `0.0006` maxDD `-2.0339`
- `market_context_high->crypto_major_1h` score `-1.0116` n `266` status `ready` deltaP `2.5652` edge `0.0307` maxDD `-6.2348`
- `market_context_high->index_4h` score `-1.1732` n `266` status `ready` deltaP `0.588` edge `0.0144` maxDD `-3.165`
- `market_context_high->crypto_alt_1h` score `-1.1913` n `266` status `ready` deltaP `1.0614` edge `0.0271` maxDD `-6.6758`
- `market_context_high->fx_4h` score `-1.6546` n `266` status `ready` deltaP `-2.3576` edge `-0.0015` maxDD `-2.2593`
- `market_context_high->fx_24h` score `-1.66` n `238` status `ready` deltaP `7.2566` edge `0.0206` maxDD `-5.5435`
- `market_context_high->metal_4h` score `-2.2028` n `266` status `ready` deltaP `-5.2035` edge `-0.0446` maxDD `-8.9164`
- `market_context_high->commodity_4h` score `-2.5553` n `266` status `ready` deltaP `-0.9021` edge `-0.0146` maxDD `-8.0531`
- `market_context_high->index_24h` score `-2.9008` n `238` status `ready` deltaP `2.9207` edge `0.0231` maxDD `-18.1572`
- `market_context_high->crypto_major_4h` score `-3.1218` n `266` status `ready` deltaP `6.2981` edge `0.1351` maxDD `-25.6458`
- `market_context_high->metal_24h` score `-4.85` n `238` status `ready` deltaP `0.4567` edge `-0.2031` maxDD `-8.329`
- `market_context_high->crypto_alt_4h` score `-4.8962` n `266` status `ready` deltaP `3.8293` edge `0.0673` maxDD `-28.7346`
- `market_context_high->commodity_24h` score `-8.6891` n `238` status `ready` deltaP `-10.7158` edge `-0.0567` maxDD `-30.3426`
- `market_context_high->crypto_alt_24h` score `-12.8332` n `238` status `ready` deltaP `-12.2534` edge `-0.5329` maxDD `-61.7883`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
