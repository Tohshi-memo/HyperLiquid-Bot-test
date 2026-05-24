# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-24T02:07:19.276823+00:00`
- Price records: `672`
- Market context records: `1690`
- Flow alert records: `6773`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8854`

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

- `market_context_high->metal_24h` score `7.2073` n `145` status `ready` deltaP `26.1914` edge `0.6686` maxDD `-12.7414`
- `market_context_high->unknown_24h` score `5.7983` n `145` status `ready` deltaP `17.1949` edge `0.9006` maxDD `-35.8966`
- `market_context_high->crypto_alt_4h` score `5.3622` n `192` status `ready` deltaP `23.1707` edge `0.5588` maxDD `-16.3135`
- `market_context_high->crypto_major_4h` score `3.9065` n `192` status `ready` deltaP `21.7988` edge `0.4511` maxDD `-13.3376`
- `market_context_high->index_24h` score `3.8782` n `145` status `ready` deltaP `17.548` edge `0.344` maxDD `-5.3574`
- `market_context_high->equity_4h` score `2.9571` n `192` status `ready` deltaP `15.7012` edge `0.2512` maxDD `-5.0894`
- `market_context_high->equity_24h` score `1.8994` n `145` status `ready` deltaP `16.5195` edge `0.538` maxDD `-33.1875`
- `market_context_high->crypto_alt_1h` score `0.6379` n `201` status `ready` deltaP `6.2584` edge `0.1138` maxDD `-4.1892`
- `market_context_high->crypto_alt_24h` score `0.3928` n `145` status `ready` deltaP `24.4422` edge `1.0507` maxDD `-88.8062`
- `market_context_high->index_4h` score `0.2843` n `192` status `ready` deltaP `6.9741` edge `0.0861` maxDD `-3.7119`
- `market_context_high->equity_1h` score `-0.0017` n `201` status `ready` deltaP `4.5015` edge `0.0507` maxDD `-2.8014`
- `market_context_high->crypto_major_1h` score `-0.1608` n `201` status `ready` deltaP `3.7753` edge `0.0796` maxDD `-4.7865`
- `market_context_high->crypto_major_24h` score `-0.4732` n `145` status `ready` deltaP `22.9066` edge `0.6452` maxDD `-62.3533`
- `market_context_high->index_1h` score `-0.507` n `201` status `ready` deltaP `0.7679` edge `0.0158` maxDD `-1.7205`
- `market_context_high->metal_1h` score `-0.5741` n `201` status `ready` deltaP `6.461` edge `0.0169` maxDD `-6.3532`
- `market_context_high->metal_4h` score `-0.5974` n `192` status `ready` deltaP `12.0299` edge `0.1392` maxDD `-12.5349`
- `market_context_high->fx_24h` score `-0.7569` n `145` status `ready` deltaP `5.0746` edge `0.008` maxDD `-1.3925`
- `market_context_high->fx_1h` score `-1.0041` n `201` status `ready` deltaP `-2.6924` edge `-0.0025` maxDD `-0.3914`
- `market_context_high->fx_4h` score `-1.7044` n `192` status `ready` deltaP `-5.8562` edge `-0.0101` maxDD `-1.4313`
- `market_context_high->commodity_1h` score `-2.0903` n `201` status `ready` deltaP `0.9399` edge `-0.0288` maxDD `-14.9691`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
