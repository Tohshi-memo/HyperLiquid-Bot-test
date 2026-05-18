# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-18T18:37:24.920699+00:00`
- Price records: `672`
- Market context records: `1144`
- Flow alert records: `5194`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8749`

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

- `market_context_high->crypto_major_24h` score `20.0916` n `151` status `ready` deltaP `43.3257` edge `1.4626` maxDD `-5.5043`
- `market_context_high->crypto_alt_24h` score `9.8824` n `151` status `ready` deltaP `19.6824` edge `0.8542` maxDD `-12.2838`
- `market_context_high->equity_24h` score `7.9603` n `151` status `ready` deltaP `19.1616` edge `0.6042` maxDD `-4.8203`
- `market_context_high->index_24h` score `6.222` n `151` status `ready` deltaP `17.7727` edge `0.4417` maxDD `-2.668`
- `market_context_high->metal_24h` score `5.7448` n `151` status `ready` deltaP `-1.7477` edge `0.6571` maxDD `-6.3373`
- `market_context_high->equity_4h` score `2.4186` n `168` status `ready` deltaP `11.8612` edge `0.1888` maxDD `-3.6396`
- `market_context_high->index_4h` score `1.1335` n `168` status `ready` deltaP `9.2044` edge `0.1014` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.5756` n `168` status `ready` deltaP `8.2442` edge `0.0247` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.5162` n `168` status `ready` deltaP `3.9278` edge `0.0546` maxDD `-1.3546`
- `market_context_high->crypto_major_4h` score `0.3606` n `168` status `ready` deltaP `9.9811` edge `0.1718` maxDD `-8.3693`
- `market_context_high->crypto_major_1h` score `0.1509` n `168` status `ready` deltaP `7.4316` edge `0.0396` maxDD `-4.1256`
- `market_context_high->fx_1h` score `0.0645` n `168` status `ready` deltaP `7.567` edge `0.0005` maxDD `-0.3124`
- `market_context_high->crypto_alt_1h` score `-0.1615` n `168` status `ready` deltaP `3.3932` edge `0.0482` maxDD `-3.4088`
- `market_context_high->metal_1h` score `-0.1633` n `168` status `ready` deltaP `7.2498` edge `-0.0009` maxDD `-2.2164`
- `market_context_high->crypto_alt_4h` score `-0.7862` n `168` status `ready` deltaP `7.2155` edge `0.1476` maxDD `-16.7194`
- `market_context_high->fx_4h` score `-0.8472` n `168` status `ready` deltaP `-1.0453` edge `-0.002` maxDD `-1.6381`
- `market_context_high->commodity_1h` score `-0.8525` n `168` status `ready` deltaP `-3.1223` edge `-0.0077` maxDD `-3.7959`
- `market_context_high->metal_4h` score `-2.2831` n `168` status `ready` deltaP `7.4622` edge `-0.0446` maxDD `-9.2991`
- `market_context_high->unknown_24h` score `-2.957` n `151` status `ready` deltaP `4.0276` edge `-0.0003` maxDD `-10.1706`
- `market_context_high->unknown_4h` score `-3.3302` n `168` status `ready` deltaP `8.856` edge `-0.2149` maxDD `-6.7322`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
