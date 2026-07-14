# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-14T16:52:27.961077+00:00`
- Price records: `672`
- Market context records: `6727`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11720`

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

- `market_context_high->unknown_24h` score `1.3736` n `176` status `ready` deltaP `2.7935` edge `0.5327` maxDD `-12.3511`
- `market_context_high->crypto_major_1h` score `-0.0006` n `176` status `ready` deltaP `7.9512` edge `0.0329` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `-0.1004` n `176` status `ready` deltaP `5.3484` edge `0.0324` maxDD `-3.7803`
- `market_context_high->fx_1h` score `-0.347` n `176` status `ready` deltaP `0.4831` edge `0.0008` maxDD `-0.5468`
- `market_context_high->commodity_24h` score `-0.3946` n `176` status `ready` deltaP `7.9704` edge `0.1008` maxDD `-5.2791`
- `market_context_high->index_1h` score `-0.5664` n `176` status `ready` deltaP `-0.4185` edge `0.0016` maxDD `-0.7136`
- `market_context_high->commodity_1h` score `-0.6336` n `176` status `ready` deltaP `-0.3028` edge `-0.0109` maxDD `-2.1314`
- `market_context_high->metal_1h` score `-0.635` n `176` status `ready` deltaP `-4.2427` edge `-0.0006` maxDD `-1.2017`
- `market_context_high->equity_1h` score `-0.9972` n `176` status `ready` deltaP `3.8548` edge `-0.0061` maxDD `-3.8827`
- `market_context_high->index_4h` score `-1.19` n `176` status `ready` deltaP `6.9013` edge `-0.0106` maxDD `-5.7046`
- `market_context_high->fx_4h` score `-1.2154` n `176` status `ready` deltaP `7.5388` edge `0.0003` maxDD `-2.1765`
- `market_context_high->commodity_4h` score `-1.5357` n `176` status `ready` deltaP `-2.536` edge `-0.031` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.9552` n `176` status `ready` deltaP `-7.9239` edge `-0.02` maxDD `-3.2083`
- `market_context_high->crypto_major_4h` score `-2.188` n `176` status `ready` deltaP `5.9451` edge `0.0113` maxDD `-16.8495`
- `market_context_high->crypto_alt_4h` score `-2.3803` n `176` status `ready` deltaP `3.4368` edge `0.0121` maxDD `-19.2145`
- `market_context_high->metal_4h` score `-2.6011` n `176` status `ready` deltaP `-6.3193` edge `-0.0053` maxDD `-5.2172`
- `market_context_high->equity_4h` score `-3.903` n `176` status `ready` deltaP `5.5987` edge `-0.1108` maxDD `-27.1529`
- `market_context_high->unknown_4h` score `-4.0632` n `176` status `ready` deltaP `-18.3066` edge `0.02` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.3563` n `176` status `ready` deltaP `-8.7437` edge `-0.0011` maxDD `-5.6237`
- `market_context_high->metal_24h` score `-7.5396` n `176` status `ready` deltaP `-8.7753` edge `-0.0596` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
