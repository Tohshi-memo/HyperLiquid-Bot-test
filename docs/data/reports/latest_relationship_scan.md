# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-18T11:07:18.917603+00:00`
- Price records: `672`
- Market context records: `1111`
- Flow alert records: `5104`
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

- `market_context_high->crypto_major_24h` score `17.9162` n `150` status `ready` deltaP `38.7709` edge `1.2809` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `7.5033` n `150` status `ready` deltaP `15.1319` edge `0.6478` maxDD `-9.5387`
- `market_context_high->equity_24h` score `6.4015` n `150` status `ready` deltaP `16.1736` edge `0.4753` maxDD `-3.6396`
- `market_context_high->metal_24h` score `5.5024` n `150` status `ready` deltaP `-2.0625` edge `0.639` maxDD `-6.3373`
- `market_context_high->index_24h` score `5.0733` n `150` status `ready` deltaP `15.1319` edge `0.3527` maxDD `-2.1308`
- `market_context_high->equity_4h` score `1.6802` n `168` status `ready` deltaP `9.7271` edge `0.1415` maxDD `-3.6396`
- `market_context_high->index_4h` score `0.8814` n `168` status `ready` deltaP `8.1373` edge `0.0875` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.4702` n `168` status `ready` deltaP `7.4957` edge `0.0209` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.2896` n `168` status `ready` deltaP `2.7302` edge `0.0437` maxDD `-1.3546`
- `market_context_high->fx_1h` score `0.11` n `168` status `ready` deltaP `8.0161` edge `0.0013` maxDD `-0.3124`
- `market_context_high->crypto_major_1h` score `0.0873` n `168` status `ready` deltaP `7.2819` edge `0.0353` maxDD `-4.1256`
- `market_context_high->crypto_major_4h` score `0.0566` n `168` status `ready` deltaP `8.4567` edge `0.143` maxDD `-8.3693`
- `market_context_high->metal_1h` score `-0.1777` n `168` status `ready` deltaP `7.1001` edge `-0.0011` maxDD `-2.2164`
- `market_context_high->crypto_alt_1h` score `-0.2058` n `168` status `ready` deltaP `3.2435` edge `0.0455` maxDD `-3.4088`
- `market_context_high->fx_4h` score `-0.7041` n `168` status `ready` deltaP `1.2412` edge `0.0011` maxDD `-1.6381`
- `market_context_high->commodity_1h` score `-0.7396` n `168` status `ready` deltaP `-1.775` edge `-0.0022` maxDD `-3.7959`
- `market_context_high->crypto_alt_4h` score `-0.9909` n `168` status `ready` deltaP `5.8435` edge `0.1305` maxDD `-16.7194`
- `market_context_high->metal_4h` score `-2.3621` n `168` status `ready` deltaP `6.7` edge `-0.0461` maxDD `-9.2991`
- `market_context_high->commodity_4h` score `-3.1424` n `168` status `ready` deltaP `-10.8159` edge `-0.014` maxDD `-13.0076`
- `market_context_high->unknown_4h` score `-3.3394` n `168` status `ready` deltaP `9.1609` edge `-0.2177` maxDD `-6.7322`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
