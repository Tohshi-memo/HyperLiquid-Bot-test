# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-25T04:07:18.964641+00:00`
- Price records: `672`
- Market context records: `1807`
- Flow alert records: `7099`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8872`

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

- `market_context_high->crypto_alt_4h` score `7.0852` n `185` status `ready` deltaP `23.0702` edge `0.5511` maxDD `-5.1574`
- `market_context_high->metal_24h` score `6.8722` n `180` status `ready` deltaP `27.7777` edge `0.6301` maxDD `-12.7414`
- `news_risk_high->commodity_4h` score `6.5173` n `30` status `ready` deltaP `29.563` edge `0.4115` maxDD `-3.5713`
- `market_context_high->crypto_major_4h` score `6.3871` n `185` status `ready` deltaP `26.8268` edge `0.4951` maxDD `-5.6681`
- `market_context_high->unknown_4h` score `4.3781` n `185` status `ready` deltaP `16.9166` edge `0.4677` maxDD `-10.2508`
- `market_context_high->index_24h` score `3.4923` n `180` status `ready` deltaP `16.9444` edge `0.3009` maxDD `-4.1604`
- `news_risk_high->commodity_1h` score `3.307` n `30` status `ready` deltaP `25.02` edge `0.1405` maxDD `-1.2043`
- `market_context_high->equity_4h` score `2.9554` n `185` status `ready` deltaP `15.9196` edge `0.2496` maxDD `-5.0894`
- `market_context_high->equity_24h` score `2.75` n `180` status `ready` deltaP `18.5416` edge `0.5954` maxDD `-33.1875`
- `market_context_high->unknown_24h` score `2.0263` n `180` status `ready` deltaP `12.4653` edge `0.6178` maxDD `-35.8966`
- `news_risk_high->fx_4h` score `0.9081` n `30` status `ready` deltaP `21.6362` edge `-0.0006` maxDD `-0.1774`
- `market_context_high->index_4h` score `0.8201` n `185` status `ready` deltaP `11.7057` edge `0.0992` maxDD `-3.7119`
- `market_context_high->crypto_major_1h` score `0.4281` n `187` status `ready` deltaP `6.193` edge `0.093` maxDD `-3.2225`
- `news_risk_high->unknown_4h` score `0.3909` n `30` status `ready` deltaP `9.9796` edge `0.0559` maxDD `-2.7857`
- `market_context_high->crypto_alt_1h` score `0.3315` n `187` status `ready` deltaP `6.7493` edge `0.094` maxDD `-4.9097`
- `market_context_high->equity_1h` score `-0.1483` n `187` status `ready` deltaP `3.9483` edge `0.0407` maxDD `-2.6836`
- `market_context_high->crypto_major_24h` score `-0.3405` n `180` status `ready` deltaP `17.9861` edge `0.7103` maxDD `-62.3533`
- `market_context_high->fx_24h` score `-0.4451` n `180` status `ready` deltaP `9.1667` edge `0.0067` maxDD `-1.3925`
- `news_risk_high->fx_1h` score `-0.4546` n `30` status `ready` deltaP `-4.8303` edge `0.0001` maxDD `-0.0948`
- `news_risk_high->unknown_1h` score `-0.4738` n `30` status `ready` deltaP `16.5569` edge `-0.1239` maxDD `-2.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
