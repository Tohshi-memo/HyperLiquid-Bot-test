# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-08T17:37:26.085486+00:00`
- Price records: `672`
- Market context records: `3301`
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

- `risk_on_high->crypto_major_4h` score `15.8673` n `32` status `ready` deltaP `30.0305` edge `1.2343` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `15.8673` n `32` status `ready` deltaP `30.0305` edge `1.2343` maxDD `-5.9781`
- `market_context_high->crypto_alt_24h` score `14.1264` n `118` status `ready` deltaP `19.1884` edge `2.6673` maxDD `-70.3986`
- `market_context_high->index_24h` score `9.9274` n `118` status `ready` deltaP `31.5502` edge `0.8724` maxDD `-16.1026`
- `market_context_high->commodity_24h` score `9.3045` n `118` status `ready` deltaP `35.7463` edge `0.6438` maxDD `-5.2052`
- `market_context_high->equity_24h` score `7.7387` n `118` status `ready` deltaP `22.7195` edge `1.6823` maxDD `-53.663`
- `risk_on_high->crypto_alt_4h` score `7.5567` n `32` status `ready` deltaP `10.747` edge `0.7425` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `7.5567` n `32` status `ready` deltaP `10.747` edge `0.7425` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `3.6612` n `32` status `ready` deltaP `14.4055` edge `0.4868` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `3.6612` n `32` status `ready` deltaP `14.4055` edge `0.4868` maxDD `-5.7426`
- `market_context_high->commodity_4h` score `2.0843` n `179` status `ready` deltaP `19.1716` edge `0.1417` maxDD `-3.9989`
- `risk_on_high->crypto_major_1h` score `2.0806` n `32` status `ready` deltaP `7.1669` edge `0.3259` maxDD `-5.8885`
- `risk_on_and_context->crypto_major_1h` score `2.0806` n `32` status `ready` deltaP `7.1669` edge `0.3259` maxDD `-5.8885`
- `market_context_high->crypto_major_24h` score `1.7012` n `118` status `ready` deltaP `19.8329` edge `2.1558` maxDD `-152.2601`
- `risk_on_high->index_4h` score `1.134` n `32` status `ready` deltaP `1.2957` edge `0.1955` maxDD `-1.7001`
- `risk_on_and_context->index_4h` score `1.134` n `32` status `ready` deltaP `1.2957` edge `0.1955` maxDD `-1.7001`
- `risk_on_high->metal_1h` score `0.3047` n `32` status `ready` deltaP `6.6991` edge `0.0629` maxDD `-1.4793`
- `risk_on_and_context->metal_1h` score `0.3047` n `32` status `ready` deltaP `6.6991` edge `0.0629` maxDD `-1.4793`
- `risk_on_high->crypto_alt_1h` score `0.2781` n `32` status `ready` deltaP `0.8982` edge `0.1734` maxDD `-8.1649`
- `risk_on_and_context->crypto_alt_1h` score `0.2781` n `32` status `ready` deltaP `0.8982` edge `0.1734` maxDD `-8.1649`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
