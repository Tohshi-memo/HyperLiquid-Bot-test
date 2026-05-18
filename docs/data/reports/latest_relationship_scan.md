# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-18T11:22:17.612015+00:00`
- Price records: `672`
- Market context records: `1112`
- Flow alert records: `5107`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8704`

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

- `market_context_high->crypto_major_24h` score `18.0141` n `150` status `ready` deltaP `38.9445` edge `1.2879` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `7.6108` n `150` status `ready` deltaP `15.3055` edge `0.6556` maxDD `-9.5387`
- `market_context_high->equity_24h` score `6.4574` n `150` status `ready` deltaP `16.3472` edge `0.4788` maxDD `-3.6396`
- `market_context_high->metal_24h` score `5.5403` n `150` status `ready` deltaP `-1.8889` edge `0.641` maxDD `-6.3373`
- `market_context_high->index_24h` score `5.1196` n `150` status `ready` deltaP `15.3055` edge `0.3554` maxDD `-2.1308`
- `market_context_high->equity_4h` score `1.6632` n `168` status `ready` deltaP `9.5746` edge `0.1411` maxDD `-3.6396`
- `market_context_high->index_4h` score `0.879` n `168` status `ready` deltaP `8.1373` edge `0.0873` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.4726` n `168` status `ready` deltaP `7.4957` edge `0.0211` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.2944` n `168` status `ready` deltaP `2.7302` edge `0.0441` maxDD `-1.3546`
- `market_context_high->fx_1h` score `0.0981` n `168` status `ready` deltaP `7.8664` edge `0.0013` maxDD `-0.3124`
- `market_context_high->crypto_major_1h` score `0.0837` n `168` status `ready` deltaP `7.2819` edge `0.035` maxDD `-4.1256`
- `market_context_high->crypto_major_4h` score `0.0559` n `168` status `ready` deltaP `8.4567` edge `0.1429` maxDD `-8.3693`
- `market_context_high->metal_1h` score `-0.1609` n `168` status `ready` deltaP `7.2498` edge `-0.0007` maxDD `-2.2164`
- `market_context_high->crypto_alt_1h` score `-0.2274` n `168` status `ready` deltaP `3.0938` edge `0.0447` maxDD `-3.4088`
- `market_context_high->fx_4h` score `-0.7041` n `168` status `ready` deltaP `1.2412` edge `0.0011` maxDD `-1.6381`
- `market_context_high->commodity_1h` score `-0.7497` n `168` status `ready` deltaP `-1.9247` edge `-0.0025` maxDD `-3.7959`
- `market_context_high->crypto_alt_4h` score `-0.9924` n `168` status `ready` deltaP `5.8435` edge `0.1303` maxDD `-16.7194`
- `market_context_high->metal_4h` score `-2.3621` n `168` status `ready` deltaP `6.7` edge `-0.0461` maxDD `-9.2991`
- `market_context_high->commodity_4h` score `-3.1542` n `168` status `ready` deltaP `-10.9683` edge `-0.0145` maxDD `-13.0076`
- `market_context_high->unknown_4h` score `-3.3394` n `168` status `ready` deltaP `9.1609` edge `-0.2177` maxDD `-6.7322`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
