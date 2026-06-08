# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-08T18:37:25.673652+00:00`
- Price records: `672`
- Market context records: `3305`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13151`

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

- `risk_on_high->crypto_major_4h` score `15.7923` n `32` status `ready` deltaP `29.5732` edge `1.2311` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `15.7923` n `32` status `ready` deltaP `29.5732` edge `1.2311` maxDD `-5.9781`
- `market_context_high->crypto_alt_24h` score `14.3959` n `122` status `ready` deltaP `20.0222` edge `2.6963` maxDD `-70.3986`
- `market_context_high->index_24h` score `10.1764` n `122` status `ready` deltaP `31.8419` edge `0.8912` maxDD `-16.1026`
- `market_context_high->commodity_24h` score `8.1423` n `122` status `ready` deltaP `33.6066` edge `0.6098` maxDD `-7.7591`
- `market_context_high->equity_24h` score `8.1347` n `122` status `ready` deltaP `23.1642` edge `1.7301` maxDD `-53.663`
- `risk_on_high->crypto_alt_4h` score `7.4011` n `32` status `ready` deltaP `10.1372` edge `0.7336` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `7.4011` n `32` status `ready` deltaP `10.1372` edge `0.7336` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `3.5648` n `32` status `ready` deltaP `13.7957` edge `0.4785` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `3.5648` n `32` status `ready` deltaP `13.7957` edge `0.4785` maxDD `-5.7426`
- `market_context_high->crypto_major_24h` score `2.1222` n `122` status `ready` deltaP `20.8333` edge `2.2031` maxDD `-152.2601`
- `market_context_high->commodity_4h` score `2.1045` n `183` status `ready` deltaP `19.4247` edge `0.1417` maxDD `-3.9989`
- `risk_on_high->crypto_major_1h` score `2.0697` n `32` status `ready` deltaP `7.1669` edge `0.3245` maxDD `-5.8885`
- `risk_on_and_context->crypto_major_1h` score `2.0697` n `32` status `ready` deltaP `7.1669` edge `0.3245` maxDD `-5.8885`
- `risk_on_high->index_4h` score `1.0806` n `32` status `ready` deltaP `0.8384` edge `0.1917` maxDD `-1.7001`
- `risk_on_and_context->index_4h` score `1.0806` n `32` status `ready` deltaP `0.8384` edge `0.1917` maxDD `-1.7001`
- `risk_on_high->metal_1h` score `0.2946` n `32` status `ready` deltaP `6.5494` edge `0.0626` maxDD `-1.4793`
- `risk_on_and_context->metal_1h` score `0.2946` n `32` status `ready` deltaP `6.5494` edge `0.0626` maxDD `-1.4793`
- `risk_on_high->crypto_alt_1h` score `0.2189` n `32` status `ready` deltaP `0.2994` edge `0.1698` maxDD `-8.1649`
- `risk_on_and_context->crypto_alt_1h` score `0.2189` n `32` status `ready` deltaP `0.2994` edge `0.1698` maxDD `-8.1649`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
