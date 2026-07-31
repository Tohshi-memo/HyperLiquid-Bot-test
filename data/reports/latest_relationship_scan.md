# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-31T13:37:28.148580+00:00`
- Price records: `672`
- Market context records: `8519`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5882`

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

- `news_risk_high->unknown_24h` score `6278.4225` n `52` status `ready` deltaP `44.7383` edge `522.9457` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `5.469` n `64` status `ready` deltaP `21.1128` edge `0.3747` maxDD `-3.4427`
- `market_context_high->equity_4h` score `2.1193` n `35` status `ready` deltaP `22.9878` edge `0.0766` maxDD `-2.2598`
- `news_risk_high->index_4h` score `1.9697` n `64` status `ready` deltaP `16.3491` edge `0.0742` maxDD `-0.191`
- `news_risk_high->equity_1h` score `1.675` n `64` status `ready` deltaP `15.8028` edge `0.0819` maxDD `-2.4803`
- `market_context_high->crypto_alt_4h` score `1.2508` n `35` status `ready` deltaP `14.2291` edge `0.1403` maxDD `-3.9846`
- `market_context_high->crypto_major_4h` score `1.2152` n `35` status `ready` deltaP `10.4181` edge `0.1597` maxDD `-2.8692`
- `news_risk_high->crypto_major_4h` score `0.7922` n `64` status `ready` deltaP `5.3735` edge `0.1433` maxDD `-3.5385`
- `news_risk_high->crypto_alt_4h` score `0.7269` n `64` status `ready` deltaP `13.872` edge `0.1399` maxDD `-5.8012`
- `news_risk_high->crypto_alt_1h` score `0.496` n `64` status `ready` deltaP `8.8604` edge `0.0572` maxDD `-1.8813`
- `news_risk_high->crypto_major_1h` score `0.2698` n `64` status `ready` deltaP `6.1658` edge `0.0447` maxDD `-2.0972`
- `market_context_high->fx_4h` score `0.1788` n `35` status `ready` deltaP `8.3275` edge `0.0169` maxDD `-0.2932`
- `news_risk_high->fx_1h` score `0.0947` n `64` status `ready` deltaP `5.436` edge `0.004` maxDD `-0.2475`
- `news_risk_high->index_1h` score `0.0433` n `64` status `ready` deltaP `4.3694` edge `0.0081` maxDD `-0.5338`
- `market_context_high->index_4h` score `0.0274` n `35` status `ready` deltaP `5.5009` edge `0.0064` maxDD `-0.4979`
- `market_context_high->commodity_1h` score `0.0155` n `47` status `ready` deltaP `7.7143` edge `0.0131` maxDD `-2.0038`
- `news_risk_high->fx_4h` score `0.0048` n `64` status `ready` deltaP `11.3186` edge `0.0207` maxDD `-0.6604`
- `news_risk_high->metal_4h` score `-0.0027` n `64` status `ready` deltaP `2.0198` edge `0.0338` maxDD `-0.8085`
- `news_risk_high->metal_1h` score `-0.1299` n `64` status `ready` deltaP `3.256` edge `0.0078` maxDD `-0.5599`
- `market_context_high->crypto_major_1h` score `-0.172` n `47` status `ready` deltaP `3.6724` edge `0.0032` maxDD `-1.9791`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
