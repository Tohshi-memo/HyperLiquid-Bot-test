# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-02T03:22:19.875956+00:00`
- Price records: `672`
- Market context records: `2624`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9216`

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

- `market_context_high->unknown_24h` score `7.6602` n `146` status `ready` deltaP `18.2958` edge `0.5492` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `5.0623` n `146` status `ready` deltaP `25.0439` edge `0.5228` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `3.2455` n `146` status `ready` deltaP `14.1539` edge `0.3571` maxDD `-10.1468`
- `market_context_high->crypto_alt_1h` score `1.2693` n `146` status `ready` deltaP `11.1312` edge `0.1503` maxDD `-6.1656`
- `market_context_high->index_24h` score `1.1318` n `146` status `ready` deltaP `10.3643` edge `0.1233` maxDD `-2.5127`
- `market_context_high->unknown_4h` score `1.0517` n `146` status `ready` deltaP `7.5321` edge `0.1424` maxDD `-3.7312`
- `market_context_high->crypto_major_1h` score `0.6645` n `146` status `ready` deltaP `8.7134` edge `0.1167` maxDD `-4.2199`
- `market_context_high->crypto_alt_24h` score `0.5795` n `146` status `ready` deltaP `2.238` edge `0.6712` maxDD `-39.0265`
- `market_context_high->index_4h` score `0.294` n `146` status `ready` deltaP `9.1276` edge `0.0478` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.1` n `146` status `ready` deltaP `4.2408` edge `0.0128` maxDD `-1.2855`
- `market_context_high->unknown_1h` score `-0.2448` n `146` status `ready` deltaP `1.9502` edge `0.0329` maxDD `-2.6375`
- `market_context_high->commodity_1h` score `-0.2828` n `146` status `ready` deltaP `6.4002` edge `0.0216` maxDD `-4.3601`
- `market_context_high->metal_1h` score `-0.7052` n `146` status `ready` deltaP `0.9618` edge `0.0096` maxDD `-2.9823`
- `market_context_high->fx_1h` score `-0.7311` n `146` status `ready` deltaP `-1.5831` edge `0.0031` maxDD `-0.278`
- `market_context_high->equity_1h` score `-0.8756` n `146` status `ready` deltaP `-0.8264` edge `0.0164` maxDD `-2.7085`
- `market_context_high->commodity_4h` score `-0.879` n `146` status `ready` deltaP `5.3207` edge `0.0461` maxDD `-10.2078`
- `market_context_high->fx_24h` score `-1.009` n `146` status `ready` deltaP `2.8467` edge `-0.0037` maxDD `-1.6157`
- `market_context_high->metal_4h` score `-1.0285` n `146` status `ready` deltaP `2.8253` edge `0.0342` maxDD `-4.7664`
- `market_context_high->fx_4h` score `-1.0443` n `146` status `ready` deltaP `-1.5975` edge `0.0094` maxDD `-0.8621`
- `market_context_high->equity_4h` score `-1.3458` n `146` status `ready` deltaP `1.6497` edge `0.0173` maxDD `-5.9024`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
