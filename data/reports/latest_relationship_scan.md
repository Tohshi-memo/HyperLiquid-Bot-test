# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-02T10:22:20.556509+00:00`
- Price records: `672`
- Market context records: `2653`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9223`

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

- `market_context_high->unknown_24h` score `7.8501` n `124` status `ready` deltaP `17.4451` edge `0.5707` maxDD `-1.626`
- `market_context_high->crypto_alt_24h` score `6.9834` n `124` status `ready` deltaP `11.0047` edge `0.86` maxDD `-20.1131`
- `market_context_high->crypto_alt_4h` score `5.4542` n `124` status `ready` deltaP `25.7572` edge `0.5507` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `4.1374` n `124` status `ready` deltaP `16.4978` edge `0.4158` maxDD `-10.1468`
- `market_context_high->unknown_4h` score `1.7862` n `124` status `ready` deltaP `9.9183` edge `0.1877` maxDD `-3.7312`
- `market_context_high->crypto_alt_1h` score `0.9483` n `133` status `ready` deltaP `9.0991` edge `0.1371` maxDD `-6.1656`
- `market_context_high->index_24h` score `0.7405` n `124` status `ready` deltaP `10.2431` edge `0.0915` maxDD `-2.5127`
- `market_context_high->crypto_major_1h` score `0.3902` n `133` status `ready` deltaP `6.2447` edge `0.1103` maxDD `-4.2199`
- `market_context_high->index_4h` score `0.1165` n `124` status `ready` deltaP `8.4383` edge `0.0376` maxDD `-2.3986`
- `market_context_high->metal_4h` score `-0.0467` n `124` status `ready` deltaP `6.2746` edge `0.0359` maxDD `-2.5301`
- `market_context_high->index_1h` score `-0.06` n `133` status `ready` deltaP `4.455` edge `0.0147` maxDD `-1.2855`
- `market_context_high->unknown_1h` score `-0.1721` n `133` status `ready` deltaP `1.7401` edge `0.0282` maxDD `-1.665`
- `market_context_high->commodity_1h` score `-0.4305` n `133` status `ready` deltaP `4.132` edge `0.0051` maxDD `-4.3601`
- `market_context_high->metal_1h` score `-0.5176` n `133` status `ready` deltaP `-1.2809` edge `0.0007` maxDD `-1.6811`
- `market_context_high->fx_24h` score `-0.5549` n `124` status `ready` deltaP `6.2948` edge `-0.0004` maxDD `-0.6911`
- `market_context_high->fx_1h` score `-0.6132` n `133` status `ready` deltaP `-1.4205` edge `0.003` maxDD `-0.2373`
- `market_context_high->equity_1h` score `-0.9392` n `133` status `ready` deltaP `-1.9821` edge `0.0188` maxDD `-2.7085`
- `market_context_high->fx_4h` score `-0.9747` n `124` status `ready` deltaP `-2.5915` edge `0.0107` maxDD `-0.6386`
- `market_context_high->commodity_4h` score `-1.227` n `124` status `ready` deltaP `3.4667` edge `0.0116` maxDD `-10.0279`
- `market_context_high->equity_24h` score `-1.3501` n `124` status `ready` deltaP `7.5661` edge `-0.0652` maxDD `-3.1535`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
